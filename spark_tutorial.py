from collections import namedtuple
from csv import DictReader

from pyspark import SparkContext
from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint

sc = SparkContext()
Row = namedtuple('Row', ['year', 'occupation', 'show', 'group', 'guess_list'])
f = open('daily_show_guests.csv', 'r')
reader = DictReader(f)

def parse(line):
    label, height, weight = line.split(',')
    return LabeledPoint(float(label), [float(height), float(weight)])

athletes = sc.textFile('athletes.csv') \
    .map(parse)

model = SVMWithSGD.train(athletes, iterations=1000)
predictions = athletes.map(lambda p: (p.label, model.predict(p.features)))
accuracy = predictions.filter(lambda (v, p): v != p)

print 'Error: {}'.format(accuracy.count() / float(athletes.count()))

# daily_show = sc.parallelize([Row(**r) for r in reader])

# guests = daily_show.map(lambda show: (show.occupation, 1)) \
#     .reduceByKey(lambda x, y: x + y)
# """
# [ (1991, 1)]
# """
# print guests.take(guests.count())
