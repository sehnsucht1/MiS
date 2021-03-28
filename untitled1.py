# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:47:45 2020

@author: sehnsucht.
"""

vernum,edgenum = map(int,input().split())
m = [[0 for i in range(vernum)] for i in range(vernum)]
for i in range(edgenum):
  a,b = map(int,input().split())
  m[a-1][b-1] = 1
  m[b-1][a-1] = 1
  

