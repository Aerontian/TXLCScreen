import os
from FactorSynthesis import *
from DataLoading import *
from ICTest import *
from GroupBackTest import *
from WriterClass import Writer
from EquityAssessment import *
"""
This part is to take 3 tests:
    1, ic test; 2, time section linear regression test; 3, grouping test
The tests results are designed to be like this:
    1, ic test:
        A bar graph;
        A table including a t-test t-value and a t-test p-value 
    2, time section linear regression test:
        A regression graph;
        A table including t-test t-values, t-test p-values for the linear term coefficient and the intercept term for each time section
        f-test f-values and f-test p-value for the regression;
    3, grouping test:
        An equity plot for all the groups and the reference;
        A table including the statistics about all the group and the reference.

The directory is structured as below:
    FactorTest:
                        factor_name_1:
                                                Pic:
                                                            factor_bar_ic.png, factor_regression_year.png, factor_group.png
                                                Xls:
                                                            factor_stats.xlsx
                                                Doc:
                                                            factor_test.docx
                        factor_name_2:
                                                Pic:
                                                            factor_bar_ic.png, factor_regression_year.png, factor_group.png
                                                Xls:
                                                            factor_stats.xlsx
                                                Doc:
                                                            factor_test.docx
                        factor_name_...:
                                                Pic:
                                                            factor_bar_ic.png, factor_regression_year.png, factor_group.png
                                                Xls:
                                                            factor_stats.xlsx
                                                Doc:
                                                            factor_test.docx
                        factor_name_n:
                                                Pic:
                                                            factor_bar_ic.png, factor_regression_year.png, factor_group_year.png
                                                Xls:
                                                            factor_stats.xlsx
                                                Doc:
                                                            factor_test.docx

"""


def create_dir(fac_id):

    path_factor = "".join(["./FactorTest", "/", fac_id])
    if os.path.exists(path_factor):
        pass
    else:
        os.makedirs(path_factor)

    path_factor_pic = "".join([path_factor, '/', 'Pic'])
    path_factor_xls = "".join([path_factor, '/', 'Xls'])
    path_factor_doc = "".join([path_factor, '/', 'Doc'])

    if os.path.exists(path_factor_pic):
        pass
    else:
        os.makedirs(path_factor_pic)

    if os.path.exists(path_factor_xls):
        pass
    else:
        os.makedirs(path_factor_xls)

    if os.path.exists(path_factor_doc):
        pass
    else:
        os.makedirs(path_factor_doc)


def factor_selection(fac_list, selection=True):

    key_list = list(factor_syn_dict.keys())
    if selection:
        for i_key in key_list:
            if i_key in fac_list:
                pass
            else:
                factor_syn_dict.pop(i_key)
    else:
        for i_key in key_list:
            if i_key in fac_list:
                factor_syn_dict.pop(i_key)
            else:
                pass


    return factor_syn_dict


def ic_test(fac_id, df_fac_slice, df_ret_slice):

    path_factor = "".join(["./FactorTest", "/", fac_id])
    path_factor_pic = "".join([path_factor, '/', 'Pic'])

    ic_value_dict = test_ic(df_fac_slice, df_ret_slice)
    pic_filename = "".join([path_factor_pic, "/", factor_id, "_", "bar_ic", ".png"])
    plt_ic = plot_bar(ic_value_dict)
    plt_ic.savefig(pic_filename, format="png")
    plt_ic.close()

    t_value, p_1tail = t_test(ic_value_dict)
    df_t_test = pd.DataFrame(np.array([[t_value[0], p_1tail[0]]]), columns=['t value', 't test p value'])

    return df_t_test


