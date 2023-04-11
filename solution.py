import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu
from scipy import stats


chat_id = 422119389 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    res = stats.cramervonmises_2samp(x, y)
    return res.pvalue < 0.08 # Ваш ответ, True или False
