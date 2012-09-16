# -*- coding: utf8 -*-
import csv, json, pymongo


def carregaGeral(filename="../dados/raw/eleitos-cut.csv"):
    # Monta dict dos eleitos 2006-2010 [precisa corrigir a esturura para multiplas eleiçoes]
    base_eleitos_file = csv.DictReader(open(filename))


    print "Carregando eleitos..."
    first_step = {}

    for e in base_eleitos_file:
        l_id = e['SEQUENCIAL_CANDIDATO']+e['ANO_ELEICAO']
        first_step[l_id] = e

    # Junta dados de bens
    base_bens_file = csv.DictReader(open("../dados/raw/bens.csv"))

    print "Carregando bens..."
    second_step = {}

    for b in base_bens_file:
        last_id = b['SQ_CANDIDATO']+b['ANO_ELEICAO'] # chave anterior
        if first_step.has_key(last_id): # pega apenas os eleitos
            next_id = first_step[last_id]['NOME_CANDIDATO']+first_step[last_id]['SIGLA_UF']+first_step[last_id]['SIGLA_PARTIDO'] # proxima chave
            second_step[next_id] = first_step[last_id]
            if second_step[next_id].has_key("BENS"):
                second_step[next_id]["BENS"].append(b)
            else:
                second_step[next_id]["BENS"] = [b]

    first_step = {}

    # Junta doações
    base_doacoes_file = csv.DictReader(open("../dados/raw/receitas.csv"))
    third_step = {}

    print "Carregando doações..."
    for b in base_doacoes_file:
        last_id = b['Nome candidato']+b['UF']+b['Sigla Partido']
        if second_step.has_key(last_id): #pega apenas os eleitos
            next_id = second_step[last_id]['NUM_TITULO_ELEITORAL_CANDIDATO']
            third_step[next_id] = second_step[last_id]
            if third_step[next_id].has_key("DOACAO"):
                third_step[next_id]["DOACAO"].append(b)
            else:
                third_step[next_id]["DOACAO"] = [b]

    second_step = {}
    return third_step

def sleepy(wholedeal) {
        connection = pymongo.Connection('localhost', 27017)
        db = connection['bancadaruralista']
        bancada = db.bancada

        for d in third_step:
            bancada.insert(third_step[d])

final = carregaGeral()
sleepy(final)
