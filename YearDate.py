# -*- coding: UTF-8 -*
import pandas as pd
import copy
import os
import operator as op

"""
There are 3 kinds of Years: nature Year, fiscal Year, position Year

nature Year:
nature Year starts at the first trading day of a nature year and ends at the last trading day of nature year
eg. nature Year 2007 starts at day 20070104 and ends at day 20071228

fiscal Year:
fiscal Year starts at the first nature day of a nature year and ends at the last nature day of nature year
eg. fiscal Year 2007 starts at day 20070101 and ends at day 20071231

position Year:
position Year(i_yr) starts at the first trading day of the Months After May(including May) and
 ends at the last trading day of the Months Before May(excluding May) in the next year(i_yr+1)

eg. position Year 2007 starts at day 20070508 and ends at day 20080430 if the current day is 20190606, 
then 20190506 is the start day of position Year 2019 and 20190606 is the end day of position Year 2019
"""

path_name_date = \
    u"/home/aeront/PycharmProjects/LocalDataBase(YFFormat)/DataReservoir/date_update.dat"
trading_day_list = pd.read_pickle(path_name_date)['TradeDate'].values.tolist()
trading_day_list.sort(reverse=False)

'''
    Get the nature year list and the start index and the end index for each year
'''

'''
    td_ny_list; the list contains the year for each trading day
    ny_list: the list contains the nature Years from the trading days
    ny_td_idx_mapper: the dict mapping from nature Year
    to tuple (the index of the start trading day of the nature Year,
    the index of the end trading day of the nature Year)
'''

td_ny_list = list(map(lambda x: x[0:4], trading_day_list))
ny_list = list(set(td_ny_list))

ny_list.sort(reverse=False)
ny_td_reverse_list = td_ny_list[::-1]
ny_td_idx_mapper = \
    {ii_yr: (td_ny_list.index(ii_yr), len(ny_td_reverse_list) - ny_td_reverse_list.index(ii_yr) - 1)
     for ii_yr in ny_list}

'''
    fy_list: the list contains the fiscal Years
    py_list: the list contains the position Years

    fy_ny_mapper: the dict mapping from fiscal Year to nature Year
    ny_fy_mapper: the dict mapping from  nature Year to fiscal Year

    py_ny_mapper: the dict mapping from position Year to nature Year
    ny_py_mapper: the dict mapping from  nature Year to position Year

    py_fy_mapper: the dict mapping from position Year to fiscal Year
    fy_py_mapper: the dict mapping from  fiscal Year to position Year
'''
fy_list = copy.deepcopy(ny_list)
py_list = copy.deepcopy(ny_list)

fy_ny_mapper = {ii_yr: ii_yr for ii_yr in fy_list}
ny_fy_mapper = {ii_yr: ii_yr for ii_yr in ny_list}

py_ny_mapper = copy.deepcopy(fy_ny_mapper)
ny_py_mapper = copy.deepcopy(ny_fy_mapper)

py_fy_mapper = dict(zip(py_list[1:], fy_list[:-1]))
fy_py_mapper = dict(zip(fy_list[:-1], py_list[1:]))
py_fy_mapper[py_list[0]] = None
fy_py_mapper[fy_list[-1]] = None
# for (ii_yr, ii_yr_nxt) in zip(fy_list[:-1], py_list[1:]):
#     py_fy_mapper[ii_yr_nxt] = ii_yr
#     fy_py_mapper[ii_yr] = ii_yr_nxt

'''
fy_td_index_mapper:  the dict mapping from fiscal Year to the index of the first trading day of January of the next year.
 The index is used to read the fiscal data from an dataframe listed in trading days.
 eg. fiscal Year 2007, in a dataframe df_net_profit, the index which indicates the date '20080102' from 
 where the fiscal data net profit of fiscal Year 2007 is read
'''

'''
Get the start index of January for each year
'''
j1st_year_start_index_dict = {}
date_month_list = map(lambda x: x[0:6], trading_day_list)
date_month_series = pd.Series(date_month_list)

for ii_yr in ny_list:
    target = ''.join([ii_yr, '01'])
    select_series = date_month_series[date_month_series == target]
    if len(select_series) == 0:
        j1st_year_start_index_dict[ii_yr] = None
    else:
        j1st_year_start_index_dict[ii_yr] = select_series.index.values.tolist()[0]

