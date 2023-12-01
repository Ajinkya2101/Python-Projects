def solution(number):
    if number==0 or number==1:
        return 1
    else:
        factorial = solution(number - 1) * number
        return factorial
number= int(input("Enter a number: "))
print(f"Factorial of {number} = ", solution(number))