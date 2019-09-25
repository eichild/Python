var=list()
while True:
	msg=raw_input('Digite alguma coisa ai, ou nada para vazar: ')
	if msg:
		var.append(msg) 
	else:
		print '---BYE---'
		break
for valor in var:
	if valor=='lilraffa':
		print valor
		print '------SEU NARIZ TA ESCORRENDO BRO------'

	
