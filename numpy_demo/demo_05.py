import numpy as np


def fill_nan_array(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]
        nan_num = np.count_nonzero(temp_col != temp_col)
        if nan_num != 0:
            temp_not_nan_col = temp_col[temp_col == temp_col]
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
    return t1


if __name__ == '__main__':
    t2 = np.arange(24).reshape((4, 6)).astype(float)

    t2[1, 2:] = np.nan

    t2 = fill_nan_array(t2)

    print(t2.astype(int))
