#Problem 1

def split_digits_list(number_to_split):
    number_word = str(number_to_split)
    
    digit_list = []
    element = 0
    
    for char in number_word:
        digit_list.append(int(number_word[element]))
        element += 1

    return digit_list

def is_happy_number():
   
    number = int(input('Enter a number > 0 to see if it is a happy number: '))
    split_number = split_digits_list(number)
    
    element = 0
    sum_of_squares = 0
    squares_checked = []

    while number >= 0:

        for number in split_number:
            sum_of_squares += pow((split_number[element]),2)
            element += 1

        if sum_of_squares == 1:
            print('This is a happy number!')
            break

        elif sum_of_squares not in squares_checked:
            squares_checked.append(sum_of_squares)

        elif sum_of_squares in squares_checked:
            print('This number is sad')
            break

        split_number = split_digits_list(sum_of_squares)
        element = 0
        sum_of_squares = 0

is_happy_number()

#Problem 2 Only Prime Numbers

def prime_1_to_100():
    for count in range(100):

        if count == 2 or count == 3 or count == 5 or count == 7:
            print(count, end = ' ')
        elif count % 2 == 0 or count % 3 == 0 or count % 5 == 0 or count % 7 == 0 or count == 1:
            continue
        else:
            print(count, end =' ')

prime_1_to_100()

#Problem 3 Fibonacci

def fib_seq_from_1():
    fib_list = [1,1]

    element = 0

    for count in range(10):
        fib_list.append(fib_list[element]+fib_list[element + 1])
        element += 1

    print(*fib_list)

fib_seq_from_1()

def fib_seq_from_user():
    user_number = int(input('Enter where you would like to begin the sequence: '))

    fib_list = [1,1]

    fib_list[0] = user_number
    fib_list[1] = user_number

    element = 0

    for count in range(10):
        fib_list.append(fib_list[element]+fib_list[element + 1])
        element += 1

    print(*fib_list)

fib_seq_from_user()