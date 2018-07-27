#!/usr/bin/python
#Reducer.py
import sys

symboldate = {}
symbolhigh = {}
#Partitoner
for line in sys.stdin:
    line = line.strip()
    symbol,open,high = line.split('\t')

    if symbol in symboldate:
        symboldate[symbol].append(float(open))
	symbolhigh[symbol].append(float(high))
    else:
        symboldate[symbol] = []
	symbolhigh[symbol] = []
        symboldate[symbol].append(float(open))
	symbolhigh[symbol].append(float(high))

#Reducer
for symbol in symboldate.keys():
    ave_age = max(symboldate[symbol])
    min_age = min(symbolhigh[symbol])
    print '%s\t%s\t%s'% (symbol,ave_age,min_age)
