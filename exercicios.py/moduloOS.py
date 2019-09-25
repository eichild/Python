import os
#CRIANDO FILE

os.path.join('C','tmp')
files=['teste1.txt','teste2.txt']

for file in files:
	print os.path.join('C:','tmp',file)

#DIRETÓRIO ATUAL 
os.getcwd() #QUANDO QUERO SABER QUE DIRETÓRIO ESTOU

os.chdir(os.path.join('/','Users','desumilde','Documentos'))#change directory, alterna diretório
os.getcwd()

#CRIANDO PASTA DENTRO DESSE DIRETÓRIO
os.makedirs(os.path.join('/','Users','desumilde','Documentos','teste'))

#RETORNA PATH ABSOLUTO OU SEJA MOSTRA O CAMINHO COMPLETO
os.path.abspath('teste)

#CHEGA SE É O PATH ABSOLUTO
os.path.isabs(os.path.abspath('teste'))

#


