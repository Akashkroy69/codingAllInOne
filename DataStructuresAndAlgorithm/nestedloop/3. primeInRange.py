
lower = int(input("Enter a number : "))
upper = int(input("Enter a number: "))
allPrimes = []
for j in range(lower,upper):
   num = j
   count = 0
   for i in range(2,num):
       if num % i == 0:
           count += 1
           print(f"{num} is not a prime number")
           break
   if count == 0:
        allPrimes.append(num)
print(f"all primes between {lower} and {upper} are: {allPrimes}")