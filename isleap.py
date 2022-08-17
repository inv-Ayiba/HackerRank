

def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year>=1900 and year<=10**5 and (year%100!=0 or (year%100==0 and year%400==0))):
        return year%4==0
    else:
        return leap
taeget =[1900,1800,2004,1600,2400]
for I in range(len(taeget)):
    print(taeget[I],":",is_leap(taeget[I]))