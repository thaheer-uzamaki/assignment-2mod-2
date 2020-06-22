try:
    num=int(input("Enter a number: - "))
    if not type(num) is int:
        raise TypeError("Only int is allowed")
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")

except:

    print("An exception occurred!!! Your input isn't proper")
    
else:
    print("Nothing went wrong")
    
finally:
    print("You have executed this program")
    
