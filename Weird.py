def weird(n):
    if (n%2!=0):
        return "Weird"
    elif (n%2==0 and n>=2 and n<=5):
        return "Not Weird"
    elif (n%2==0 and n>=6 and n<=20):
        return "Weird"
    elif (n%2==0 and n>20):
        return "Not Weird"

for I in range(40):
    print(I,":",weird(I))

