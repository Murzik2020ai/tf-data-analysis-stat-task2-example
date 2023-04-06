import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1226526788 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #alpha = 1 - p
    #loc = x.mean()
    #scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    #return loc - scale * norm.ppf(1 - alpha / 2), \
    #       loc - scale * norm.ppf(alpha / 2)
    import scipy.stats as st
    lst = list(x)
    force = []
    for i in range(0,len(lst)):
      temp = lst[i]/((i+1)*(i+1))
      force.append(temp)
    return st.t.interval(alpha=1-p,df=len(lst)-1,loc=np.mean(force),scale=st.sem(force))
