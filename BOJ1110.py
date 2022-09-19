num_int = int(input())
check_num = num_int
counter = 0
while True:
    if num_int < 10:
        num_int = (num_int*10) + num_int
        counter += 1
    elif (counter == 0) and (check_num == num_int) and (num_int > 10):
        num_int = ((num_int%10)*10) + (((num_int//10) + (num_int%10))%10)
        counter += 1
    elif (counter != 0) and (check_num == num_int):
        print(counter)
        break
