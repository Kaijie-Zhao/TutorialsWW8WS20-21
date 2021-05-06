# -*- coding: utf-8 -*-

# Funktionsdefinition: Syntax
#  def FuncName(Parameterliste):
#      # Anweisungen
#      return Wert1, Wert2, ...


def convertF(TC):
	"""
	A function definition: Converts from Centigrade to Fahrenheit
	TC: temperature in Centrigrade
	TF: temperature in Fahrenheit
	"""
	TF = 9.0/5.0*TC + 32.0
	return TF
	
def convertC(TF):
	
	TC = (TF - 32.0) * 5.0/9.0
	return TC

