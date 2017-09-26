Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def caculateArea(length,breath):
	if str.isdigit(length) and str.isdigit(breath):
		return length * breath
	else:
		print("please enter a value")
		return False
	
