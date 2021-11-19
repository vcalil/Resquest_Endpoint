import requests
import uuid
import json
from datetime import datetime

#Funcao para realizar a request e devolver a response
def doRequest(domain, endpoint,value, headers,token):
	response = requests.get(domain+endpoint+value, headers=headers)
	return response.content

#Funcao para decriptografar o token
def readJWT(token):
	return jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])

#Funcao para pegar o tempo real
def getTime():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	return current_time

if __name__ == '__main__':

	#Variaveis para a chamada do enpoint testado
	uuid_test = "" 
	token = {
	""
	}
	domain = "https://"
	endopoint = "/api/"
	my_headers = { 
		"Host": "", 
		"X-Platform": "Android", 
		"App-Platform": "", 
		"App-Build": "203", 
		"App-Version": "1.64.2", 
		"App-System": "28", 
		"Accept-Encoding": "gzip, deflate", 
		"User-Agent": "okhttp/4.9.1", 
		"Connection": "close",
		"Authorization": ""
	}
	#Variaveis para arquivos
	arqResponseOk = open('responseOk.txt', 'w')
	arqResponseNoOk = open('responseNotOk.txt', 'w')
	#Variavel para o numero de testes realizados
	numero_repeticoes = 5

	#Variaveis para a requisicao e leitura do tempo de expiracao
	responseToken = doRequest()#TO DO: Preencher informacoes para a request
	variableToken = json.loads(responseToken.content)
	myToken = variableToken["NOME DO CAMPO"]#TO DO: Validar se o nome do campo
	payloadJWT = readJWT(myToken)
	dataPayload = json.loads(payloadJWT)

	for count in range(numero_repeticoes):
		while(dataPayload["exp"] < getTime())
		myuuid = str(uuid.uuid4())

		try:
	    	response = doRequest(domain,endopoint,myuuid,token)
	    	response.raise_for_status()
	    	arqResponseOk.write(str(r.content)+'\n')
		except requests.exceptions.HTTPError as errh:
			arqResponseNoOk.write(myuuid+'\n'+response.content+'\n')
	    	print ("Http Error:",errh)
		except requests.exceptions.ConnectionError as errc:
			arqResponseNoOk.write(myuuid+'\n'+response.content+'\n')
	    	print ("Error Connecting:",errc)
		except requests.exceptions.Timeout as errt:
			arqResponseNoOk.write(myuuid+'\n'+response.content+'\n')
	    	print ("Timeout Error:",errt)
		except requests.exceptions.RequestException as err:
			arqResponseNoOk.write(myuuid+'\n'+response.content+'\n')
	    	print ("OOps: Something Else",err)
			

	arqResponseOk.close()
	arqResponseNoOk.close()