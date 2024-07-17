def divide(a):
    try:
        return 42/a
    except ZeroDivisionError:
        print("Cant divide by zero")

print(divide(42))        
print(divide(0))
print(divide(21))