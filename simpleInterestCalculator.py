Principal=int(input("enter pricipal_amount : "))
rate=int(input("enter rate of interest : "))
time=int(input("enter time period : "))

SI=(Principal*time*rate)/100
total_amount=Principal+SI
print(SI)
print(total_amount)

