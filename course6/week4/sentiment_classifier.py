#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'astar'
import sys
from sklearn.externals import joblib


class SentimentClassifier(object):
    def __init__(self):
        self.model = joblib.load("./SentimentModel.pkl")        
        self.classes_dict = {'1': u'положительный', '0': u'отрицательный', -1: u'произошла ошибка'}  
        

    def predict_text(self, text):
        try:                        
            return self.model.predict(text)[0]
                  
        except Exception as inst:
            print "prediction error"
            print inst
            return -1
        

    def get_prediction_message(self, text):
        prediction = self.predict_text(text)     
        print prediction
        return self.classes_dict[prediction]