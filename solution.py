import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1226526788 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:   
    #alpha = 1 - p
    #n = len(x)
    #left = (-min(-x) - 1 / 2) / (14**2 / 2)
    #right = (-np.log(alpha) / n -min(-x) - 1 / 2) / (14**2 / 2)
    #return left, right
    import scipy.stats as st
    alfa = 1 - p
    lst = list(x)
    force = []
    for i in range(0,len(lst)):
      temp = 2*lst[i]/(14*14)
      force.append(temp)
    return st.t.interval(alpha=alfa,df=len(force)-1,loc=np.mean(force),scale=st.sem(force))
