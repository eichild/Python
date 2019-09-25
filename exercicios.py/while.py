'''
contador=0
while contador<=255:
	print '192.168.0.'+str(contador)
	#print 'fishballcat'
	contador=contador+1
	if contador==233:
		print 'IP IDENTIFICADO 192.168.0.'+str(contador)	
		'''

while True:
	user = raw_input('Digite o login: ')
	if user=='root':
		print '---Usuario logado---'
		break
	else:
		print 'Usuario incorreto!!!'
		