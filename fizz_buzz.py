fizz= 'Fizz'
buzz= 'Buzz'
fizzbuzz= 'FizzBuzz'
for numbers in range(1, 101) :
    if (numbers % 3 == 0) and (numbers % 5 == 0):
        numbers = fizzbuzz
    elif (numbers % 3 == 0) :
        numbers = fizz
    elif (numbers % 5 == 0) :
        numbers = buzz
    print(numbers)
