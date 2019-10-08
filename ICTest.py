# -*- coding: UTF-8 -*
from YearDate import *
from ShareListDelistSelection import *
from FactorSynthesis import get_eps, get_waa
import numpy as np
import statsmodels.api as sm
from matplotlib import pyplot as plt
from scipy import stats
import pickle
from DataVisualizing import *


source_path = "/home/aeront/PycharmProjects/LocalDataBase(YFFormat)/DataReservoir"
filename_stk = "".join([source_path, "/", "stk_update.dat"])
filename_date = "".join([source_path, "/", "date_update.dat"])
df_stk = pd.read_pickle(filename_stk)
df_date = pd.read_pickle(filename_date)


def person_ic(s_fac, s_ret):

    return s_fac.corr(s_ret, method='pearson')


def rank_ic(s_fac, s_ret):

    return s_fac.corr(s_ret, method='spearman')


def test_ic(df_factor, df_return):

    if isinstance(df_factor, pd.DataFrame):
        if df_factor.shape == (len(ny_list), len(df_stk)):
            pass
        else:
            print("The size of the dataframe df_factor errors.")
            os._exit(1)
    else:
        print("The arg df_factor genre errors")
        os._exit(1)

    if isinstance(df_return, pd.DataFrame):
        if df_return.shape == (len(ny_list), len(df_stk)):
            pass
        else:
            print("The size of the dataframe df_ret errors.")
            os._exit(1)
    else:
        print("The arg df_ret genre errors")
        os._exit(1)

    fiscal_year = fy_list
    ic_dict = dict.fromkeys(fiscal_year, [])
    # excl_anl_dict
    # excl_anl_dict = get_excl_dict()
    for ii_year in fiscal_year:
        pos_year = fy_py_mapper[ii_year]
        if pos_year is not None:
            # excl_1 = excl_anl_dict[ii_year]
            # excl_2 = excl_anl_dict[pos_year]
            # excl = list(set(excl_1).union(set(excl_2)))
            series_factor = df_factor.loc[ii_year, :]
            # series_factor.loc[excl] = np.nan
            series_return = df_return.loc[pos_year, :]
            # series_return.loc[excl] = np.nan
            ic_dict[pos_year] = rank_ic(series_factor, series_return)

    for i_yr, i_ic in ic_dict.items():
        if np.isnan(i_ic):
            ic_dict[i_yr] = []

    return ic_dict


def get_return_anl(src="local"):

    path_destination = u"/home/aeront/PycharmProjects/TXLCScreen/FactorReservoir"
    file_name = u"factor_pct_df_anl.dat"
    path_filename_pct_anl = "".join([path_destination, "/", file_name])

    if src != "local":

        path_source = u"/home/aeront/PycharmProjects/LocalDataBase(YFFormat)/DataReservoir"
        file_name = u"factor_pct_df_update.dat"
        path_filename_pct = "".join([path_source, "/", file_name])
        df_ret_daily = pd.read_pickle(path_filename_pct, compression='bz2') / 100.0 + 1

        def get_ret(s_ret_daily):
            ret_list = list()
            for ii_year, td_idx in py_td_idx_mapper.items():
                ret_anl = s_ret_daily.iloc[td_idx[0]:td_idx[1] + 1]
                ret_list.append(ret_anl.prod(skipna=False))
            return ret_list

        df_return_anl = df_ret_daily.apply(get_ret, axis=0, result_type='expand')
        df_return_anl.index = py_list

        df_return_anl.to_pickle(path_filename_pct_anl, compression='bz2')

    else:
        df_return_anl = pd.read_pickle(path_filename_pct_anl, compression='bz2')

    return df_return_anl


