import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

#Construir funcionalidades
@app.route('/')
def homepage():
    return 'API está no ar'

@app.route('/pegarvendas')
def pegarvendas():
    table_data = pd.read_csv('First API\data_table.csv')
    total_vendas = table_data['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)

#rodar a nossa API
app.run()

#table_data = pd.read_csv('First API\data_table.csv')
#print(table_data)
