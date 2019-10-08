# -*- coding: UTF-8 -*
from ShareListDelistSelection import *
import collections
from DataLoading import get_pct_data, get_index_data
from EquityCalculation import *
from DataVisualizing import *
from functools import reduce
import pandas as pd
from WindCode import NUM_WIND_CODE
from EquityAssessment import equity_assess

num_year = NUM_YEAR
num_wind_code = NUM_WIND_CODE

SOURCE_PATH = "/home/aeront/PycharmProjects/TXLCScreen/Output"

screen_criterion = dict()
'''
加权平均净资产收益率
'''
criterion = ("factor_WAA_df_slice_update.dat", "加权净资产收益率.xlsx", 15, "+", 10, "+")
screen_criterion['WAA'] = criterion
'''
ROA
'''
criterion = ("factor_ROA_df_slice_update.dat", "总资产收益率.xlsx", 7, "+", 6, "+")
screen_criterion['ROA'] = criterion
'''
每股经营活动产生的现金流量净额
'''
criterion = ("factor_OCFPS_df_slice_update.dat", "每股经营活动产生的现金流量净额.xlsx", 0, "+", 0, "+")
screen_criterion['OCFPS'] = criterion
'''
资产负债率
'''
criterion = ("factor_debt2assets_df_slice_update.dat", "资产负债率.xlsx", 40, "-", None, None)
screen_criterion['debt2assets'] = criterion
'''
扣除商誉资产负债率（%）
'''
criterion = ("factor_debt2assets_minus_GOODWILL_df_slice_update.dat", "扣除商誉资产负债率.xlsx", 40, "-", None, None)
screen_criterion['debt2assets_minus_GOODWILL'] = criterion
'''
经营现金保证率（%）
'''
criterion = ("factor_CASH_GUARANTEE_df_slice_update.dat", "经营现金保证率.xlsx", 10, "+", None, None)
screen_criterion['CASH_GUARANTEE'] = criterion
'''
总应收账款与销售额之比（%）
'''
criterion = ("factor_RATIO_TOT_RCV_TO_SALE_df_slice_update.dat", "应收账款与销售额之比.xlsx", 40, "-", None, None)
screen_criterion['RATIO_TOT_RCV_TO_SALE'] = criterion
'''
存货与销售额之比（%）
'''
criterion = ("factor_RATIO_INVENTORIES_TO_SALE_df_slice_update.dat", "存货与销售额之比.xlsx", 40, "-", None, None)
screen_criterion['RATIO_INVENTORIES_TO_SALE'] = criterion
'''
营业净利润率（%）
'''
criterion = ("factor_NET_PROFIT_RATIO_df_slice_update.dat", "营业净利润率.xlsx", 15, "+", None, None)
screen_criterion['NET_PROFIT_RATIO'] = criterion
'''
营业收入同比增长率（%）
'''
criterion = ("factor_YOY_OR_df_slice_update.dat", "营业收入同比增长率.xlsx", 0, "+", None, None)
screen_criterion['YOY_OR'] = criterion
'''
沉淀资金与销售额之比（%）
'''
criterion = ("factor_RATIO_INVENTORIES_TO_SALE_df_slice_update.dat", "沉淀资金与销售额之比.xlsx", 0, "+", None, None)
screen_criterion['RATIO_SENDIMENTATION_TO_SALE'] = criterion

df_anl_on = get_annual_on_df(year_genre='fiscal')


# def get_excl_dict():
#
#     return get_annual_on_dict(on=False, year_genre='position')


def tot_pos_to_excel(pos_dict):

    output_path = "/home/aeront/PycharmProjects/TXLCScreen/Output"
    filename_output = "".join([output_path, "/", "综合.xlsx"])

    with pd.ExcelWriter(filename_output) as writer:
        for i_yr, i_pos in pos_dict.items():
            df_pos = pd.DataFrame(i_pos, columns=['Wind Code'])

            if df_pos.empty:
                pass
            else:
                df_pos.sort_values(by=['Wind Code'], inplace=True, ascending=True)
                df_pos.reset_index(drop=True, inplace=True)

            df_pos.to_excel(writer, sheet_name=i_yr)


