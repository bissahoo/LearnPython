# while True:
#     for i in range(5,0,-1):
#         print(" "*i,"*"*8)
#     for i in range(5):
#         print(" "*i,"*"*8)        
    


for i in range(1,3):
    for j in range(5):
        if 2%i == 1:
            print(" "*(5-j),"*"*8)
        else:
            print(" "*j,"*"*8)
