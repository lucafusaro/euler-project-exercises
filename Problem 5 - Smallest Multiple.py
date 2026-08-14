number = 20
while True:
    is_divisible = True
    
    for i in range(1, 21):
        if number % i != 0:
            is_divisible = False
            break
        
    if is_divisible:
        break
        
    number += 20
            
print(number)