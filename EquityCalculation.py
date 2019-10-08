# -*- coding: UTF-8 -*
import numpy as np


def get_daily_equity(slice_pct_np_array, init_equity, pos_wgh_np_array=None):

    (date_num, wind_code_num) = slice_pct_np_array.shape

    if pos_wgh_np_array is None:
        """
        The weight for the cash in position is set to be 1 constantly
        """
        pos_wgh_np_array = np.ones([wind_code_num, ])

    if wind_code_num > 0:

        date_return_np_array = np.cumprod(slice_pct_np_array / 100.0 + 1, axis=0)
        # init_values_share_np_diag_array = np.diag(init_values_share_np_array)
        # date_value_np_array = \
        #     np.matmul(date_return_np_array, init_values_share_np_diag_array)
        # date_sum_value_np_array = np.sum(date_value_np_array, axis=1)
        pos_wgh_np_diag_array = np.diag(pos_wgh_np_array)
        date_return_np_array = \
            np.matmul(date_return_np_array, pos_wgh_np_diag_array)
        date_sum_value_np_array = np.sum(date_return_np_array, axis=1)

        date_sum_value_ex_np_array = np.ones([date_num + 1, ]) * np.sum(pos_wgh_np_array)
        date_sum_value_ex_np_array[1:] = date_sum_value_np_array
        """
        epct is the abbreviation for Equivalent Percentage Change
        """
        epct_np_array = \
            (date_sum_value_ex_np_array[1:] / date_sum_value_ex_np_array[0:-1] - 1)

        daily_equity_np_array = init_equity * np.cumprod(1 + epct_np_array)
    else:
        daily_equity_np_array = init_equity * np.ones([date_num, ])

    return daily_equity_np_array
