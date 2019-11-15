
'''Assignmet #02'''

#Question 1
print("------------------------- Q#01 MarkSheet ------------------------- \n\n")

eng = int(input("Enter marks obtained in English \n"))
prog = int(input("Enter marks obtained in Programming \n"))
hist = int(input("Enter marks obtained in History \n"))
mth = int(input("Enter marks obtained in Maths \n"))
chem = int(input("Enter marks obtained in Chemistry \n"))


per = ((eng+prog+hist+mth+chem)*100) / 500

print("Your percentage is " +str(per))
if per >=80 and per <=100:
    print("Your grade is A+")
elif per >= 70 and per <80:
    print("Your grade is A")
elif per >=60 and per < 70:
    print("Your grade is B")
elif per >= 0 and per <60:
    print("Sorry, your grade is an F")
else:
    print("Enter a valid value")

print("\n\n")

#Question 2

print("------------------------- Q#02 Even/Odd ------------------------- \n\n")

num = int(input("Enter a number \n"))
if num % 2 == 0:
    print("The number is Even")
elif num < 0:
    print("The number is Odd")
print("\n\n")


#Question 3

print("------------------------- Q#03 Length of a list -------------------------\n")
cars = ["corvetteZ06", "lamborghiniMarcialago", "FerrariF50", "MclarenF1"]
print("The list: "+str(cars))
no = len(cars)
print("The length of the list above is: " +str(no))
print("\n\n")

#Question 4
print("------------------------- Q#04 Largest number in the list -------------------------\n\n")

b = [1,1,2,3,5,8,13,21,34,55,89]
largestNo = max(b)
print("The largest no in the list: " +str(b) +" is")
print(largestNo)
print("\n\n")


#Question 5
print("------------------------- Q#05 Numbers greater than 5 in the list----------------------\n")

t = 5
print("The List: " +str(b))

for nos in b:
    if nos > 5:
        print(nos)
print("\n\n")
