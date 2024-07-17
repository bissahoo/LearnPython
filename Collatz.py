
def collatz(number):
    if number%2==0:
        number = number//2        
    else:
        number = 3*number+1
    
    print("Number ",number)
    return number

start = int(input())
while start!=1:
    start=collatz(start)

