def isPrime(i):
  prime = True
  if i < 2:
    prime = False
    return prime
  elif i == 2 or i == 3:
    return prime
  else:
    for j in range(2,int(i**0.5) + 1):
      if i % j == 0:
        prime = False
        break
        
    return prime
      
arr = list (map(int, input().split()))
for i in arr:
  if isPrime(i):
    print(1 ,end= " ")
  else:
    print(0 ,end= " ")


# we can also return true or false directly and not use prime = true,