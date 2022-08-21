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

def gfor(i,r):
    #smallest int such that sf(n)=i
    for n in range(r):
        if(sf(n)==i):
            # return("sf(",n,")=",i)
            return(n)


def sgfor(i,r):
    #sum of g(i) digits
    gg=gfor(i,r)
    strNum=str(gg)
    
    sumi=0
    try:
        for i in range(len(strNum)):
            sumi+=(int(strNum[i]))
        return(sumi)
    except(ValueError):
        return "error! range r probably too small"
        


def summforsg(ra1,ra2):
    sum=0
    for k in range(ra1,ra2+1):
        sum+= sgfor(k,268)
        print(k, sgfor(k,268))
    print(sum)
# print(sf(25))
print(sgfor(1,268))

import time
# summforsg(1,20)
#### why is sf(1) 1 and  sgfor(1,268) 0
target=sf
print(target.__name__)
# time.time.__name__ 