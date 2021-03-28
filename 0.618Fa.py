def f(x):
    return x*x-6*x+2
while 1:
    a,b = map(float,input().split())
    l = b - a
    lam,miu = a + 0.382*l,a+0.618*l
    print("a=%.3f,b=%.3f,l=%.3f,lam=%.3f,miu=%.3f,f1=%.3f,f2=%.3f"%(a,b,l,lam,miu,f(lam),f(miu)))
