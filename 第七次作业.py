import numpy as np

global k
k=1

def f(x):
    return np.e**x-3
def func(a,b,sigma):
    mid=(a+b)/2.
    global k
    if f(a)*f(b)>0:
        return '方程无解'
    elif f(a)*f(b)==0:
        if f(a)==0:
            return a
        else:
            return b
    elif abs(b-a)<sigma:
        return mid
    else:
        k=k+1
        if (f(a)*f(mid)< 0):
            return func(a, mid, sigma)
        else:
            return func(mid, b, sigma)

a=int(input('请输入左边界:'))
b=int(input('请输入右边界:'))
s=float(input('请输入误差精度:'))
result=func(a,b,s)
print('方程的解为：',result)
print('运行次数：',k)