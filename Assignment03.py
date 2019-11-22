
#Program 01

print("-----------------------------Calculator-----------------------------")
print("\n\n")
val1 = int(input("Enter First number \n"))
val2 = int(input("Enter Second number or power\n"))

operator = input("Enter Operator \n")


if operator == "+":
    result = val1 + val2
    print("The answer is: " +str(result))
elif operator == "**":
    result = val1 ** val2
    print("The answer is: " +str(result))
elif operator == "-":
    result = val1 - val2
    print("The answer is: " +str(result))
elif operator == "*":
    result = val1 * val2
    print("The answer is: " +str(result))
elif operator == "/":
    result = val1 / val2
    print("The answer is: " +str(result))
else:
    print("Check your inputs")

print("--------------------------------End---------------------------------")
print("\n\n")


#Program 02

print("---------------------Q#02 Numeric Val in a list---------------------")

z = [5, 's', 2, 'u', 0, 'p', 1]
print("List defined below","\n",z)

for it in z:
    if type(it) == int:
        print(it, 'is an integer')

print("--------------------------------End---------------------------------")
print("\n\n")


#Program 03
print("----------------Q#03 Add key/value in a dictionary -----------------")
print("\n\n")
entry = {
        "name":"Bruce Wayne",
        "city":"Gotham",
        "net_worth": "9.2 Million"
    }
print("The dictionary has the following items:")
for each_key, each_value in entry.items():
    print(each_key,":",each_value)
    
b = input("\nEnter the key you wanna add in the dictionary above \n")
c = input("Enter the value for the key \n")
entry[b] = c

print("Now the dictionry has the following keys: ")
for each_key in entry.keys():
    print(each_key)
print("--------------------------------End---------------------------------")
print("\n\n")

#Program 04
print("--------Q#04 Sum of all the numeric values in a dictionary ---------")
print("\n\n")
numbers = {
        "num1": 10,
        "num2": 20,
        "num3": 30
    }
print("The dictionary has: ", numbers)
addition = 0

for i in numbers.values():
    addition = addition + i

print("The sum of the values is: ", addition)
print("--------------------------------End---------------------------------")
print("\n\n")


#Program 05
print("------------Q#05 Finding the duplicate values in a list-------------")
print("\n\n")
the_list = [1,2,3,4,5,6,7,8,9,10,2,4,6,8]
 
the_list.sort()
print(the_list)
 
new_list = sorted(set(the_list))
dup_list =[]
 
 
for i in range(len(new_list)):
        if (the_list.count(new_list[i]) > 1 ):
            dup_list.append(new_list[i])
        
print(dup_list)

print("--------------------------------End---------------------------------")
print("\n\n")

#Program 06
print("-------Q#06 Checking if a key already exists in a dictionary--------")
super_heroes = {
        "Superman" :"Super Strength",
        "Batman" : "Awesome",
        "Spiderman": "Friendly",
        "Ironman" : 3000,
    }
print("The dictionary is defined below", "\n")
for p,q in super_heroes.items():
    print(p,q)
k = input("Enter a key\n")
k = k.title()
for j in super_heroes.keys():
    if j == k:
        print("The key already exists")
   
print("--------------------------------End---------------------------------")
print("\n\n")
print("--------------------------------End---------------------------------")
print("\n\n")