def regression_test(fac_id, df_fac_slice, df_ret_slice):

    path_factor = "".join(["./FactorTest", "/", fac_id])
    path_factor_pic = "".join([path_factor, '/', 'Pic'])

    # excl_anl_dict = get_excl_dict(src='local')
    stats_test_dict = dict()
    for ii_fy in fy_list:

        ii_py = fy_py_mapper[ii_fy]
        if ii_py is None:
            continue
        srs_factor = df_fac_slice.loc[ii_fy, :]
        srs_valid_factor = srs_factor.notna()

        srs_ret = (df_ret_slice.loc[ii_py, :] - 1) * 100
        srs_valid_ret = srs_ret.notna()

        sec_mean = srs_factor.mean()
        sec_std_dev = srs_factor.std()
        down_bound = sec_mean - 1 * sec_std_dev
        up_bound = sec_mean + 3 * sec_std_dev
        down_bound = 0
        up_bound = 60

        print("The mean of the factor is: {0}\n".format(sec_mean))
        print("The standard deviation of the factor is: {0}\n".format(sec_std_dev))
        print("The range in consideration of the factor is {0}: {1} \n".format(down_bound, up_bound))

        srs_range_valid = \
            srs_factor.apply(lambda factor_value: True if down_bound <= factor_value <= up_bound else False)

        srs_valid_all = srs_valid_factor & srs_valid_ret & srs_range_valid



        # srs_interval_valid = \
        #     srs_factor.apply(lambda factor_value: True if -100 <= factor_value <= 100 else False)

        # srs_interval_valid = \
        #     srs_factor.apply(lambda factor_value: True)
        # factor_excl_list = srs_interval_valid[~srs_interval_valid].index.tolist()
        #
        # excl_list = \
        #     list(set(excl_anl_dict[ii_py]).union(set(excl_anl_dict[ii_fy])).union(set(factor_excl_list)))
        #
        # srs_valid.loc[excl_list] = False

        srs_exog = srs_factor.loc[srs_valid_all]
        srs_endog = srs_ret.loc[srs_valid_all]

        if srs_endog.size == 0:
            continue
        else:
            np_exog = np.array(srs_exog).transpose()
            np_endog = np.array(srs_endog).transpose()
            np_exog = sm.add_constant(np_exog)

            model = sm.OLS(np_endog, np_exog)
            result = model.fit()
            print(result.summary())

            y_fitted = result.fittedvalues
            plt_reg = plot_regression(srs_exog, srs_endog, y_fitted, fac_id)
            pic_filename = "".join([path_factor_pic, "/", fac_id, "_", "regression", "_", ii_py, ".png"])
            plt_reg.savefig(pic_filename, format="png")
            plt_reg.close()

            stats_section_test_list = list()

            stats_section_test_list.append(result.fvalue)
            stats_section_test_list.append(result.f_pvalue)
            stats_section_test_list.append(result.tvalues[0])
            stats_section_test_list.append(result.pvalues[0])
            stats_section_test_list.append(result.tvalues[1])
            stats_section_test_list.append(result.pvalues[1])

            stats_test_dict[ii_py] = stats_section_test_list

    index = ['f value', 'f_pvalue', 'intcpt t value', 'intcpt t test p value', 'linear t values', 'linear t test p values']
    df_reg_test = pd.DataFrame(data=stats_test_dict, index=index)
    df_reg_test = df_reg_test.T

    return df_reg_test


def get_group_line(df_fac_slice, quantile=None, border=None):

    df_border_lines = None
    if border is None:
        """
            Grouping by quantile
        """
        # df_factor_anl = df_factor_slice
        # df_factor_anl3avg = df_factor_anl.rolling(5, axis=0).min()
        # df_factor_anl3avg.where(df_anl_on, inplace=True)

        # df_border_lines = df_factor_anl3avg.quantile(quantile, axis=1)
        # df_border_lines.index = quantile
        df_border_lines = df_fac_slice.quantile(quantile, axis=1)
        df_border_lines.index = quantile
    else:
        """
            Grouping by border
        """
        quantile_dict = dict()
        for i_yr in df_fac_slice.columns.tolist():
            quantile_dict[i_yr] = border

            df_border_lines = pd.DataFrame(quantile_dict, index=list(range(0, len(border))))

    return df_border_lines


def exclude_black_list(blacklist_dict, pos_dict):

    """
    Excluding all the shares which are not in consideration
    """
    for i_yr, i_pos_list in pos_dict.items():
        if i_pos_list:
            pos_set = set(i_pos_list)
            excl_anl_set = blacklist_dict[i_yr]
            pos_set = pos_set.difference(excl_anl_set)
            pos_dict[ii_yr] = list(pos_set)

    return pos_dict


