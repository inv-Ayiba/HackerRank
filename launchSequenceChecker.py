def incre(statues):
    length=len(statues)
    # this Forloop goes through all pairs to check if increasing
    for i in range(length-1):
        difff=statues[i+1]-statues[i]
        if difff<=0:
            return False
    return True
def discov(systn,stepn):
    obj={}
    for i in range(len(systn)):
        try:
            obj[systn[i]].append(stepn[i])
        except(KeyError):
            obj.update({systn[i]:[stepn[i]]})
    # print( obj)
    return obj
def solution(systemNames, stepNumbers):
    setlist=list(set(systemNames))
    thing = discov(systemNames,stepNumbers)
    for i in setlist:
        if not incre(thing[i]):
            return False
    return(True)

