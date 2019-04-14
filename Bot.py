#!/usr/bin/python3.6
import telepot #Importa a lib Telpot
import pymongo
import datetime


from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

import time # Importa Time
import urllib3 #Importa urllib3
#Essa parte é necessária para comunicar com a API do telegram na vesão gratuita no pythonanyhere
'''proxy_url = "http://proxy.server:3128" #Endereço do proxy à ser utilizado
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
#Fim do código necessário para comunicar-se com a API do telegram na versão gratuita do pythonanywhere'''
bot = telepot.Bot('713527824:AAH3YsRQjTpWeuh93O8AWv7oX2aCJ3JXn0Y')
step=0
controlador={}
relatorio={}


insumo=['Gamit','NPK','Fosfato reativo','calcário']	
def recebemsg (msg):
	global step
	global comando
	global chat
	global name
	global relatorio
	global controlador	
	global user
	global insumo
	global p
	global data
	user=msg['from']['id']
	comando=msg['text']
	chat=msg['chat']['id']
	name=msg['chat']['first_name']
	
	datatime=msg['date'] 
	p=comando
		
	data = datetime.datetime.fromtimestamp(datatime).strftime('%H:%M:%S %d-%m-%Y')
	if user in controlador :

		step=controlador[user]
		
		print(controlador)
		
	elif controlador=={} or user  not in controlador:
		step=0
		controlador[user]=step
		
		print(controlador)
		
	if user in controlador and step==19:#Esse passo não está sendo utilizado
		del controlador[user]

		
		
			
	print(step)
	print(comando)

	if comando.lower()=='olá' and step==0:		
		expediente(msg)
		step+=1
		controlador[user]=step
	elif comando.lower() in ['sim','não'] and step==1:
		expediente(msg)	
	elif step==3:
		propriedade	(msg)
	elif step==5:
		servicos(msg)
	elif step==7:
		utilizaproduto(msg)
	elif step==9:
		produto(msg)
	elif step==11:
		quantidade(msg)
	elif step==13:
		diarista(msg)
	elif step==14:
		diarista(msg)
	elif step==15:
		diarista(msg)
	elif step==17:
		terceiros(msg)
	elif step==18:
		terceiros(msg)
	elif step==19:
		voltar(msg)	
	elif step==21:
		motivo(msg)
	elif step==0 and comando.lower()=='enviar':
		enviar(msg)

	

def expediente(msg):	
	global step
	global user
	relatorio[user]=[]
	if comando.lower()=='olá' and step==0:
		bot.sendMessage(chat, 'Olá %s vamos iniciar o preenchimento do relatório. Houve expediente hoje?'%name)		
	elif comando.lower()=='sim' and step==1:
		relatorio.setdefault(user, []).append('expediente')
		relatorio.setdefault(user, []).append(comando.lower())
		
		print(relatorio[user])
		step+=1
		controlador[user]=step
		propriedade(msg)
	elif comando.lower()=='não' and step==1:
		relatorio.setdefault(user, []).append('expediente')
		relatorio.setdefault(user, []).append(comando.lower())
		print(relatorio[user])
		step=20
		controlador[user]=step
		motivo(msg)

def propriedade(msg):
	global step
	if step==2:
		bot.sendMessage(chat, 'Em qual propriedade os serviços foram realizados?')
		step+=1
		controlador[user]=step
	elif step==3:
		relatorio.setdefault(user, []).append('propriedade')
		relatorio[user].append(comando.lower())
		print(relatorio[user])
		step+=1
		controlador[user]=step
		servicos(msg)
def servicos(msg):
	global step
	if step==4:
		bot.sendMessage(chat,'Descreva quais serviços foram realizados.:')
		step+=1
		controlador[user]=step
	elif step==5:
		relatorio[user].append('serviços')
		relatorio[user].append(comando.lower())
		print(relatorio[user])
		step+=1
		controlador[user]=step
		utilizaproduto(msg)
def utilizaproduto(msg):
	global step
	if step==6:
		bot.sendMessage(chat,'Algum produto foi utilizado?')
		step+=1
		controlador[user]=step
	elif comando.lower()=='sim' and step==7:
		relatorio[user].append('utilizou produto')
		relatorio[user].append(comando.lower())
		print(relatorio[user])
		step+=1
		controlador[user]=step
		produto(msg)
	elif comando.lower()=='não' and step==7:
		relatorio[user].append('utilizou produto')
		relatorio[user].append(comando.lower())
		print(relatorio[user])
		step=12
		controlador[user]=step
		diarista(msg)

def produto(msg):
	global step
	global insumo
	global p
	if comando.lower()=='sim' and step==8:
		i=0
		while i != len(insumo):
			a='%s -'%i
			b=insumo[i]
			c=a+b
			bot.sendMessage(chat,'%s'%c)
			i =i+1
		step+=1
		controlador[user]=step
		bot.sendMessage(chat,'Selecione uma opção acima.:')
	elif step==9:			
		if p.isdigit()==False:
			bot.sendMessage(chat,'###### Por favor digite uma opção válida ######')				
		elif int(p)>=len(insumo):
			bot.sendMessage(chat,'###### Por favor digite uma opção válida ######')				
		else:
			relatorio[user].append('produto')
			relatorio[user].append(insumo[int(p)])			
			print (relatorio[user])
			print(step)
			
			step+=1
			controlador[user]=step
			quantidade(msg)
