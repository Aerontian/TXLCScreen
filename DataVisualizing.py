# -*- coding: UTF-8 -*
import os
import math
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import random


def rand_color():

    return random.randint(0, 255) / 255.0, random.randint(0, 255) / 255.0, random.randint(0, 255) / 255.0


# def plot_sum_equity_date_all(x_list, y_np_array, ref_np_array):
def plot_sum_equity_date_all(**kwargs):

    x_list = kwargs['date_list']
    y_np_array = kwargs['equity_np_array']
    ref_np_array = kwargs['ref_np_array']
    pos_pro_np_array = kwargs['pos_pro_np_array']

    if not (len(x_list) == y_np_array.shape[0] == ref_np_array.shape[0]):
        print("Abscissa and Ordinate do not share the same length.\n")
        os._exit(1)

    num_trade_day = len(x_list)
    trade_day_list = x_list
    abscissa_x_np_array = np.arange(1, num_trade_day + 1, 1)
    ordinate_y_np_array = y_np_array
    ordinate_ref_np_array = ref_np_array
    ordinate_pos_pro_np_array = pos_pro_np_array
    date_formatted = [datetime.strptime(d, '%Y%m%d').date() for d in trade_day_list]
    abscissa_label_full = [dt.strftime("%Y%m%d") for dt in date_formatted]

    if num_trade_day <= 8:
        abscissa_tick = list(range(1, num_trade_day + 1))
        abscissa_tick_label = abscissa_label_full[1:num_trade_day + 1]
    elif 8 < num_trade_day <= 20:
        abscissa_tick = list(range(1, num_trade_day + 1, 2))
        abscissa_tick_label = abscissa_label_full[1:num_trade_day + 1:2]
        if abscissa_tick[-1] != num_trade_day:
            abscissa_tick.append(num_trade_day)
            abscissa_tick_label.append(abscissa_label_full[-1])
    else:
        step = int(math.ceil(1.0 * num_trade_day / 10))
        abscissa_tick = list(range(1, num_trade_day + 1, step))
        abscissa_tick_label = abscissa_label_full[1:num_trade_day + 1:step]
        if abscissa_tick[-1] != num_trade_day:
            abscissa_tick.append(num_trade_day)
            abscissa_tick_label.append(abscissa_label_full[-1])

    # plt.plot(abscissa_data, ordinate_data_y, 'b')
    # plt.plot(abscissa_data, ordinate_data_index, 'r')
    fig = plt.figure()
    axis_equity = fig.add_subplot(111)
    line1 = axis_equity.plot(abscissa_x_np_array, ordinate_y_np_array, 'b', label='Portfolio')
    line2 = axis_equity.plot(abscissa_x_np_array, ordinate_ref_np_array, 'r', label='szzz')
    axis_equity.set_xticks(abscissa_tick)
    axis_equity.set_xticklabels(abscissa_tick_label, rotation=45, color="red", fontsize=6)
    axis_equity.set_ylabel("Equity")

    axis_pos = plt.twinx()
    line3 = \
        axis_pos.plot(abscissa_x_np_array, ordinate_pos_pro_np_array, 'y', label='Position Proportion')
    axis_pos.set_ylabel("Position")

    lines = line1 + line2 + line3
    labels = [line.get_label() for line in lines]

    axis_equity.legend(lines, labels, loc=0)
    axis_equity.grid(axis='both')

    return plt


