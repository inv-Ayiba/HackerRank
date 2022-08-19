# https://projecteuler.net/problem=254
import math
def f(n):
    strNum=str(n)
    sumi=0
    for i in range(len(strNum)):
        sumi+=(math.factorial(int(strNum[i])))
    return(sumi)

def sf(n):
    ff=f(n)
    strNum=str(ff)
    sumi=0
    for i in range(len(strNum)):
        sumi+=(int(strNum[i]))
    return(sumi)
sf(234)