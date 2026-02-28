x=10
def show():
	global x
	x=30
	print(x)#30
	return
show()
print(x)#10
