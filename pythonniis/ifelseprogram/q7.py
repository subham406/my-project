"""write a program take emp salary from keybord if sal>=5000 da=30% hra=20%
then display basic salary do hra and total salary"""

print("enter baasic salary")
sal=float(input())
da,hra=0,0
if sal>=5000:
	da=sal*0.3
	hra=sal*0.2
totasal=sal+da+hra
print("enter baasic salary",sal)
print("da",da)
print("hra",hra)
print("totalsalary",totasal)











"""
enter basic salary
5000
basic salary=5000
da=1500
hra=1000
total salary=9000
"""