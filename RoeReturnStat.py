from TimeSeries import *
from VisualizationTools import *
from ICTest import get_return_anl
from ICTest import get_drawback
from ShareListDelistSelection import get_annual_on_df
from FactorSynthesis import raw_data_dict
BOTTOM = 0
UPPER = 50


def retrieve_raw_data(rw_data_list):

    """
    :param rw_data_list: the raw data id list
    :return: df_raw_data_dict: the dict whose keys are the  raw data id and
    whose values are the dataframes for raw data
    """

    df_raw_data_dict = dict()

    """
    The path of the raw data files
    """
    path_source = "/home/aeront/PycharmProjects/TXLCScreen/FactorReservoir/"

    for raw_data_id in rw_data_list:
        filename = raw_data_dict[raw_data_id][2]
        path_filename_source = "".join([path_source, filename])
        df_raw_data = pd.read_pickle(path_filename_source, compression='bz2')

        df_raw_data_dict[raw_data_id] = df_raw_data

    return df_raw_data_dict


def specific_range(srs_data, roe_range):
    for ii_data in srs_data[0:-1].tolist():
        if roe_range[0] < ii_data < roe_range[1]:
            pass
        else:
            return False

    return True


def stat_dis_ret(srs_ret_tot, srs_on_tot):

    srs_ret_tot = srs_ret_tot[srs_on_tot]
    print("The mean is: {0} and the standard deviation is: {1}".format(srs_ret_tot.mean(), srs_ret_tot.std()))
    equity_list = [ii_eqy for ii_eqy in srs_ret_tot.values.tolist()]
    plot_hist(equity_list, title="return_distribution")


def drawback_show(wind_code_select, srs_db):
    srs_db = srs_db.loc[wind_code_select]
    print("The mean is: {0} and the standard deviation is: {1}".format(srs_db.mean(), srs_db.std()))
    title = "".join(["drawback"])
    plot_bar(wind_code_select, srs_db.values.tolist(), title)


def select_by_stability(df_roe, srs_on_tot, srs_equity, range_roe):

    srs_specific_range = df_roe.apply(specific_range, axis=0, roe_range=range_roe)
    df_roe = df_roe.loc[:, srs_on_tot & srs_specific_range]

    stability_value = df_roe.apply(stability, axis=0)
    stability_value.sort_values(ascending=True, inplace=True)
    wind_code_select = stability_value.iloc[BOTTOM:UPPER].index.tolist()
    srs_equity = srs_equity.loc[wind_code_select]
    print("The mean is: {0} and the standard deviation is: {1}".format(srs_equity.mean(), srs_equity.std()))
    # title = "".join(["stability", str(range_roe[0]), "_", str(range_roe[1])])
    # plot_bar(wind_code_select, srs_equity.values.tolist(), title)
    return wind_code_select


def select_by_growth(df_roe, srs_on_tot, srs_equity, by="diff", range_roe=(0, 100)):

    srs_specific_range = df_roe.apply(specific_range, axis=0, roe_range=range_roe)
    df_roe = df_roe.loc[:, srs_on_tot & srs_specific_range]
    srs_equity = srs_equity.loc[srs_on_tot & srs_specific_range]

    if by == "diff":
        growth_value = df_roe.apply(growth, axis=0, by="diff")
        growth_value.sort_values(ascending=False, inplace=True)
        wind_code_select = growth_value.iloc[BOTTOM:UPPER].index.tolist()
        equity_list = srs_equity.loc[wind_code_select].values.tolist()
        print("The mean is: {0} and the standard deviation is: {1}".
              format(srs_equity.loc[wind_code_select].mean(), srs_equity.loc[wind_code_select].std()))
        title = "".join(["growth_diff_", str(range_roe[0]), "_", str(range_roe[1])])
        plot_bar(wind_code_select, equity_list, title)
    else:
        growth_value = df_roe.apply(growth, axis=0, by="regression")
        growth_value.sort_values(ascending=True, inplace=True)
        wind_code_select = growth_value.iloc[BOTTOM:UPPER].index.tolist()
        equity_list = srs_equity.loc[wind_code_select].values.tolist()
        print("The mean is: {0} and the standard deviation is: {1}".
              format(srs_equity.loc[wind_code_select].mean(), srs_equity.loc[wind_code_select].std()))
        # title = "".join(["growth_regression_", str(range_roe[0]), "_", str(range_roe[1])])
        # plot_bar(wind_code_select, equity_list, title)

    return wind_code_select

        # growth_value = df_roe.apply(growth, axis=0, by="regression")
        # srs_equity.sort_values(ascending=False, inplace=True)
        # wind_code_select = srs_equity.iloc[0:120].index.tolist()
        # growth_list = growth_value.loc[wind_code_select].values.tolist()
        # plot_bar(wind_code_select, growth_list, "Test")

        # wind_code_select = growth_value.iloc[::].index.tolist()
        # equity_list = srs_equity.loc[wind_code_select].values.tolist()
        # title = "".join(["growth_regression_", str(range_roe[0]), "_", str(range_roe[1])])
        # plot_bar(wind_code_select, equity_list, title)


