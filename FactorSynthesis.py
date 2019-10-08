# -*- coding: UTF-8 -*
import pandas as pd
import numpy as np
"""
The module is the set of the functions create all the synthesis factors.
"""

raw_data_dict = dict()

'''
净资产收益率(扣除非经常损益)
'''
raw_data_dict["roe"] = \
    ("ROE_DILUTED",  "净资产收益率(扣除非经常损益)", "factor_roe_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareANNFinancialIndicator",  "REPORT_PERIOD", None)

'''
应收票据
'''
raw_data_dict["notes_rcv"] = \
    ("NOTES_RCV",  "应收票据", "factor_notes_rcv_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
固定资产
'''
raw_data_dict["fix_assets"] = \
    ("FIX_ASSETS",  "固定资产", "factor_fix_assets_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
在建工程
'''
raw_data_dict["const_in_prog"] = \
    ("CONST_IN_PROG",  "在建工程", "factor_const_in_prog_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
研发支出
'''
raw_data_dict["r_d_costs"] = \
    ("R_AND_D_COSTS",  "研发支出", "factor_r_d_costs_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
长期待摊费用
'''
raw_data_dict["long_tern_deferred_exp"] = \
    ("LONG_TERM_DEFERRED_EXP",  "长期待摊费用", "factor_long_tern_deferred_exp_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
递延所得税资产
'''
raw_data_dict["deferred_tax_assets"] = \
    ("DEFERRED_TAX_ASSETS",  "递延所得税资产", "factor_deferred_tax_assets_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
非流动资产合计
'''
raw_data_dict["tot_non_cur_assets"] = \
    ("TOT_NON_CUR_ASSETS",  "非流动资产合计", "factor_tot_non_cur_assets_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
短期借款
'''
raw_data_dict["st_borrow"] = \
    ("ST_BORROW",  "短期借款", "factor_st_borrow_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
应付账款
'''
raw_data_dict["acct_payable"] = \
    ("ACCT_PAYABLE",  "应付账款", "factor_acct_payable_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
应付职工薪酬
'''
raw_data_dict["empl_ben_payable"] = \
    ("EMPL_BEN_PAYABLE",  "应付职工薪酬", "factor_empl_ben_payable_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
应缴税费
'''
raw_data_dict["taxes_surcharges_payable"] = \
    ("TAXES_SURCHARGES_PAYABLE",  "应缴税费", "factor_taxes_surcharges_payable_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
应付利息
'''
raw_data_dict["int_payable"] = \
    ("INT_PAYABLE",  "应付利息", "factor_int_payable_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
其他应付款
'''
raw_data_dict["oth_payable"] = \
    ("OTH_PAYABLE",  "其他应付款", "factor_oth_payable_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
一年到期的非流动负债
'''
raw_data_dict["non_cur_liab_due_within_1y"] = \
    ("NON_CUR_LIAB_DUE_WITHIN_1Y",  "一年到期的非流动负债", "factor_non_cur_liab_due_within_1y_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
流动负债合计
'''
raw_data_dict["tot_cur_liab"] = \
    ("TOT_CUR_LIAB",  "流动负债合计", "factor_tot_cur_liab_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
长期借款
'''
raw_data_dict["lt_borrow"] = \
    ("LT_BORROW",  "长期借款", "factor_lt_borrow_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
 应付债券
 '''
raw_data_dict["bonds_payable"] = \
    ("BONDS_PAYABLE",  "应付债券", "factor_bonds_payable_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
长期应付款
'''
raw_data_dict["lt_payable"] = \
    ("LT_PAYABLE",  "长期应付款", "factor_lt_payable_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
递延所得税负债
'''
raw_data_dict["deferred_tax_liab"] = \
    ("DEFERRED_TAX_LIAB",  "递延所得税负债", "factor_deferred_tax_liab_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
非流动负债合计
'''
raw_data_dict["tot_non_cur_liab"] = \
    ("TOT_NON_CUR_LIAB",  "非流动负债合计", "factor_tot_non_cur_liab_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
负债合计
'''
raw_data_dict["tot_liab"] = \
    ("TOT_LIAB",  "负债合计", "factor_tot_liab_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
资本公积金
'''
raw_data_dict["cap_rsrv"] = \
    ("CAP_RSRV",  "资本公积金", "factor_cap_rsrv_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
盈余公积金
'''
raw_data_dict["surplus_rsrv"] = \
    ("SURPLUS_RSRV",  "盈余公积金", "factor_surplus_rsrv_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
未分配利润
'''
raw_data_dict["undistributed_profit"] = \
    ("UNDISTRIBUTED_PROFIT",  "未分配利润", "factor_undistributed_profit_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
股东权益合计(不含少数股东权益)
'''
raw_data_dict["equity"] = \
    ("TOT_SHRHLDR_EQY_EXCL_MIN_INT",  "股东权益合计(不含少数股东权益)",
     "factor_equity_df_slice_update.dat", "S_INFO_WINDCODE",
     "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

'''
负债及股东权益总计
'''
raw_data_dict["tot_liab_shrhldr_eqy"] = \
    ("TOT_LIAB_SHRHLDR_EQY",  "负债及股东权益总计", "factor_tot_liab_shrhldr_eqy_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")

# '''
# Earnings盈余能力
# '''
'''
净利润(扣非)
'''
raw_data_dict["net_profit"] = \
    ("S_FA_DEDUCTEDPROFIT",  "净利润(扣非)", "factor_net_profit_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareFinancialIndicator",  "REPORT_PERIOD", None)


# '''
# Productivity经营效率
# '''
'''
资产负债率
'''
raw_data_dict["debt2assets"] = \
    ("S_FA_DEBTTOASSETS",  "资产负债率", "factor_debt2assets_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareFinancialIndicator",  "REPORT_PERIOD", None)

'''
经营活动产生的现金流量净额
'''
raw_data_dict["oper_net_cash_flow"] = \
    ("NET_CASH_FLOWS_OPER_ACT",  "经营活动产生的现金流量净额", "factor_oper_net_cash_flow_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareCashFlow",  "REPORT_PERIOD", '408001000')
'''
投资活动产生的现金流量净额
'''
raw_data_dict["invest_net_cash_flow"] = \
    ("NET_CASH_FLOWS_INV_ACT",  "投资活动产生的现金流量净额", "factor_invest_net_cash_flow_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD",  "UADMIN.AShareCashFlow",  "REPORT_PERIOD", "408001000")
#
# '''
# Quality盈余质量
# '''
#
'''
基本每股收益
'''
raw_data_dict['eps'] = \
    ("S_FA_EPS_BASIC", "基本每股收益", "factor_eps_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome",  "REPORT_PERIOD", "408001000")

'''
基本每股净资产
'''
raw_data_dict['bps'] = \
    ("S_FA_BPS", "基本每股净资产", "factor_bps_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator",  "REPORT_PERIOD", None)

'''
加权平均净资产收益率
'''
raw_data_dict['waa'] = \
    ("WAA_ROE", "加权平均净资产收益率", "factor_waa_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator",  "REPORT_PERIOD", None)

'''
每股经营活动产生的现金流量净额
'''
raw_data_dict['ocfps'] = \
    ("S_FA_OCFPS", "每股经营活动产生的现金流量净额", "factor_ocfps_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator",  "REPORT_PERIOD", None)

'''
总股本（万股）
'''
raw_data_dict['tot_shr'] = \
    ("TOT_SHR", "总股本（万股）", "factor_tot_shr_df_slice_update.dat",
     "S_INFO_WINDCODE", "CHANGE_DT", "UADMIN.AShareCapitalization",  "CHANGE_DT", None)

'''
期末总股本（股）
'''
raw_data_dict['tot_shr_report'] = \
    ("TOT_SHR", "期末总股本", "factor_tot_shr_report_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet",  "REPORT_PERIOD", "408001000")


'''
资产总计（元）
'''
raw_data_dict['assets'] = \
    ("TOT_ASSETS", "资产总计", "factor_assets_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

'''
商誉
'''
raw_data_dict['goodwill'] = \
    ("GOODWILL", "商誉", "factor_goodwill_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

'''
货币资金（元）
'''
raw_data_dict['monetary'] = \
    ("MONETARY_CAP", "货币资金", "factor_monetary_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

'''
 其他流动资产
'''
raw_data_dict['cur_assets'] = \
    ("OTH_CUR_ASSETS", "其他流动资产", "factor_cur_assets_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

'''
应收账款
'''
raw_data_dict['rcv'] = \
    ("ACCT_RCV", "应收账款", "factor_rcv_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

'''
预付款项
'''
raw_data_dict['prepay'] = \
    ("PREPAY", "预付款项", "factor_prepay_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

'''
其它应收账款
'''
raw_data_dict['oth_rcv'] = \
    ("OTH_RCV", "其它应收账款", "factor_oth_rcv_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

'''
存货
'''
raw_data_dict['inventories'] = \
    ("INVENTORIES", "存货", "factor_inventories_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

'''
营业收入
'''
raw_data_dict['oper_rcv'] = \
    ("OPER_REV", "营业收入", "factor_oper_rcv_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", '408001000')

'''
营业收入同比增长率(%)
'''
raw_data_dict['oper_rcv_yor_or'] = \
    ("S_FA_YOY_OR", "营业收入同比增长率(%)", "factor_oper_rcv_yor_or_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

'''
ROA
'''
raw_data_dict['roa'] = \
    ("S_FA_ROA", "ROA", "factor_roa_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

'''
营业总成本
'''
raw_data_dict['cost'] = \
    ("TOT_OPER_COST", "营业总成本", "factor_cost_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
营业总收入
"""
raw_data_dict['tot_oper_rev'] = \
    ("TOT_OPER_REV", "营业总收入", "factor_tot_oper_rev_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")


"""
营业税金及附加
"""
raw_data_dict['less_taxes_surcharges_ops'] = \
    ("LESS_TAXES_SURCHARGES_OPS", "营业税金及附加", "factor_less_taxes_surcharges_ops_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
减：销售费用
"""
raw_data_dict['less_selling_dist_exp'] = \
    ("LESS_SELLING_DIST_EXP", "减：销售费用", "factor_less_selling_dist_exp_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
减：管理费用
"""
raw_data_dict['less_gerl_admin_exp'] = \
    ("LESS_GERL_ADMIN_EXP", "减：管理费用", "factor_less_gerl_admin_exp_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
减：财务费用
"""
raw_data_dict['less_fin_exp'] = \
    ("LESS_FIN_EXP", "减：财务费用", "factor_less_fin_exp_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
# 减：资产减值损失
# """
raw_data_dict['less_impair_loss_assets'] = \
    ("LESS_IMPAIR_LOSS_ASSETS", "减：资产减值损失", "factor_less_impair_loss_assets_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
加：投资净收益
"""
raw_data_dict['plus_net_invest_inc'] = \
    ("PLUS_NET_INVEST_INC", "加：投资净收益", "factor_plus_net_invest_inc_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
营业利润
"""
raw_data_dict['oper_profit'] = \
    ("OPER_PROFIT", "营业利润", "factor_oper_profit_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
减：营业外支出
"""
raw_data_dict['less_non_oper_exp'] = \
    ("LESS_NON_OPER_EXP", "减：营业外支出", "factor_less_non_oper_exp_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
加：营业外收入
"""
raw_data_dict['plus_non_oper_rev'] = \
    ("PLUS_NON_OPER_REV", "加：营业外收入", "factor_plus_non_oper_rev_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
利润总额
"""
raw_data_dict['tot_profit'] = \
    ("TOT_PROFIT", "利润总额", "factor_tot_profit_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
所得税费用
"""
raw_data_dict['inc_tax'] = \
    ("INC_TAX", "所得税费用", "factor_inc_tax_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
净利润(不含少数股东损益)
"""
raw_data_dict['net_profit_excl'] = \
    ("NET_PROFIT_EXCL_MIN_INT_INC", "净利润(不含少数股东损益)", "factor_net_profit_excl_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
净利润(含少数股东损益)  
"""
raw_data_dict['net_profit_incl'] = \
    ("NET_PROFIT_INCL_MIN_INT_INC", "净利润(含少数股东损益)  ", "factor_net_profit_incl_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
经营活动现金流入小计
"""
raw_data_dict['oper_cash_flow_in'] = \
    ("STOT_CASH_INFLOWS_OPER_ACT", "经营活动现金流入小计", "factor_oper_cash_flow_in_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", "408001000")

"""
经营活动现金流出小计
"""
raw_data_dict['oper_cash_flow_out'] = \
    ("STOT_CASH_OUTFLOWS_OPER_ACT", "经营活动现金流出小计", "factor_oper_cash_flow_out_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", "408001000")

"""
投资活动现金流入小计
"""
raw_data_dict['invest_cash_flow_in'] = \
    ("STOT_CASH_INFLOWS_INV_ACT", "投资活动现金流入小计", "factor_invest_cash_flow_in_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", "408001000")

"""
投资活动现金流出小计
"""
raw_data_dict['invest_cash_flow_out'] = \
    ("STOT_CASH_OUTFLOWS_INV_ACT", "投资活动现金流出小计", "factor_invest_cash_flow_out_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", "408001000")

"""
筹资活动现金流入小计
"""
raw_data_dict['fin_cash_flow_in'] = \
    ("STOT_CASH_INFLOWS_FNC_ACT", "筹资活动现金流入小计", "factor_fin_cash_flow_in_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", "408001000")

"""
筹资活动现金流出小计
"""
raw_data_dict['fin_cash_flow_out'] = \
    ("STOT_CASH_OUTFLOWS_FNC_ACT", "筹资活动现金流出小计", "factor_fin_cash_flow_out_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", "408001000")

"""
筹资活动产生的现金流量净额
"""
raw_data_dict['fin_net_cash_flow'] = \
    ("NET_CASH_FLOWS_FNC_ACT", "筹资活动产生的现金流量净额", "factor_fin_net_cash_flow_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", "408001000")

"""
汇率变动对现金的影响
"""
raw_data_dict['eff_fx_flu_cash'] = \
    ("EFF_FX_FLU_CASH", "汇率变动对现金的影响", "factor_eff_fx_flu_cash_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", "408001000")

"""
现金及现金等价物净增加额
"""
raw_data_dict['net_incr_cash_cash_equ'] = \
    ("NET_INCR_CASH_CASH_EQU", "现金及现金等价物净增加额", "factor_net_incr_cash_cash_equ_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", "408001000")

"""
期初现金及现金等价物余额
"""
raw_data_dict['cash_cash_equ_beg_period'] = \
    ("CASH_CASH_EQU_BEG_PERIOD", "期初现金及现金等价物余额", "factor_cash_cash_equ_beg_period_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", "408001000")

"""
期末现金及现金等价物余额
"""
raw_data_dict['cash_cash_equ_end_period'] = \
    ("CASH_CASH_EQU_END_PERIOD", "期末现金及现金等价物余额", "factor_cash_cash_equ_end_period_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", "408001000")

"""
加：资产减值准备
"""
raw_data_dict['plus_prov_depr_assets'] = \
    ("PLUS_PROV_DEPR_ASSETS", "资产减值准备", "factor_plus_prov_depr_assets_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", "408001000")

"""
折旧（固定资产折旧、油气资产折旧、生产性生物资产折旧）
"""
raw_data_dict['depr_fa_coga_dpba'] = \
    ("DEPR_FA_COGA_DPBA", "折旧", "factor_depr_fa_coga_dpba_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", "408001000")

'''
每股派息(元)
'''
raw_data_dict['cash_dvd'] = \
    ("CASH_DVD_PER_SH_PRE_TAX", "每股派息", "factor_cash_dvd_df_slice_update.dat",
     "S_INFO_WINDCODE", "DVD_PAYOUT_DT", "UADMIN.AShareDividend", "DVD_PAYOUT_DT", None)


'''
派息比例
分红率
'''
raw_data_dict['cash_dividend_ratio'] = \
    ("CASH_DIVIDEND_RATIO", "派息比例", "factor_cash_dividend_ratio_df_slice_update.dat",
     "S_INFO_WINDCODE", "EX_DATE", "UADMIN.AShareEXRightDividendRecord", "EX_DATE", None)

"""
职工奖金福利
"""
raw_data_dict['workers_welfare'] = \
    ("WORKERS_WELFARE", "职工奖金福利", "factor_workers_welfare_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
无形资产
"""
raw_data_dict['intang_assets'] = \
    ("INTANG_ASSETS", "无形资产", "factor_intang_assets_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

"""
总资产周转率
"""
raw_data_dict['assets_turn'] = \
    ("S_FA_ASSETSTURN", "总资产周转率", "factor_assets_turn_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
固定资产周转率
"""
raw_data_dict['fa_turn'] = \
    ("S_FA_FATURN", "固定资产周转率", "factor_fa_turn_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
流动资产周转率
"""
raw_data_dict['ca_turn'] = \
    ("S_FA_CATURN", "流动资产周转率", "factor_ca_turn_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
预收款项
"""
raw_data_dict['adv_from_cust'] = \
    ("ADV_FROM_CUST", "预收款项", "factor_adv_from_cust_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", None)

"""
有形资产
"""
raw_data_dict['tangible_assets'] = \
    ("S_FA_TANGIBLEASSET", "有形资产", "factor_tangible_assets_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
带息债务
"""
raw_data_dict['int_debt'] = \
    ("S_FA_INTERESTDEBT", "带息债务", "factor_int_debt_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
净债务
"""
raw_data_dict['net_debt'] = \
    ("S_FA_NETDEBT", "净债务", "factor_net_debt_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
息税折旧前利润
"""
raw_data_dict['ebit'] = \
    ("EBIT", "息税折旧前利润", "factor_ebit_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
息税折旧摊销前利润
"""
raw_data_dict['ebitda'] = \
    ("EBITDA", "息税折旧摊销前利润", "factor_ebitda_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareIncome", "REPORT_PERIOD", "408001000")

"""
财务费用：利息费用
"""
raw_data_dict['fin_exp'] = \
    ("S_STMNOTE_FINEXP", "财务费用：利息费用", "factor_fin_exp_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
企业自由现金流量(FCFF)
"""
raw_data_dict['fcff'] = \
    ("FREE_CASH_FLOW", "企业自由现金流量(FCFF)", "factor_fcff_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", "408001000")

"""
全部投入资本
"""
raw_data_dict['invest_capital'] = \
    ("S_FA_INVESTCAPITAL", "全部投入资本", "factor_invest_capital_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
流动资产合计
"""
raw_data_dict['tot_cur_assets'] = \
    ("TOT_CUR_ASSETS", "流动资产合计", "factor_tot_cur_assets_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

"""
可供出售金融资产
"""
raw_data_dict['fin_assets_avail_for_sale'] = \
    ("FIN_ASSETS_AVAIL_FOR_SALE", "可供出售金融资产", "factor_fin_assets_avail_for_sale_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareBalanceSheet", "REPORT_PERIOD", "408001000")

"""
股权自由现金流量(FCFE)
"""
raw_data_dict['fcfe'] = \
    ("S_FA_FCFE", "股权自由现金流量", "factor_fcfe_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)


"""
每股留存收益
"""
raw_data_dict['rtps'] = \
    ("S_FA_RETAINEDPS", "每股留存收益", "factor_rtps_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
优先股
"""
raw_data_dict['prf_shr'] = \
    ("S_SHARE_NTRD_PRFSHARE", "优先股", "factor_prf_shr_df_slice_update.dat",
     "S_INFO_WINDCODE", "CHANGE_DT", "UADMIN.AShareCapitalization", "CHANGE_DT", None)


"""
每股现金净流量
"""
raw_data_dict['cfps'] = \
    ("S_FA_CFPS", "每股现金净流量", "factor_cfps_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
每股企业自由现金流量(元)
"""
raw_data_dict['fcffps'] = \
    ("S_FA_FCFFPS", "每股企业自由现金流量(元)", "factor_fcffps_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
每股股东自由现金流量(元)
"""
raw_data_dict['fcfeps'] = \
    ("S_FA_FCFEPS", "每股股东自由现金流量(元)", "factor_fcfeps_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)


"""
每股盈余公积（元）
"""
raw_data_dict['srps'] = \
    ("S_FA_SURPLUSRESERVEPS", "每股盈余公积", "factor_srps_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
每股资本公积（元）
"""
raw_data_dict['scps'] = \
    ("S_FA_SURPLUSCAPITALPS", "每股资本公积", "factor_scps_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
每股息税前利润（元）
"""
raw_data_dict['ebitps'] = \
    ("S_FA_EBITPS", "每股息税前利润", "factor_ebitps_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
每股营业收入（元）
"""
raw_data_dict['orps'] = \
    ("S_FA_ORPS", "每股营业收入", "factor_orps_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
每股营业总收入（元）
"""
raw_data_dict['grps'] = \
    ("S_FA_GRPS", "每股营业总收入", "factor_grps_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
每股未分配利润（元）
"""
raw_data_dict['udps'] = \
    ("S_FA_UNDISTRIBUTEDPS", "每股未分配利润", "factor_udps_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareFinancialIndicator", "REPORT_PERIOD", None)

"""
销售商品提供劳务收到的现金合计(元)
"""
raw_data_dict['cash_rev_sg_rs'] = \
    ("CASH_RECP_SG_AND_RS", "销售商品提供劳务收到的现金合计", "factor_cash_rev_sg_rs_df_slice_update.dat",
     "S_INFO_WINDCODE", "REPORT_PERIOD", "UADMIN.AShareCashFlow", "REPORT_PERIOD", None)


def get_raw_data(filename_source):
    """
            获得财务数据(按照年报切片)
            :return: the dataframe for data
            m * n: m fiscal years and n wind codes
    """
    """
    The path of the raw data files
    """
    path_source = "/home/aeront/PycharmProjects/TXLCScreen/FactorReservoir"
    """
    The filename of the raw data file
    """
    # filename_source = "".join(["factor_", data_id, "__df_slice_update.dat"])

    """
    The complete filename of the raw data files
    """
    path_filename_source = "".join([path_source, "/", filename_source])

    df_data_slice = pd.read_pickle(path_filename_source, compression='bz2')

    return df_data_slice


def get_eps(original_data_dict):
    """
        每股收益(EPS):EPS
        :return: the dataframe for EPS.
        m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['eps'][2]
    df_eps_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_eps_slice

    return df_syn_factor_slice


def get_eps_diluted(original_data_dict):
    """
           扣非每股收益: EPS_DILUTED
           :return: the dataframe for EPS_DILUTED
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['net_profit'][2]
    df_net_profit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_shr_report'][2]
    df_tot_shr_report_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_net_profit_slice / (df_tot_shr_report_slice * 10000)
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_bps(original_data_dict):
    """
           每股净资产(BPS): BPS
           :return: the dataframe for BPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['bps'][2]
    df_cash_dvd_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_cash_dvd_slice

    return df_syn_factor_slice


def get_dps(original_data_dict):
    """
           每股股利(DPS): DPS
           :return: the dataframe for DPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['cash_dvd'][2]
    df_dps_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_dps_slice

    return df_syn_factor_slice


def get_scps(original_data_dict):
    """
           每股资本公积: SCPS
           :return: the dataframe for SCPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['scps'][2]
    df_scps_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_scps_slice

    return df_syn_factor_slice


def get_srps(original_data_dict):
    """
           每股盈余公积: SRPS
           :return: the dataframe for SRPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['srps'][2]
    df_srps_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_srps_slice

    return df_syn_factor_slice


def get_grps(original_data_dict):
    """
           每股营业总收入: GRPS
           :return: the dataframe for GRPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['grps'][2]
    df_grps_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_grps_slice

    return df_syn_factor_slice


def get_orps(original_data_dict):
    """
           每股营业收入: ORPS
           :return: the dataframe for ORPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['orps'][2]
    df_orps_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_orps_slice

    return df_syn_factor_slice


def get_ebitps(original_data_dict):
    """
           每股息税前利润: EBITPS
           :return: the dataframe for EBITPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['ebitps'][2]
    df_ebitps_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_ebitps_slice

    return df_syn_factor_slice


def get_fcffps(original_data_dict):
    """
           每股企业自由现金流量: FCFFPS
           :return: the dataframe for FCFFPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['fcffps'][2]
    df_fcffps_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_fcffps_slice

    return df_syn_factor_slice


def get_fcfeps(original_data_dict):
    """
           每股股东自由现金流量: FCFEPS
           :return: the dataframe for FCFEPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['fcfeps'][2]
    df_fcfeps_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_fcfeps_slice

    return df_syn_factor_slice


def get_ebitdaps(original_data_dict):
    """
           每股EBITDA: EBITDAPS
           :return: the dataframe for EBITDAPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['ebitda'][2]
    df_ebitda_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_shr_report'][2]
    df_tot_shr_report_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_ebitda_slice / df_tot_shr_report_slice * 10000
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_rtps(original_data_dict):
    """
           每股留存收益: RTPS
           :return: the dataframe for RTPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['rtps'][2]
    df_rtps_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_rtps_slice

    return df_syn_factor_slice


def get_ncps(original_data_dict):
    """
           每股净流动资产: NCPS
           :return: the dataframe for NCPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_shr_report'][2]
    df_tot_shr_report_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = (df_tot_cur_assets_slice - df_tot_cur_liab_slice) / (df_tot_shr_report_slice * 10000)
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_udps(original_data_dict):
    """
           每股未分配利润: UDPS
           :return: the dataframe for UDPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['udps'][2]
    df_udps_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_udps_slice

    return df_syn_factor_slice


def get_cfps(original_data_dict):
    """
           每股现金净流量: CFPS
           :return: the dataframe for CFPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['cfps'][2]
    df_cfps_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_cfps_slice

    return df_syn_factor_slice


def get_ocfps(original_data_dict):
    """
           每股经营活动产生的现金流量净额: OCFPS
           :return: the dataframe for OCFPS
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['ocfps'][2]
    df_ocfps_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_ocfps_slice

    return df_syn_factor_slice


def get_waa(original_data_dict):
    """
           加权净资产收益率(ROE): WAA
           :return: the dataframe for WAA
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['waa'][2]
    df_waa_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_waa_slice

    return df_syn_factor_slice


def get_roa(original_data_dict):
    """
           总资产收益率(ROA)
           :return: the dataframe for ROA
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['roa'][2]
    df_roa_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_roa_slice

    return df_syn_factor_slice


def get_opr(original_data_dict):
    """
           经营性资产回报率: OPR
           :return: the dataframe for OPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_rcv_slice / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan
    return df_syn_factor_slice


def get_roic(original_data_dict):
    """
           投资回报率(ROIC): ROIC
           :return: the dataframe for ROIC
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_profit'][2]
    df_oper_profit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['invest_capital'][2]
    df_invest_capital_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_profit_slice / df_invest_capital_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan
    return df_syn_factor_slice


def get_rop(original_data_dict):
    """
           人力投入回报率(ROP): ROP
           :return: the dataframe for ROP
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['net_profit'][2]
    df_net_profit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['empl_ben_payable'][2]
    df_empl_ben_payable_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_net_profit_slice / df_empl_ben_payable_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_gpm(original_data_dict):
    """
           毛利率(GPM): GPM
           :return: the dataframe for GPM
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['cost'][2]
    df_cost_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = (df_oper_rcv_slice - df_cost_slice) / df_oper_rcv_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_npm(original_data_dict):
    """
           净利率(NPM): NPM
           :return: the dataframe for NPM
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['net_profit'][2]
    df_net_profit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_net_profit_slice / df_oper_rcv_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_mcr(original_data_dict):
    """
           管理成本率: MCR
           :return: the dataframe for MCR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['cost'][2]
    df_cost_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['net_profit'][2]
    df_net_profit_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        (df_oper_rcv_slice - df_cost_slice) / df_oper_rcv_slice * 100 \
        + df_net_profit_slice / df_oper_rcv_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_scr(original_data_dict):
    """
           销售成本率: SCR
           :return: the dataframe for SCR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['cost'][2]
    df_cost_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_cost_slice / df_oper_rcv_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_cer(original_data_dict):
    """
           资本支出比率: CER
           :return: the dataframe for CER
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['invest_net_cash_flow'][2]
    df_invest_net_cash_flow_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_invest_net_cash_flow_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_slcrtr(original_data_dict):
    """
           销售现金比率: SLCRTR
           :return: the dataframe for SLCRTR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['cash_rev_sg_rs'][2]
    df_cash_rev_sg_rs_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_cash_rev_sg_rs_slice / df_oper_rcv_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_gpoa(original_data_dict):
    """
           总资产毛利率(GPOA): GPOA
           :return: the dataframe for GPOA
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['cost'][2]
    df_cost_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = (df_oper_rcv_slice - df_cost_slice) / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ctar(original_data_dict):
    """
           现金总资产比率(CTAR): CTAR
           :return: the dataframe for CTAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['monetary'][2]
    df_monetary_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_monetary_slice / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_cnar(original_data_dict):
    """
           现金净利润率(CNAR): CNAR
           :return: the dataframe for CNAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['net_profit'][2]
    df_net_profit_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_net_profit_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_coir(original_data_dict):
    """
           现金营业收入比率(COIR): COIR
           :return: the dataframe for COIR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_rcv'][2]
    df_net_profit_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_net_profit_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_fle(original_data_dict):
    """
           财务杠杆效应(FLE): FLE
           :return: the dataframe for FLE
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['net_profit'][2]
    df_net_profit_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_rcv_slice / df_net_profit_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_cfo(original_data_dict):
    """
           经营性现金净流量 / 资产总计(CFO): CFO
           :return: the dataframe for CFO
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_cpr(original_data_dict):
    """
           成本费用利润率: CPR
           :return: the dataframe for CPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['net_profit'][2]
    df_net_profit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['cost'][2]
    df_cost_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['less_selling_dist_exp'][2]
    df_less_selling_dist_exp_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_net_profit_slice / (df_cost_slice + df_less_selling_dist_exp_slice) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_mobr(original_data_dict):
    """
           主营业务比率: MOBR
           :return: the dataframe for MOBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_oper_rev'][2]
    df_tot_oper_rev_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_rcv_slice / df_tot_oper_rev_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ebitr(original_data_dict):
    """
           息税前利润率: EBITR
           :return: the dataframe for EBITR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['ebit'][2]
    df_ebit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_ebit_slice / df_oper_rcv_slice * 200
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_nsocr(original_data_dict):
    """
           净销售额/运营资本: NSOCR
           :return: the dataframe for NSOCR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_rcv_slice / (df_tot_cur_assets_slice - df_tot_cur_liab_slice) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_laopr(original_data_dict):
    """
           资产减值损失/营业利润: LAOPR
           :return: the dataframe for LAOPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['less_impair_loss_assets'][2]
    df_less_impair_loss_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_profit'][2]
    df_oper_profit_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_less_impair_loss_assets_slice / df_oper_profit_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opm(original_data_dict):
    """
           营业利润率(OPM): OPM
           :return: the dataframe for OPM
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_profit'][2]
    df_oper_profit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_profit_slice / df_oper_rcv_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_tr(original_data_dict):
    """
           综合税负率: TR
           :return: the dataframe for TR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['taxes_surcharges_payable'][2]
    df_taxes_surcharges_payable_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_taxes_surcharges_payable_slice / df_oper_rcv_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_onctpr(original_data_dict):
    """
           经营活动净收益/利润总额: ONCTPR
           :return: the dataframe for ONCTPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_profit'][2]
    df_tot_profit_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_tot_profit_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_rpr(original_data_dict):
    """
           应收应付比率: RPR
           :return: the dataframe for RPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['rcv'][2]
    df_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['acct_payable'][2]
    df_acct_payable_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_rcv_slice / df_acct_payable_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_nonoptpr(original_data_dict):
    """
           营业外收支净额/利润总额: NONOPTPR
           :return: the dataframe for NONOPTPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['plus_non_oper_rev'][2]
    df_plus_non_oper_rev_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['less_non_oper_exp'][2]
    df_less_non_oper_exp_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_profit'][2]
    df_tot_profit_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = (df_plus_non_oper_rev_slice - df_less_non_oper_exp_slice) / df_tot_profit_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ttpr(original_data_dict):
    """
           所得税/利润总额: TTPR
           :return: the dataframe for TTPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['inc_tax'][2]
    df_inc_tax_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_profit'][2]
    df_tot_profit_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_inc_tax_slice / df_tot_profit_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_dptpr(original_data_dict):
    """
           扣除非经常损益后的净利润/净利润净利润(含少数股东损益): DPTPR
           :return: the dataframe for DPTPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['net_profit'][2]
    df_net_profit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['net_profit_incl'][2]
    df_net_profit_incl_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_net_profit_slice / df_net_profit_incl_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_arprr(original_data_dict):
    """
           预收款占营业收入比率: ARPRR
           :return: the dataframe for ARPRR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['adv_from_cust'][2]
    df_adv_from_cust_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_adv_from_cust_slice / df_oper_rcv_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opcar(original_data_dict):
    """
           资产现金收益率: OPCAR
           :return: the dataframe for OPCAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opcer(original_data_dict):
    """
           股东权益现金收益率: OPCER
           :return: the dataframe for OPCER
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opcclr(original_data_dict):
    """
           经营净现金比率: OPCCLR
           :return: the dataframe for OPCCLR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_tot_cur_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opctcr(original_data_dict):
    """
           全部现金流量比率: OPCTCR
           :return: the dataframe for OPCTCR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['fin_cash_flow_out'][2]
    df_fin_cash_flow_out_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['invest_cash_flow_out'][2]
    df_invest_cash_flow_out_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / (df_fin_cash_flow_out_slice + df_invest_cash_flow_out_slice) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opctlr(original_data_dict):
    """
           经营现金负债总额比: OPCTLR
           :return: the dataframe for OPCTLR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_tot_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opctar(original_data_dict):
    """
           全部资产现金回收率: OPCTAR
           :return: the dataframe for OPCTAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_npoi(original_data_dict):
    """
           净收益营运指数: NPOI
           :return: the dataframe for NPOI
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['net_profit'][2]
    df_net_profit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['net_profit_incl'][2]
    df_net_profit_incl_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_net_profit_slice / df_net_profit_incl_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_oprtoprr(original_data_dict):
    """
           营业利润/利润总额: OPRTOPRR
           :return: the dataframe for OPRTOPRR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_profit'][2]
    df_oper_profit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_profit'][2]
    df_tot_profit_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_profit_slice / df_tot_profit_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_sgrsroprr(original_data_dict):
    """
           销售商品提供劳务收到的现金/营业收入: SGRSROPRR
           :return: the dataframe for SGRSROPRR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['cash_rev_sg_rs'][2]
    df_cash_rev_sg_rs_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_cash_rev_sg_rs_slice / df_oper_rcv_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_oproppr(original_data_dict):
    """
           经营活动产生的现金流量净额/营业利润: OPROPPR
           :return: the dataframe for OPROPPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_profit'][2]
    df_oper_profit_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_oper_profit_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opncnpdr(original_data_dict):
    """
           经营活动产生的现金流量净额/经营活动净收益: OPNCNPDR
           :return: the dataframe for OPNCNPDR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['net_profit'][2]
    df_net_profit_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_net_profit_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_deprfar(original_data_dict):
    """
           折旧率: DEPRFAR
           :return: the dataframe for DEPRFAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['depr_fa_coga_dpba'][2]
    df_depr_fa_coga_dpba_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['fix_assets'][2]
    df_fix_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_depr_fa_coga_dpba_slice / df_fix_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_incdepr(original_data_dict):
    """
           资本支出/折旧和摊销: INCDEPR
           :return: the dataframe for INCDEPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['invest_net_cash_flow'][2]
    df_invest_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['depr_fa_coga_dpba'][2]
    df_depr_fa_coga_dpba_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_invest_net_cash_flow_slice / df_depr_fa_coga_dpba_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_onctorr(original_data_dict):
    """
           经营性现金净流量/营业总收入: ONCTORR
           :return: the dataframe for ONCTORR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_oper_rev'][2]
    df_tot_oper_rev_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_tot_oper_rev_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_oncfiair(original_data_dict):
    """
           经营性现金资本支出比率: ONCFIAIR
           :return: the dataframe for ONCFIAIR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['fix_assets'][2]
    df_fix_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / \
                          (df_fix_assets_slice + df_tot_cur_assets_slice + df_tot_cur_liab_slice) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opcdprr(original_data_dict):
    """
           经营性现金折旧费用比率: OPCDPRR
           :return: the dataframe for OPCDPRR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['depr_fa_coga_dpba'][2]
    df_depr_fa_coga_dpba_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_depr_fa_coga_dpba_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_cbgr(original_data_dict):
    """
           现金股利保障倍数: CBGR
           :return: the dataframe for CBGR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['net_profit'][2]
    df_net_profit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['cash_dividend_ratio'][2]
    df_cash_dividend_ratio_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / (df_net_profit_slice + df_cash_dividend_ratio_slice) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_prptcar(original_data_dict):
    """
           预付账款/流动资产: PRPTCAR
           :return: the dataframe for PRPTCAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['prepay'][2]
    df_prepay_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_prepay_slice / df_tot_cur_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_rcvar(original_data_dict):
    """
           应收账款/总资产: RCVAR
           :return: the dataframe for RCVAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['rcv'][2]
    df_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_rcv_slice / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_rcvtar(original_data_dict):
    """
           应收账款/流动资产: RCVTAR
           :return: the dataframe for RCVTAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['rcv'][2]
    df_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_rcv_slice / df_tot_cur_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_iaer(original_data_dict):
    """
           无形资产占净资产比率: IAER
           :return: the dataframe for IAER
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['intang_assets'][2]
    df_intang_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_intang_assets_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_fadprr(original_data_dict):
    """
           固定资产/折旧: FADPRR
           :return: the dataframe for FADPRR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['fix_assets'][2]
    df_fix_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['depr_fa_coga_dpba'][2]
    df_depr_fa_coga_dpba_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_fix_assets_slice / df_depr_fa_coga_dpba_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_mtcar(original_data_dict):
    """
           货币资金/流动资产: MTCAR
           :return: the dataframe for MTCAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['monetary'][2]
    df_monetary_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_monetary_slice / df_tot_cur_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_scoprr(original_data_dict):
    """
           销售现金比率: SCOPRR
           :return: the dataframe for SCOPRR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['cash_rev_sg_rs'][2]
    df_cash_rev_sg_rs_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_cash_rev_sg_rs_slice / df_oper_rcv_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_cr(original_data_dict):
    """
           现金比率(CR): CR
           :return: the dataframe for CR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['monetary'][2]
    df_monetary_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['fin_assets_avail_for_sale'][2]
    df_fin_assets_avail_for_sale_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = (df_monetary_slice + df_fin_assets_avail_for_sale_slice) / df_tot_cur_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ccclp(original_data_dict):
    """
           现金循环期: CCCLP
           :return: the dataframe for CCCLP
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['rcv'][2]
    df_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['inventories'][2]
    df_inventories_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['cost'][2]
    df_cost_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = (df_rcv_slice + df_inventories_slice) / df_cost_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opcfnpr(original_data_dict):
    """
           净利润现金含量: OPCFNPR
           :return: the dataframe for OPCFNPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['rcv'][2]
    df_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['inventories'][2]
    df_inventories_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['cost'][2]
    df_cost_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = (df_rcv_slice + df_inventories_slice) / df_cost_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_fcf(original_data_dict):
    """
           自由现金流(FCF): FCF
           :return: the dataframe for FCF
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['invest_net_cash_flow'][2]
    df_invest_net_cash_flow_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = (df_oper_net_cash_flow_slice - df_invest_net_cash_flow_slice)
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_fcff(original_data_dict):
    """
           企业自由现金流(FCFF): FCFF
           :return: the dataframe for FCFF
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['fcff'][2]
    df_fcff_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_fcff_slice

    return df_syn_factor_slice


def get_fcfe(original_data_dict):
    """
           股权自由现金流(FCFE): FCFE
           :return: the dataframe for FCFE
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['fcfe'][2]
    df_fcfe_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_fcfe_slice

    return df_syn_factor_slice


def get_opncinvr(original_data_dict):
    """
           现金占投资比率: OPNCINVR
           :return: the dataframe for OPNCINVR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['invest_net_cash_flow'][2]
    df_invest_net_cash_flow_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_invest_net_cash_flow_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_capexp(original_data_dict):
    """
           资本性支出: CAPEXP
           :return: the dataframe for CAPEXP
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['invest_net_cash_flow'][2]
    df_invest_net_cash_flow_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_invest_net_cash_flow_slice

    return df_syn_factor_slice


def get_nicce(original_data_dict):
    """
           现金及现金等价物净增加额: NICCE
           :return: the dataframe for NICCE
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['net_incr_cash_cash_equ'][2]
    df_net_incr_cash_cash_equ_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_net_incr_cash_cash_equ_slice

    return df_syn_factor_slice


def get_opnctcr(original_data_dict):
    """
           经营活动产生的现金流量净额占比: OPNCTCR
           :return: the dataframe for OPNCTCR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['invest_cash_flow_in'][2]
    df_invest_cash_flow_in_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['fin_cash_flow_in'][2]
    df_fin_cash_flow_in_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        df_oper_net_cash_flow_slice / \
        (df_oper_net_cash_flow_slice + df_invest_cash_flow_in_slice + df_fin_cash_flow_in_slice) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ivnctcr(original_data_dict):
    """
           投资活动产生的现金流量净额占比: IVNCTCR
           :return: the dataframe for IVNCTCR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['invest_cash_flow_in'][2]
    df_invest_cash_flow_in_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['fin_cash_flow_in'][2]
    df_fin_cash_flow_in_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        df_invest_cash_flow_in_slice / \
        (df_oper_net_cash_flow_slice + df_invest_cash_flow_in_slice + df_fin_cash_flow_in_slice) * 100

    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_finctcr(original_data_dict):
    """
           筹资活动产生的现金流量净额占比: FINCTCR
           :return: the dataframe for FINCTCR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['invest_cash_flow_in'][2]
    df_invest_cash_flow_in_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['fin_cash_flow_in'][2]
    df_fin_cash_flow_in_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        df_fin_cash_flow_in_slice / \
        (df_oper_net_cash_flow_slice + df_invest_cash_flow_in_slice + df_fin_cash_flow_in_slice) * 100

    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_tat(original_data_dict):
    """
           总资产周转率(TAT): TAT
           :return: the dataframe for TAT
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['assets_turn'][2]
    df_assets_turn_slice = get_raw_data(filename_source)


    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_assets_turn_slice

    return df_syn_factor_slice


def get_tatd(original_data_dict):
    """
           总资产周转天数: TATD
           :return: the dataframe for TATD
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['assets_turn'][2]
    df_assets_turn_slice = get_raw_data(filename_source)


    """
    The synthesis of the factors
    """
    df_syn_factor_slice = 365 / (df_assets_turn_slice / 100)

    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_fat(original_data_dict):
    """
           固定资产周转率(FAT): FAT
           :return: the dataframe for FAT
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['fa_turn'][2]
    df_fa_turn_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_fa_turn_slice

    return df_syn_factor_slice


def get_ncat(original_data_dict):
    """
           非流动资产周转率: NCAT
           :return: the dataframe for NCAT
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_non_cur_assets'][2]
    df_tot_non_cur_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_rcv_slice / df_tot_non_cur_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_lat(original_data_dict):
    """
           流动资产周转率(LAT): LAT
           :return: the dataframe for LAT
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['ca_turn'][2]
    df_ca_turn_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_ca_turn_slice

    return df_syn_factor_slice


def get_nat(original_data_dict):
    """
           净资产周转率(NAT): NAT
           :return: the dataframe for NAT
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_rcv_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_fatd(original_data_dict):
    """
           固定资产周转天数: FATD
           :return: the dataframe for FATD
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['fa_turn'][2]
    df_fa_turn_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = 365 / (df_fa_turn_slice / 100)
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_rat(original_data_dict):
    """
           应收账款周转率(RAT): RAT
           :return: the dataframe for RAT
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['rcv'][2]
    df_rcv_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_rcv_slice / df_rcv_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_dso(original_data_dict):
    """
           应收账款周转天数(DSO): DSO
           :return: the dataframe for DSO
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['rcv'][2]
    df_rcv_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = 365 / (df_oper_rcv_slice / df_rcv_slice)
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_apt(original_data_dict):
    """
           应付账款周转率: APT
           :return: the dataframe for APT
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['acct_payable'][2]
    df_acct_payable_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_rcv_slice / df_acct_payable_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_dpo(original_data_dict):
    """
           应付账款周转天数(DPO): DPO
           :return: the dataframe for DPO
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['acct_payable'][2]
    df_acct_payable_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = 365 / (df_oper_rcv_slice / df_acct_payable_slice)
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_int(original_data_dict):
    """
           存货周转率(INT): INT
           :return: the dataframe for INT
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['inventories'][2]
    df_inventories_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_rcv_slice / df_inventories_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_doh(original_data_dict):
    """
           存货周转天数(DOH): DOH
           :return: the dataframe for DOH
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['inventories'][2]
    df_inventories_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = 365 / (df_oper_rcv_slice / df_inventories_slice)
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_crpoppr(original_data_dict):
    """
           现金转换周期/营业周期: CRPOPPR
           :return: the dataframe for CRPOPPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['inventories'][2]
    df_inventories_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['rcv'][2]
    df_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['acct_payable'][2]
    df_acct_payable_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        365 / (df_oper_rcv_slice / df_inventories_slice) + \
        365 / (df_oper_rcv_slice / df_rcv_slice) + \
        365 / (df_oper_rcv_slice / df_acct_payable_slice)
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_cmgmi(original_data_dict):
    """
           成本管理指数: CMGMI
           :return: the dataframe for CMGMI
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['cost'][2]
    df_cost_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['less_selling_dist_exp'][2]
    df_less_selling_dist_exp_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['less_gerl_admin_exp'][2]
    df_less_gerl_admin_exp_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        (df_cost_slice + df_less_selling_dist_exp_slice + df_less_gerl_admin_exp_slice) / df_oper_rcv_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opct(original_data_dict):
    """
           营运资本周转率: OPCT
           :return: the dataframe for OPCT
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_cur_assets_slice / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_eqyt(original_data_dict):
    """
           资产负债率(TDR): EQYT
           :return: the dataframe for EQYT
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_rcv_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_tdr(original_data_dict):
    """
           资产负债率(TDR): TDR
           :return: the dataframe for TDR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['debt2assets'][2]
    df_debt2assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_debt2assets_slice

    return df_syn_factor_slice


def get_tder(original_data_dict):
    """
           产权比率: TDER
           :return: the dataframe for TDER
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_liab_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_tdmprp2a(original_data_dict):
    """
           剔除预收款项后的资产负债率: TDMPRP2A
           :return: the dataframe for TDMPRP2A
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['adv_from_cust'][2]
    df_adv_from_cust_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = (df_tot_liab_slice - df_adv_from_cust_slice) / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_dactr(original_data_dict):
    """
           坏账费用率: DACTR
           :return: the dataframe for DACTR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['plus_prov_depr_assets'][2]
    df_plus_prov_depr_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_plus_prov_depr_assets_slice / df_oper_rcv_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_eqyacc(original_data_dict):
    """
           账面净值: EQYACC
           :return: the dataframe for EQYACC
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_assets_slice - df_tot_liab_slice

    return df_syn_factor_slice


def get_dbtwtint(original_data_dict):
    """
           有息负债: DBTWTINT
           :return: the dataframe for DBTWTINT
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['st_borrow'][2]
    df_st_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['non_cur_liab_due_within_1y'][2]
    df_non_cur_liab_due_within_1y_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_st_borrow_slice + df_non_cur_liab_due_within_1y_slice + df_lt_borrow_slice

    return df_syn_factor_slice


def get_de(original_data_dict):
    """
           长期资本负债率(D/E): D/E
           :return: the dataframe for D/E
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_lt_borrow_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_falbr(original_data_dict):
    """
           固定资产/长期负债: FALBR
           :return: the dataframe for FALBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['fix_assets'][2]
    df_fix_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_fix_assets_slice / df_lt_borrow_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ltaar(original_data_dict):
    """
           长期资产适合率: LTAAR
           :return: the dataframe for LTAAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_non_cur_assets'][2]
    df_tot_non_cur_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = (df_equity_slice + df_lt_borrow_slice) / df_tot_non_cur_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_catar(original_data_dict):
    """
           流动资产/总资产: CATAR
           :return: the dataframe for CATAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_cur_assets_slice / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ncatar(original_data_dict):
    """
           非流动资产/总资产: NCATAR
           :return: the dataframe for NCATAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_non_cur_assets'][2]
    df_tot_non_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_non_cur_assets_slice / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_tatar(original_data_dict):
    """
           有形资产/总资产: TATAR
           :return: the dataframe for TATAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tangible_assets'][2]
    df_tangible_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tangible_assets_slice / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_catdr(original_data_dict):
    """
           流动资产/负债合计: CATDR
           :return: the dataframe for CATDR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_cur_assets_slice / df_tot_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ncatdr(original_data_dict):
    """
           非流动资产/负债合计: NCATDR
           :return: the dataframe for NCATDR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_non_cur_assets'][2]
    df_tot_non_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_non_cur_assets_slice / df_tot_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ncdeqyr(original_data_dict):
    """
           非流动负债权益比率: NCDEQYR
           :return: the dataframe for NCDEQYR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_non_cur_liab'][2]
    df_tot_non_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_non_cur_assets_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_cdeqyr(original_data_dict):
    """
           流动负债权益比率: CDEQYR
           :return: the dataframe for CDEQYR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_cur_liab_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_em(original_data_dict):
    """
           权益乘数(股本乘数)(EM): EM
           :return: the dataframe for EM
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_assets_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_eqyr(original_data_dict):
    """
           净资产比率: EQYR
           :return: the dataframe for EQYR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_equity_slice / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_far(original_data_dict):
    """
           资本固定化比率: FAR
           :return: the dataframe for FAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = (df_assets_slice - df_tot_cur_assets_slice) / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_fatar(original_data_dict):
    """
           固定资产比率: FATAR
           :return: the dataframe for FATAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['fix_assets'][2]
    df_fix_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_fix_assets_slice / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opncdbdr(original_data_dict):
    """
           现金到期债务比: OPNCDBDR
           :return: the dataframe for OPNCDBDR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['st_borrow'][2]
    df_st_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['non_cur_liab_due_within_1y'][2]
    df_non_cur_liab_due_within_1y_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        df_oper_net_cash_flow_slice / (df_st_borrow_slice + df_non_cur_liab_due_within_1y_slice) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opnclbr(original_data_dict):
    """
           现金流量/长期债务: OPNCLBR
           :return: the dataframe for OPNCLBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_lt_borrow_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opncdbr(original_data_dict):
    """
           经营现金债务保护比: OPNCDBR
           :return: the dataframe for OPNCDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_tot_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_dbwintinvcpr(original_data_dict):
    """
           带息债务/全部投入资本: DBWINTINVCPR
           :return: the dataframe for DBWINTINVCPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['st_borrow'][2]
    df_st_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['non_cur_liab_due_within_1y'][2]
    df_non_cur_liab_due_within_1y_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['invest_capital'][2]
    df_invest_capital_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        (df_st_borrow_slice + df_non_cur_liab_due_within_1y_slice + df_lt_borrow_slice) / df_invest_capital_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_npexcvcpr(original_data_dict):
    """
           归属母公司股东的权益/全部投入资本: NPEXCVCPR
           :return: the dataframe for NPEXCVCPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['st_borrow'][2]
    df_st_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['non_cur_liab_due_within_1y'][2]
    df_non_cur_liab_due_within_1y_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['invest_capital'][2]
    df_invest_capital_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        (df_st_borrow_slice + df_non_cur_liab_due_within_1y_slice + df_lt_borrow_slice) / df_invest_capital_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_npextdb(original_data_dict):
    """
           归属母公司股东的权益/负债总额: NPEXTDB
           :return: the dataframe for NPEXTDB
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['net_profit_excl'][2]
    df_net_profit_excl_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_net_profit_excl_slice / df_tot_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_npexdbwini(original_data_dict):
    """
           归属母公司股东的权益/带息债务: NPEXDBWINI
           :return: the dataframe for NPEXDBWINI
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['net_profit_excl'][2]
    df_net_profit_excl_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['st_borrow'][2]
    df_st_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['non_cur_liab_due_within_1y'][2]
    df_non_cur_liab_due_within_1y_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        df_net_profit_excl_slice / (df_st_borrow_slice + df_non_cur_liab_due_within_1y_slice + df_lt_borrow_slice) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_cdtdr(original_data_dict):
    """
           流动负债/总负债: CDTDR
           :return: the dataframe for CDTDR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_cur_liab_slice / df_tot_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ncdtdr(original_data_dict):
    """
           非流动负债/总负债: NCDTDR
           :return: the dataframe for NCDTDR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_non_cur_liab'][2]
    df_tot_non_cur_liab_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_non_cur_liab_slice / df_tot_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_tadbwinir(original_data_dict):
    """
           有形资产/带息债务: TADBWINIR
           :return: the dataframe for TADBWINIR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tangible_assets'][2]
    df_tangible_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['st_borrow'][2]
    df_st_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['non_cur_liab_due_within_1y'][2]
    df_non_cur_liab_due_within_1y_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        df_tangible_assets_slice / (df_st_borrow_slice + df_non_cur_liab_due_within_1y_slice + df_lt_borrow_slice) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_tandbr(original_data_dict):
    """
           有形资产/净债务: TANDBR
           :return: the dataframe for TANDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tangible_assets'][2]
    df_tangible_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['net_debt'][2]
    df_net_debt_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        df_tangible_assets_slice / df_net_debt_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_tatdbr(original_data_dict):
    """
           有形资产/总负债: TATDBR
           :return: the dataframe for TATDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tangible_assets'][2]
    df_tangible_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        df_tangible_assets_slice / df_tot_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ebittdbr(original_data_dict):
    """
           有形资产/息税折旧摊销前利润/负债合计: EBITTDBR
           :return: the dataframe for EBITTDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['ebit'][2]
    df_ebit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        df_ebit_slice / df_tot_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opnctdbr(original_data_dict):
    """
           经营活动产生的现金流量净额/负债合计: OPNCTDBR
           :return: the dataframe for OPNCTDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        df_oper_net_cash_flow_slice / df_tot_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opncdbwinir(original_data_dict):
    """
           经营活动产生的现金流量净额/带息债务: OPNCDBWINIR
           :return: the dataframe for OPNCDBWINIR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['st_borrow'][2]
    df_st_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['non_cur_liab_due_within_1y'][2]
    df_non_cur_liab_due_within_1y_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        df_oper_net_cash_flow_slice / \
        (df_st_borrow_slice + df_non_cur_liab_due_within_1y_slice + df_lt_borrow_slice) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opnccdbr(original_data_dict):
    """
           经营活动产生的现金流量净额/流动负债: OPNCCDBR
           :return: the dataframe for OPNCCDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_tot_cur_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opncndbr(original_data_dict):
    """
           经营活动产生的现金流量净额/净债务: OPNCNDBR
           :return: the dataframe for OPNCNDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['net_debt'][2]
    df_net_debt_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_net_debt_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opncncdbr(original_data_dict):
    """
           经营活动产生的现金流量净额/非流动负债: OPNCNCDBR
           :return: the dataframe for OPNCNCDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_non_cur_liab'][2]
    df_tot_non_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_tot_non_cur_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_nfnnccdbr(original_data_dict):
    """
           非筹资性现金净流量与流动负债的比率: NFNNCCDBR
           :return: the dataframe for NFNNCCDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['invest_net_cash_flow'][2]
    df_invest_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_non_cur_liab'][2]
    df_tot_non_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        (df_oper_net_cash_flow_slice + df_invest_net_cash_flow_slice) / df_tot_non_cur_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_nfnnctdbr(original_data_dict):
    """
           非筹资性现金净流量与负债总额的比率: NFNNCTDBR
           :return: the dataframe for NFNNCTDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['invest_net_cash_flow'][2]
    df_invest_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        (df_oper_net_cash_flow_slice + df_invest_net_cash_flow_slice) / df_tot_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_cfcr(original_data_dict):
    """
           现金流覆盖率(CFCR): CFCR
           :return: the dataframe for CFCR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['int_payable'][2]
    df_int_payable_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        (df_oper_net_cash_flow_slice + df_int_payable_slice) / df_int_payable_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_taeqydbr(original_data_dict):
    """
           有形资产净值债务率: TAEQYDBR
           :return: the dataframe for TAEQYDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['intang_assets'][2]
    df_intang_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        df_tot_liab_slice / (df_equity_slice - df_intang_assets_slice) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ndbeqyr(original_data_dict):
    """
           净债务/股权价值: NDBEQYR
           :return: the dataframe for NDBEQYR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['net_debt'][2]
    df_net_debt_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_net_debt_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_dbwinieqyr(original_data_dict):
    """
           带息债务/股权价值: DBWINIEQYR
           :return: the dataframe for DBWINIEQYR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['st_borrow'][2]
    df_st_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['non_cur_liab_due_within_1y'][2]
    df_non_cur_liab_due_within_1y_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        (df_st_borrow_slice + df_non_cur_liab_due_within_1y_slice + df_lt_borrow_slice) / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ebitdadbwinir(original_data_dict):
    """
           EBITDA/带息债务: EBITDADBWINIR
           :return: the dataframe for EBITDADBWINIR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['ebitda'][2]
    df_ebitda_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['st_borrow'][2]
    df_st_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['non_cur_liab_due_within_1y'][2]
    df_non_cur_liab_due_within_1y_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        df_ebitda_slice / (df_st_borrow_slice + df_non_cur_liab_due_within_1y_slice + df_lt_borrow_slice) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ebitdainiexpr(original_data_dict):
    """
           EBITDA/利息费用: EBITDAINIEXPR
           :return: the dataframe for EBITDAINIEXPR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['ebitda'][2]
    df_ebitda_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['fin_exp'][2]
    df_fin_exp_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_ebitda_slice / df_fin_exp_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_tdbebitdar(original_data_dict):
    """
           全部债务/EBITDA: TDBEBITDAR
           :return: the dataframe for TDBEBITDAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['ebitda'][2]
    df_ebitda_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_liab_slice / df_ebitda_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_inipyr(original_data_dict):
    """
           偿付比率: INIPYR
           :return: the dataframe for INIPYR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['net_profit'][2]
    df_net_profit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['fin_exp'][2]
    df_fin_exp_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_net_profit_slice / df_fin_exp_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_fnlvi(original_data_dict):
    """
           财务杠杆指数: FNLVI
           :return: the dataframe for FNLVI
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['waa'][2]
    df_waa_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['roa'][2]
    df_roa_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_waa_slice / df_roa_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_mntlbr(original_data_dict):
    """
           货币资金/短期债务: MNTLBR
           :return: the dataframe for MNTLBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['monetary'][2]
    df_monetary_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['st_borrow'][2]
    df_st_borrow_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_monetary_slice / df_st_borrow_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_mntcdbr(original_data_dict):
    """
           货币资金/流动负债: MNTCDBR
           :return: the dataframe for MNTCDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['monetary'][2]
    df_monetary_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_monetary_slice / df_tot_cur_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ccr(original_data_dict):
    """
           现金流动负债比率(CCR): CCR
           :return: the dataframe for CCR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_tot_cur_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opncfxr(original_data_dict):
    """
           现金支付利息能力比率: OPNCFXR
           :return: the dataframe for OPNCFXR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['fin_exp'][2]
    df_fin_exp_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_fin_exp_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opfcdbr(original_data_dict):
    """
           营业利润/流动负债: OPFCDBR
           :return: the dataframe for OPFCDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_profit'][2]
    df_oper_profit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_profit_slice / df_tot_cur_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opftdbr(original_data_dict):
    """
           营业利润/负债合计: OPFTDBR
           :return: the dataframe for OPFTDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_profit'][2]
    df_oper_profit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_profit_slice / df_tot_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_eqydbr(original_data_dict):
    """
           净资产负债率: EQYDBR
           :return: the dataframe for EQYDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['st_borrow'][2]
    df_st_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['monetary'][2]
    df_monetary_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        (df_st_borrow_slice + df_lt_borrow_slice - df_monetary_slice) / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_er(original_data_dict):
    """
           财务杠杆(产权比率)(ER): ER
           :return: the dataframe for ER
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_liab_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_icr(original_data_dict):
    """
           利息保障倍数(ICR): ICR
           :return: the dataframe for ICR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_liab_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ebitdainir(original_data_dict):
    """
           息税折旧及摊销前利润利息覆盖率: EBITDAINIR
           :return: the dataframe for EBITDAINIR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['ebitda'][2]
    df_ebitda_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['int_payable'][2]
    df_int_payable_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_ebitda_slice / df_int_payable_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_dted(original_data_dict):
    """
           股东权益比率(DTED): DTED
           :return: the dataframe for DTED
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_equity_slice / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_dbpyr(original_data_dict):
    """
           债务偿还率: DBPYR
           :return: the dataframe for DBPYR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['ebit'][2]
    df_ebit_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_ebit_slice / df_tot_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_cpexgr(original_data_dict):
    """
           资本支出保障倍数: CPEXGR
           :return: the dataframe for CPEXGR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['invest_net_cash_flow'][2]
    df_invest_net_cash_flow_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_oper_net_cash_flow_slice / df_invest_net_cash_flow_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ltdbr(original_data_dict):
    """
           长期负债比率(资本化比率): LTDBR
           :return: the dataframe for LTDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_liab'][2]
    df_tot_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_lt_borrow_slice / df_tot_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_lbopncr(original_data_dict):
    """
           长期负债/现金流量比: LBOPNCR
           :return: the dataframe for LBOPNCR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_lt_borrow_slice / df_oper_net_cash_flow_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_eqyfar(original_data_dict):
    """
           股东权益与固定资产比率: EQYFAR
           :return: the dataframe for EQYFAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['fix_assets'][2]
    df_fix_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_equity_slice / df_fix_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_ltbfcfr(original_data_dict):
    """
           长期债务/自由现金流: LTBFCFR
           :return: the dataframe for LTBFCFR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_net_cash_flow'][2]
    df_oper_net_cash_flow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['fix_assets'][2]
    df_fix_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        df_lt_borrow_slice / \
        (df_oper_net_cash_flow_slice - (df_fix_assets_slice - (df_tot_cur_assets_slice - df_tot_cur_liab_slice))) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_lbopcr(original_data_dict):
    """
           长期负债与营运资金比率: LBOPCR
           :return: the dataframe for LBOPCR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['lt_borrow'][2]
    df_lt_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_lt_borrow_slice / (df_tot_cur_assets_slice - df_tot_cur_liab_slice) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_cur(original_data_dict):
    """
           流动比率(CUR): CUR
           :return: the dataframe for CUR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_cur_assets_slice / df_tot_cur_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_qr(original_data_dict):
    """
           速动比率(QR): QR
           :return: the dataframe for QR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['inventories'][2]
    df_inventories_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = (df_tot_cur_assets_slice - df_inventories_slice) / df_tot_cur_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_mntar(original_data_dict):
    """
           现金/总资产比: MNTAR
           :return: the dataframe for MNTAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['monetary'][2]
    df_monetary_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assests_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_monetary_slice / df_assests_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_mnteqyr(original_data_dict):
    """
           现金/净资产比: MNTEQYR
           :return: the dataframe for MNTEQYR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['monetary'][2]
    df_monetary_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_monetary_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_rvqr(original_data_dict):
    """
           保守速动比率: RVQR
           :return: the dataframe for RVQR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['monetary'][2]
    df_monetary_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['fin_assets_avail_for_sale'][2]
    df_fin_assets_avail_for_sale_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['notes_rcv'][2]
    df_notes_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['rcv'][2]
    df_rcv_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = \
        (df_monetary_slice + df_fin_assets_avail_for_sale_slice + df_notes_rcv_slice + df_rcv_slice) / \
        df_tot_cur_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_opcp(original_data_dict):
    """
           运营资本: OPCP
           :return: the dataframe for OPCP
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['tot_cur_assets'][2]
    df_tot_cur_assets_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_tot_cur_assets_slice - df_tot_cur_liab_slice

    return df_syn_factor_slice


def get_mntdbdr(original_data_dict):
    """
           现金到期债务比: MNTDBDR
           :return: the dataframe for MNTDBDR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['monetary'][2]
    df_monetary_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['st_borrow'][2]
    df_st_borrow_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['non_cur_liab_due_within_1y'][2]
    df_non_cur_liab_due_within_1y_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_monetary_slice / (df_st_borrow_slice + df_non_cur_liab_due_within_1y_slice) * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_mntinigr(original_data_dict):
    """
           现金流量利息保障倍数: MNTINIGR
           :return: the dataframe for MNTINIGR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['monetary'][2]
    df_monetary_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['fin_exp'][2]
    df_fin_exp_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_monetary_slice / df_fin_exp_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_incceqtcdbr(original_data_dict):
    """
           现金比率: INCCEQTCDBR
           :return: the dataframe for INCCEQTCDBR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['net_incr_cash_cash_equ'][2]
    df_net_incr_cash_cash_equ_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['tot_cur_liab'][2]
    df_tot_cur_liab_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_net_incr_cash_cash_equ_slice / df_tot_cur_liab_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_gweqyr(original_data_dict):
    """
           商誉占净资产比率: GWEQYR
           :return: the dataframe for GWEQYR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['goodwill'][2]
    df_goodwill_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_goodwill_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_rdor(original_data_dict):
    """
           商誉收入比率(RDOR): RDOR
           :return: the dataframe for RDOR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['goodwill'][2]
    df_goodwill_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['oper_rcv'][2]
    df_oper_rcv_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_goodwill_slice / df_oper_rcv_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_gwar(original_data_dict):
    """
           商誉占总资产比率: GWAR
           :return: the dataframe for GWAR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['goodwill'][2]
    df_goodwill_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['assets'][2]
    df_assets_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_goodwill_slice / df_assets_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


def get_itaeqyr(original_data_dict):
    """
           无形资产占净资产比率: ITAEQYR
           :return: the dataframe for ITAEQYR
           m * n: m fiscal years and n wind codes
    """
    """
    Get the raw data
    """
    filename_source = original_data_dict['goodwill'][2]
    df_goodwill_slice = get_raw_data(filename_source)

    filename_source = original_data_dict['equity'][2]
    df_equity_slice = get_raw_data(filename_source)

    """
    The synthesis of the factors
    """
    df_syn_factor_slice = df_goodwill_slice / df_equity_slice * 100
    df_syn_factor_slice[np.isinf(df_syn_factor_slice)] = np.nan

    return df_syn_factor_slice


get_syn_factor_dict = dict()
get_syn_factor_dict['EPS'] = get_eps
get_syn_factor_dict['EPS_DILUTED'] = get_eps_diluted
get_syn_factor_dict['BPS'] = get_bps
get_syn_factor_dict['DPS'] = get_dps
get_syn_factor_dict['SCPS'] = get_scps
get_syn_factor_dict['SRPS'] = get_srps
get_syn_factor_dict['GRPS'] = get_grps
get_syn_factor_dict['ORPS'] = get_orps
get_syn_factor_dict['EBITPS'] = get_ebitps
get_syn_factor_dict['FCFFPS'] = get_fcffps
get_syn_factor_dict['FCFEPS'] = get_fcfeps
get_syn_factor_dict['EBITDAPS'] = get_ebitdaps

get_syn_factor_dict['RTPS'] = get_rtps
get_syn_factor_dict['NCPS'] = get_ncps
get_syn_factor_dict['UDPS'] = get_udps
get_syn_factor_dict['CFPS'] = get_cfps
get_syn_factor_dict['OCFPS'] = get_ocfps
get_syn_factor_dict['WAA'] = get_waa
get_syn_factor_dict['ROA'] = get_roa
get_syn_factor_dict['OPR'] = get_opr
get_syn_factor_dict['ROIC'] = get_roic
get_syn_factor_dict['ROP'] = get_rop
get_syn_factor_dict['GPM'] = get_fcffps
get_syn_factor_dict['NPM'] = get_npm
get_syn_factor_dict['MCR'] = get_mcr

get_syn_factor_dict['SCR'] = get_scr
get_syn_factor_dict['CER'] = get_cer
get_syn_factor_dict['SLCRTR'] = get_slcrtr
get_syn_factor_dict['GPOA'] = get_gpoa
get_syn_factor_dict['CTAR'] = get_ctar
get_syn_factor_dict['CNAR'] = get_cnar
get_syn_factor_dict['COIR'] = get_coir
get_syn_factor_dict['FLE'] = get_fle
get_syn_factor_dict['CFO'] = get_cfo
get_syn_factor_dict['CPR'] = get_cpr
get_syn_factor_dict['MOBR'] = get_mobr
get_syn_factor_dict['EBITR'] = get_ebitr

get_syn_factor_dict['NSOCR'] = get_nsocr
get_syn_factor_dict['LAOPR'] = get_laopr
get_syn_factor_dict['OPM'] = get_opm
get_syn_factor_dict['TR'] = get_tr
get_syn_factor_dict['ONCTPR'] = get_onctpr
get_syn_factor_dict['RPR'] = get_rpr
get_syn_factor_dict['NONOPTPR'] = get_nonoptpr
get_syn_factor_dict['TTPR'] = get_ttpr
get_syn_factor_dict['DPTPR'] = get_dptpr
get_syn_factor_dict['ARPRR'] = get_arprr
get_syn_factor_dict['OPCAR'] = get_opcar
get_syn_factor_dict['OPCER'] = get_opcer

get_syn_factor_dict['OPCCLR'] = get_opcclr
get_syn_factor_dict['OPCTCR'] = get_opctcr
get_syn_factor_dict['OPCTLR'] = get_opctlr
get_syn_factor_dict['OPCTAR'] = get_opctar
get_syn_factor_dict['NPOI'] = get_npoi
get_syn_factor_dict['OPRTOPRR'] = get_oprtoprr
get_syn_factor_dict['SGRSROPRR'] = get_sgrsroprr
get_syn_factor_dict['OPROPPR'] = get_oproppr
get_syn_factor_dict['OPNCNPDR'] = get_opncnpdr
get_syn_factor_dict['DEPRFAR'] = get_deprfar
get_syn_factor_dict['INCDEPR'] = get_incdepr
get_syn_factor_dict['INCDEPR'] = get_incdepr
get_syn_factor_dict['ONCTORR'] = get_onctorr

get_syn_factor_dict['ONCFIAIR'] = get_oncfiair
get_syn_factor_dict['OPCDPRR'] = get_opcdprr
get_syn_factor_dict['CBGR'] = get_cbgr
get_syn_factor_dict['PRPTCAR'] = get_prptcar
get_syn_factor_dict['RCVAR'] = get_rcvar
get_syn_factor_dict['RCVTAR'] = get_rcvtar
get_syn_factor_dict['IAER'] = get_iaer
get_syn_factor_dict['FADPRR'] = get_fadprr
get_syn_factor_dict['MTCAR'] = get_mtcar
get_syn_factor_dict['SCOPRR'] = get_scoprr
get_syn_factor_dict['CR'] = get_cr
get_syn_factor_dict['CCCLP'] = get_ccclp

get_syn_factor_dict['OPCFNPR'] = get_opcfnpr
get_syn_factor_dict['FCF'] = get_fcf
get_syn_factor_dict['FCFF'] = get_fcff
get_syn_factor_dict['FCFE'] = get_fcfe
get_syn_factor_dict['OPNCINVR'] = get_opncinvr
get_syn_factor_dict['CAPEXP'] = get_capexp
get_syn_factor_dict['NICCE'] = get_nicce
get_syn_factor_dict['OPNCTCR'] = get_opnctcr
get_syn_factor_dict['IVNCTCR'] = get_ivnctcr
get_syn_factor_dict['FINCTCR'] = get_finctcr
get_syn_factor_dict['TAT'] = get_tat
get_syn_factor_dict['TATD'] = get_tatd

get_syn_factor_dict['FAT'] = get_fat
get_syn_factor_dict['NCAT'] = get_ncat
get_syn_factor_dict['LAT'] = get_lat
get_syn_factor_dict['NAT'] = get_nat
get_syn_factor_dict['FATD'] = get_fatd
get_syn_factor_dict['RAT'] = get_rat
get_syn_factor_dict['DSO'] = get_dso
get_syn_factor_dict['APT'] = get_apt
get_syn_factor_dict['DPO'] = get_dpo
get_syn_factor_dict['INT'] = get_int
get_syn_factor_dict['DOH'] = get_doh
get_syn_factor_dict['CRPOPPR'] = get_crpoppr

get_syn_factor_dict['CMGMI'] = get_cmgmi
get_syn_factor_dict['OPCT'] = get_opct
get_syn_factor_dict['EQYT'] = get_eqyt
get_syn_factor_dict['TDR'] = get_tdr
get_syn_factor_dict['TDER'] = get_tder
get_syn_factor_dict['TDMPRP2A'] = get_tdmprp2a
get_syn_factor_dict['DACTR'] = get_dactr
get_syn_factor_dict['EQYACC'] = get_eqyacc
get_syn_factor_dict['DBTWTINT'] = get_dbtwtint
get_syn_factor_dict['DE'] = get_de
get_syn_factor_dict['FALBR'] = get_falbr
get_syn_factor_dict['LTAAR'] = get_ltaar

get_syn_factor_dict['CATAR'] = get_catar
get_syn_factor_dict['NCATAR'] = get_ncatar
get_syn_factor_dict['TATAR'] = get_tatar
get_syn_factor_dict['CATDR'] = get_catdr
get_syn_factor_dict['NCATDR'] = get_ncatdr
get_syn_factor_dict['NCDEQYR'] = get_ncdeqyr
get_syn_factor_dict['CDEQYR'] = get_cdeqyr
get_syn_factor_dict['EM'] = get_em
get_syn_factor_dict['EQYR'] = get_eqyr
get_syn_factor_dict['FAR'] = get_far
get_syn_factor_dict['FATAR'] = get_fatar
get_syn_factor_dict['OPNCDBDR'] = get_opncdbdr

get_syn_factor_dict['OPNCLBR'] = get_opnclbr
get_syn_factor_dict['OPNCDBR'] = get_opncdbr
get_syn_factor_dict['DBWINTINVCPR'] = get_dbwintinvcpr
get_syn_factor_dict['NPEXCVCPR'] = get_npexcvcpr
get_syn_factor_dict['NPEXTDB'] = get_npextdb
get_syn_factor_dict['NPEXDBWINI'] = get_npexdbwini
get_syn_factor_dict['CDTDR'] = get_cdtdr
get_syn_factor_dict['NCDTDR'] = get_ncdtdr
get_syn_factor_dict['TADBWINIR'] = get_tadbwinir
get_syn_factor_dict['TANDBR'] = get_tandbr
get_syn_factor_dict['TATDBR'] = get_tatdbr
get_syn_factor_dict['EBITTDBR'] = get_ebittdbr

get_syn_factor_dict['OPNCTDBR'] = get_opnctdbr
get_syn_factor_dict['OPNCDBWINIR'] = get_opncdbwinir
get_syn_factor_dict['OPNCCDBR'] = get_opnccdbr
get_syn_factor_dict['OPNCNDBR'] = get_opncndbr
get_syn_factor_dict['OPNCNCDBR'] = get_opncncdbr
get_syn_factor_dict['NFNNCCDBR'] = get_nfnnccdbr
get_syn_factor_dict['NFNNCTDBR'] = get_nfnnctdbr
get_syn_factor_dict['CFCR'] = get_cfcr
get_syn_factor_dict['TAEQYDBR'] = get_taeqydbr
get_syn_factor_dict['NDBEQYR'] = get_ndbeqyr
get_syn_factor_dict['DBWINIEQYR'] = get_dbwinieqyr
get_syn_factor_dict['EBITDADBWINIR'] = get_ebitdadbwinir

get_syn_factor_dict['EBITDAINIEXPR'] = get_ebitdainiexpr
get_syn_factor_dict['TDBEBITDAR'] = get_tdbebitdar
get_syn_factor_dict['INIPYR'] = get_inipyr
get_syn_factor_dict['FNLVI'] = get_fnlvi
get_syn_factor_dict['MNTLBR'] = get_mntlbr
get_syn_factor_dict['MNTCDBR'] = get_mntcdbr
get_syn_factor_dict['CCR'] = get_ccr
get_syn_factor_dict['OPNCFXR'] = get_opncfxr
get_syn_factor_dict['OPFCDBR'] = get_opfcdbr
get_syn_factor_dict['OPFTDBR'] = get_opftdbr
get_syn_factor_dict['EQYDBR'] = get_eqydbr
get_syn_factor_dict['ER'] = get_er

get_syn_factor_dict['ICR'] = get_icr
get_syn_factor_dict['EBITDAINIR'] = get_ebitdainir
get_syn_factor_dict['DTED'] = get_dted
get_syn_factor_dict['DBPYR'] = get_dbpyr
get_syn_factor_dict['CPEXGR'] = get_cpexgr
get_syn_factor_dict['LTDBR'] = get_ltdbr
get_syn_factor_dict['LBOPNCR'] = get_lbopncr
get_syn_factor_dict['EQYFAR'] = get_eqyfar
get_syn_factor_dict['LTBFCFR'] = get_ltbfcfr
get_syn_factor_dict['LBOPCR'] = get_lbopcr
get_syn_factor_dict['CUR'] = get_cur
get_syn_factor_dict['QR'] = get_qr


get_syn_factor_dict['MNTAR'] = get_mntar
get_syn_factor_dict['MNTEQYR'] = get_mnteqyr
get_syn_factor_dict['RVQR'] = get_rvqr
get_syn_factor_dict['OPCP'] = get_opcp
get_syn_factor_dict['MNTDBDR'] = get_mntdbdr
get_syn_factor_dict['MNTINIGR'] = get_mntinigr
get_syn_factor_dict['INCCEQTCDBR'] = get_incceqtcdbr
get_syn_factor_dict['GWEQYR'] = get_gweqyr
get_syn_factor_dict['RDOR'] = get_rdor
get_syn_factor_dict['GWAR'] = get_gwar
get_syn_factor_dict['ITAEQYR'] = get_itaeqyr

factor_syn_dict = dict()
factor_syn_dict['EPS'] = ('EPS', "每股收益(EPS)")
factor_syn_dict['EPS_DILUTED'] = ('EPS_DILUTED', "扣非每股收益")
factor_syn_dict['BPS'] = ('BPS', "每股净资产(BPS)")
"""
DPS 数据分布集中难以分组
"""
# factor_syn_dict['DPS'] = ('DPS', "每股股利(DPS)")

factor_syn_dict['SCPS'] = ('SCPS', "每股资本公积")
factor_syn_dict['SRPS'] = ('SRPS', "每股盈余公积")
factor_syn_dict['GRPS'] = ('GRPS', "每股营业总收入")
factor_syn_dict['ORPS'] = ('ORPS', "每股营业收入")
factor_syn_dict['EBITPS'] = ('EBITPS', "每股息税前利润")
factor_syn_dict['FCFFPS'] = ('FCFFPS', "每股企业自由现金流量")
factor_syn_dict['FCFEPS'] = ('FCFEPS', "每股股东自由现金流量")
"""
EBITDAPS 数据来源肯能有问题！！！！！！！！
"""
# factor_syn_dict['EBITDAPS'] = ('EBITDAPS', "每股EBITDA")

factor_syn_dict['RTPS'] = ('RTPS', "每股留存收益")
factor_syn_dict['NCPS'] = ('NCPS', "每股净流动资产")
factor_syn_dict['UDPS'] = ('UDPS', "每股未分配利润")
factor_syn_dict['CFPS'] = ('CFPS', "每股现金净流量")
factor_syn_dict['OCFPS'] = ('OCFPS', "每股经营活动产生的现金流量净额")
factor_syn_dict['WAA'] = ('WAA', "加权净资产收益率(ROE)")
factor_syn_dict['ROA'] = ('ROA', "总资产收益率(ROA)")
factor_syn_dict['OPR'] = ('OPR', "经营性资产回报率")

factor_syn_dict['ROIC'] = ('ROIC', "投资回报率(ROIC)")
factor_syn_dict['ROP'] = ('ROP', "人力投入回报率(ROP)")
factor_syn_dict['GPM'] = ('GPM', "毛利率(GPM)")
factor_syn_dict['NPM'] = ('NPM', "净利率(NPM)")
factor_syn_dict['MCR'] = ('MCR', "管理成本率")
factor_syn_dict['SCR'] = ('SCR', "销售成本率")
factor_syn_dict['CER'] = ('CER', "资本支出比率")
factor_syn_dict['SLCRTR'] = ('SLCRTR', "销售现金比率")
factor_syn_dict['GPOA'] = ('GPOA', "总资产毛利率(GPOA)")
factor_syn_dict['CTAR'] = ('CTAR', "现金总资产比率(CTAR)")
factor_syn_dict['CNAR'] = ('CNAR', "现金净利润率(CNAR)")
factor_syn_dict['COIR'] = ('COIR', "现金营业收入比率(COIR)")
factor_syn_dict['FLE'] = ('FLE', "财务杠杆效应(FLE)")
factor_syn_dict['CFO'] = ('CFO', "经营性现金净流量 / 资产总计(CFO)")
factor_syn_dict['CPR'] = ('CPR', "成本费用利润率")
"""
MOBR 因子差异太小，难以分组
"""
# factor_syn_dict['MOBR'] = ('MOBR', "主营业务比率")
"""
EBITR 数据来源肯能有问题！！！！！！！！
"""
# factor_syn_dict['EBITR'] = ('EBITR', "息税前利润率")
factor_syn_dict['NSOCR'] = ('NSOCR', "净销售额/运营资本")
factor_syn_dict['LAOPR'] = ('LAOPR', "资产减值损失/营业利润")
factor_syn_dict['OPM'] = ('OPM', "营业利润率(OPM)")


factor_syn_dict['TR'] = ('TR', "综合税负率")
factor_syn_dict['ONCTPR'] = ('ONCTPR', "经营活动净收益/利润总额")
factor_syn_dict['RPR'] = ('RPR', "应收应付比率")
factor_syn_dict['NONOPTPR'] = ('NONOPTPR', "营业外收支净额/利润总额")
factor_syn_dict['TTPR'] = ('TTPR', "所得税/利润总额")
factor_syn_dict['DPTPR'] = ('DPTPR', "扣除非经常损益后的净利润/净利润净利润(含少数股东损益)")
"""
ARPRR 数据分布集中难以分组
"""
# factor_syn_dict['ARPRR'] = ('ARPRR', "预收款占营业收入比率")
factor_syn_dict['OPCAR'] = ('OPCAR', "资产现金收益率")
factor_syn_dict['OPCER'] = ('OPCER', "股东权益现金收益率")
factor_syn_dict['OPCCLR'] = ('OPCCLR', "经营净现金比率")
factor_syn_dict['OPCTCR'] = ('OPCTCR', "全部现金流量比率")
factor_syn_dict['OPCTLR'] = ('OPCTLR', "经营现金负债总额比")
factor_syn_dict['OPCTAR'] = ('OPCTAR', "全部资产现金回收率")
factor_syn_dict['NPOI'] = ('NPOI', "净收益营运指数")
factor_syn_dict['OPRTOPRR'] = ('OPRTOPRR', "营业利润/利润总额")
factor_syn_dict['SGRSROPRR'] = ('SGRSROPRR', "销售商品提供劳务收到的现金/营业收入")
factor_syn_dict['OPROPPR'] = ('OPROPPR', "经营活动产生的现金流量净额/营业利润")
factor_syn_dict['OPNCNPDR'] = ('OPNCNPDR', "经营活动产生的现金流量净额/经营活动净收益")
"""
DEPRFAR 数据分布集中难以分组
"""
# factor_syn_dict['DEPRFAR'] = ('DEPRFAR', "折旧率")


factor_syn_dict['INCDEPR'] = ('INCDEPR', "资本支出/折旧和摊销")
factor_syn_dict['ONCTORR'] = ('ONCTORR', "经营性现金净流量/营业总收入")
factor_syn_dict['ONCFIAIR'] = ('ONCFIAIR', "经营性现金资本支出比率")
factor_syn_dict['OPCDPRR'] = ('OPCDPRR', "经营性现金折旧费用比率")
factor_syn_dict['CBGR'] = ('CBGR', "现金股利保障倍数")
factor_syn_dict['PRPTCAR'] = ('PRPTCAR', "预付账款/流动资产")
factor_syn_dict['RCVAR'] = ('RCVAR', "应收账款/总资产")
factor_syn_dict['RCVTAR'] = ('RCVTAR', "应收账款/流动资产")
factor_syn_dict['IAER'] = ('IAER', "无形资产占净资产比率")
factor_syn_dict['FADPRR'] = ('FADPRR', "固定资产/折旧")
factor_syn_dict['MTCAR'] = ('MTCAR', "货币资金/流动资产")
factor_syn_dict['SCOPRR'] = ('SCOPRR', "销售现金比率")
factor_syn_dict['CR'] = ('CR', "现金比率(CR)")
factor_syn_dict['CCCLP'] = ('CCCLP', "现金循环期")
factor_syn_dict['OPCFNPR'] = ('OPCFNPR', "净利润现金含量")
factor_syn_dict['FCF'] = ('FCF', "自由现金流(FCF)")
factor_syn_dict['FCFF'] = ('FCFF', "企业自由现金流(FCFF)")
factor_syn_dict['FCFE'] = ('FCFE', "股权自由现金流(FCFE)")
factor_syn_dict['OPNCINVR'] = ('OPNCINVR', "现金占投资比率")
factor_syn_dict['CAPEXP'] = ('CAPEXP', "资本性支出")


factor_syn_dict['NICCE'] = ('NICCE', "现金及现金等价物净增加额")
factor_syn_dict['OPNCTCR'] = ('OPNCTCR', "经营活动产生的现金流量净额占比")
factor_syn_dict['IVNCTCR'] = ('IVNCTCR', "投资活动产生的现金流量净额占比")
factor_syn_dict['FINCTCR'] = ('FINCTCR', "筹资活动产生的现金流量净额占比")
factor_syn_dict['TAT'] = ('TAT', "总资产周转率(TAT)")
factor_syn_dict['TATD'] = ('TATD', "总资产周转天数")
factor_syn_dict['FAT'] = ('FAT', "固定资产周转率(FAT)")
factor_syn_dict['NCAT'] = ('NCAT', "非流动资产周转率")
factor_syn_dict['LAT'] = ('LAT', "流动资产周转率(LAT)")
factor_syn_dict['NAT'] = ('NAT', "净资产周转率(NAT)")
factor_syn_dict['FATD'] = ('FATD', "固定资产周转天数")
factor_syn_dict['RAT'] = ('RAT', "应收账款周转率(RAT)")
factor_syn_dict['DSO'] = ('DSO', "应收账款周转天数(DSO)")
factor_syn_dict['APT'] = ('APT', "应付账款周转率")
factor_syn_dict['DPO'] = ('DPO', "应付账款周转天数(DPO)")
factor_syn_dict['INT'] = ('INT', "存货周转率(INT)")
factor_syn_dict['DOH'] = ('DOH', "存货周转天数(DOH)")
factor_syn_dict['CRPOPPR'] = ('CRPOPPR', "现金转换周期/营业周期")
factor_syn_dict['CMGMI'] = ('CMGMI', "成本管理指数")

factor_syn_dict['OPCT'] = ('OPCT', "营运资本周转率")
factor_syn_dict['EQYT'] = ('EQYT', "股东权益周转率")
factor_syn_dict['TDR'] = ('TDR', "资产负债率(TDR)")
factor_syn_dict['TDER'] = ('TDER', "产权比率")
factor_syn_dict['TDMPRP2A'] = ('TDMPRP2A', "剔除预收款项后的资产负债率")
factor_syn_dict['DACTR'] = ('DACTR', "坏账费用率")
factor_syn_dict['EQYACC'] = ('EQYACC', "账面净值")
"""
DBTWTINT 数据分布集中难以分组
"""
# factor_syn_dict['DBTWTINT'] = ('DBTWTINT', "有息负债")
"""
DE数据分布集中难以分组
"""
# factor_syn_dict['DE'] = ('DE', "长期资本负债率(DE)")
factor_syn_dict['FALBR'] = ('FALBR', "固定资产/长期负债")
factor_syn_dict['LTAAR'] = ('LTAAR', "长期资产适合率")
factor_syn_dict['CATAR'] = ('CATAR', "流动资产/总资产")
factor_syn_dict['NCATAR'] = ('NCATAR', "非流动资产/总资产")
factor_syn_dict['TATAR'] = ('TATAR', "有形资产/总资产")
factor_syn_dict['CATDR'] = ('CATDR', "流动资产/负债合计")
factor_syn_dict['NCATDR'] = ('NCATDR', "非流动资产/负债合计")
factor_syn_dict['NCDEQYR'] = ('NCDEQYR', "非流动负债权益比率")
factor_syn_dict['CDEQYR'] = ('CDEQYR', "流动负债权益比率")
factor_syn_dict['EM'] = ('EM', "权益乘数(股本乘数)(EM)")
factor_syn_dict['EQYR'] = ('EQYR', "净资产比率")

factor_syn_dict['FAR'] = ('FAR', "资本固定化比率")
factor_syn_dict['FATAR'] = ('FATAR', "固定资产比率")
factor_syn_dict['OPNCDBDR'] = ('OPNCDBDR', "现金到期债务比")
factor_syn_dict['OPNCLBR'] = ('OPNCLBR', "现金流量/长期债务")
factor_syn_dict['OPNCDBR'] = ('OPNCDBR', "经营现金债务保护比")
"""
DBWINTINVCPR 数据分布集中难以分组
"""
# factor_syn_dict['DBWINTINVCPR'] = ('DBWINTINVCPR', "带息债务/全部投入资本")
"""
NPEXCVCPR 数据分布集中难以分组
"""
# factor_syn_dict['NPEXCVCPR'] = ('NPEXCVCPR', "归属母公司股东的权益/全部投入资本")
factor_syn_dict['NPEXTDB'] = ('NPEXTDB', "归属母公司股东的权益/负债总额")
factor_syn_dict['NPEXDBWINI'] = ('NPEXDBWINI', "归属母公司股东的权益/带息债务")
"""
CDTDR 数据分布集中难以分组
"""
# factor_syn_dict['CDTDR'] = ('CDTDR', "流动负债/总负债")
"""
NCDTDR 数据分布集中难以分组
"""
# factor_syn_dict['NCDTDR'] = ('NCDTDR', "非流动负债/总负债")

factor_syn_dict['TADBWINIR'] = ('TADBWINIR', "有形资产/带息债务")
factor_syn_dict['TANDBR'] = ('TANDBR', "有形资产/净债务")
factor_syn_dict['TATDBR'] = ('TATDBR', "有形资产/总负债")
"""
EBITTDBR 数据分布集中难以分组
"""
# factor_syn_dict['EBITTDBR'] = ('EBITTDBR', "息税折旧摊销前利润/负债合计")
factor_syn_dict['OPNCTDBR'] = ('OPNCTDBR', "经营活动产生的现金流量净额/负债合计")
factor_syn_dict['OPNCDBWINIR'] = ('OPNCDBWINIR', "经营活动产生的现金流量净额/带息债务")
factor_syn_dict['OPNCCDBR'] = ('OPNCCDBR', "经营活动产生的现金流量净额/流动负债")
factor_syn_dict['OPNCNDBR'] = ('OPNCNDBR', "经营活动产生的现金流量净额/净债务")
factor_syn_dict['OPNCNCDBR'] = ('OPNCNCDBR', "经营活动产生的现金流量净额/非流动负债")
factor_syn_dict['NFNNCCDBR'] = ('NFNNCCDBR', "非筹资性现金净流量与流动负债的比率")
factor_syn_dict['NFNNCTDBR'] = ('NFNNCTDBR', "非筹资性现金净流量与负债总额的比率")
factor_syn_dict['CFCR'] = ('CFCR', "现金流覆盖率(CFCR)")
factor_syn_dict['TAEQYDBR'] = ('TAEQYDBR', "有形资产净值债务率")

factor_syn_dict['NDBEQYR'] = ('NDBEQYR', "净债务/股权价值")
"""
DBWINIEQYR 数据分布集中难以分组
"""
# factor_syn_dict['DBWINIEQYR'] = ('DBWINIEQYR', "带息债务/股权价值")
"""
EBITDADBWINIR 数据分布集中难以分组
"""
# factor_syn_dict['EBITDADBWINIR'] = ('EBITDADBWINIR', "EBITDA/带息债务")
"""
EBITDAINIEXPR 数据分布集中难以分组
"""
# factor_syn_dict['EBITDAINIEXPR'] = ('EBITDAINIEXPR', "EBITDA/利息费用")
factor_syn_dict['TDBEBITDAR'] = ('TDBEBITDAR', "全部债务/EBITDA")
factor_syn_dict['INIPYR'] = ('INIPYR', "偿付比率")
factor_syn_dict['FNLVI'] = ('FNLVI', "财务杠杆指数")
factor_syn_dict['MNTLBR'] = ('MNTLBR', "货币资金/短期债务")
factor_syn_dict['MNTCDBR'] = ('MNTCDBR', "货币资金/流动负债")
factor_syn_dict['CCR'] = ('CCR', "现金流动负债比率(CCR)")

factor_syn_dict['OPNCFXR'] = ('OPNCFXR', "现金支付利息能力比率")
factor_syn_dict['OPFCDBR'] = ('OPFCDBR', "营业利润/流动负债")
factor_syn_dict['OPFTDBR'] = ('OPFTDBR', "营业利润/负债合计")
factor_syn_dict['EQYDBR'] = ('EQYDBR', "净资产负债率")
factor_syn_dict['ER'] = ('ER', "财务杠杆(产权比率)(ER)")
factor_syn_dict['ICR'] = ('ICR', "利息保障倍数(ICR)")

"""
EBITDAINIR 数据分布集中难以分组
"""
# factor_syn_dict['EBITDAINIR'] = ('EBITDAINIR', "息税折旧及摊销前利润利息覆盖率")
factor_syn_dict['DTED'] = ('DTED', "股东权益比率(DTED)")

"""
DBPYR 数据分布集中难以分组
"""
# factor_syn_dict['DBPYR'] = ('DBPYR', "债务偿还率")
factor_syn_dict['CPEXGR'] = ('CPEXGR', "资本支出保障倍数")
"""
LTDBR 数据分布集中难以分组
"""
# factor_syn_dict['LTDBR'] = ('LTDBR', "长期负债比率(资本化比率)")
"""
LBOPNCR 数据分布集中难以分组
"""
# factor_syn_dict['LBOPNCR'] = ('LBOPNCR', "长期负债/现金流量比")
factor_syn_dict['EQYFAR'] = ('EQYFAR', "股东权益与固定资产比率")
"""
LTBFCFR 数据分布集中难以分组
"""
# factor_syn_dict['LTBFCFR'] = ('LTBFCFR', "长期债务/自由现金流")
"""
LBOPCR 数据分布集中难以分组
"""
# factor_syn_dict['LBOPCR'] = ('LBOPCR', "长期负债与营运资金比率")
factor_syn_dict['CUR'] = ('CUR', "流动比率(CUR)")
factor_syn_dict['QR'] = ('QR', "速动比率(QR)")
factor_syn_dict['MNTAR'] = ('MNTAR', "现金/总资产比")
factor_syn_dict['MNTEQYR'] = ('MNTEQYR', "现金/净资产比")
factor_syn_dict['RVQR'] = ('RVQR', "保守速动比率")
factor_syn_dict['OPCP'] = ('OPCP', "运营资本")
factor_syn_dict['MNTDBDR'] = ('MNTDBDR', "现金到期债务比")
factor_syn_dict['MNTINIGR'] = ('MNTINIGR', "现金流量利息保障倍数")
factor_syn_dict['INCCEQTCDBR'] = ('INCCEQTCDBR', "现金比率")
"""
GWEQYR 数据分布集中难以分组
"""
# factor_syn_dict['GWEQYR'] = ('GWEQYR', "商誉占净资产比率")
"""
RDOR 数据分布集中难以分组
"""
# factor_syn_dict['RDOR'] = ('RDOR', "商誉收入比率(RDOR)")
"""
GWAR 数据分布集中难以分组
"""
# factor_syn_dict['GWAR'] = ('GWAR', "商誉占总资产比率")
"""
ITAEQYR 数据分布集中难以分组
"""
# factor_syn_dict['ITAEQYR'] = ('ITAEQYR', "无形资产占净资产比率")


# def get_eps():
#     """
#     每股收益(EPS)
#     :return: the dataframe for eps.
#     m * n: m fiscal years and n wind codes
#     """
#     """
#     The path of the raw data files
#     """
#     path_source = "/home/aeront/PycharmProjects/TXLCScreen/FactorReservoir"
#     """
#     The file names for each fiscal factor
#     """
#     filename_dict = {'EPS': 'factor_EPS_df_slice_update.dat'}
#     raw_factor_dict = dict()
#
#     """
#     The extraction of the raw data from the .dat files
#     """
#     for ii_raw_factor, ii_filename in filename_dict.items():
#         filename_data = "".join([path_source, "/", ii_filename])
#         raw_factor_dict[ii_raw_factor] = pd.read_pickle(filename_data, compression='bz2')
#
#     """
#     The synthesis of the factors
#     """
#     # df_syn_factor_slice = synthesis('EPS', raw_factor_dict)
#     df_syn_factor_slice = raw_factor_dict['EPS']
#
#     return df_syn_factor_slice
#
#
# def get_waa():
#     """
#     加权平均净资产收益率(WAA)
#     :return: the dataframe for eps.
#     m * n: m fiscal years and n wind codes
#     """
#     """
#     The path of the raw data files
#     """
#     path_source = "/home/aeront/PycharmProjects/TXLCScreen/FactorReservoir"
#     """
#     The file names for each fiscal factor
#     """
#     filename_dict = {'WAA': 'factor_WAA_df_slice_update.dat'}
#     raw_factor_dict = dict()
#
#     """
#     The extraction of the raw data from the .dat files
#     """
#     for ii_raw_factor, ii_filename in filename_dict.items():
#         filename_data = "".join([path_source, "/", ii_filename])
#         raw_factor_dict[ii_raw_factor] = pd.read_pickle(filename_data, compression='bz2')
#
#     """
#     The synthesis of the factors
#     """
#     # df_syn_factor_slice = synthesis('EPS', raw_factor_dict)
#     df_syn_factor_slice = raw_factor_dict['WAA']
#
#     return df_syn_factor_slice
