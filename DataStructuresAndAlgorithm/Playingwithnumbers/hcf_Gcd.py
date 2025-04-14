num1 = int(input("Enter a num: "))
num2 = int(input("Enter a num: "))
i = 2
hcf = 1
while i <= num1:
    if num1%i == 0 and num2%i == 0:
        hcf = i
    i +=1

print(f"hcf: {hcf}")
