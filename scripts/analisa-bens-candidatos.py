# -*- coding: utf8 -*-
import csv, re


# Esse script cria uma série de expressões regulares para extrair elementos da linha de descrição do arquivo de declaração de bens.


# Definição dos tipos. O script vai passear por todos os tipos, marcando as tags que forem localizadas pelas expressões regulares.

# Tipos de imóvel. Urbano e Rural.
e = {}
e['types'] = {}
e['types']['URBANO'] = re.compile("(TERRENO) URBANO|(LOTE) URBANO|IMÓVEL (URBANO)|(APARTAMENTO)|(COMERCIAL)|(POSTO)|(URBANO)")
e['types']['RURAL'] = re.compile("(FAZENDA)|(RURAL)|(SITIO)|(SÍTIO)|(CHACARA)|(LOT\. DE TERRA)|(LOTE\W)|(CHÁCARA)")

# Tamanho dos imóveis.
e['sizes'] = {}
e['sizes']['ALQ'] = re.compile("([\.,0-9]*) ALQ")
e['sizes']['M2'] = re.compile("([\.,0-9]*) M[2²]|([\.,0-9]*) METROS")
e['sizes']['HECTAR'] = re.compile("([\.,0-9 ]*) HA|([\.,0-9 ]*) HECTARES")
e['types']['GLEBA'] = re.compile("(GLEBA)")

# Informações geográficas. Ainda precisa fazer uma lista de munícipios e melhorar o parser dos estados.
e['geo'] = {}
e['geo']['ENDERECO'] = re.compile("(RUA .*? [0-9,]*?)[,\.]|(AV\. .*? [0-9]*?)[,\.]|(AVENIDA .*)")
#e['geo']['ESTADOS'] = re.compile("\W(AC)\W|\W(AL)\W|\W(AM)\W|\W(AP)\W|\W(BA)\W|\W(CE)\W|\W(DF)\W|\W(ES)\W|\W(GO)\W|\W(MA)\W|\W(MG)\W|\W(MS)\W|\W(MT)\W|\W(RJ)\W|\W(SP)\W|\W(PA)\W|\W(PB)\W|\W(PE)\W|\W(PI)\W|\W(PR)\W|\W(RN)\W|\W(RO)\W|\W(RR)\W")
e['geo']['MUNICIPIO'] = re.compile("MUNICIPIO|MUNÍCIPIO")

# Outros bens móveis.
e['gado'] = {}
e['gado']['GADO'] = re.compile("([\.,0-9 ]*) CABEÇAS DE GADO|([\.,0-9 ]*) .* BOVINOS|([\.,0-9 ]*) REZES|(VACAS)|(BEZERROS)|([\.,0-9 ]*) RESES|([\.,0-9 ]*) NOVILHAS")
e['gado']['MAQUINAS'] = re.compile("(TRATOR)|(ROÇADEIRA)|(ARADORA)|(COLHETADEIRA)")
e['gado']['CAVALO'] = re.compile("(CAVALOS)|(EQUINOS)|(EGUAS)")
e['gado']['SACAS'] = re.compile("SACAS DE (\w*)|SACOS DE (\w*)")


extractors = ['types', 'sizes', 'geo', 'gado']

def extract(text, expressions, solo=False):   
    t = []
    for e in expressions:
        matches = re.search(expressions[e], text)
        if solo:
            print "Looking for " + e
            print matches
        if matches:
            for g in matches.groups():
                if g != None:
                    t.append({ e : g.strip()})
    if solo:
        print t
    return t
    
# Mudar o nome e diretório do arquivo conforme seu sistema
assets_list = csv.DictReader(open("../dados/raw/benstotal.csv", "r"))
for asset in assets_list:
    choice = asset['DS_TIPO_BEM_CANDIDATO']
    
    # Pula tipos desnecessários
    if choice == 'VE\xc3\x8dCULO AUTOMOTOR TERRESTRE: CAMINH\xc3\x83O, AUTOM\xc3\x93VEL, MOTO, ETC.':
        pass
    
    # Aplica os parsers específicos para cada tipo de bem
    elif choice == "TERRENO" or choice == "OUTROS BENS IMÓVEIS":
        tags = []
            for c in ['types', 'sizes', 'geo']:
                tags += extract(asset['DS_BEM'], e[c])
            if tags:
                print asset['DS_BEM']
                print tags
    elif choice == "OUTROS BENS MÓVEIS":
        tags = []
        for c in ['gado']:
            tags += extract(asset['DS_BEM'], e[c])
        if tags:
            print asset['DS_BEM']
            print tags
    else:
        pass
        #print choice
