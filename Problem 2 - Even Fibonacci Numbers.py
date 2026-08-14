fibonacci_list = [1, 2]
while True:
    next_fib = fibonacci_list[-1] + fibonacci_list[-2]
    if next_fib > 4000000:
        break
    fibonacci_list.append(next_fib)

sum_fibo = sum(x for x in fibonacci_list if x % 2 == 0)
print(sum_fibo)