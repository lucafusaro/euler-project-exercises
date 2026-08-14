largest_palindrome = -1
for i in range(999, 99, -1):
    if i * 999 <= largest_palindrome:
        break
    
    for j in range(999, i-1, -1):
        res = i * j
        if res <= largest_palindrome:
            break
        
        res = str(res)
        if res == res[::-1]:
            largest_palindrome = int(res)
        

print(largest_palindrome)