def get_group_pos(df_border_lines, df_fac_slice, group_idx):

    pos_dict = dict()
    yr_list = df_border_lines.columns.tolist()
    border_list = df_border_lines.index.tolist()
    for i_yr in yr_list:

        value_up = df_border_lines.loc[border_list[group_idx], i_yr]
        value_down = df_border_lines.loc[border_list[group_idx - 1], i_yr]
        srs_row = df_fac_slice.loc[i_yr, :]
        srs_valid_fy = srs_row.notna()

        def select(factor_value, **kwargs):

            v_up = kwargs['value_up']
            v_down = kwargs['value_down']
            if np.isnan(factor_value):
                return False
            elif v_down < factor_value <= v_up:
                return True
            else:
                return False

        if np.isnan(value_up) or np.isnan(value_down):
            srs_valid_select = srs_row.apply(lambda _: False)
        else:
            srs_valid_select = srs_row.apply(select, value_up=value_up, value_down=value_down)
            # srs_select = srs_row[srs_row.apply(select, value_up=value_up, value_down=value_down)]

        pos_key = fy_py_mapper[i_yr]
        if pos_key is not None:

            srs_valid_py = df_fac_slice.loc[pos_key, :].notna()
            srs_valid_all = srs_valid_select & srs_valid_fy & srs_valid_py
            srs_select = srs_row[srs_valid_all]
            pos_dict[pos_key] = srs_select.index.tolist()

    return pos_dict


def get_group_eqy(grp_pos_dict, df_pct):

    pos_date_idx_dict = copy.deepcopy(py_td_idx_mapper)
    pos_date_idx_dict = collections.OrderedDict(pos_date_idx_dict)
    trade_day_list = df_pct.index.tolist()

    """
        Initializing back test data
    """

    eqy_prtfl = 1.0

    eqy_anl_dict = collections.OrderedDict()

    for key_yr, value_pos in grp_pos_dict.items():

        start_idx = pos_date_idx_dict[key_yr][0]
        end_idx = pos_date_idx_dict[key_yr][1]
        trade_day_start = trade_day_list[start_idx]
        trade_day_end = trade_day_list[end_idx]
        pct_pos = df_pct.loc[trade_day_start:trade_day_end, value_pos]

        eqy_anl_np_array = get_daily_equity(pct_pos.values, eqy_prtfl)
        index_label = trade_day_list[start_idx:end_idx + 1]
        srs_eqy_anl = pd.Series(eqy_anl_np_array, index=index_label)
        eqy_anl_dict[key_yr] = srs_eqy_anl
        eqy_prtfl = srs_eqy_anl[-1]

    """
        Piece up equity data by position years
    """
    df_eqy_assbly = pd.concat(eqy_anl_dict.values())

    return df_eqy_assbly


