'''
Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro
O link de estudo é: https://www.youtube.com/watch?v=WWVEymSt1iI&t=1417s
Estou usando: https://replit.com/@EddyGiusepe/MinhaAPI#main.py
'''
import requests
link = "https://minhaapi.eddygiusepe.repl.co/pegarvendas"
requisicao = requests.get(link)
print(requisicao) # 200 significa
print(requisicao.json())
# Também podemos fazer:
dicionario = requisicao.json()
print(dicionario["total_vendas"])
