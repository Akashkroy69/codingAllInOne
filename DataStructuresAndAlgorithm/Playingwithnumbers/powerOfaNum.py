# 2^3


def powOfANum(base,power):
    if power == 1: return base

    return base * powOfANum(base,power-1)

print(powOfANum(2,5))