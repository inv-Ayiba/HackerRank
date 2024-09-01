def solution(inputArray):
    lengths=[]
    for i in inputArray:
        lengths.append(len(i))
    maxlenght=max(lengths)
    result=[]
    for i in range(len(inputArray)):
        if lengths[i]==maxlenght:
            result.append(inputArray[i])
    return result
