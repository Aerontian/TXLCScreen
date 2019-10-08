# -*- coding: UTF-8 -*
import os
import pandas as pd
import shutil
from DataLoading import factor_param_dict
import numpy as np

path_source = \
    "/home/aeront/PycharmProjects/TXLCScreen/FactorReservoir"
path_destination = \
    "/home/aeront/PycharmProjects/TXLCScreen/FactorReservoir"


def factor_creation_originate(factor_code):

    pass
    # file_name = factor_param_dict[factor_code][2]
    # source_file = ''.join([path_source, '/', file_name])
    # destination_file = ''.join([path_destination, '/', file_name])
    # shutil.copyfile(source_file, destination_file)


# def factor_creation_tot_cash_dividend(factor_dict):
#
#     factor_code_shr = "SHR"
#     factor_code_cash_dvd = "CASH_DVD"
#
#     filename_source = "".join(["factor_", factor_dict[factor_code_shr][1], "_df_slice_update.dat"])
#     source_file = ''.join([path_source, '/', filename_source])
#     df_shr_slice = pd.read_pickle(source_file, compression='bz2')
#
#     filename_source = "".join(["factor_", factor_dict[factor_code_cash_dvd][1], "_df_slice_update.dat"])
#     source_file = ''.join([path_source, '/', filename_source])
#     df_cash_dvd_slice = pd.read_pickle(source_file, compression='bz2')
#
#     if df_shr_slice.shape == df_cash_dvd_slice.shape:
#         pass
#     else:
#         print("df_shr_slice and df_cash_dvd_slice differ in shape.")
#         return None
#
# #################################################################################
#
#     def tot_cash_dividend(x, y):
#         if np.isnan(x) or np.isnan(y):
#             return np.nan
#         else:
#             return x * 10000 * y
#
#     mat_opr = np.frompyfunc(tot_cash_dividend, 2, 1)
#     tot_cash_np_array = mat_opr(df_shr_slice.values, df_cash_dvd_slice.values)
#     df_tot_cash_slice = pd.DataFrame(tot_cash_np_array, index=df_shr_slice.index, columns=df_shr_slice.columns)
# #################################################################################
#
#     file_name = "factor_tot_cash_dividend_df_slice_update.dat"
#     path_file_name = ''.join([path_destination, '/', file_name])
#     df_tot_cash_slice.to_pickle(path_file_name, compression='bz2')


def factor_creation_ratio_dividend_yield(factor_dict):

    factor_code_shr = "SHR"
    factor_code_cash_dvd = "CASH_DVD"
    factor_code_s_val_mv = "S_VAL_MV"

    file_name = factor_dict[factor_code_shr][2]
    source_file = ''.join([path_source, '/', file_name])
    factor_shr_df = pd.read_pickle(source_file, compression='bz2')

    file_name = factor_dict[factor_code_cash_dvd][2]
    source_file = ''.join([path_source, '/', file_name])
    factor_cash_dvd_df = pd.read_pickle(source_file, compression='bz2')

    file_name = factor_dict[factor_code_s_val_mv][2]
    source_file = ''.join([path_source, '/', file_name])
    factor_s_val_mv_df = pd.read_pickle(source_file, compression='bz2')

    if factor_shr_df.shape == factor_cash_dvd_df.shape == factor_s_val_mv_df.shape:
        (row_num, column_num) = factor_shr_df.shape
    else:
        print("factor_shr_df , factor_cash_dvd_df and factor_s_val_mv_df differ in shape.")
        return None

    factor_shr_np_array = factor_shr_df.values.flatten(order='C')
    factor_cash_dvd_np_array = factor_cash_dvd_df.values.flatten(order='C')
    factor_s_val_mv_np_array = factor_s_val_mv_df.values.flatten(order='C')


