# https://projecteuler.net/problem=254
import math
universalRange=2000

def inHere(this,here):
    try:
        yoou =here.index(this)
        return True
    except(ValueError):
        
        return False

# print(inHere(3,[2,4,56]))

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
    workedList=[]
    for k in range(ra1,ra2+1):
        
        try:
            grab=sgfor(k,universalRange)
            if(grab=="error! range r probably too small"):
                # print(k,"messed up") ##test
                worked-=1  ##test


            sum+= grab
            workedList.append(k) ##test
        except(TypeError):
            continue
        # print(k, grab)  ##test string
    # return(workedList)
    return(sum,"  ","worked :",worked,"  at range:",universalRange) ##test
    # return(sum)

# print(summforsg(1,150))
# print(sgfor(150,100000)) ##

excludeobj={2000:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]}
#[number,g()] = [[1, 1], [2, 2], [3, 5], [4, 15], [5, 25], [6, 3], [7, 13], [8, 23], [9, 6], [10, 16], [11, 26], [12, 44], [13, 144], [14, 256], [15, 36], [16, 136], [17, 236], [18, 67], [19, 167], [20, 267], [21, 349], [22, 1349], [24, 49], [25, 149], [26, 249], [27, 9], [28, 19], [29, 29], [30, 129], [31, 229], [32, 1229], [33, 39], [34, 139], [35, 239], [36, 1239]]
target04=excludeobj[2000]
take=[]
count = 0
# # # for i in range(len(target04)):
# # #     take.append([target04[i],gfor(target04[i],2500)])
# # #     count+=1
# # # print(take)
# # # print("count",count)

for i in range(1,36+1):
    take.append([i,gfor(i,2500)])
    count+=1
print(take)
print("count",count)


# print(sf(25))
# target2 = sgfor ;print(target2.__name__,"  ",target2(1,universalRange))
# import time


# target=sf ;print(target.__name__,"  ",target(1))
# time.time.__name__ 