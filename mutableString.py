#!/usr/bin/python3.10
# use for python3.10
# 适用于Python3.10
class String():
	def __init__(self, object: str=''):
		self.__listofthestring = list(object)
	def __getitem__(self,index):
		return self.__listofthestring[index]
	def __setitem__(self,index,value):
		self.__listofthestring[index] = value
	def __str__(self) -> str:
		return ''.join(self.__listofthestring)
	def __repr__(self) -> str:
		return "'" + ''.join(self.__listofthestring) + "'"
	def __eq__(self, o: object) -> bool:
		return ''.join(self.__listofthestring) == o
	def __ne__(self, o: object) -> bool:
		return not self == o
	def __add__(self,o):
		return self.__class__(''.join(self.__listofthestring) + str(o))
	def __radd__(self,o):
		return self.__class__(''.join(self.__listofthestring) + str(o))




