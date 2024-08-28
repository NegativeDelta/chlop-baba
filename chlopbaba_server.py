import math
import time

from flask import Flask
import pandas as pd
import random

import chlopbaba

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "hello chłop baba"


@app.route('/bench')
def bench():  # put application's code here
    return chlopbaba.bench()


@app.route('/chlop')
def chlop():  # put application's code here
    return chlopbaba.losuj_chlopa()


@app.route('/baba')
def baba():  # put application's code here
    return chlopbaba.losuj_babe()


if __name__ == '__main__':
    app.run()
