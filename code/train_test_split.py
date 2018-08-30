#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/16
import random


def train_test_triple_split(infile, test_rate=0.2):
    with open('origin_data/target_train_triple.txt', 'w') as f_train, \
            open('origin_data/target_test_triple.txt', 'w') as f_test:
        for line in open(infile):
            if random.random() > test_rate:
                f_train.write(line)
            else:
                f_test.write(line)
def train_test_triple(infile):
    train = {}
    test = {}
    for line in open('origin_data/target_train_triple.txt'):
        train[line.strip()]=1
    for line in open('origin_data/target_test_triple.txt'):
        test[line.strip()]=1
    with open('origin_data/target_train.txt', 'w') as f_train, \
         open('origin_data/target_test.txt', 'w') as f_test:
        for line in open(infile):
            t = line.strip().split('\t')
            if t[0]+'#'+t[1]+'#'+t[4]  in train:
                f_train.write(line)
            else:
                f_test.write(line)


if __name__ == '__main__':
    train_test_triple_split('origin_data/target_triple.txt')
    train_test_triple('origin_data/target_nyt.txt')

