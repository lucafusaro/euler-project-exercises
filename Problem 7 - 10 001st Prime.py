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

while count < 10001:
    number += 1
    if is_prime(number):
        count += 1

print(number)  # 104743
        