# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
num1 = int(input())

def divide():
	for i in range(1, num1+1):
		if(num1 % i) == 0:
			print (i, end=' ')

divide()