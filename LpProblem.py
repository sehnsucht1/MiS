# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:23:36 2020

@author: sehnsucht.
"""

from pulp import *
def Lp():
  
  prob = LpProblem("分支定界",LpMaximize)
  x1 = LpVariable("x1",0)
  x2 = LpVariable("x2",0)
  prob += 2*x1 + 3*x2
  prob += x1 + 2*x2 <= 8
  prob += x1 <=4
  prob += 4*x2 <= 12
  prob.solve()
  print("StatusL:",LpStatus[prob.status])
  for i in prob.variables():
    print(i.name,"=",i.varValue)
  print("resulet = ",value(prob.objective))
if __name__ == '__main__':
  Lp()
  