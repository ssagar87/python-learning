#task 1
val = int(input("Enter a number: "))

if val % 2 == 0:
  print(val,"is an even value")
else:
    print(val,"is an odd value")

#task 2
totalSum = 0

for i in range(1, 51):
    totalSum += i   
    
print("Total sum of numbers from 1 to 50 is: ",totalSum)
