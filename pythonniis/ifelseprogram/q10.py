"""write a program take emp salary from keybord if sal>=5000 da=30% hra=20%
then display basic salary do hra and total salary"""

print("enter baasic salary")
sal=float(input())
da=sal*0.3 if sal>=5000 else sal*0.2
hra=sal*0.2 if sal>=5000 else sal*0.2
else:
  da=sal*0.2
  hra=sal*0.1	
totasal=sal+da+hra
print("enter baasic salary",sal)
print("da",da)
print("hra",hra)
print("totalsalary",totasal)