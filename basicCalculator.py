a=float(input("enter any value for a :"))
b=float(input("enter any value for b :"))
inputt=input("enter + to perform addition \n"
             " enter - to perform substraction \n "
             "enter * to perform multiplication \n "
             "enter / to perform division \n "
             "enter % to perform modulo division")

if inputt=='+':
    print(a+b)
elif inputt=='-':
    print(a-b)
elif inputt== '*':
    print(a*b)

elif inputt== '%':
    try:
        print(a%b)
    except Exception as e:
         print("you can't perform division by 0")
elif inputt== '/' :
    try:
            print(a/b)
    except Exception as e:
        print("you can't perform division by 0")
else:
    print("please choose correct option")    
