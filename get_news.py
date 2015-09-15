#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright(C) 2015 [Ruichaung Cao]


import tushare as ts
import jieba

df = ts.guba_sina(show_content=True)
print df.ix[3]['content']
print type(df.ix[3]['content'])
seglist = jieba.cut(df.ix[3]['content'])


count = {}
for x in seglist:
    print x
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

print str(count).decode('utf-8')

'''
print type(seglist)
print ' '.join(seglist)
count = {}
for x in seglist:
    print x
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

print count
'''