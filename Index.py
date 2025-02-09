
Place = 'Paris'

print(dir(Place))

print(Place.find('i'))

Task = "You have to this work in 3 days"

print(Task.startswith('You'))

print(Task.endswith('days'))

Message = "I will be on time"
print(Message.replace('I','You'))

Line= "Sun rises in the East"
print(Line.split())

# SWAPPING PROGRAM

a = input("enter value of (a): ")
b = input("enter value of (b): ")
c = input("enter value of (c): ")
d = input("enter value of (d): ")

print("Before Swpping: ",a,b,c,d)

a,b,c,d = d,c,a,b

print("After Swpping: ",a,b,c,d)


# CONVERSION OF TEMPERATURES

C =float(input("Enter Temp in C: "))
F = (C * (9/5)) + 32
print(f"Tempeature in Fahrenheit is: ",F)

F =float(input("Enter Temp in F: "))
C = (F - 32) *(5/9)
print(f"Temperture in Celcius is:  ",C)
