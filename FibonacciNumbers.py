def fibonacci(n):
    assert n>=0 and int(n)==n, 'Please enter positive integer value!'
    if n in [0,1]:
        return n
    else:       
        return fibonacci(n-1) + fibonacci(n-2)

value = int(input("Enter a number: "))
print(fibonacci(value))