def eqy_assess(df_eqy_grp, df_mrkt_avg):

    group_test_dict = dict()
    for ii_grp, df_cols in df_eqy_grp.items():
        prpty_list, value_list = equity_assess_2(df_cols.values)
        group_test_dict[ii_grp] = value_list
        print("Group: {0}:\n".format(ii_grp))
        for i_prpty, i_value in zip(prpty_list, value_list):
            print("\t {0}: {1} \n".format(i_prpty, i_value))

    prpty_list, value_list = equity_assess_2(df_mrkt_avg.values)
    group_test_dict['market'] = value_list
    print("Group: market:\n")
    for i_prpty, i_value in zip(prpty_list, value_list):
        print("\t {0}: {1} \n".format(i_prpty, i_value))

    df_grp_test = pd.DataFrame(data=group_test_dict, index=prpty_list)
    df_grp_test = df_grp_test.T

    df_grp_test = \
        df_grp_test.astype(dtype={'trading day number': 'int32', 'win day': 'int32', 'lose day': 'int32'})

    return df_grp_test

    # for gp, eqy_np_array in equity_np_group_array_dict.items():
    #
    #     egy_assess_dict = equity_assess(eqy_np_array)
    #     egy_assess_group_dict[gp] = egy_assess_dict
    #     print("Group: {0}:\n".format(gp))
    #     for key, index_value in egy_assess_dict.items():
    #         print("\t {0}: {1} \n".format(key, index_value))
    #
    # egy_assess_dict = equity_assess(mkt_avg_close_joint_np_array)
    # egy_assess_group_dict['market'] = egy_assess_dict
    #
    # group_test_dict = dict()
    # group_stat_list = list()
    # for key, stats_back_test in egy_assess_group_dict.items():
    #     group_stat_list = list()
    #     group_stat_list.append(int(stats_back_test['trading day number']))
    #     group_stat_list.append(stats_back_test['equity'])
    #     group_stat_list.append(stats_back_test['annual return'])
    #     group_stat_list.append(stats_back_test['annual_volatility'])
    #     group_stat_list.append(stats_back_test['sharp ratio'])
    #     group_stat_list.append(int(stats_back_test['win day']))
    #     group_stat_list.append(int(stats_back_test['lose day']))
    #     group_stat_list.append(stats_back_test['win ratio'])
    #     group_stat_list.append(stats_back_test['win mean'])
    #     group_stat_list.append(stats_back_test['lose mean'])
    #     group_stat_list.append(stats_back_test['win lose ratio'])
    #     group_stat_list.append(stats_back_test['max win'])
    #     group_stat_list.append(stats_back_test['max lose'])
    #     group_test_dict[key] = group_stat_list
    #
    # index = ['trading day number', 'equity', 'annual return', 'annual_volatility',
    #          'sharp ratio', 'win day', 'lose day', 'win ratio', 'win mean', 'lose mean',
    #          'win lose ratio', 'max win', 'max lose']
    # df_group_test = pd.DataFrame(data=group_test_dict, index=index)
    # df_group_test = df_group_test.T


def group_test(fac_id, df_fac_slice, df_pct, blacklist):

    path_factor = "".join(["./FactorTest", "/", fac_id])
    path_factor_pic = "".join([path_factor, '/', 'Pic'])

    """
        Get the position for each group
    """
    grp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    quantile_list = [0]
    quantile_list.extend(grp_list)
    quantile_list = np.linspace(0, 10, 11) / 10

    df_value_lines = get_group_line(df_fac_slice, quantile_list)

    """
    The keys of gp_pos_dict are the group codes,
    the values of gp_pos_dict are position of each group.
    The position of each group is presented in dict pos_dict:
        The keys of pos_dict are the positioning years,
        the values of pos_dict are lists containing all the codes 
        of the shares in position
    """
    eqy_group_df_dict = dict()
    pos_dict = dict()
    for i_gp in grp_list:
        pos_dict = get_group_pos(df_value_lines, df_fac_slice, i_gp)
        pos_dict = exclude_black_list(blacklist, pos_dict)
        df_eqy_group = get_group_eqy(pos_dict, df_pct)
        eqy_group_df_dict[i_gp] = df_eqy_group

    idx_start = 0
    for key_pos_yr, pos_list in pos_dict.items():
        if pos_list:
            idx_start = py_td_idx_mapper[key_pos_yr][0]
            break

    df_eqy_all_gps = pd.DataFrame(eqy_group_df_dict, columns=grp_list)
    trade_day_list = df_pct.index.tolist()
    (start_day, end_day) = (trade_day_list[idx_start], trade_day_list[-1])
    # (start_day, end_day) = (trade_day_list[0], trade_day_list[-1])
    df_mkt_avg = get_mkt_avg_eqy(start_day, end_day)
    df_eqy_windowed_gps = df_eqy_all_gps.loc[start_day:end_day, :]

    pic_filename = "".join([path_factor_pic, "/", factor_id, "_", "group", ".png"])
    plt_group = plot_eqy_all_group(df_eqy_windowed_gps, df_mkt_avg)
    # plt_group.show()
    plt_group.savefig(pic_filename, format="png")
    plt_group.close()

    df_group_stast = eqy_assess(df_eqy_windowed_gps, df_mkt_avg)

    return df_group_stast


