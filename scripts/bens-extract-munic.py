# -*- coding: utf8 -*-
import csv, difflib, re
from unidecode import unidecode

# Carrega um arquivo com os municipios e seus códigos do IBGE
# Prepara a expressão regular - precisa melhorar

def loadMunicipios(filename="../dados/munic.csv"):
    munic_csv = csv.DictReader(open(filename))
    munic = []

    for m in munic_csv:
        m['REGEX'] = re.compile("("+m['MUNIC']+")")
        munic.append(m)

    return munic



# Tenta encontrar os munícipios na descrição dos bens
# Retorna uma array com todos os matches encontrados - por enquanto só estou considerando o primeiro
    
def searchMunicipios(csvlist, munic):
    geo_ref = []
    print "Buscando por municipios..."
    for b in csv_list:
        data = b
        data['geo'] = []
        asset = b['DS_TIPO_BEM_CANDIDATO']
        if asset == "TERRENO":
            for m in munic:
                search = re.search(m['REGEX'] ,b['DS_BEM'])
                if search != None:
                    data['geo'].append(m)
        if data['geo']:
            geo_ref.append(data)
    return geo_ref

# Gera um objeto com uma soma dos valores por código do IBGE    
def generateMunics(geo_ref):
    print "Somando valores por municipios..."
    terras_count = {}
    for e in geo_ref:
        l_id = e['geo'][0]['CODIGO_MUN']
        valor = float(e['VALOR_BEM'])
        if terras_count.has_key(l_id):
            terras_count[l_id] += valor
        else:
            terras_count[l_id] = valor
    return terras_count

# Gera um objeto com uma soma dos valores por Estado
def generateEstados(geo_ref):
    print "Somando valores por estados..."
    terras_count = {}
    for e in geo_ref:
        l_id = e['geo'][0]['ESTADOS']
        valor = float(e['VALOR_BEM'])
        if terras_count.has_key(l_id):
            terras_count[l_id] += valor
        else:
            terras_count[l_id] = valor
    return terras_count


# Roda o script - comentado
bens_csv = csv.DictReader(open("../dados/raw/bens.csv", "r"))
munic = loadMunicipios()
geo_ref = searchMunicipios(bens_csv, munic)
estados_list = generateEstados(geo_ref)
munic_list = generateMunics(geo_ref)

print estados_list
