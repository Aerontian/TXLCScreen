import os
from FactorSynthesis import *
from DataLoading import *
from ICTest import *
from GroupBackTest import *
from WriterClass import Writer

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

"""
The factors dict to be test
"""
factor_dict = dict()

# '''
# 加权平均净资产收益率
# '''
# factor_info = ("waa", "加权平均净资产收益率", "factor_WAA_df_slice_update.dat")
# factor_dict["waa"] = factor_info

"""
"""

"""
Test the factors:
    1, Create the directory structure
    2, Loading the pct data
    2, Load the factor data
    
"""
percentage_df = get_pct_data()
"""
Create the directory structure
"""

path_test = "./FactorTest"
if os.path.exists(path_test):
    pass
else:
    os.makedirs(path_test)

"""
Load the return data
"""
df_ret_slice = get_return_anl()

for factor_id, factor_info in factor_syn_dict.items():

    """
    Create the directory structure
    """
    path_factor = "".join(["./FactorTest", "/", factor_id])
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

    """
    Load the factor data 
    """
    get_syn_factor_fun = get_syn_factor_dict[factor_id]
    df_factor_slice = get_syn_factor_fun(raw_data_dict)

    """
    ic test
    """
    ic_value_dict = test_ic(df_factor_slice, df_ret_slice)
    # pic_filename = "".join([path_factor_pic, "/", factor_id, "_", "bar_ic", ".png"])
    # plt_ic = plot_bar(ic_value_dict)
    # plt_ic.savefig(pic_filename, format="png")
    # plt_ic.close()

    t_value, p_1tail = t_test(ic_value_dict)
    df_t_test = pd.DataFrame(np.array([[t_value[0], p_1tail[0]]]), columns=['t value', 't test p value'])
    # xls_filename = "".join([path_factor_xls, "/", factor_id, "_", "stats", ".xlsx"])

    """
    time section linear regression test
    """
    stats_test_dict = dict()
    for ii_fy in fy_list:

        ii_py = fy_py_mapper[ii_fy]
        if ii_py is None:
            continue
        srs_factor = df_factor_slice.loc[ii_fy, :]
        srs_valid_factor = srs_factor.notna()

        srs_ret = df_ret_slice.loc[ii_py, :] - 1
        srs_valid_ret = srs_ret.notna()

        srs_valid = srs_valid_factor & srs_valid_ret

        excl_dict = get_excl_dict(src='local')

        # srs_interval_valid = \
        #     srs_factor.apply(lambda factor_value: True if -100 <= factor_value <= 100 else False)

        srs_interval_valid = \
            srs_factor.apply(lambda factor_value: True)
        factor_excl_list = srs_interval_valid[~srs_interval_valid].index.tolist()

        excl_list = \
            list(set(excl_dict[ii_py]).union(set(excl_dict[ii_fy])).union(set(factor_excl_list)))

        srs_valid.loc[excl_list] = False

        srs_exog = srs_factor.loc[srs_valid]
        srs_endog = srs_ret.loc[srs_valid] * 100
        np_exog = np.array(srs_exog).transpose()
        np_endog = np.array(srs_endog).transpose()
        np_exog = sm.add_constant(np_exog)

        model = sm.OLS(np_endog, np_exog)
        result = model.fit()
        print(result.summary())

        y_fitted = result.fittedvalues
        # plt_reg = plot_regression(srs_exog, srs_endog, y_fitted, factor_id)
        # pic_filename = "".join([path_factor_pic, "/", factor_id, "_", "regression", "_", ii_py, ".png"])
        # plt_reg.savefig(pic_filename, format="png")
        # plt_reg.close()

        # stats_section_test_dict = dict()
        # stats_section_test_dict['fvalue'] = result.fvalue
        # stats_section_test_dict['f_pvalue'] = result.f_pvalue
        # stats_section_test_dict['tvalues'] = result.tvalues
        # stats_section_test_dict['pvalues'] = result.pvalues
        # stats_test_dict[ii_py] = stats_section_test_dict

        stats_section_test_list = list()

        stats_section_test_list.append(result.fvalue)
        stats_section_test_list.append(result.f_pvalue)
        stats_section_test_list.append(result.tvalues[0])
        stats_section_test_list.append(result.pvalues[0])
        stats_section_test_list.append(result.tvalues[1])
        stats_section_test_list.append(result.pvalues[1])

        stats_test_dict[ii_py] = stats_section_test_list

    index = ['f value', 'f_pvalue', 'intcpt t value', 'intcpt t test p value', 'linear t values', 'linear t test p values']
    df_regression_test = pd.DataFrame(data=stats_test_dict, index=index)
    df_regression_test = df_regression_test.T

    """
    grouping test
    """

    """
    Get Position, Pct and Index Data
    """
    index_mkt_avg_close = get_index_data()
    # percentage_df = get_pct_data()

    """
    Get the position for each group
    """
    group_pos_dict = dict()
    gp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # gp_list = [1,  10]

    for ii_gp in gp_list:
        group_pos_dict[ii_gp] = get_position_factor(df_factor_slice, group=ii_gp)

    excl_dict = get_excl_dict()
    equity_np_group_array_dict = dict()

    for ii_gp in gp_list:

        position_dict = group_pos_dict[ii_gp]
        for ii_yr, ii_pos_list in position_dict.items():
            if ii_pos_list:
                position_set = set(ii_pos_list)
                excl_set = excl_dict[ii_yr]
                position_set = position_set.difference(excl_set)
                position_dict[ii_yr] = list(position_set)

        position_dict = collections.OrderedDict(position_dict)
        pos_date_index_dict = copy.deepcopy(py_td_idx_mapper)
        pos_date_index_dict = collections.OrderedDict(pos_date_index_dict)

        pct_slice_dict = \
            {ii_year: percentage_df.ix[pos_date_index_dict[ii_year][0]:pos_date_index_dict[ii_year][1] + 1, position_dict[ii_year]]  # position_dict[ii_year]
             for ii_year in position_dict.keys()}

        pct_slice_dict = collections.OrderedDict(pct_slice_dict)

        """
        Initializing back test data
        """

        equity_portfolio = 1.0
        equity_assembly_np_array = np.array([])
        mkt_avg_close_assembly_np_array = np.array([])
        pos_pro_np_array = np.array([])
        date_assembly_list = list()
        equity_piece_dict = collections.OrderedDict()

        """
        Get the equity for each position year respectively
        """
        for key, value in position_dict.items():
            if len(value) == 0:
                equity_piece_dict[key] = np.array([])
            else:
                pct_slice = pct_slice_dict[key]
                # pos_wgh_piece_np_array = \
                #     position_proportion_np_array[pos_date_index_dict[key][0]: pos_date_index_dict[key][1] + 1]
                equity_piece_np_array = get_daily_equity(pct_slice, equity_portfolio)
                equity_piece_dict[key] = equity_piece_np_array
                equity_portfolio = equity_piece_np_array[-1]

        # equity_piece_dict = collections.OrderedDict(equity_piece_dict)

        """
        Piece up equity data by position years
        """
        for key, value in equity_piece_dict.items():

            if value.size != 0:
                equity_assembly_np_array = np.append(equity_assembly_np_array, value)

        equity_np_group_array_dict[ii_gp] = equity_assembly_np_array

    """
    Piece up trading day, market average close price, 
    """
    # mkt_avg_close_slice_dict = \
    #     {ii_year: index_mkt_avg_close[pos_date_index_dict[ii_year][0]:pos_date_index_dict[ii_year][1] + 1]
    #      for ii_year in position_dict.keys()}
    # mkt_avg_close_slice_dict = collections.OrderedDict(mkt_avg_close_slice_dict)
    for key, value in equity_piece_dict.items():

        if value.size != 0:
            # mkt_avg_close_assembly_np_array = np.append(mkt_avg_close_assembly_np_array, mkt_avg_close_slice_dict[key])
            date_piece = trading_day_list[pos_date_index_dict[key][0]: pos_date_index_dict[key][1] + 1]
            date_assembly_list.extend(date_piece)

    mkt_avg_close_slice_dict = \
        {ii_year: index_mkt_avg_close[pos_date_index_dict[ii_year][0]:pos_date_index_dict[ii_year][1] + 1]
         for ii_year in position_dict.keys() if len(position_dict[ii_year]) != 0}
    mkt_avg_close_slice_dict = collections.OrderedDict(mkt_avg_close_slice_dict)

    mkt_avg_close_joint_np_array = np.array([])

    for year, piece in mkt_avg_close_slice_dict.items():
        if piece is not None:
            mkt_avg_close_joint_np_array = np.append(mkt_avg_close_joint_np_array, piece.values)
        else:
            pass
    mkt_avg_close_joint_np_array = mkt_avg_close_joint_np_array / mkt_avg_close_joint_np_array[0]

    # szzz_close_assembly_np_array = mkt_avg_close_assembly_np_array / mkt_avg_close_assembly_np_array[0]
    para_plot_dict = dict()
    para_plot_dict['date_list'] = date_assembly_list
    para_plot_dict['equity_np_group_array_dict'] = equity_np_group_array_dict
    para_plot_dict['ref_np_array'] = mkt_avg_close_joint_np_array
    para_plot_dict['pos_pro_np_array'] = np.ones((len(date_assembly_list),), dtype=int)

    egy_assess_group_dict = dict()
    for gp, eqy_np_array in equity_np_group_array_dict.items():

        egy_assess_dict = equity_assess(eqy_np_array)
        egy_assess_group_dict[gp] = egy_assess_dict
        print("Group: {0}:\n".format(gp))
        for key, index_value in egy_assess_dict.items():
            print("\t {0}: {1} \n".format(key, index_value))

    egy_assess_dict = equity_assess(mkt_avg_close_joint_np_array)
    egy_assess_group_dict['market'] = egy_assess_dict

    group_test_dict = dict()
    group_stat_list = list()
    for key, stats_back_test in egy_assess_group_dict.items():
        group_stat_list = list()
        group_stat_list.append(int(stats_back_test['trading day number']))
        group_stat_list.append(stats_back_test['equity'])
        group_stat_list.append(stats_back_test['annual return'])
        group_stat_list.append(stats_back_test['annual_volatility'])
        group_stat_list.append(stats_back_test['sharp ratio'])
        group_stat_list.append(int(stats_back_test['win day']))
        group_stat_list.append(int(stats_back_test['lose day']))
        group_stat_list.append(stats_back_test['win ratio'])
        group_stat_list.append(stats_back_test['win mean'])
        group_stat_list.append(stats_back_test['lose mean'])
        group_stat_list.append(stats_back_test['win lose ratio'])
        group_stat_list.append(stats_back_test['max win'])
        group_stat_list.append(stats_back_test['max lose'])
        group_test_dict[key] = group_stat_list

    index = ['trading day number', 'equity', 'annual return', 'annual_volatility',
             'sharp ratio', 'win day', 'lose day', 'win ratio', 'win mean', 'lose mean',
             'win lose ratio', 'max win', 'max lose']
    df_group_test = pd.DataFrame(data=group_test_dict, index=index)
    df_group_test = df_group_test.T

    plt_group = plot_sum_equity_date_group(**para_plot_dict)
    pic_filename = "".join([path_factor_pic, "/", factor_id, "_", "group", ".png"])
    plt_group.savefig(pic_filename, format="png")
    # plt_group.show()
    plt_group.close()

    xls_filename = "".join([path_factor_xls, "/", factor_id, "_", "stats", ".xlsx"])

    report_writer = Writer()
    df_gp_tb_test = df_group_test.iloc[:, 0:-2]
    report_writer.test_report(factor_info, df_t_test, df_regression_test, df_gp_tb_test)

    with pd.ExcelWriter(xls_filename) as writer:
        sht_name = "id test"
        df_t_test.to_excel(writer, sheet_name=sht_name)
        sht_name = "regression test"
        df_regression_test.to_excel(writer, sheet_name=sht_name)
        sht_name = "group test"
        df_group_test.to_excel(writer, sheet_name=sht_name)

    print("factor:  {0} is done.".format(factor_id))

a = 1

