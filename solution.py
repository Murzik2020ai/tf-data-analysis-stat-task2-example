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
    #alpha = 1 - p
    #n = len(x)
    #left = (-min(-x) - 1 / 2) / (14**2 / 2)
    #right = (-np.log(alpha) / n -min(-x) - 1 / 2) / (14**2 / 2)
    #return left, right
      alfa = 1 - p
  # create dataframe for convinience
  df= pd.DataFrame({'x':x},index=[_ for _ in range(14)])
  # вычитаем из 0.5 чтобы получить логнормальное распределение
  df['0.5 - x'] = df['x'] - 0.5
  # логарифмируем чтобы получить нормальное распределение
  df['log'] = df['0.5 - x'].apply(np.log)
  #print(df)
  # вычисляем среднее
  loc = df['log'].mean()
  #print(loc)
  # вычисляем дисперсию
  std = df['log'].std()
  #print(std)
  # получаем шкалу
  scale = np.sqrt(std)/np.sqrt(len(x))
  #print(scale)
  # получаем левую оценку
  left = loc - scale * norm.ppf(1 - alfa/2)
  # получаем правую оценку
  right = loc - scale * norm.ppf(alfa/2)
  return 2*left/(14*14), 2*right/(14*14)
