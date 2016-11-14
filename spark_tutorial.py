from collections import namedtuple
from csv import DictReader
from pyspark import SparkContext

sc = SparkContext()
Row = namedtuple('Row', ['year', 'occupation', 'show', 'group', 'guess_list'])
f = open('daily_show_guests.csv', 'r')
reader = DictReader(f)