# -*- coding: UTF-8 -*
import pandas as pd

path_stk = "/home/aeront/PycharmProjects/LocalDataBase(YFFormat)/DataReservoir"
filename_stk = "stk_update.dat"
path_filename_stk = "".join([path_stk, "/", filename_stk])
df_stk = pd.read_pickle(path_filename_stk)
NUM_WIND_CODE = len(df_stk)


