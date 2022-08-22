# https://projecteuler.net/problem=254
import math
universalRange=2000



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
        if(sf(n)==i and n!=0):
            #have to remove 0(zero) 
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
    worked=150 ##test
    for k in range(ra1,ra2+1):
        if(sgfor(k,universalRange)=="error! range r probably too small"):
            # print(k,"messed up") ##test
            worked-=1  ##test
        try:
            sum+= sgfor(k,universalRange)
        except(TypeError):
            continue
        # print(k, sgfor(k,universalRange))  ##test string
    return(sum,"  ","worked :",worked,"  at range:",universalRange) ##test
    # return(sum)

# print(summforsg(1,150))
print(sgfor(150,100000))



# print(sf(25))
# target2 = sgfor ;print(target2.__name__,"  ",target2(1,universalRange))
# import time


# target=sf ;print(target.__name__,"  ",target(1))
# time.time.__name__ 