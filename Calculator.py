a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
Result=(input("Enter operator:"))
if Result==('+'): 
    print("Addition:", a+b)
if Result==('-'):
     print("Subtraction:", a-b)
     if Result==(""): 
         print("Multiplication:", a*b)
         if Result==("/"): 
             print("Division:", a/b)
             if Result==("//"):
                 print("Floor Division:", a//b)
                 if Result==("%"):
                     print("Modulus:", a%b)
                     if Result==(""): 
                         print("Exponential:", a*b)