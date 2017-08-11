#Algoritmo S-DES de cifragem
#Feito para a disciplina de Seguranca de Redes
#Autor: Gisleude Linhares

#Abrindo arquivo
arq_text = open("text-to-encrypt.txt")
text = arq_text.read()

#Transformando o texto em lista de caracteres
list_text = list(text)


print(list_text)

############################# PRIMEIRO PASSO #############################
###################### PERMUTACAO COM 10 TERMOS ##########################

p10 = [3,5,2,7,4,10,1,9,8,6]
i = 0 #Contador
lista_aux = [] # lista auxiliar vazia
while(i < len(p10)):
	lista_aux[i:i] = list_text[p10[i]-1]
	i = i + 1

#Preenchendo a lista com a lista auxiliar
list_text = lista_aux

########################### FIM PRIMEIRO PASSO ###########################

############################# SEGUNDO PASSO ##############################
########################## GERACAO DE CHAVES #############################

####### SUB PASSO 1 #######
######## SEPARACAO ########
list_text_lft = []
i = 0
while(i < len(list_text)/2):
	list_text_lft[i:i] = list_text[i]
	i = i + 1

list_text_rght = []
i = len(list_text)/2
while(i < len(list_text)):
	list_text_rght[i:i] = list_text[i]
	i = i + 1

##### FIM SUB PASSO 1 #####

####### SUB PASSO 2 #######
#### ROTACAO ESQUERDA 1 ###
def rotacionar(lista,vezes):
	cont = 0
	while(cont < vezes):
		n = len(lista)
		aux = lista[0]
		i = 0
		while(i < n-1):
			lista[i] = lista[i+1]
			i = i + 1

		lista[n-1] = aux
		cont = cont + 1

	return lista

list_text_lft = rotacionar(list_text_lft,1)
list_text_rght = rotacionar(list_text_rght,1)

##### FIM SUB PASSO 2 #####

####### SUB PASSO 3 #######
# PERMUTACAO COM 8 TERMOS #
list_text = list_text_lft + list_text_rght
p8 = [6,3,7,4,8,5,10,9]
i = 0 #Contador
k1 = [] # chave 1
while(i < len(p8)):
	k1[i:i] = list_text[p8[i]-1]
	i = i + 1

##### FIM SUB PASSO 3 #####

####### SUB PASSO 4 #######
#### ROTACAO ESQUERDA 2 ###
list_text_lft = rotacionar(list_text_lft,2)
list_text_rght = rotacionar(list_text_rght,2)

##### FIM SUB PASSO 4 #####

####### SUB PASSO 5 #######
# PERMUTACAO COM 8 TERMOS #
list_text = list_text_lft + list_text_rght
p8 = [6,3,7,4,8,5,10,9]
i = 0 #Contador
k2 = [] # chave 1
while(i < len(p8)):
	k2[i:i] = list_text[p8[i]-1]
	i = i + 1

##### FIM SUB PASSO 5 #####

print(list_text_lft)
print(list_text_rght)
print("Chave k1="+str(k1))
print("Chave k2="+str(k2))
#Fechando arquivo
arq_text.close