import re
n= input("enter")
i = True
while i:
    if (len(n)<6 or len(n)>16):
        break
    
    elif not re.search("[$#@]",n):
        break
    
    elif not re.search("[0-9]",n):
        break
    
    elif not re.search("[A-Z]",n):
        break
    
    elif not re.search("[a-z]",n):
        break
    
    elif re.search("\s",n):
        break
    
    else:
        
        print("Valid Password")
        
        i=False
        break
if i:
    print("Not a Valid Password")