#################################################################################

    def ratio_dividend_yield(x, y, z):
        if np.isnan(x) or np.isnan(y) or np.isnan(z) or z == 0:
            return np.nan
        else:
            return x * 10000 * y / (z * 10000)

    factor_ratio_dividend_yield_np_array = \
        map(ratio_dividend_yield,
            factor_shr_np_array,
            factor_cash_dvd_np_array,
            factor_s_val_mv_np_array)

#################################################################################

    factor_ratio_dividend_yield_np_array = \
        np.reshape(factor_ratio_dividend_yield_np_array, (row_num, column_num))

    factor_ratio_dividend_yield_df = pd.DataFrame(factor_ratio_dividend_yield_np_array)
    factor_ratio_dividend_yield_df.index = factor_s_val_mv_df.index
    factor_ratio_dividend_yield_df.columns = factor_s_val_mv_df.columns

    file_name = "factor_Ratio_Dividend_Yield_df_slice_update.dat"
    path_file_name = ''.join([path_destination, '/', file_name])
    factor_ratio_dividend_yield_df.to_pickle(path_file_name, compression='bz2')


def factor_creation_debt2assets_minus_goodwill(factor_dict):

    factor_code_debt2assets = "debt2assets"
    factor_code_assets = "ASSETS"
    factor_code_goodwill = "GOODWILL"

    filename_source = "".join(["factor_", factor_dict[factor_code_debt2assets][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_debt2assets_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_assets][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_assets_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_goodwill][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_goodwill_slice = pd.read_pickle(source_file, compression='bz2')

    if df_debt2assets_slice.shape == df_assets_slice.shape and \
            df_goodwill_slice.shape == df_goodwill_slice.shape:
        pass
    else:
        print("df_debt2assets_slice, df_assets_slice and df_goodwill_slice differ in shape.")
        return None

#################################################################################
    def func_debt2assets_minus_goodwill(x, y, z):
        if np.isnan(x) or np.isnan(y) or np.isnan(z) or x - z == 0:
            return np.nan
        else:
            return x * y / 100.0 / (x - z) * 100.0

    mat_opt = np.frompyfunc(func_debt2assets_minus_goodwill, 3, 1)
    debt2assets_minus_goodwill_np_array = \
        mat_opt(df_assets_slice.values, df_debt2assets_slice.values, df_goodwill_slice.values)
    df_debt2assets_minus_goodwill_slice = \
        pd.DataFrame(debt2assets_minus_goodwill_np_array,
                     index=df_assets_slice.index,
                     columns=df_assets_slice.columns)
#################################################################################

    file_name = "factor_debt2assets_minus_GOODWILL_df_slice_update.dat"
    path_file_name = ''.join([path_destination, '/', file_name])
    df_debt2assets_minus_goodwill_slice.to_pickle(path_file_name, compression='bz2')


def factor_creation_cash(factor_dict):

    factor_code_monetary = "MONETARY"
    factor_code_cur_assets = "CUR_ASSETS"

    filename_source = "".join(["factor_", factor_dict[factor_code_monetary][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_monetary_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_cur_assets][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_code_cur_assets_slice = pd.read_pickle(source_file, compression='bz2')

    if df_monetary_slice.shape == df_code_cur_assets_slice.shape:
        pass
    else:
        print("df_monetary_slice and df_code_cur_assets_slice differ in shape.")
        return None

#################################################################################

    def func_add(x, y):
        if np.isnan(x) or np.isnan(y):
            return np.nan
        else:
            return x + y

    mat_opt = np.frompyfunc(func_add, 2, 1)
    cash_np_array = mat_opt(df_monetary_slice.values, df_code_cur_assets_slice.values)
#################################################################################

    df_cash_slice = \
        pd.DataFrame(cash_np_array, index=df_monetary_slice.index, columns=df_monetary_slice.columns)

    file_name = "factor_CASH_df_slice_update.dat"
    path_file_name = ''.join([path_destination, '/', file_name])
    df_cash_slice.to_pickle(path_file_name, compression='bz2')


def factor_creation_cash_guarantee(factor_dict):

    factor_code_monetary = "MONETARY"
    factor_code_cur_assets = "CUR_ASSETS"
    factor_code_oper_rev = "OPER_REV"

    filename_source = "".join(["factor_", factor_dict[factor_code_monetary][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_monetary_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_cur_assets][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_cur_assets_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_oper_rev][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_oper_rev_slice = pd.read_pickle(source_file, compression='bz2')

    if df_monetary_slice.shape == df_cur_assets_slice.shape == df_oper_rev_slice.shape:
        pass
    else:
        print("df_monetary_slice, df_cur_assets_slice and  df_oper_rev_slice differ in shape.")
        return None

#################################################################################

    def func_cash_guarantee(x, y, z):
        if np.isnan(x) or np.isnan(y) or np.isnan(z) or z == 0:
            return np.nan
        else:
            return (x + y) / z * 100.0

    mat_opt = np.frompyfunc(func_cash_guarantee, 3, 1)
    cash_guarantee_np_array = \
        mat_opt(df_monetary_slice.values, df_cur_assets_slice.values, df_oper_rev_slice.values)
    df_cash_guarantee_slice = \
        pd.DataFrame(cash_guarantee_np_array, index=df_monetary_slice.index, columns=df_monetary_slice.columns)
#################################################################################

    file_name = "factor_CASH_GUARANTEE_df_slice_update.dat"
    path_file_name = ''.join([path_destination, '/', file_name])
    df_cash_guarantee_slice.to_pickle(path_file_name, compression='bz2')


def factor_creation_ratio_tot_rcv_to_sale(factor_dict):

    factor_code_rcv = "RCV"
    factor_code_pre_pay = "PRE_PAY"
    factor_code_oth_rcv = "OTH_RCV"
    factor_oper_rcv = "OPER_REV"

    filename_source = "".join(["factor_", factor_dict[factor_code_rcv][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_rcv_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_pre_pay][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_pre_pay_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_oth_rcv][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_oth_rcv_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_oper_rcv][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_oper_rcv_slice = pd.read_pickle(source_file, compression='bz2')

    if df_rcv_slice.shape == df_pre_pay_slice.shape \
            == df_oth_rcv_slice.shape == df_oper_rcv_slice.shape:
        pass
    else:
        print("df_rcv_slice, df_pre_pay_slice, df_oth_rcv_slice and  df_oper_rcv_slice differ in shape.")
        return None

#################################################################################

    def func_ratio_tot_rcv_to_sale(x, y, z, h):
        if np.isnan(x) or np.isnan(y) or np.isnan(z) or np.isnan(h) or h == 0:
            return np.nan
        else:
            return (x + y + z) / h * 100.0

    mat_opt = np.frompyfunc(func_ratio_tot_rcv_to_sale, 4, 1)
    ratio_tot_rcv_to_sale_np_array = \
        mat_opt(df_rcv_slice.values,
                df_pre_pay_slice.values,
                df_oth_rcv_slice.values,
                df_oper_rcv_slice.values)
    df_ratio_tot_rcv_to_sale_slice = \
        pd.DataFrame(ratio_tot_rcv_to_sale_np_array, index=df_rcv_slice.index, columns=df_rcv_slice.columns)
#################################################################################

    file_name = "factor_RATIO_TOT_RCV_TO_SALE_df_slice_update.dat"
    path_file_name = ''.join([path_destination, '/', file_name])
    df_ratio_tot_rcv_to_sale_slice.to_pickle(path_file_name, compression='bz2')


def factor_creation_ratio_inventories_to_sale(factor_dict):

    factor_code_inventories = "INVENTORIES"
    factor_code_oper_rev = "OPER_REV"

    filename_source = "".join(["factor_", factor_dict[factor_code_inventories][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_inventories_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_oper_rev][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_oper_rev_slice = pd.read_pickle(source_file, compression='bz2')

    if df_inventories_slice.shape == df_oper_rev_slice.shape:
        pass
    else:
        print("df_inventories_slice and df_oper_rev_slice differ in shape.")
        return None

#################################################################################

    def fuc_divide(x, y):
        if np.isnan(x) or np.isnan(y) or y == 0:
            return np.nan
        else:
            return x / y * 100.0

    mat_opt = np.frompyfunc(fuc_divide, 2, 1)
    ratio_inventories_to_sale_np_array = mat_opt(df_inventories_slice.values, df_oper_rev_slice.values)
    df_ratio_inventories_to_sale_slice = \
        pd.DataFrame(ratio_inventories_to_sale_np_array, index=df_inventories_slice.index, columns=df_inventories_slice.columns)

#################################################################################

    file_name = "factor_RATIO_INVENTORIES_TO_SALE_df_slice_update.dat"
    path_file_name = ''.join([path_destination, '/', file_name])
    df_ratio_inventories_to_sale_slice.to_pickle(path_file_name, compression='bz2')


def factor_creation_gross_profit_ratio(factor_dict):

    factor_code_cost = "COST"
    factor_code_oper_rev = "OPER_REV"

    filename_source = "".join(["factor_", factor_dict[factor_code_cost][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_cost_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_oper_rev][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_oper_rev_slice = pd.read_pickle(source_file, compression='bz2')

    if df_cost_slice.shape == df_oper_rev_slice.shape:
        pass
    else:
        print("df_cost_slice and df_oper_rev_slice differ in shape.")
        return None

#################################################################################

    def func_gross_profit_ratio(x, y):
        if np.isnan(x) or np.isnan(y) or y == 0:
            return np.nan
        else:
            return (y - x) / y * 100.0

    mat_opt = np.frompyfunc(func_gross_profit_ratio, 2, 1)
    gross_profit_ratio_np_array = mat_opt(df_cost_slice, df_oper_rev_slice)
    df_gross_profit_ratio_slice = \
        pd.DataFrame(gross_profit_ratio_np_array, index=df_cost_slice.index, columns=df_cost_slice.columns)

#################################################################################

    file_name = "factor_GROSS_PROFIT_RATIO_df_slice_update.dat"
    path_file_name = ''.join([path_destination, '/', file_name])
    df_gross_profit_ratio_slice.to_pickle(path_file_name, compression='bz2')


def factor_creation_ratio_sendimentation_to_sale(factor_dict):

    factor_code_inventories = "INVENTORIES"
    factor_code_rcv = "RCV"
    factor_code_oth_rcv = "OTH_RCV"
    factor_code_oper_rev = "OPER_REV"

    filename_source = "".join(["factor_", factor_dict[factor_code_inventories][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_inventories_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_rcv][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_rcv_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_oth_rcv][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_oth_rcv_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_oper_rev][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_oper_rev_slice = pd.read_pickle(source_file, compression='bz2')

    if df_inventories_slice.shape == df_rcv_slice.shape\
            == df_oth_rcv_slice.shape == df_oper_rev_slice.shape:
        pass
    else:
        print("df_inventories_slice, df_rcv_slice, df_oth_rcv_slice and df_oper_rev_slice differ in shape.")
        return None

#################################################################################

    def func_ratio_sendimentation_to_sale(x, y, z, h):
        if np.isnan(x) or np.isnan(y) or np.isnan(z) or np.isnan(h) or h == 0:
            return np.nan
        else:
            return (x + y + z) / h * 100.0

    mat_opt = np.frompyfunc(func_ratio_sendimentation_to_sale, 4, 1)
    ratio_sendimentation_to_sale_np_array = \
        mat_opt(df_inventories_slice.values, df_rcv_slice.values, df_oth_rcv_slice.values, df_oper_rev_slice.values)
    df_ratio_sendimentation_to_sale = \
        pd.DataFrame(ratio_sendimentation_to_sale_np_array,
                     index=df_inventories_slice.index,
                     columns=df_inventories_slice.columns)

#################################################################################

    file_name = "factor_GRATIO_SENDIMENTATION_TO_SALE_df_slice_update.dat"
    path_file_name = ''.join([path_destination, '/', file_name])
    df_ratio_sendimentation_to_sale.to_pickle(path_file_name, compression='bz2')


def factor_creation_net_profit_ratio(factor_dict):

    factor_net_profit = "net_profit"
    factor_code_oper_rev = "OPER_REV"

    filename_source = "".join(["factor_", factor_dict[factor_net_profit][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_net_profit_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_oper_rev][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_oper_rev_slice = pd.read_pickle(source_file, compression='bz2')

    if df_net_profit_slice.shape == df_oper_rev_slice.shape:
        pass
    else:
        print("df_net_profit_slice and df_oper_rev_slice differ in shape.")
        return None

#################################################################################

    def func_net_profit_ratio(x, y):
        if np.isnan(x) or np.isnan(y) or y == 0:
            return np.nan
        else:
            return (y - x) / y * 100.0

    mat_opt = np.frompyfunc(func_net_profit_ratio, 2, 1)
    net_profit_ratio_np_array = mat_opt(df_net_profit_slice.values, df_oper_rev_slice.values)
    df_net_profit_ratio_slice = \
        pd.DataFrame(net_profit_ratio_np_array, index=df_net_profit_slice.index, columns=df_net_profit_slice.columns)
#################################################################################

    file_name = "factor_NET_PROFIT_RATIO_df_slice_update.dat"
    path_file_name = ''.join([path_destination, '/', file_name])
    df_net_profit_ratio_slice.to_pickle(path_file_name, compression='bz2')


def factor_creation_management_cost_ratio(factor_dict):

    factor_net_profit = "net_profit"
    factor_code_oper_rev = "OPER_REV"
    factor_code_cost = "COST"

    filename_source = "".join(["factor_", factor_dict[factor_net_profit][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_net_profit_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_oper_rev][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_code_oper_rev_slice = pd.read_pickle(source_file, compression='bz2')

    filename_source = "".join(["factor_", factor_dict[factor_code_cost][1], "_df_slice_update.dat"])
    source_file = ''.join([path_source, '/', filename_source])
    df_cost_slice = pd.read_pickle(source_file, compression='bz2')

    if df_net_profit_slice.shape == df_code_oper_rev_slice.shape == df_cost_slice.shape:
        pass
    else:
        print("df_net_profit_slice, df_code_oper_rev_slice and df_oper_rev_slice differ in shape.")
        return None

#################################################################################

    def func_management_cost_ratio(x, y, z):
        if np.isnan(x) or np.isnan(y) or np.isnan(z) or z == 0:
            return np.nan
        else:
            return (z - x - y) / z * 100.0

    mat_opt = np.frompyfunc(func_management_cost_ratio, 3, 1)
    management_cost_np_array = \
        mat_opt(df_net_profit_slice.values,
                df_cost_slice.values,
                df_code_oper_rev_slice.values)
    df_management_cost_slice = \
        pd.DataFrame(management_cost_np_array, index=df_net_profit_slice.index, columns=df_net_profit_slice.columns)
#################################################################################

    file_name = "factor_MANAGEMENT_COST_df_slice_update.dat"
    path_file_name = ''.join([path_destination, '/', file_name])
    df_management_cost_slice.to_pickle(path_file_name, compression='bz2')

#     file_name = factor_dict[factor_code][2]
#     source_file = ''.join([path_source, '/', file_name])
#     destination_file = ''.join([path_destination, '/', file_name])
#     factor_source_df = pd.read_pickle(source_file, compression='bz2')
#     factor_destination_df = factor_source_df.apply(lambda item: item)
#     factor_destination_df.to_pickle(destination_file, compression='bz2')


factor_creation_function_dict = dict()
# factor_creation_function_dict['TOT_CASH_DIVIDEND'] = \
#     factor_creation_tot_cash_dividend
# factor_creation_function_dict['Ratio_Dividend_Yield'] = \
#     factor_creation_ratio_dividend_yield
factor_creation_function_dict['debt2assets_minus_GOODWILL'] =\
    factor_creation_debt2assets_minus_goodwill
factor_creation_function_dict['CASH'] =\
    factor_creation_cash
factor_creation_function_dict['CASH_GUARANTEE'] = \
    factor_creation_cash_guarantee
factor_creation_function_dict['RATIO_TOT_RCV_TO_SALE'] = \
    factor_creation_ratio_tot_rcv_to_sale
factor_creation_function_dict['RATIO_INVENTORIES_TO_SALE'] = \
    factor_creation_ratio_inventories_to_sale
factor_creation_function_dict['GROSS_PROFIT_RATIO'] = \
    factor_creation_gross_profit_ratio
factor_creation_function_dict['RATIO_SENDIMENTATION_TO_SALE'] = \
    factor_creation_ratio_sendimentation_to_sale
factor_creation_function_dict['NET_PROFIT_RATIO'] = \
    factor_creation_net_profit_ratio
factor_creation_function_dict['MANAGEMENT_COST_RATIO'] = \
    factor_creation_management_cost_ratio


def factor_creation_combination(factor_code, factor_dict, factor_creation_function_dict):
    func_call = factor_creation_function_dict[factor_code]
    if func_call:
        func_call(factor_dict)
    else:
        print("The function to be called does not exist.")
        os._exit(1)


factor_creation_list = list()
"""
info = (factor_name, factor_type)
factor_type: 'O' is for original, 'C' if for combination
"""

'''
主要指标:

基本每股收益：EPS
基本每股净资产：BPS
加权平均净资产收益率：WAA
ROA: ROA
每股经营活动产生的现金流量净额：OCFPS
总股本（万股）: SHR
'''

'''
基本每股收益
'''
info = ('EPS', 'O')
factor_creation_list.append(info)
'''
基本每股净资产
'''
info = ('BPS', 'O')
factor_creation_list.append(info)
'''
加权平均净资产收益率
'''
info = ('WAA', 'O')
factor_creation_list.append(info)
'''
ROA
'''
info = ('ROA', 'O')
factor_creation_list.append(info)
'''
每股经营活动产生的现金流量净额
'''
info = ('OCFPS', 'O')
factor_creation_list.append(info)
'''
总股本
'''
info = ('SHR', 'O')
factor_creation_list.append(info)

'''
资产状况:

资产负债率(%): debt2assets
资产总计（元）：ASSETS
商誉(元): GOODWILL
扣除商誉资产负债率（%）: debt2assets_minus_GOODWILL
货币资金（元）： MONETARY
其他流动资产（元）: CUR_ASSETS
现金（元）： CASH
经营现金保证率（%）: CASH_GUARANTEE
应收账款（元）：RCV
预付账款（元）: PRE_PAY
其他应收账款（元）： OTH_RCV
总应收账款与销售额之比（%）: RATIO_TOT_RCV_TO_SALE
存货（元）: INVENTORIES
存货与销售额之比（%）: RATION_INVENTORIES_TO_SALE
'''

'''
资产负债率(%)
'''
info = ('debt2assets', 'O')
factor_creation_list.append(info)
'''
资产总计（元
'''
info = ('ASSETS', 'O')
factor_creation_list.append(info)
'''
商誉(元)
'''
info = ('GOODWILL', 'O')
factor_creation_list.append(info)
'''
扣除商誉资产负债率（%）
'''
info = ('debt2assets_minus_GOODWILL', 'C')
factor_creation_list.append(info)
'''
货币资金（元）
'''
info = ('MONETARY', 'O')
factor_creation_list.append(info)
'''
其他流动资产（元）
'''
info = ('CUR_ASSETS', 'O')
factor_creation_list.append(info)
'''
现金（元）
'''
info = ('CASH', 'C')
factor_creation_list.append(info)
'''
经营现金保证率（%）
'''
info = ('CASH_GUARANTEE', 'C')
factor_creation_list.append(info)
'''
应收账款（元）
'''
info = ('RCV', 'O')
factor_creation_list.append(info)
'''
预付账款（元）
'''
info = ('PRE_PAY', 'O')
factor_creation_list.append(info)
'''
其他应收账款（元）
'''
info = ('OTH_RCV', 'O')
factor_creation_list.append(info)
'''
总应收账款与销售额之比（%）
'''
info = ('RATIO_TOT_RCV_TO_SALE', 'C')
factor_creation_list.append(info)
'''
存货（元）
'''
info = ('INVENTORIES', 'O')
factor_creation_list.append(info)
'''
存货与销售额之比（%）
'''
info = ('RATIO_INVENTORIES_TO_SALE', 'C')
factor_creation_list.append(info)


'''
运营能力：
营业毛利润率（%）：GROSS_PROFIT_RATIO
营业净利润率（%）：NET_PROFIT_RATIO
管理成本 （%）： MANAGEMENT_COST_RATIO
营业收入（元）：OPER_REV
营业收入同比增长率（%）：YOY_OR
沉淀资金与销售额之比（%）： RATIO_SENDIMENTATION_TO_SALE
'''

'''
营业毛利润率（%）
'''
info = ('GROSS_PROFIT_RATIO', 'C')
factor_creation_list.append(info)

'''
营业净利润率（%）
'''
info = ('NET_PROFIT_RATIO', 'C')
factor_creation_list.append(info)

'''
管理成本 （%）
'''
info = ('MANAGEMENT_COST_RATIO', 'C')
factor_creation_list.append(info)

'''
营业收入（元）
'''
info = ('OPER_REV', 'O')
factor_creation_list.append(info)

'''
营业收入同比增长率（%）
'''
info = ('YOY_OR', 'O')
factor_creation_list.append(info)

'''
沉淀资金与销售额之比（%）
'''
info = ('RATIO_SENDIMENTATION_TO_SALE', 'C')
factor_creation_list.append(info)


if __name__ == "__main__":

    # for ii_factor_tuple in factor_creation_list:
    #     if ii_factor_tuple[1] == "C":
    #         factor_name = ii_factor_tuple[0]
    #         factor_creation_combination(factor_name, factor_param_dict, factor_creation_function_dict)
    #         print("factor: {0}(Combination) is done.".format(factor_name))
    #     else:
    #         print("factor: {0}(Origin) is done.".format(ii_factor_tuple[0]))

    factor_creation_combination('debt2assets_minus_GOODWILL', factor_param_dict, factor_creation_function_dict)
    factor_creation_combination('CASH', factor_param_dict, factor_creation_function_dict)
    factor_creation_combination('CASH_GUARANTEE', factor_param_dict, factor_creation_function_dict)
    factor_creation_combination('RATIO_TOT_RCV_TO_SALE', factor_param_dict, factor_creation_function_dict)
    factor_creation_combination('RATIO_INVENTORIES_TO_SALE', factor_param_dict, factor_creation_function_dict)
    factor_creation_combination('GROSS_PROFIT_RATIO', factor_param_dict, factor_creation_function_dict)
    factor_creation_combination('RATIO_SENDIMENTATION_TO_SALE', factor_param_dict, factor_creation_function_dict)
    factor_creation_combination('NET_PROFIT_RATIO', factor_param_dict, factor_creation_function_dict)
    factor_creation_combination('RATIO_SENDIMENTATION_TO_SALE', factor_param_dict, factor_creation_function_dict)
    factor_creation_combination('MANAGEMENT_COST_RATIO', factor_param_dict, factor_creation_function_dict)



