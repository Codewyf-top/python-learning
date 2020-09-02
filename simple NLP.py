# -*- coding: utf-8 -*-
"""
@Time ： 2020/9/2 4:00 下午
@Auth ： Codewyf
@File ：simple NLP.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
import re

def parse(text):
    text = re.sub(r'[^\w ]', ' ', text)#使用正则化表达式去除标点符号和换行符
    text = text.lower()         #转为小写
    word_list = text.split(' ') #生成所有单词的列表
    word_list = filter(None, word_list)     #去除空白单词
    word_cnt = {}               #生成单词和词频的字典
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1

    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)  #按照词频排序

    return sorted_word_cnt

with open('in.txt', 'r') as fin:
    text = fin.read()

word_and_freq = parse(text)

with open('out.txt', 'w') as fout:
    for word, freq in word_and_freq:
        fout.write('{} {}\n'.format(word, freq))