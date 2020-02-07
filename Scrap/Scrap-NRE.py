from urllib.request import Request, urlopen
import re
url="http://www.nre.seed.pr.gov.br/modules/documentos/index.php?curent_dir=1248"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage=str(web_byte)
'''webpage = web_byte.decode('utf-8')'''
chave = 'ÀS 16H00'
print(webpage)

'''posicao = int(webpage.index(chave) + len(chave))

dolar = webpage[ posicao : posicao+4]
print('Cotação do dolar hoje.: R$ %s'%dolar)'''





