t=int(input("Enter num: -"))
p=0
for i in range(t+1):
    o=i**2
    p=o+p
    p=0
print("Sum of the squares of numbers till {} is {}".format(t,p))
    
