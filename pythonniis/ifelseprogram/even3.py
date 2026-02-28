#write a program take a persion age from keybord chack eligible for voting or not
print("enter a age")
age=int(input())
msg="eligible" if age>=18 else "not eligible"
print(msg)