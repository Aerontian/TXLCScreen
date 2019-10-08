# -*- coding: UTF-8 -*
from ShareListDelistSelection import *
from WindCode import NUM_WIND_CODE
import os

screen_criterion = dict()

num_year = NUM_YEAR
num_wind_code = NUM_WIND_CODE

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

if __name__ == "__main__":

    delist_delist_dict = get_annual_on_dict(on=False, year_genre='fiscal')

    for ii_factor_name, ii_criterion in screen_criterion.items():

        print("Now factor {0} is being dealt with...".format(ii_factor_name))
        path_data = "/home/aeront/PycharmProjects/TXLCScreen/FactorReservoir"
        filename_data = ii_criterion[0]
        path_filename_data = "".join([path_data, "/", filename_data])
        if ii_criterion[3] not in ["+", "-"]:
            print("criterion error.")
            os._exit(1)

        df_factor_slice = pd.read_pickle(path_filename_data, compression='bz2')
        if df_factor_slice.shape != (num_year, num_wind_code):
            print("The size of the  sliced factor {0} error.".format(ii_factor_name))
            os._exit(1)

        path_output = "/home/aeront/PycharmProjects/TXLCScreen/Output"
        excel_output_filename = ii_criterion[1]
        filename_output = "".join([path_output, "/", excel_output_filename])

        df_factor_anl = df_factor_slice
        # a = df_factor_anl.rolling(3, axis=0)
        df_factor_anl3avg = df_factor_anl.rolling(3, axis=0).mean()
        if ii_criterion[3] == '+':
            df_select_anl = df_factor_anl >= ii_criterion[2]
        else:
            df_select_anl = df_factor_anl <= ii_criterion[2]

        if ii_criterion[5] is None:
            df_select_anl3avg = df_factor_anl3avg.applymap(lambda _: True)
        elif ii_criterion[5] == '+':
            df_select_anl3avg = df_factor_anl3avg >= ii_criterion[4]
        else:
            df_select_anl3avg = df_factor_anl3avg <= ii_criterion[4]

        df_select_scr = df_select_anl & df_select_anl3avg

        with pd.ExcelWriter(filename_output) as writer:

            for index, row in df_factor_slice.iterrows():

                delist_anl_list = delist_delist_dict[index]
                row_select = df_select_scr.loc[index, :]
                row_select.loc[delist_anl_list] = False
                row_filtered = row[row_select]
                row_filtered = row_filtered.to_frame()
                row_filtered.reset_index(inplace=True)
                row_filtered.columns = ["Wind Code", "Value"]
                if ii_criterion[3] == '+':
                    row_filtered.sort_values(by=["Value"], ascending=False, inplace=True)
                    row_filtered.reset_index(drop=True, inplace=True)
                else:
                    row_filtered.sort_values(by=["Value"], ascending=True, inplace=True)
                    row_filtered.reset_index(drop=True, inplace=True)

                if isinstance(row_filtered, pd.DataFrame):
                    row_filtered.to_excel(writer, sheet_name=index)


    a=1