def plot_sum_equity_date_group(**kwargs):

    x_list = kwargs['date_list']
    y_np_group_array_dict = kwargs['equity_np_group_array_dict']
    ref_np_array = kwargs['ref_np_array']
    pos_pro_np_array = kwargs['pos_pro_np_array']

    group_list = list(y_np_group_array_dict.keys())
    if not (len(x_list) == y_np_group_array_dict[group_list[0]].shape[0] == ref_np_array.shape[0]):
        print("Abscissa and Ordinate do not share the same length.\n")
        os._exit(1)

    num_trade_day = len(x_list)
    trade_day_list = x_list
    abscissa_x_np_array = np.arange(1, num_trade_day + 1, 1)
    ordinate_y_np_array_dict = y_np_group_array_dict
    ordinate_ref_np_array = ref_np_array
    ordinate_pos_pro_np_array = pos_pro_np_array
    date_formatted = [datetime.strptime(d, '%Y%m%d').date() for d in trade_day_list]
    abscissa_label_full = [dt.strftime("%Y%m%d") for dt in date_formatted]

    if num_trade_day <= 8:
        abscissa_tick = list(range(1, num_trade_day + 1))
        abscissa_tick_label = abscissa_label_full[1:num_trade_day + 1]
    elif 8 < num_trade_day <= 20:
        abscissa_tick = list(range(1, num_trade_day + 1, 2))
        abscissa_tick_label = abscissa_label_full[1:num_trade_day + 1:2]
        if abscissa_tick[-1] != num_trade_day:
            abscissa_tick.append(num_trade_day)
            abscissa_tick_label.append(abscissa_label_full[-1])
    else:
        step = int(math.ceil(1.0 * num_trade_day / 10))
        abscissa_tick = list(range(1, num_trade_day + 1, step))
        abscissa_tick_label = abscissa_label_full[1:num_trade_day + 1:step]
        if abscissa_tick[-1] != num_trade_day:
            abscissa_tick.append(num_trade_day)
            abscissa_tick_label.append(abscissa_label_full[-1])

    # plt.plot(abscissa_data, ordinate_data_y, 'b')
    # plt.plot(abscissa_data, ordinate_data_index, 'r')
    plt.ioff()
    fig = plt.figure(figsize=(8, 6))
    # fig = plt.figure()
    axis_equity = fig.add_subplot(111)
    line1 = []
    for ii_group, ordinate_np_array in ordinate_y_np_array_dict.items():
        color = rand_color()
        line = axis_equity.plot(abscissa_x_np_array, ordinate_np_array, linewidth=0.5, color=color, label=str(ii_group))
        line1 = line1 + line

    line2 = axis_equity.plot(abscissa_x_np_array, ordinate_ref_np_array, 'r--', linewidth=1.5, label='market')
    axis_equity.set_xticks(abscissa_tick)
    font = {"weight": "bold", "color": "red", "fontsize": 6}
    axis_equity.set_xticklabels(abscissa_tick_label, rotation=45, fontdict=font)
    axis_equity.set_ylabel("Equity")

    # axis_pos = plt.twinx()
    # line3 = \
    #     axis_pos.plot(abscissa_x_np_array, ordinate_pos_pro_np_array, 'y', label='Position Proportion')
    # axis_pos.set_ylabel("Position")

    # lines = line1 + line2 + line3
    lines = line1 + line2
    labels = [line.get_label() for line in lines]

    axis_equity.legend(lines, labels, loc=0)
    axis_equity.grid(axis='both')

    font = {"weight": "bold", "fontsize": 9}
    plt.xlabel("Trading Day", fontdict=font)
    plt.ylabel("Equity", fontdict=font)

    return plt


