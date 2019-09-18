#!/usr/bin/python3.6
bi=input("Enter binary bit data that has to be transmitted:")
lis=list(bi)
one=lis.count("1")
if one%2==0:
	print("Parity bit data:"+bi+"1")

new=bi.replace("010","0101")
data=(new+"0101")
print("Transmitting data:"+data)










