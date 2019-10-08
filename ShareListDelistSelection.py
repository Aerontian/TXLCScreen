# -*- coding: UTF-8 -*
from YearDate import *
import pandas as pd
import numpy as np
import copy


def get_annual_on_df(year_genre='position', path_filename_src=
                                "/home/aeront/PycharmProjects/LocalDataBase(YFFormat)/DataReservoir/list_delist_flag_update.dat"):

    list_delist_flag_df = pd.read_pickle(path_filename_src, compression='bz2')

    '''
        Get the trade day list and the wind code list
        '''
    wind_code_list = list_delist_flag_df.columns.tolist()

    yr_list = copy.deepcopy(ny_list)

    def get_logic_union(on_list_series, **kwargs):

        """
        :param on_list_series:   series for each wind code, the logical value is listed by trade days,
        True if the wind code is listed in the trading day, False if the wind code has not yet been
        listed or the wind code has been delisted.
        **kwargs: the start and end index for each year
        :return logical_list_year: list for each wind code, True if the wind code is listed in the whole year,
        otherwise False
        """

        range_index_dict = kwargs['index_dict']
        range_index_list = [range_index_dict[ii_anl] for ii_anl in py_list]
        logical_list_year = []
        list_logic_series_list = [on_list_series.iloc[ii_index[0]: ii_index[1] + 1].values.tolist() for ii_index in range_index_list]
        for ii_list in list_logic_series_list:
            if False in ii_list:
                logical_list_year.append(False)
            else:
                logical_list_year.append(True)

        return logical_list_year

    if year_genre == 'position':
        list_delist_annual_selection_df = \
            list_delist_flag_df.apply(get_logic_union, axis=0, result_type='expand', index_dict=py_td_idx_mapper)
    elif year_genre == 'fiscal':
        list_delist_annual_selection_df = \
            list_delist_flag_df.apply(get_logic_union, axis=0, result_type='expand', index_dict=ny_td_idx_mapper)

    list_delist_annual_selection_df.index = yr_list
    list_delist_annual_selection_df.columns = wind_code_list

    return list_delist_annual_selection_df


def get_annual_on_dict(on=True, year_genre='position', path_filename_src=
                       "/home/aeront/PycharmProjects/LocalDataBase(YFFormat)/DataReservoir/list_delist_flag_update.dat"):
    list_delist_flag_df = pd.read_pickle(path_filename_src, compression='bz2')
    list_delist_flag_df = list_delist_flag_df.astype('int')
    list_delist_flag_np_array = list_delist_flag_df.values
    '''
    Get the trade day list and the wind code list
    '''
    wind_code_list = list_delist_flag_df.columns.tolist()

    yr_list = copy.deepcopy(ny_list)

    # def get_logic_union(on_list_series, **kwargs):
    #
    #     """
    #     :param on_list_series:   series for each wind code, the logical value is listed by trade days,
    #     True if the wind code is listed in the trading day, False if the wind code has not yet been
    #     listed or the wind code has been delisted.
    #     **kwargs: the start and end index for each year
    #     :return logical_list_year: list for each wind code, True if the wind code is listed in the whole year,
    #     otherwise False
    #     """
    #
    #     range_index_dict = kwargs['index_dict']
    #     range_index_list = [range_index_dict[ii_anl] for ii_anl in py_list]
    #     logical_list_year = []
    #     list_logic_series_list = [on_list_series.iloc[ii_index[0]: ii_index[1] + 1].values.tolist() for ii_index in range_index_list]
    #     for ii_list in list_logic_series_list:
    #         if False in ii_list:
    #             logical_list_year.append(False)
    #         else:
    #             logical_list_year.append(True)
    #
    #     return logical_list_year

    anl_on_off_dict = {}
    if year_genre == 'position':
        # list_delist_annual_selection_df = \
        #     list_delist_flag_df.apply(get_logic_union, axis=0, result_type='expand', index_dict=py_td_idx_mapper)
        for ii_year, ii_index in py_td_idx_mapper.items():
            anl_on_off_dict[ii_year] = np.prod(list_delist_flag_np_array[ii_index[0]: ii_index[1] + 1, :], axis=0)
    elif year_genre == 'fiscal':
        for ii_year, ii_index in ny_td_idx_mapper.items():
            anl_on_off_dict[ii_year] = np.prod(list_delist_flag_np_array[ii_index[0]: ii_index[1] + 1, :], axis=0)

    list_delist_annual_selection_df = pd.DataFrame.from_dict(anl_on_off_dict, orient='index', columns=wind_code_list)
    # list_delist_annual_selection_df.columns = wind_code_list
    list_delist_annual_selection_df.sort_index(axis=0, ascending=True, inplace=True)
    # list_delist_annual_selection_df.sort_index(axis=1, ascending=True, inplace=True)
    list_delist_annual_selection_df = list_delist_annual_selection_df.astype('bool')

    if on:
        anl_on_dict = {}
        for idx, row in list_delist_annual_selection_df.iterrows():
            on_list = row[row].index.tolist()
            anl_on_dict[idx] = on_list
        return anl_on_dict
    else:
        anl_off_dict = {}
        for idx, row in list_delist_annual_selection_df.iterrows():
            off_list = row[~row].index.tolist()
            anl_off_dict[idx] = off_list
        return anl_off_dict


if __name__ == "__main__":

    list_on_dict = get_annual_on_dict(year_genre='position')
    # list_on_dict = get_on_list_wind_code_dict(list_on_df)

    a = 1