def get_drawback(src="local"):

    path_destination = u"/home/aeront/PycharmProjects/TXLCScreen/FactorReservoir"
    file_name = u"factor_drawback_df.dat"
    path_filename_db_daily = "".join([path_destination, "/", file_name])

    if src != "local":

        pct_path_filename_source = \
            '/home/aeront/PycharmProjects/LocalDataBase(YFFormat)/DataReservoir/factor_pct_df_update.dat'
        df_pct_daily = pd.read_pickle(pct_path_filename_source, compression='bz2')
        df_pct_daily.fillna(0.0, inplace=True)

        df_pct_daily = df_pct_daily / 100.0 + 1
        df_ret_daily = df_pct_daily.cumprod(axis=0)

        def get_max(s_ret_daily):
            max_list = list()
            max_list.append(s_ret_daily.iloc[0])
            for ii_ret in s_ret_daily.iloc[1:].tolist():
                max_value = max(ii_ret, max_list[-1])
                max_list.append(max_value)
            return max_list

        # def get_db(s_ret_daily):
        #
        #     max_list = [max()]
        #     s_ret_daily = (s_pct_daily + 1).cumprod()
        #     s_db_daily =
        #     ret_list = list()
        #     for ii_year, td_idx in py_td_idx_mapper.items():
        #         ret_anl = s_ret_daily.iloc[td_idx[0]:td_idx[1] + 1]
        #         ret_list.append(ret_anl.prod(skipna=False))
        #     return ret_list

        df_max_daily = df_ret_daily.apply(get_max, axis=0, result_type='expand')
        df_db = (df_ret_daily - df_max_daily) / df_max_daily

        df_db.to_pickle(path_filename_db_daily, compression='bz2')

    else:
        df_db = pd.read_pickle(path_filename_db_daily, compression='bz2')

    return df_db


def t_test(ic_dict):

    ic_dict = {ii_key: ic_dict[ii_key] for ii_key in ic_dict.keys() if ic_dict[ii_key]}
    df_ic = pd.DataFrame([ic_dict])
    df_ic = df_ic.T
    des_stat = df_ic.describe()
    print(des_stat)

    t, p_2tail = stats.ttest_1samp(des_stat, 0, axis=0)

    a=1

    return t, p_2tail


def get_excl_dict(src='local'):

    filename = "../TXLCScreen/excl_dict.dat"

    if src == 'local':
        with open(filename, 'rb') as f:
            excl_windcode_dict = pickle.load(f)
    else:
        excl_windcode_dict = get_annual_on_dict(on=False, year_genre='position')
        with open(filename, 'wb') as f:
            pickle.dump(excl_windcode_dict, f)
    return excl_windcode_dict


if __name__ == "__main__":

    # df_eps_slice = get_eps()
    # df_ret_slice = get_return_anl()

    # ic_value_dict = test_ic(df_eps_slice, df_ret_slice)
    # t_test(ic_value_dict)

    df_waa_slice = get_waa()
    df_ret_slice = get_return_anl()

    # ic_value_dict = test_ic(df_waa_slice, df_ret_slice)
    # plot_bar(ic_value_dict)

    # srs_eps = df_eps_slice.iloc[0, :]
    # srs_valid_eps = srs_eps.notna()

    index_factor = 3
    index_pos = index_factor + 1
    srs_waa = df_waa_slice.iloc[index_factor, :]
    srs_valid_waa = srs_waa.notna()

    srs_ret = df_ret_slice.iloc[index_pos, :] - 1
    srs_valid_ret = srs_ret.notna()

    srs_valid = srs_valid_waa & srs_valid_ret

    excl_dict = get_excl_dict(src='local')
    year_pos = str(index_pos + 2006)
    year_factor = str(index_factor + 2006)

    srs_interval_valid = \
        srs_waa.apply(lambda waa: True if 0 <= waa <= 30 else False)
    waa_excl_list = srs_interval_valid[~srs_interval_valid].index.tolist()

    excl_list = \
        list(set(excl_dict[year_pos]).union(set(excl_dict[year_factor])).union(set(waa_excl_list)))

    srs_valid.loc[excl_list] = False

    srs_waa = srs_waa.loc[srs_valid]
    srs_ret = srs_ret.loc[srs_valid]
    np_waa = np.array(srs_waa).transpose()
    np_ret = np.array(srs_ret).transpose()
    np_waa = sm.add_constant(np_waa)

    model = sm.OLS(np_ret, np_waa)
    result = model.fit()
    print(result.summary())

    y_fitted = result.fittedvalues
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(srs_waa, srs_ret, 'o', label='data')
    ax.plot(srs_waa, y_fitted, 'r--.', label='OLS')
    ax.legend(loc='best')
    plt.grid()
    plt.show()

    a=1


