# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/15 4:05 下午
@Auth ： Codewyf
@File ：score_filter.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
from operator import itemgetter
predictions = [['A', 'B', 'A'], [(1,1,4,4), (3,3,6,6), (0,1,8,7)], [0.98, 0.84, 0.85]]

threshold = {'A': 0.95, 'B': 0.90}


def filter(predictions, threshold):
    for i in range(len(predictions[0])):
        if predictions[0][i] == 'A':
            if predictions[2][i] > threshold['A']:
                result = [x[i] for x in predictions ]
                print(f'filtered_predictions = {result}')
            else:
                print('The score is lower than threshold')
        else:
            if predictions[0][i] == 'B':
                if predictions[2][i] > threshold['B']:
                    result = [x[i] for x in predictions]
                    print(f'filtered_predictions = {result}')
                else:
                    print('The score is lower than threshold')



filter(predictions, threshold)