def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))

count = 0
number = 1
prime_numbers = []

while number < 2000000:
    number += 1
    if is_prime(number):
        count += 1
        prime_numbers.append(number)

print(sum(prime_numbers))