def get_position_tot():

    """
        Back test all the factors, get the intersection of the position of all the factors
    """

    factor_name_list = screen_criterion.keys()
    fis_dict_list = [get_fiscal_factor(ii_factor_name) for ii_factor_name in factor_name_list]

    def dict_intersect(fis1, fis2):
        fis = dict()
        for i_yr, i_pos in fis1.items():
            fis[i_yr] = list(set(i_pos).intersection(set(fis2[i_yr])))
        return fis

    fis_dict = reduce(dict_intersect, fis_dict_list)
    pos_dict = dict.fromkeys(fy_list, [])

    for key_yr, _ in fis_dict.items():

        pos_key = fy_py_mapper[key_yr]
        if pos_key is not None:
            pos_dict[pos_key] = fis_dict[key_yr]

    return pos_dict


def get_fiscal_factor(factor_name):

    if not isinstance(factor_name, str):
        print("The arg factor_name is supposed to be a string.")
        os._exit(1)

    factor_info = screen_criterion.get(factor_name)
    if factor_info is None:
        print("The factor {0} does not exist.".format(factor_name))
        os._exit(1)

    fis_dict = dict.fromkeys(py_list, [])

    src_xlsx_filename = factor_info[1]
    src_xlsx_path = SOURCE_PATH
    src_xlsx_path_filename = "".join([src_xlsx_path, "/", src_xlsx_filename])

    for key_yr, _ in fis_dict.items():

        pd_fis = \
            pd.read_excel(
                open(src_xlsx_path_filename, 'rb'),
                index_col=0,
                sheet_name=key_yr,
                dtype={"Windcode": str, "Value": float})

        fis_dict[key_yr] = pd_fis["Wind Code"].values.tolist()

        # pos_key = fy_py_mapper[key_yr]
        # if pos_key is not None:
        #     if pd_pos.empty:
        #         pos_dict[pos_key] = []
        #     else:
        #         pos_dict[pos_key] = pd_pos["Wind Code"].values.tolist()

    return fis_dict


def get_position_factor(df_factor_slice, group=1):

    # if not isinstance(factor_name, str):
    #     print("The arg factor_name is supposed to be a string.")
    #     os._exit(1)
    #
    # factor_info = screen_criterion.get(factor_name)
    # if factor_info is None:
    #     print("The factor {0} does not exist.".format(factor_name))
    #     os._exit(1)
    #
    # print("Now factor {0} is being dealt with...".format(factor_name))
    # path_data = "/home/aeront/PycharmProjects/TXLCScreen/FactorReservoir"
    # filename_data = factor_info[0]
    # path_filename_data = "".join([path_data, "/", filename_data])
    #
    # df_factor_slice = pd.read_pickle(path_filename_data, compression='bz2')
    # if df_factor_slice.shape != (num_year, num_wind_code):
    #     print("The size of the  sliced factor {0} error.".format(factor_name))
    #     os._exit(1)

    df_factor_anl = df_factor_slice
    df_factor_anl3avg = df_factor_anl.rolling(1, axis=0).min()
    df_factor_anl3avg.where(df_anl_on, inplace=True)

    quantile_up = group / 10.0
    quantile_down = (group - 1) / 10.0
    df_value_lines = df_factor_anl3avg.quantile([quantile_up, quantile_down], axis=1)
    df_value_lines.index = ["Up", "Down"]
    # interval = [60, 15]
    # v1 = {'2006': interval, '2007': interval, '2008': interval, '2009': interval, '2010': interval,
    #     '2011': interval, '2012': interval, '2013': interval, '2014': interval, '2015': interval,
    #      '2016': interval, '2017': interval, '2018': interval, '2019': interval}
    #
    # interval = [10,  0]
    # v2 = {'2006': interval, '2007': interval, '2008': interval, '2009': interval, '2010': interval,
    #       '2011': interval, '2012': interval, '2013': interval, '2014': interval, '2015': interval,
    #       '2016': interval, '2017': interval, '2018': interval, '2019': interval}
    #
    # if group == 9:
    #     df_value_lines = pd.DataFrame(v1, index=["Up", "Down"])
    # else:
    #     df_value_lines = pd.DataFrame(v2, index=["Up", "Down"])

    pos_dict = dict.fromkeys(py_list, [])

    for ii_year in fy_list:

        value_up = df_value_lines.loc["Up", ii_year]
        value_down = df_value_lines.loc["Down", ii_year]
        srs_row = df_factor_anl3avg.loc[ii_year, :]

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
            srs_select = pd.Series([])
        else:
            srs_select = srs_row[srs_row.apply(select, value_up=value_up, value_down=value_down)]

        pos_key = fy_py_mapper[ii_year]
        if pos_key is not None:
            if srs_select.empty:
                pos_dict[pos_key] = []
            else:
                pos_dict[pos_key] = srs_select.index.tolist()

    return pos_dict


