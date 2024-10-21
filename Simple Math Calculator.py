import random
while True:
    x = random.randint(1, 1000)
    y = random.randint(1, 1000)
    print(x, '+', y, '=', end = ' ')
    answer_add = int(input())
    if answer_add == x + y:
        print("You are correct")
    else:
        print("Incorrect, Correct answer is =", x+y)
        
    x = random.randint(1, 1000)
    y = random.randint(1, 1000)    
    print(x, '-', y, '=', end = ' ')
    answer_sub = int(input())
    if answer_sub == x - y:
        print("You are correct")
    else:
        print("Incorrect, Correct answer is =", x-y)
        
    x = random.randrange(1,1001,10)
    y = random.randint(1,10)    
    print(x, '/', y, '=', end = ' ')
    answer_div = float(input())
    corr_ans = x / y
    if abs(answer_div - corr_ans)<0.001:
        print("You are correct")  
    else:
        print("Incorrect, Correct answer is =", x/y)
        
    x = random.randrange(1,1001,10)
    y = random.randint(1,10)
    print(x, '*', y, '=', end = ' ')
    answer_mul = float(input())
    correct_ans = x * y
    if abs(answer_mul-correct_ans)<0.001:
        print("You are correct")
    else:
        print("Incorrect, Correct answer is =", x*y)
    
    
    
