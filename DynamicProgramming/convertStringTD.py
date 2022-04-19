
def findMinOperationTD(s1, s2, index1, index2, tempDict):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return findMinOperationTD(s1, s2, index1+1, index2+1, tempDict)
    else:
        dictKey = str(index1)+str(index2)
        if dictKey not in tempDict:
            deleteOp = 1 + findMinOperationTD(s1, s2, index1, index2+1, tempDict)
            insertOp = 1 + findMinOperationTD(s1, s2, index1+1, index2, tempDict)
            replaceOp = 1 + findMinOperationTD(s1, s2, index1+1, index2+1, tempDict)
            tempDict[dictKey] = min(deleteOp, insertOp, replaceOp)
        return tempDict[dictKey]

print(findMinOperationTD("table", "tbrltt", 0, 0, {}))

