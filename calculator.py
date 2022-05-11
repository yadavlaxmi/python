def add (a,b):
    c=a+b
    return c
def sub(x,y):
	z=x-y
	return z
def multi(k,f):
	g=k*f
	return g
def div(m,n):
	o=m/n
	return o
def main( ):
	if optn=='+':
		print(add(num1,num2))
	elif optn=='-':
		print(sub(num1,num2))
	elif optn=='*':
		print(multi(num1,num2))
	elif optn=='/':
		print(div(num1,num2))
	else:
		print('nothing')
num1=int(input('enter the num1'))
num2=int(input('enter the num2'))
optn=input('enter the operator')
main()