def plot_eqy_all_group(df_eqy_grp, df_eqy_mkt_avg):

    x_list = df_eqy_grp.index.tolist()
    ref_np_array = df_eqy_mkt_avg.values

    num_trade_day = len(x_list)
    trade_day_list = x_list
    abscissa_x_np_array = np.arange(1, num_trade_day + 1, 1)

    ordinate_ref_np_array = ref_np_array
    date_formatted = [datetime.strptime(d, '%Y%m%d').date() for d in trade_day_list]
    abscissa_label_full = [dt.strftime("%Y%m%d") for dt in date_formatted]

    if num_trade_day <= 8:
        abscissa_tick = list(range(1, num_trade_day + 1))
        abscissa_tick_label = abscissa_label_full[1:num_trade_day + 1]
    elif 8 < num_trade_day <= 20:
        abscissa_tick = list(range(1, num_trade_day + 1, 2))
        abscissa_tick_label = abscissa_label_full[1:num_trade_day + 1:2]
        if abscissa_tick[-1] != num_trade_day:
            abscissa_tick.append(num_trade_day)
            abscissa_tick_label.append(abscissa_label_full[-1])
    else:
        step = int(math.ceil(1.0 * num_trade_day / 10))
        abscissa_tick = list(range(1, num_trade_day + 1, step))
        abscissa_tick_label = abscissa_label_full[1:num_trade_day + 1:step]
        if abscissa_tick[-1] != num_trade_day:
            abscissa_tick.append(num_trade_day)
            abscissa_tick_label.append(abscissa_label_full[-1])

    plt.ioff()
    fig = plt.figure(figsize=(8, 6))

    axis_equity = fig.add_subplot(111)
    line1 = []
    color_list = ['blue', 'lime', 'yellow', 'orange', 'forestgreen', 'tan', 'violet', 'purple', 'darkcyan', 'slategray']
    for ii_grp, df_cols in df_eqy_grp.items():
        # color = rand_color()
        color = color_list[ii_grp - 1]
        ordinate_np_array = df_cols.values.tolist()
        line = axis_equity.plot(abscissa_x_np_array, ordinate_np_array, linewidth=0.5, color=color, label=str(ii_grp))
        line1 = line1 + line

    line2 = axis_equity.plot(abscissa_x_np_array, ordinate_ref_np_array,
                             color='red', linestyle='dashed', label='market')
    axis_equity.set_xticks(abscissa_tick)
    font = {"weight": "bold", "color": "red", "fontsize": 6}
    axis_equity.set_xticklabels(abscissa_tick_label, rotation=45, fontdict=font)
    axis_equity.set_ylabel("Equity")

    lines = line1 + line2
    labels = [line.get_label() for line in lines]

    axis_equity.legend(lines, labels, loc=0)
    axis_equity.grid(axis='both')

    font = {"weight": "bold", "fontsize": 9}
    plt.xlabel("Trading Day", fontdict=font)
    plt.ylabel("Equity", fontdict=font)

    return plt


def plot_bar(ic_dict):

    year_list = []
    ic_list = []
    for key, value in ic_dict.items():
        if value:
            year_list.append(key)
            ic_list.append(value)

    plt.ioff()
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)

    plt.bar(year_list, ic_list)
    xtick_labels = year_list
    max_ic = max(ic_list)
    min_ic = min(ic_list)
    up_tick = math.ceil(max_ic / 0.05)
    down_tick = math.floor(min_ic / 0.05)
    ytick = [ii_tick / 20.0 for ii_tick in list(range(down_tick, up_tick + 1, 1))]
    ytick_labels = ["{:+.2f}".format(ii_tick) for ii_tick in ytick]

    font = {"weight": "bold", "fontsize": 9}
    plt.xlabel("Year", fontdict=font)
    plt.ylabel("IC", fontdict=font)
    font = {"weight": "bold", "color": "red", "fontsize": 9}
    ax.set_xticklabels(xtick_labels, rotation=45, fontdict=font)

    ax.set_yticks(ytick)
    font = {"weight": "bold", "fontsize": 9}
    ax.set_yticklabels(ytick_labels, fontdict=font)

    return plt


def plot_regression(series_factor, series_return, y_data_fitted, fac_id):

    plt.ioff()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(series_factor, series_return, 'o', label='data')
    ax.plot(series_factor, y_data_fitted, 'r--.', label='OLS')
    ax.legend(loc='best')
    font = {'family': 'Times New Roman', 'size': 12, 'weight': 'bold'}
    plt.ylabel('Return %', fontdict=font)
    font = {'family': 'Times New Roman', 'size': 12, 'weight': 'bold', 'color': 'red'}
    plt.xlabel('{0}'.format(fac_id), fontdict=font)
    # font = {'family': 'Times New Roman', 'size': 10, 'weight': 'bold'}

    plt.yticks(fontproperties='Times New Roman', size=10, weight='bold')
    plt.xticks(fontproperties='Times New Roman', size=10, weight='bold')

    plt.grid()

    return plt


