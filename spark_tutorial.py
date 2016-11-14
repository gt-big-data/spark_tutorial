from collections import namedtuple
from csv import DictReader

from pyspark import SparkContext
from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint

sc = SparkContext()
Row = namedtuple('Row', ['year', 'occupation', 'show', 'group', 'guess_list'])
f = open('daily_show_guests.csv', 'r')
reader = DictReader(f)
