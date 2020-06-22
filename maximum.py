  
def max(a, b, c): 
  
    if (a >= b) and (a >= c): 
        largest = a 
  
    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
          
    return largest 
  
  
a=float(input('enter a:'))
b=float(input('enter b:'))
c=float(input('enter c:'))
print(max(a, b, c)) 
