import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 689985882 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    a = True
    ttest = ttest_ind(x, y, equal_var=False)
    p = ttest.pvalue
    if (p<=0.01):
        a = False
    return a
