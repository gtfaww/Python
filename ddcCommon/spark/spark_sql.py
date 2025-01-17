#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from pyspark import SparkContext, SparkConf
from pyspark.sql.context import SQLContext
from pyspark.sql.types import Row

__author__ = 'guotengfei'
__time__ = 2019 / 11 / 26

"""
Module comment
"""

LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':
    conf = SparkConf().setAppName('vcom')
    sc = SparkContext(conf=conf)
    sql = SQLContext(sc)

    lines = sc.textFile('../data/users.txt')
    user = lines.map(lambda l: l.split(",")).map(lambda p: (p[0], p[1]))

    sql.createDataFrame(user, ['id', 'name']).registerTempTable('user')
    df = sql.sql("select id,name from user")

    df.write.save("../data/result", format='json')
