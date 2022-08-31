import math
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
    sumi=0
    if(len(strNum)==1):sumi+=(math.factorial(int(strNum[0])))
    if(len(strNum)==2):sumi+=(math.factorial(int(strNum[0]))) ;sumi+=(math.factorial(int(strNum[1]))) 
    if(len(strNum)==3):sumi+=(math.factorial(int(strNum[0]))) ;sumi+=(math.factorial(int(strNum[1])));sumi+=(math.factorial(int(strNum[2])))

    
    return(sumi)

def sf(n):
    # sf(33) = 3 because f(33)=12, and 1+2=3
    # sf(5)= 3 because f(5)=120, and 1+2+0=3
    ff=f(n)
    strNum=str(ff)
    sumi=0
    for i in range(len(strNum)):
        sumi+=(int(strNum[i]))
    return(sumi)

def gfor(i,r1=0,r=2500):
    # added r1 to range
    #smallest int such that sf(n)=i
    #gfor(11)= 26 because sf(26)=11
    for n in range(r1,r):
        if(sf(n)==i and n!=0):
            #have to remove 0(zero) 
            # return("sf(",n,")=",i)
            
            return(n)


def sgfor(i,r1=0,r=2500):
    #sum of g(i) digits
    #sgfor(11)= 8 ,gfor(11)= 26 so 2+6= 8
    gg=gfor(i,r1,r)
    strNum=str(gg)
    
    sumi=0
    try:
        for i in range(len(strNum)):
            sumi+=(int(strNum[i]))
        return(sumi)
    except(ValueError):
        return "error! range r probably too small"


tagrget=299
# # print("no.1",gfor(29))
# print("no.2",sgfor(29))

# print(newf(tagrget))

# print(math.factorial(10))
# print((2**5) * (3**3) * (5**2) *7*9)







def newg(I):
    nothing=0

def getFactOut(k):
    # getFactOut(1)=1, getFactOut(2)=2,getFactOut(3)=21{because 2! + 1! =3} ,getFactOut(5)=25{because 2!+5!=122,and 1+2+2=5}
    print("cocococ")



##f(25) =122
##sf(25) = 5

#g(5)= 25
#sg(5)= 7


    ##f(?1) =?2=99999....6
    ##sf(?1) = 150

    #g(150)= ?1
    #sg(150)= ?3


##f(29) =362882
##sf(29) = 29

#g(29)= 29
#sg(29)= 11

    ##f(299) =725762 
    ##sf(299) = 29

    #g(29)= 29
    #sg(29)= 11


num=45
# print(num,",",gfor(num,44000,80000))

def oyago(numstart,numend,r1,r2,gap):
    g=[]
    sg=[]
    while numstart!=numend:
        gg=gfor(numstart,r1,r2)
        if(gg!=None):
            g.append([numstart,gg])
            numstart+=1
        else:
            r1=r2
            r2+=gap
        print(numstart,r1,r2,g)
# oyago(46,56,1,147,50000) # outpput man!

def addDigits(num):
    strNum=str(num)
    sumi=0
    for i in range(len(strNum)):
        sumi+=int(strNum[i])
    return(sumi)

# sequenceOfnumberAndg = [[1, 1], [2, 2], [3, 5], [4, 15], [5, 25], [6, 3], [7, 13], [8, 23], [9, 6], [10, 16], [11, 26], [12, 44], [13, 144], [14, 256], [15, 36], [16, 136], [17, 236], [18, 67], [19, 167], [20, 267], [21, 349], [22, 1349], [23, 2349], [24, 49], [25, 149], [26, 249], [27, 9], [28, 19], [29, 29], [30, 129], [31, 229], [32, 1229], [33, 39], [34, 139], [35, 239], [36, 1239],[37, 13339],[38 , 23599],[39 , 44679],[40, 44079], [41, 2355679], [42, 3677899], [43, 3704449], [44, 3728889],[45, 12378889],[46, 133378889]]

# take=[]
# for o in range(len(sequenceOfnumberAndg)):
#     sequenceOfnumberAndg[o][1]=addDigits(sequenceOfnumberAndg[o][1])
#     take.append(sequenceOfnumberAndg[o])
# print(take)

print("loop",sf(133378889))