def quantidade(msg):
	global step
	if step==10:
		bot.sendMessage(chat,'Digite a quantidade do produto com a unidade de medida')
		step+=1
		controlador[user]=step
	elif step==11:
		relatorio[user].append('quantidade do produto')
		relatorio[user].append(comando.lower())
		
		print(relatorio[user])
		step+=1
		controlador[user]=step
		diarista(msg)
def diarista(msg):
	global step
	if step==12:
		bot.sendMessage(chat,'Teve a contratação de diáristas?')
		step+=1
		controlador[user]=step
	elif comando.lower()=='sim' and step==13:
		relatorio[user].append('diaristas')
		relatorio[user].append(comando.lower())
		print(relatorio[user])
		step+=1
		controlador[user]=step
		bot.sendMessage(chat,'Digite o valor da diária em R$')	
	elif comando.lower()=='não' and step==13:
		relatorio[user].append('diaristas')
		relatorio[user].append(comando.lower())
		print(relatorio[user])
		step+=3
		controlador[user]=step
		terceiros(msg)
	elif step==14:
		relatorio[user].append('valor da diária')
		relatorio[user].append(comando.lower())
		print(relatorio[user])
		step+=1
		controlador[user]=step
		bot.sendMessage(chat,'Quantas diárias foram contratadas?')
	elif step==15:
		relatorio[user].append('número de diárias')
		relatorio[user].append(comando.lower())
		print(relatorio[user])
		step+=1
		controlador[user]=step
		terceiros(msg)
def terceiros(msg):
	global step
	if step==16:
		bot.sendMessage(chat,'Houve serviços de terceiros?')
		step+=1
		controlador[user]=step
	elif comando.lower()=='sim' and step==17:
		relatorio[user].append('terceiros')
		relatorio[user].append(comando.lower())		
		print(relatorio[user])
		step+=1
		controlador[user]=step
		bot.sendMessage(chat,'Descreva o fornecedor')
	elif comando.lower()=='não' and step==17:
		relatorio[user].append('terceiros')
		relatorio[user].append(comando.lower())
		print(relatorio[user])
		step=0
		controlador[user]=step
		relatorio[user].append('data')
		relatorio[user].append(data)
		relatorio[user].append('usuário')
		relatorio[user].append(name)
		
		bot.sendMessage(chat,'Obrigado pelas informações:), aqui está seu relatório:')
		bot.sendMessage(chat,'%s'%relatorio[user])
		bot.sendMessage(chat,'Verifique seu relatório, se estiver correto digite (''Enviar'') para enviar. Se estiver errado comece novamente digitando (''olá'')')
		
	elif step ==18:
		relatorio[user].append('descrição de terceiros')
		relatorio[user].append(comando.lower())			
		print(relatorio[user])
		step=0
		controlador[user]=step
		bot.sendMessage(chat,'Obrigado pelas informações:), aqui está seu relatório:')
		relatorio[user].append('data')
		relatorio[user].append(data)
		relatorio[user].append('usuário')
		relatorio[user].append(name)	
		
		bot.sendMessage(chat,'%s'%relatorio[user])
		bot.sendMessage(chat,'Verifique seu relatório, se estiver correto digite (''Enviar'') para enviar. Se estiver errado comece novamente digitando (''olá'')')
		
		
def motivo(msg):
	global step
	if step==20:
		bot.sendMessage(chat, 'Por qual motivo não houve expediente?')
		step+=1
		controlador[user]=step
	elif step==21:
		bot.sendMessage(chat,'Obrigado pelas informações:), aqui está seu relatório:')
		relatorio[user].append('motivo')
		relatorio[user].append(comando.lower())	
		relatorio[user].append('data')
		relatorio[user].append(data)
		relatorio[user].append('usuário')
		relatorio[user].append(name)		
		print(relatorio[user])	
		bot.sendMessage(chat,'%s'%relatorio[user])
		bot.sendMessage(chat,'Verifique seu relatório, se estiver correto digite (''Enviar'') para enviar. Se estiver errado comece novamente digitando (''olá'')')
		step=0
		controlador[user]=step	
def enviar(msg):
	
	client = pymongo.MongoClient("mongodb+srv://engtools:485455@cluster0-mtmdb.gcp.mongodb.net/Engbot?retryWrites=true")
	i=0
	listakey=[]
	while i!= len(relatorio[user]):
		listakey.append((relatorio[user])[i])	
		i+=2
	i=1
	listaval=[]
	while i<= len(relatorio[user]):
		listaval.append((relatorio[user])[i])	
		i+=2
		print(listakey)
		print(listaval)
		dados=dict(zip(listakey,listaval))

		print(dados)

	db = client.Engbot 
	db.agro.insert_one(dados)

	try:
		bot.sendMessage(chat,'relatório enviado')
		bot.sendMessage(chat,'muito obrigado e até a próxima :)')
	except ConnectionFailure:
		print("Estamos com problema na conexão, verifique se você está com internet e tente novamente. Caso o problema continue favor tentar novamente em outro horário, ou entre em contato o suporte técnico")
		

		
		
		


















bot.message_loop(recebemsg, run_forever = 'rodando ...')
     