fy_td_index_mapper = dict.fromkeys(fy_list, None)
for ii_idx, ii_yr in enumerate(fy_list):
    ii_yr_nxt = fy_list[ii_idx + 1] if ii_idx != len(fy_list) - 1 else '0000'
    fy_td_index_mapper[ii_yr] = j1st_year_start_index_dict.get(ii_yr_nxt)

'''
    py_td_idx_mapper: the dict mapping from position Year
    to tuple (the index of the start trading day of the position Year,
    the index of the end trading day of the position Year)

    SS(i_yr) is defined as the index of the first trading day of the Months After May(including May) in the year i_yr
    SE(i_yr) is defined as the index of the last trading day of the Months Before May(excluding May) in the year i_yr
    ST(i_yr) is short for the index of the start trading day in the year i_yr
    ET(i_yr) is short for the index of the end trading day in the year i_yr
    LT is short for the index of the last trading day of all the trading days

    For a certain year i_yr:

        A: If SS does not exist:
            ST is set to be None
        B: If SS exists:
            ST is set to be SS

        A: If ES does not exist:
            the end trading day is set to be None
        B: If ES exists:
            ET is set to be ES

    For a certain year i_yr:
    A. If the start trading day is None:
        the position index of year i_yr is set to be None.
    B.  If the start trading day is not None:
        a. If year i_yr is not the final year:
            the position index of year i_yr is set to be (ST(i_yr), ET(i_yr_next))
        b. If year i_yr is the final year:
            the position index of year i_yr is set to be (ST(i_yr, LT)

    Comments: For year i_yr, ET exists unconditionally and ST does not necessarily exist.

    A:If the start trading day of the position Year does not exist(None): 
        the end trading day also does not exist, the position index of this year is set to be None.

    B:If the start trading day of the position Year exists
        a: if the end trading day of April of the next year exists: 
            the end trading day of the position is set to be the final trading day of April of 
            the next year. 

        b: If this year is not the final year:
            1: If the end trading day of April of the next year does not exist:
                the end trading day of the position is set to be the final day of all the trading days.

            2: If this year is the final year:
                the end trading day of the position is set to be the final day of all the trading days.
'''


def str_cmp_ge(yr_mt, **kwargs):
    year = kwargs['year']
    yr_mt_start = ''.join([year, '05'])
    return True if op.ge(yr_mt, yr_mt_start) else False


def str_cmp_lt(yr_mt, **kwargs):
    year = kwargs['year']
    yr_mt_end = ''.join([year, '05'])
    return True if op.lt(yr_mt, yr_mt_end) else False


yr_mt_list = map(lambda x: x[0:6], trading_day_list)
date_month_series = pd.Series(yr_mt_list)

start_index_dict = {}
for ii_yr in ny_list:
    pass_series = date_month_series.apply(str_cmp_ge, year=ii_yr)
    index_list = date_month_series[pass_series].index.values.tolist()
    if len(index_list) != 0:
        start_index_dict[ii_yr] = index_list[0]
    else:
        start_index_dict[ii_yr] = None

end_index_dict = {}
for ii_yr in ny_list:
    ii_yr_nxt = str(int(ii_yr) + 1)
    pass_series = date_month_series.apply(str_cmp_lt, year=ii_yr_nxt)
    index_list = date_month_series[pass_series].index.values.tolist()
    if len(index_list) != 0:
        end_index_dict[ii_yr] = index_list[-1]
    else:
        end_index_dict[ii_yr] = None

py_td_idx_mapper = \
    {ii_yr: (start_index_dict[ii_yr], end_index_dict[ii_yr]) if start_index_dict[ii_yr] is not None else None
     for ii_yr in ny_list}

for ii_yr in ny_list:
    if py_td_idx_mapper[ii_yr] is None:
        print("Year {0}: No Position.\n".format(ii_yr))
    else:
        start_index = py_td_idx_mapper[ii_yr][0]
        end_index = py_td_idx_mapper[ii_yr][1]
        print("Year {0}: Position from {1} to {2}.\n".
              format(ii_yr, trading_day_list[start_index], trading_day_list[end_index]))

NUM_DATE = len(trading_day_list)
NUM_YEAR = len(ny_list)

