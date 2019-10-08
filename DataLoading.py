# -*- coding: UTF-8 -*
from YearDate import *

'''
the factor param tuple is as follows:

    (key_word_factor, key_word_factor_columns, 
    key_word_factor_file_name, key_word_wind_code, 
    key_word_trade_date, data_base_name, 
    date_type, statement_type)
'''

factor_param_dict = dict()
'''
基本每股收益
'''
factor_param_dict['EPS'] = \
    ("S_FA_EPS_BASIC", "EPS", "factor_EPS_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

factor_param_dict['BPS'] = \
    ("S_FA_BPS", "BPS", "factor_BPS_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

'''
加权平均净资产收益率
'''
factor_param_dict['WAA'] = \
    ("WAA_ROE", "WAA", "factor_WAA_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator",  "REPORT_PERIOD", None)

'''
ROA
'''
factor_param_dict['ROA'] = \
    ("S_FA_ROA", "ROA", "factor_ROA_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

'''
每股经营活动产生的现金流量净额
'''
factor_param_dict['OCFPS'] = \
    ("S_FA_OCFPS", "OCFPS", "factor_OCFPS_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator",  "REPORT_PERIOD", None)


'''
总股本（万股）
'''
factor_param_dict['SHR'] = \
    ("TOT_SHR", "SHR", "factor_SHR_df_update.dat",
     "S_INFO_WINDCODE", "CHANGE_DT", "UADMIN.AShareCapitalization",  "CHANGE_DT")

'''
期末总股本（股）
'''
factor_param_dict['TOT_SHR_REPORT'] = \
    ("TOT_SHR", "SHR", "factor_TOT_SHR_REPORT_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
资产总计（元）
'''
factor_param_dict['ASSETS'] = \
    ("TOT_ASSETS", "ASSETS", "factor_ASSETS_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

'''
商誉
'''
factor_param_dict['GOODWILL'] = \
    ("GOODWILL", "GOODWILL", "factor_GOODWILL_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

'''
货币资金（元）
'''
factor_param_dict['MONETARY'] = \
    ("MONETARY_CAP", "MONETARY", "factor_MONETARY_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

'''
其他流动资产
'''
factor_param_dict['CUR_ASSETS'] = \
    ("OTH_CUR_ASSETS", "CUR_ASSETS", "factor_CUR_ASSETS_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")


'''
应收账款
'''
factor_param_dict['RCV'] = \
    ("ACCT_RCV", "RCV", "factor_CUR_RCV_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

'''
预收账款
'''
factor_param_dict['PRE_PAY'] = \
    ("PREPAY", "PRE_PAY", "factor_PRE_PAY_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

'''
其它应收账款
'''
factor_param_dict['OTH_RCV'] = \
    ("OTH_RCV", "OTH_RCV", "factor_OTH_RCV_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

'''
存货
'''
factor_param_dict['INVENTORIES'] = \
    ("INVENTORIES", "INVENTORIES", "factor_INVENTORIES_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", '408001000')

'''
营业收入
'''
factor_param_dict['OPER_REV'] = \
    ("OPER_REV", "OPER_REV", "factor_OPER_REV_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", '408001000')

'''
营业收入同比增长率(%)
'''
factor_param_dict['YOY_OR'] = \
    ("S_FA_YOY_OR", "YOY_OR", "factor_YOY_OR_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

'''
营业总成本
'''
factor_param_dict['COST'] = \
    ("TOT_OPER_COST", "COST", "factor_COST_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

'''
净利润
'''
factor_param_dict["net_profit"] = \
    ("S_FA_DEDUCTEDPROFIT",  "net_profit", "factor_net_profit_df_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareFinancialIndicator",  "REPORT_PERIOD", None)

'''
资产负债率
'''
factor_param_dict["debt2assets"] = \
    ("S_FA_DEBTTOASSETS",  "debt2assets", "factor_debt2assets_df.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareFinancialIndicator",  "REPORT_PERIOD", None)


def get_pct_data():
    """
        :return: pct data in dataframe format
    """

    pct_path_filename_source = \
        '/home/aeront/PycharmProjects/LocalDataBase(YFFormat)/DataReservoir/factor_pct_df_update.dat'
    pct_df = pd.read_pickle(pct_path_filename_source, compression='bz2')
    pct_df.fillna(0.0, inplace=True)

    return pct_df


def get_index_data():
    """
    :return: SZZZ index data in dataframe format
    """

    # path_filename_source = \
    #     "/home/aeront/PycharmProjects/LocalDataBase(YFFormat)/DataReservoir/index_SZZZ_close_df_update.dat"
    path_filename_source = \
        "/home/aeront/PycharmProjects/LocalDataBase(YFFormat)/DataReservoir/index_equ_weighted_update.dat"
    index_df = pd.read_pickle(path_filename_source, compression='bz2')

    return index_df

