import sys
num_int = int(sys.stdin.readline())
check_num = num_int
counter = 0

while True:
    a = num_int%10 
    b = num_int//10
    c = num_int*10
    
    if num_int < 10:
        if (counter > 0) and (num_int == check_num):
            print(counter)
            break
        num_int = c + num_int
        counter += 1
        
    elif (num_int >= 10) and (check_num != num_int):
        num_int = (a*10) + ((a+b)%10)
        counter += 1
        continue
        
    elif (check_num == num_int) and (counter == 0) and (num_int >= 10):
        num_int = (a*10) + ((a+b)%10)
        counter += 1
        continue
        
    elif check_num == num_int:
        print(counter)
        break
    
    else:
        print(counter)
        break
