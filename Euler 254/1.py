# https://projecteuler.net/problem=254
#Define f(n) as the sum of the factorials of the digits of n. For example, f(342) = 3! + 4! + 2! = 32.

# Define sf(n) as the sum of the digits of f(n). So sf(342) = 3 + 2 = 5.

# Define g(i) to be the smallest positive integer n such that sf(n) = i. Though sf(342) is 5, sf(25) is also 5, and it can be verified that g(5) is 25.

# Define sg(i) as the sum of the digits of g(i). So sg(5) = 2 + 5 = 7.

# Further, it can be verified that g(20) is 267 and ∑ sg(i) for 1 ≤ i ≤ 20 is 156.

# What is ∑ sg(i) for 1 ≤ i ≤ 150?
# lengedre formula looks promising
import math
universalRange=2000

def inHere(this,here):
    try:
        yoou =here.index(this)
        return True
    except(ValueError):
        
        return False


def f(n):
    # f(33) = 12 because 3!+3!=12 
    strNum=str(n)
    sumi=0
    for i in range(len(strNum)):
        sumi+=(math.factorial(int(strNum[i])))
    return(sumi)
def newf(n):
    # f(33) = 12 because 3!+3!=12 
    strNum=str(n)
    if(len(strNum)==1):sumi+=(math.factorial(int(strNum[0])))
    if(len(strNum)==2):sumi+=(math.factorial(int(strNum[0]))) ;sumi+=(math.factorial(int(strNum[1]))) 
    if(len(strNum)==3):sumi+=(math.factorial(int(strNum[0]))) ;sumi+=(math.factorial(int(strNum[1])));sumi+=(math.factorial(int(strNum[2])))

    
    return(sumi)
tagrget=13


def sf(n):
    # sf(33) = 3 because f(33)=12, and 1+2=3
    # sf(5)= 3 because f(5)=120, and 1+2+0=3
    ff=f(n)
    strNum=str(ff)
    sumi=0
    for i in range(len(strNum)):
        sumi+=(int(strNum[i]))
    return(sumi)

def gfor(i,r=2500):
    #smallest int such that sf(n)=i
    #gfor(11)= 26 because sf(26)=11
    for n in range(r):
        if(sf(n)==i and n!=0):
            #have to remove 0(zero) 
            # return("sf(",n,")=",i)
            
            return(n)

def sgfor(i,r=2500):
    #sum of g(i) digits
    #sgfor(11)= 8 ,gfor(11)= 26 so 2+6= 8
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
    # sum of from sgfor(ra1) to sgfor(ra2)
    sum=0
    worked=150 ##test
    workedList=[]
    for k in range(ra1,ra2+1):
        
        try:
            grab=sgfor(k,universalRange)
            if(grab=="error! range r probably too small"):
                worked-=1  ##test


            sum+= grab
            workedList.append(k) ##test
        except(TypeError):
            continue
    # return(workedList)
    return(sum,"  ","worked :",worked,"  at range:",universalRange) ##test
    # return(sum)


excludeobj={2000:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]}
#[number,g()] = [[1, 1], [2, 2], [3, 5], [4, 15], [5, 25], [6, 3], [7, 13], [8, 23], [9, 6], [10, 16], [11, 26], [12, 44], [13, 144], [14, 256], [15, 36], [16, 136], [17, 236], [18, 67], [19, 167], [20, 267], [21, 349], [22, 1349], [24, 49], [25, 149], [26, 249], [27, 9], [28, 19], [29, 29], [30, 129], [31, 229], [32, 1229], [33, 39], [34, 139], [35, 239], [36, 1239]]
target04=excludeobj[2000]
take=[]
count = 0
# # # for i in range(len(target04)):
# # #     take.append([target04[i],gfor(target04[i],2500)])
# # #     count+=1

# #generate an array ,don't recall what it's for though
# for i in range(1,36+1):
#     take.append([i,gfor(i,2500)])
#     count+=1

print(summforsg(1,20))


def justSumDigits(num,wantit="yes"):
    food=str(num)
    sum=0
    for i in range(len(food)):
        sum+=int(food[i])
    if wantit=="yes":
        return sum
    else:
        return "//////////"

target = 99999999999999996

divide =(target/math.factorial(9))
giberish=(divide*math.factorial(9))




# target = 999999999999999999999999999999999999999999999999999999999999999





# import time


# time.time.__name__ 





