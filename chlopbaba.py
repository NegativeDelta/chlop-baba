import math
import time

from flask import Flask
import pandas as pd
import random

fi = pd.read_csv("csv/f_imiona.csv", header=0, encoding="cp1250", delimiter=";", engine='python')
fn = pd.read_csv("csv/f_nazwiska.csv", header=0, encoding="cp1250", delimiter=";", engine='python')
mi = pd.read_csv("csv/m_imiona.csv", header=0, encoding="cp1250", delimiter=";", engine='python')
mn = pd.read_csv("csv/m_nazwiska.csv", header=0, encoding="cp1250", delimiter=";", engine='python')


def slowsearch(n, df, column_index):
    if df.iloc[0].iloc[column_index] > n:
        return 0
    for i in range(1, len(df)):
        if df.iloc[i].iloc[column_index] > n:
            return i


def binsearch(n, df, column_index):
    step = pos = int(math.ceil(len(df) / 2))
    iteracje = 0
    while True:
        iteracje += 1
        step = int(math.ceil(step / 2))
        # print(n, step, pos, iteracje)
        if df.iloc[pos].iloc[column_index] > n > df.iloc[pos - 1].iloc[column_index] or iteracje > 30:
            return pos
        elif df.iloc[pos].iloc[column_index] > n:
            pos -= step
        else:
            pos += step


def losuj(s):
    while True:
        h = \
            s.iloc[
                int(binsearch(random.randint(0, s.iloc[len(s) - 1].iloc[len(s.columns) - 1]), s,
                              len(s.columns) - 1))].iloc[
                0].title()
        if "?" not in h:
            return h
        print(f"był ewenement: {h}")


def bench():  # put application's code here
    start = time.time()
    iteracje = 0
    while time.time() - start < 1:
        iteracje += 1
        losuj(mi)
        losuj(mn)
        losuj(fi)
        losuj(fn)
    return f"iteracje: {iteracje} : wychodzi średnio {iteracje / 2}/s"


def losuj_chlopa():  # put application's code here
    return [losuj(mi), losuj(mn)]


def losuj_babe():  # put application's code here
    return [losuj(fi), losuj(fn)]
