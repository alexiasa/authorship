user = int(input('Enter a number between one and ten:'))
    if user > 10:
        print('This number is too large!')
    elif user < 1:
        print('This number is too small!')
    else:
        print(user*10)