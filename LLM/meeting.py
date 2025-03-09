def is_prime(k): 
    count = 0
    for i in range(1, int(k**0.5)+1):
        if k % i == 0:
            count += 1
    return count == 1

    
def is_pow(k): 
    while k > 1:
        if k % 2 == 1:
            return False 
        k //= 2
    return True

  
def func(n):
    sol = [[],[]] 
    for num in range(1, n+1):
        if num > 1 and is_prime(num):
            sol[0].append(num)
        if is_pow(num):
            sol[1].append(num)
    return sol


sol = func(100)
print("prime = ", sol[0])
print("pos = ", sol[1])