if __name__ == "__main__":

    """
    Get Position, Pct and Index Data
    """
    index_mkt_avg_close = get_index_data()
    percentage_df = get_pct_data()
    """
    Back test a certain factor.
    """
    factor_name = "WAA"
    group_pos_dict = dict()
    # group_pos_dict[7] = get_position_factor(factor_name, group=7)
    # gp_list = np.linspace(1, 5, 9).tolist()
    gp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for ii_gp in gp_list:
        group_pos_dict[ii_gp] = get_position_factor(factor_name, group=ii_gp)

    # position_dict = get_position_tot()
    # tot_pos_to_excel(position_dict)

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
        b = ['000514.SZ', '600363.SH', '600468.SH', '000523.SZ', '000158.SZ', '600218.SH', '000591.SZ', '600128.SH', '600064.SH',
             '600488.SH', '000980.SZ', '600379.SH', '600893.SH', '002017.SZ', '600676.SH', '000733.SZ', '600861.SH', '600300.SH',
             '000632.SZ', '000993.SZ', '600038.SH', '600679.SH', '600841.SH', '600523.SH', '000503.SZ', '000682.SZ', '600667.SH',
             '600356.SH', '600774.SH', '600278.SH', '600343.SH', '600222.SH', '600775.SH', '600992.SH', '000766.SZ', '000851.SZ',
             '000756.SZ', '000530.SZ', '600168.SH', '600099.SH', '601588.SH', '000705.SZ', '000099.SZ', '000882.SZ', '600590.SH',
             '000768.SZ', '000990.SZ', '600078.SH', '601333.SH', '600624.SH', '600172.SH', '600461.SH', '600215.SH', '600630.SH',
             '600059.SH', '000153.SZ', '000564.SZ', '600189.SH']
        # c = ['600511.SH', '000538.SZ', '600036.SH', '000069.SZ', '600271.SH', '600276.SH']
        c = ['000651.SZ', '600511.SH', '002081.SZ', '600036.SH', '000963.SZ', '600048.SH', '600271.SH', '000069.SZ', '600519.SH', '600276.SH', '000538.SZ']

        if ii_gp == 9:
            pct_slice_dict = \
                {ii_year: percentage_df.ix[pos_date_index_dict[ii_year][0]:pos_date_index_dict[ii_year][1] + 1, position_dict[ii_year]] #position_dict[ii_year]
                 for ii_year in position_dict.keys()}
        else:
            pct_slice_dict = \
                {ii_year: percentage_df.ix[pos_date_index_dict[ii_year][0]:pos_date_index_dict[ii_year][1] + 1, position_dict[ii_year]]
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
        Piece up these data
        """
        for key, value in equity_piece_dict.items():

            if value.size != 0:
                equity_assembly_np_array = np.append(equity_assembly_np_array, value)

        equity_np_group_array_dict[ii_gp] = equity_assembly_np_array

    """
    Piece up these data
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

    for gp, eqy_np_array in equity_np_group_array_dict.items():

        egy_assess_dict = equity_assess(eqy_np_array)
        print("Group: {0}:\n".format(gp))
        for key, index_value in egy_assess_dict.items():
            print("\t {0}: {1} \n".format(key, index_value))

    mplot = plot_sum_equity_date_group(**para_plot_dict)
    mplot.show()
        # path_output = "/home/aeront/PycharmProjects/TXLCScreen/Output"
        # xlsx_filename = screen_criterion[factor_name][1]
        # pure_filename = xlsx_filename.split(".")[0]
        # filename_fig = "".join([pure_filename, ".png"])
        # path_filename_output = "".join([path_output, "/", filename_fig])
        # mplot.savefig(path_filename_output)
    a = 1


        # for ii_factor_name, ii_criterion in screen_criterion.items():
        #     pass