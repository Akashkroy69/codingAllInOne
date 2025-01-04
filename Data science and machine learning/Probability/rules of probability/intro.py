# setA = {1,2,3,4,5}
# setB = {4,5,6,7,8}

# print(setA)
# print(setB)

# print(setA | setB)
# print(setA.union(setB))

# print(setA & setB)
# print(setA.intersection(setB))

# print(setA-setB)
# print(setB-setA)
# print(setA.difference(setB))

# print(setA.symmetric_difference(setB))
# print(setA ^ setB)

evens = {2,4,6}
greaterThan2 = {3,4,5,6}

allPossible = {1,2,3,4,5,6}

# probability of even or greaterthan2
pE1 = len(evens)/len(allPossible)
pE2 = len(greaterThan2)/len(allPossible)

probOfIntersection = len(evens & greaterThan2)/len(allPossible)

pE1_or_pE2 = pE1 + pE2 - probOfIntersection

print(pE1_or_pE2)





