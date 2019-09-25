while True:

	nome = raw_input('Digite login: ')
	#if nome=='root' or nome=='admin' or nome=='chefe':
	if nome=='root':
		print '---BEM VINDO SENHOR %s---'%nome
		#print '---BEM VINDO SENHOR---'+nome
		break

	elif nome=='admin':
		print 'ELIF RUNFANDO PAI'
		break	
	else:
		print '---USUARIO INCORRETO---'			
		