#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright(C) 2015 [Ruichaung Cao]

import jieba

jieba.load_userdict('user_dict.txt')
seg_list = jieba.cut('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')
print '/ '.join(seg_list)

seg_list = jieba.cut_for_search('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')
print '/ '.join(seg_list)
