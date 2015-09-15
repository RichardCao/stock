#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright(C) 2015 [Ruichaung Cao]

import MySQLdb
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

conn=MySQLdb.connect(host="localhost",
                     user="stock",
                     passwd="stock",
                     db="stock",
                     charset="utf8")

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS sh")
sql_cmd = """CREATE TABLE sh(id int PRIMARY KEY auto_increment,
                             shdate DATE ,
                             code VARCHAR (6),
                             shname VARCHAR (16),
                             endprice FLOAT,
                             highprice FLOAT,
                             lowprice FLOAT,
                             startprice FLOAT,
                             formerprice FLOAT,
                             changeamount FLOAT,
                             changepercent FLOAT,
                             tradingcount DOUBLE ,
                             tradingamount DOUBLE )"""
cursor.execute(sql_cmd)
conn.commit()

lines = []
with open('000001.csv', 'rb') as f:
    reader = csv.reader(f)
    lines = [line for line in reader]


#import chardet
#print lines[2][2],
#    print type(ins).__name__
#print chardet.detect(lines[2][2])
#print lines[2][2].decode("GB2312").encode('utf-8')


import datetime
from datetime import date
str = '2012-11-19'
date_time = datetime.datetime.strptime(str,'%Y-%m-%d')
date_time.date()

for line in lines[1:]:
    for index, ins in enumerate(line):
        if ins == 'None':
            line[index] = '-999999.99'
    sql_cmd = "INSERT INTO sh(shdate, code, shname, endprice, highprice, lowprice, startprice, formerprice, changeamount," \
              "changepercent, tradingcount, tradingamount) VALUES ('%s', %s', '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s)"\
              % (datetime.datetime.strptime(line[0],'%Y-%m-%d').date(), line[1], unicode(line[2],"GB2312"), line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11])
#    print sql_cmd
    cursor.execute(sql_cmd)
    conn.commit()

