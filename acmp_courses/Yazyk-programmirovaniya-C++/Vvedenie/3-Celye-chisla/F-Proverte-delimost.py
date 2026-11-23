first_number, second_number = map(int, input().split())
if second_number > first_number:
    if second_number % first_number == 0:
        print(1)
    else:
        print(666)
else:
    if first_number % second_number == 0:
        print(1)
    else:
        print(666)
