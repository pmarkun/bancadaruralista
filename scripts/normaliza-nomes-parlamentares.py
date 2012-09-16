from compare import *

# Script que compara os nomes dos candidatos e gera uma lista csv para correções
# Utiliza o compare.py que precisa da difflib e do unidecode
# pip install difflib
# pip install unidecode

# Cria um objeto Matcher - específique o arquivo que vai servir de base para comparações e o campo para comparar
m = Matcher("senadocut.csv", "NOME_CANDIDATO")
votatoon = open('senado-votacoes.csv', "r")
votacoes = csv.DictReader(votatoon)

test_list = []
for v in votacoes:
    test_list.append(v['NOME'])

# A função test e a função csv_comparisson recebem uma lista como paramêtro de entrada.
# Use o print_result para ver o resultado das comparações.
m.test(test_list, print_result=True)
    