def get_mkt_avg_eqy(trade_day_start, trade_day_end):

    df_idx_mkt_avg_close = get_index_data()
    df_idx_mkt_avg_close_slice = df_idx_mkt_avg_close.loc[trade_day_start:trade_day_end, 'Equity']
    equity_base = df_idx_mkt_avg_close.loc[trade_day_start::-1, 'Equity'].tolist()[1]
    df_mkt_avg_eqy = df_idx_mkt_avg_close_slice / equity_base

    return df_mkt_avg_eqy


def write_docx(fac_info, df_ic, df_regression, df_gp):

    report_writer = Writer()
    df_gp_tb = df_gp.iloc[:, 0:-2]
    report_writer.test_report(fac_info, df_ic, df_regression, df_gp_tb)


def write_xlsx(fac_id, df_ic, df_regression, df_gp):

    path_factor = "".join(["./FactorTest", "/", fac_id])
    path_factor_xls = "".join([path_factor, '/', 'Xls'])
    xls_filename = "".join([path_factor_xls, "/", fac_id, "_", "stats", ".xlsx"])

    with pd.ExcelWriter(xls_filename) as writer:
        sht_name = "id test"
        df_ic.to_excel(writer, sheet_name=sht_name)
        sht_name = "regression test"
        df_regression.to_excel(writer, sheet_name=sht_name)
        sht_name = "group test"
        df_gp.to_excel(writer, sheet_name=sht_name)

    print("factor:  {0} is done.".format(factor_id))


def factor_rolling(df_fac):

    df_factor_anl = df_fac
    df_factor_anl_avg = df_factor_anl.rolling(2, axis=0).mean()
    df_factor_anl_avg.where(df_anl_on, other=np.nan, inplace=True)

    return df_factor_anl_avg


def exclude_black(df_value, black_dict):
    """
    Excluding all the shares which are not in consideration
    """
    for i_yr, i_black_list in black_dict.items():
        if i_black_list:
            df_value.loc[i_yr, i_black_list] = np.nan
    return df_value


def bound_factor_value(df_fac, down=0, up=100):
    """
    Bounding the factor value
    """
    df_fac[(df_fac < down) | (df_fac > up)] = np.nan

    return df_fac


"""
Data Loading

The data required in the program are:
1, factor data: the data differs from a factor to another
2, pct daily data
3, annual return data
4, black list
"""

df_percentage = get_pct_data()
"""
Load the annual return data
"""

df_return_slice = get_return_anl()
"""
Load the black list
"""
black_anl_dict = get_excl_dict()
"""
Excluding the black list
"""
df_return_slice = exclude_black(df_return_slice, black_anl_dict)


"""
In the loop, all the factors are tested.
For each factor, the following operations are taken respectively:
    1, create the directory for the factor 
    2, load the factor data
    3, ic test
    4, regression test
    5, group test
    6, create the report of the test
"""
factor_select_list = ['WAA']
factor_selection(factor_select_list, selection=True)
for factor_id, factor_info in factor_syn_dict.items():

    """
        Create the directory structure
    """
    create_dir(factor_id)
    """
        Load the factor data 
    """
    get_syn_factor_fun = get_syn_factor_dict[factor_id]
    df_factor_slice = get_syn_factor_fun(raw_data_dict)
    df_factor_slice = factor_rolling(df_factor_slice)
    df_factor_slice = bound_factor_value(df_factor_slice, down=0, up=60)
    df_factor_slice = exclude_black(df_factor_slice, black_anl_dict)

    # """
    #         group test: comparison among groups
    #     """
    # group_test(factor_id, df_factor_slice, df_percentage, excl_anl_dict)

    """
        ic test: time section ic test, and all the ic test values undergo t test
    """
    df_ic_test = ic_test(factor_id, df_factor_slice, df_return_slice)
    """
        regression test: time section linear regression
    """
    df_regression_test = regression_test(factor_id, df_factor_slice, df_return_slice)
    """
        group test: comparison among groups
    """
    df_group_test = group_test(factor_id, df_factor_slice, df_percentage, black_anl_dict)

    """
    Write all the test results to .docx file
    """
    write_docx(factor_info, df_ic_test, df_regression_test, df_group_test)

    """
    Write all the tables to .xlsx file
    """
    write_xlsx(factor_id, df_ic_test, df_regression_test, df_group_test)

