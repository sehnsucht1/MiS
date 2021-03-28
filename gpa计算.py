def gpa(x):
	return 4-3*(100-x)**2/1600
zongx = 0
zongg1 = 0
zongg2 = 0
while 1:
    fenshu,xuefen = map(float,input().split())
    if fenshu == xuefen:
        break
    zongx += xuefen
    zongg1 += xuefen*gpa(fenshu)
    zongg2 += xuefen*fenshu
print("您的gpa为%.4f"%(zongg1/zongx))
print("另一种算法：%.4f"%(gpa(zongg2/zongx)))
