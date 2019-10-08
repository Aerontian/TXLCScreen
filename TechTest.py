import pandas as pd
import numpy as np


if __name__ == "__main__":

    # df = pd.DataFrame(np.linspace(start=0, stop=100, num=101))
    df = pd.DataFrame(np.array([1, 1, 1, 1, 1, 1, 2]))
    for ii_value in range(0, 11, 1):
        line = df.quantile(ii_value / 10.0, axis=0, interpolation='midpoint').values[0]
        print("quantile: {0} is {1}".format(ii_value / 10.0, line))
