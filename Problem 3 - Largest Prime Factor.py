import math

def largest_prime_factor(n):
    max_prime = -1
    
    while n % 2 == 0:
        max_prime = 2
        
    # Check for odd factors starting from 3 up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i
            
    # 3. If n is still greater than 2, then n itself must be prime
    if n > 2:
        max_prime = n
        
    return max_prime

number = 600851475143
print(f"The largest prime factor of {number} is {largest_prime_factor(number)}")
