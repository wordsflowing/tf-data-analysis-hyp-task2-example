import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu


chat_id = 422119389 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, p = ttest_ind(x, y)
    return p < 0.08 # Ваш ответ, True или False
