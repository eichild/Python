'''def hello():
	try:
		var='hello mundo'
		print var
	except:
		print 'Error'

hello()
'''
#TRY AND EXCEPT E EQUIVALENTE AO TRY CATCH
def conta(x):
	try:
		print 10/x
	except Exception as e:
		print str(e)
conta(0)
#conta(1)