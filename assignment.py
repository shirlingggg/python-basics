#A python program that checks whether a number is even or odd

num= int(input("Enter number:"))
if num==0:
    print("The number is a neutral number.")
elif  num%2==0:
    print("The number is even.")

else:
    print("The number is odd.")
print()


#A python program that checks whether a letter is a vowel or consonant
letter=input("Enter letter:")
if letter=='a, e, i, o, u':
    print("Letter is a vowel")

else:
    print("The letter is a consonant")

print()



#A python program that returns the perimeter of a rectangle
width=float(input("Enter the width:"))
length=float(input("Enter the length:"))
perimeter= 2*(width+length)
print("The perimeter is:", perimeter)