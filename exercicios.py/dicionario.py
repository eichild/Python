'''var.keys() #Printa os indices do dicionario
var.values() #Printa os valores
var.items() #Printa tudo separando por indices, ex: var.items()[1]
'''

var = {'ip':'192.168.15.1','porta':'80'}
var['service'] = 'http'

for key,value in var.items():
	print key,value
