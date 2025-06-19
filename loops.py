#while loop

#incrementing
number= 20
while number<=25:
    print(number)
    number+=1
print()

#decrementing
count=105
while count>=100:
    print(count)
    count-=1
print()



#break and continue
a = 20
while a<=25:
    print(a)
    if a== 23:
        break
    a +=1
print()

counter=35
while counter<=40:
    if counter==37:
        counter+=1
        continue
    print(counter)
    counter+=1
print()

#for loop
languages= ["Python", "C++", "Java", "PHP"]
for lang in languages:
    print(lang)

print()

for num in range(5):
    print(num)

print()

for x in range(10, 15):
    print(x)

print()


for z in range(10, 20, 3):
    print(z)
