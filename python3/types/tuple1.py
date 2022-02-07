def nullTupleFunc1():
	t=()
	print(type(t))

def singleTupleFunc1():
	t=(10,)
	print(type(t))

def bytesFunc1():
	r=range(0,256)
	b=bytes(r)
	print(b[0])
	print(b[-1])

def NoneFunc1():
	a=None
	print(id(a))
	print(type(a))

if __name__ == '__main__' :
    NoneFunc1() 
    bytesFunc1()
    singleTupleFunc1()
    nullTupleFunc1()
    