if __name__ == "__main__":

    """
    The code is to test the effect that the financial defections bring about
    """

    raw_data_list = ['waa']

    """
    Load ROE
    """
    df_data_dict = retrieve_raw_data(raw_data_list)
    df_waa = df_data_dict['waa']

    """
    Loading the returns
    """
    df_return_slice = get_return_anl()
    for index, row in df_return_slice.iterrows():
        a = row[row > 3.0]
        print("Year: {0}   GT 1.3: {1}".format(index, len(a)))

    srs_return_tot = df_return_slice.prod(axis=0)

    srs_share_merit = srs_return_tot[srs_return_tot > 10]
    share_merit_list = srs_share_merit.index.tolist()

    """
    Loading the drawbacks
    """
    # df_drawback_daily = get_drawback(src="local")
    # srs_drawback_min = df_drawback_daily.min(axis=0)
    """
    The shares which are always on list are marked as True
    """
    df_on_list = get_annual_on_df()
    srs_on_total_list = df_on_list.apply(lambda x: False if False in x.values.tolist() else True, axis=0)

    """
    Do the statistics about the distribution of the returns
    """
    # stat_dis_ret(srs_return_tot, srs_on_total_list)

    """
    Select the shares by ROE stability and compare the returns
    """
    # select_by_stability(df_waa, srs_on_total_list, srs_return_tot, [0, 100])
    # select_by_stability(df_waa, srs_on_total_list, srs_return_tot, [5, 100])
    wind_code_stability = select_by_stability(df_waa, srs_on_total_list, srs_return_tot, [10, 100])
    abscissa_list = wind_code_stability
    ordinate_list = srs_return_tot.loc[wind_code_stability].values.tolist()

    """
    Select the shares by ROE growth and compare the returns
    """
    # select_by_growth(df_waa, srs_on_total_list, srs_return_tot, "diff", [-100, 100])
    wind_code_growth = select_by_growth(df_waa, srs_on_total_list, srs_return_tot, "regression", [-100, 100])

    """
    Show the drawback of the shares
    """
    # wind_code_list = srs_on_total_list.index.tolist()
    # drawback_show(wind_code_list, srs_drawback_min)

    # drawback_show(wind_code_stability, srs_drawback_min)

    # drawback_show(wind_code_growth, srs_drawback_min)
    # drawback_show(wind_code_stability, srs_drawback_min)

    wind_code_select = list(set(wind_code_stability).union(set(wind_code_growth)))

    wind_code_miss = list(set(share_merit_list).difference(set(wind_code_select)))

    print("The number of wind_code_select is: {0} and the number of share_merit_list is {1} "
          "and the number of wind_code_miss is {2}".
          format(len(wind_code_select), len(share_merit_list), len(wind_code_miss)))

    df_miss_roe = df_waa.loc[:, wind_code_miss]

    stability_value = df_miss_roe.apply(stability, axis=0)
    grow_value = df_miss_roe.apply(growth, axis=0)


    a=1
