#coding: utf-8
import hashlib
import time
from itertools import product
import time

def main():
	timebegin = time.time()
	worddic = open('wordlista','r')
	dicionario = worddic.read()
	dicmaker = open('caracteres','r')
	caracteres = dicmaker.read()
	caracteres = caracteres.strip('\n')
	hashoriginal = input("Digite um Hash MD5 de uma palavra: ")
	#pesquisadic(hashoriginal,dicionario)
	allpass(hashoriginal,6,caracteres)
	timeend = time.time()
	print (timeend - timebegin)

def pesquisadic(hashoriginal,dicionario):
	inicial = time.time()
	for palavra in dicionario.split('\n'):
		hashpalavra = hashlib.md5(palavra.encode('utf-8')).hexdigest()
		if(hashoriginal == hashpalavra):
			print ("Palavra:",palavra,"\n- - - Hash:", hashpalavra,
					"\n- - - HashOriginal:",hashoriginal)
	final = time.time()
	print ("Tempo de busca:",final-inicial,"segundos") 
			
def allpass(hashoriginal,numcar,caracteres):
	genComb = product(caracteres, repeat=numcar)
	for subset in genComb:
		senha=''
		i=0
		while i < numcar:
			senha+= (subset[i])
			i=i+1
		print (senha,"\n")
		hashsenha = hashlib.md5(senha.encode('utf8')).hexdigest()
		if hashsenha == hashoriginal:
			print ('IGUAL!!!!!\nHash original =',hashoriginal,'\nHash senha = ',hashsenha)
			break
			
if __name__ == '__main__':
	main()
