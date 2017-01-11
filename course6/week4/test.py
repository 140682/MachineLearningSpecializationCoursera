__author__ = 'astar'
# coding: utf-8

from sentiment_classifier import SentimentClassifier

clf = SentimentClassifier()

pred = clf.get_prediction_message([])

print pred