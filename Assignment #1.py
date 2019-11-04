import sys

#   Different Question
print("-------------- #1 --------------")
print("\n")
a = """ Twinkle, twinkle, little star
              How I Wonder what you are!
                Up above the world so high,
                Like a diamond in the sky
        Twinkle, twinkle, little star
              How I wonder what you are"""
print("     "+a+"     ")
print("\n\n")



#   Different Question
print("-------------- #2 --------------")
print("\n")
print("Python Version")
print(sys.version)
print("\n\n")


#   Different Question
print("-------------- #3 --------------")
print("\n")
c = int(input("Enter the Circumference of the circle" +"\n"))
radius = c/(2*3.14)
print("The radius of the circle is ---> ",radius)
print("\n\n")



#   Different Question
print("-------------- #4 --------------")
print("\n")
firstName = input ("Enter first name" +"\n")
lastName = input ("Enter last name" +"\n")
o = firstName +" " +lastName
n = lastName +" " +firstName

print("\nWhat you typed ---> " +o, "<----")
print("Reverse Order ---> "+n, "<----")
