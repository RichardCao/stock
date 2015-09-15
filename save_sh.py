#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright(C) 2015 [Ruichaung Cao]

import tushare as ts
# import sqlalchemy

sz50 = ts.get_sz50s()
print sz50

df  = ts.get_hist_data('sh', start='2015-02-01', end='2015-02-20')
print df
