temp = float(input("Enter the temperature: "))
inputunit = input("Enter the input unit (C, F, K): ")
outputunit= input("Enter the output unit (C, F, K): ")
CtoF=(temp*9/5)+32
CtoK=temp+273.15
FtoC=(temp-32)*5/9
FtoK=((temp-32)*5/9)+273.15
KtoC=temp-273.15
KtoF=((temp-273.15)*9/5)+32
if inputunit=='C':
    if outputunit=='F':
        print(f"the converted temparature is :{CtoF}F")
    else:
        print(f"the converted temparature is :{CtoK}K")
elif inputunit=='F':
    if outputunit=='C':
        print(f"the converted temparature is :{FtoC}C")
    else:
        print(f"the converted temparature is :{FtoK}K")
elif inputunit=='K':
    if outputunit=='C':
        print(f"the converted temparature is :{KtoC}C")
    else:
        print(f"the converted temparature is :{KtoF}F")

else:
    print("invalid input/output\nplease provide valid input/output")