lis=[]
print("enter your score in Telugu, Hindi, English, Maths, Science, Social respectively")
for i in range(6):
    inputt=float(input())
    res=lis.append(inputt)
print(lis)
avg=(sum(lis))/len(lis)
print(f"your average Score : {avg} ")

if  avg>=85 and avg<=100:
    print("Grade : A")
    print("feedback : outstanding performance")
elif avg>=70 and avg<=84:
    print("Grade : B")
    print("Feedback : Very Good")
elif   avg>=55 and avg<=69:
    print("Grade : C")
    print("Feedback : work hard to achieve B grade")
elif   avg>=35 and avg<=54:
    print("Grade : D")
    print("Feedback : need to improve alot")
else:    
    print("Grade : F Fail")
    print("Feedback : Try atleast for pass")    



