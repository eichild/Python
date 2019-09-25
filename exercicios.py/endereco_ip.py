'''ip = raw_input('Digite o numero ip: ')
#print 'O endereco ip e: '+ip+ 'Endereco valido'
print 'O endereco ip %s e um endereco valido' %ip
print 'O endereco %s tem o tamanho de %s caracteres: ' %(ip,str(len(ip))
'''	

#FOR PARA ENDERECO IP

for x in xrange(0,255):
	ip= '192.168.0.'+str(x)
	print '192.168.0.'+str(x)
	if ip=='192.168.0.233':
		print '---ENDERECO ENCONTRADO---> '+str(ip)
		break


		


	