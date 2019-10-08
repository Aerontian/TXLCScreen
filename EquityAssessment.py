# -*- coding: UTF-8 -*
import numpy as np
import math


def equity_assess(equity_np_array):

    """
    :param equity_np_array:
    :return: srs_index
    """
    equity_np_array = np.append([1.0], equity_np_array)
    return_np_array = equity_np_array[1: -1] / equity_np_array[0:-2] - 1
    equity_assess_dict = dict()
    """
    Trading Day Number
    """
    num_trade_day = len(equity_np_array) - 1
    equity_assess_dict['trading day number'] = num_trade_day
    """
    Equity
    """
    equity = equity_np_array[-1] / equity_np_array[0]
    equity_assess_dict['equity'] = equity
    """
    Annual Return
    """
    annual_return = math.pow(equity, 242.0 / num_trade_day) - 1
    equity_assess_dict['annual return'] = annual_return
    """
    Annual Volatility
    """
    annual_volatility = return_np_array.std() * (24 ** 0.5)
    equity_assess_dict['annual_volatility'] = annual_volatility
    """
    Sharp Ratio
    """
    sharp_ratio = annual_return / annual_volatility
    equity_assess_dict['sharp ratio'] = sharp_ratio
    """
    Win Day
    """
    num_win_day = len(return_np_array[return_np_array > 0.0])
    equity_assess_dict['win day'] = num_win_day
    """
    Lose Day
    """
    num_lose_day = len(return_np_array[return_np_array < 0.0])
    equity_assess_dict['lose day'] = num_lose_day
    """
    Win Ratio
    """
    win_ratio = (1.0 * num_win_day) / num_trade_day
    equity_assess_dict['win ratio'] = win_ratio
    """
    Win Mean
    """
    win_mean = return_np_array[return_np_array > 0.0].mean()
    equity_assess_dict['win mean'] = win_mean
    """
    Lose Mean
    """
    lose_mean = return_np_array[return_np_array < 0.0].mean()
    equity_assess_dict['lose mean'] = lose_mean
    """
    Win Lose Ratio
    """
    win_lose_ratio = win_mean / lose_mean
    equity_assess_dict['win lose ratio'] = win_lose_ratio
    """
    Max Win
    """
    max_win = return_np_array[return_np_array > 0.0].max()
    equity_assess_dict['max win'] = max_win
    """
    Max Lose
    """
    max_lose = return_np_array[return_np_array < 0.0].min()
    equity_assess_dict['max lose'] = max_lose

    return equity_assess_dict


def equity_assess_2(equity_np_array):

    """
    :param equity_np_array:
    :return: srs_index
    """
    equity_np_array = np.append([1.0], equity_np_array)
    return_np_array = equity_np_array[1: -1] / equity_np_array[0:-2] - 1
    equity_assess_dict = dict()
    """
    Trading Day Number
    """
    num_trade_day = len(equity_np_array) - 1
    equity_assess_dict['trading day number'] = num_trade_day
    """
    Equity
    """
    equity = equity_np_array[-1] / equity_np_array[0]
    equity_assess_dict['equity'] = equity
    """
    Annual Return
    """
    annual_return = math.pow(equity, 242.0 / num_trade_day) - 1
    equity_assess_dict['annual return'] = annual_return
    """
    Annual Volatility
    """
    annual_volatility = return_np_array.std() * (24 ** 0.5)
    equity_assess_dict['annual_volatility'] = annual_volatility
    """
    Sharp Ratio
    """
    sharp_ratio = annual_return / annual_volatility
    equity_assess_dict['sharp ratio'] = sharp_ratio
    """
    Win Day
    """
    num_win_day = len(return_np_array[return_np_array > 0.0])
    equity_assess_dict['win day'] = num_win_day
    """
    Lose Day
    """
    num_lose_day = len(return_np_array[return_np_array < 0.0])
    equity_assess_dict['lose day'] = num_lose_day
    """
    Win Ratio
    """
    win_ratio = (1.0 * num_win_day) / num_trade_day
    equity_assess_dict['win ratio'] = win_ratio
    """
    Win Mean
    """
    win_mean = return_np_array[return_np_array > 0.0].mean()
    equity_assess_dict['win mean'] = win_mean
    """
    Lose Mean
    """
    lose_mean = return_np_array[return_np_array < 0.0].mean()
    equity_assess_dict['lose mean'] = lose_mean
    """
    Win Lose Ratio
    """
    win_lose_ratio = win_mean / lose_mean
    equity_assess_dict['win lose ratio'] = win_lose_ratio
    """
    Max Win
    """
    max_win = return_np_array[return_np_array > 0.0].max()
    equity_assess_dict['max win'] = max_win
    """
    Max Lose
    """
    max_lose = return_np_array[return_np_array < 0.0].min()
    equity_assess_dict['max lose'] = max_lose

    return list(equity_assess_dict.keys()), list(equity_assess_dict.values())
