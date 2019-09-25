print 'PORTSCAN'
for y in xrange(1,5):
	for x in xrange(20,24):
		print 'Scan sendo realizado no IP ---192.168.0'+str(y)+'--- na porta => '+str(x)
	print '---------------------------------------------------------------------------'

	'''
import socket,sys
	for portas in xrange(1,65535):
		s = socket.socket(socket.AFF_INET, socket.SOCK_STREAM)

		if s.connect_ex((sys.argv[1], portas)) == 0:
			print ' PORTA=>', portas, 'ABERTA'

			s.close()	