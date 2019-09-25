lista = [1,2,3,4,5,6,7,8,9,10]
while True:
	num=int(raw_input('Digite o numero que deseja procurar na lista: '))
	if num in lista:
		print 'O numero digitado existe na lista'
		print '<----------------------------------->'
		print ''
	else:
		print 'O numero digitado nao existe na lista papai'	
		print '<----------------------------------->'
		print ''
