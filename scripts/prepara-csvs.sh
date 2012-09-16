#!/bin/bash

# Script para preprar os arquivos do TSE
# Aglutina os arquivos da pasta em um só arquivão (atenção: as colunas devem ser as mesmas)
cat *.txt > tmp_file.tmp

# Usa o csvkit para converter em um CSV decente
in2csv --format csv -e iso-8859-1 tmp_file.tmp > tmp_file.csv

#Coloca um header no CSV descomente a linha certa

#Informação sobre Candidatos
#echo "DATA_GERACAO,HORA_GERACAO,ANO_ELEICAO,NUM_TURNO,DESCRICAO_ELEICAO,SIGLA_UF,SIGLA_UE,DESCRICAO_UE,CODIGO_CARGO,DESCRICAO_CARGO,NOME_CANDIDATO,SEQUENCIAL_CANDIDATO,NUMERO_CANDIDATO,NOME_URNA_CANDIDATO,COD_SITUACAO_CANDIDATURA,DES_SITUACAO_CANDIDATURA,NUMERO_PARTIDO,SIGLA_PARTIDO,NOME_PARTIDO,CODIGO_LEGENDA,SIGLA_LEGENDA,COMPOSICAO_LEGENDA,NOME_LEGENDA,CODIGO_OCUPACAO,DESCRICAO_OCUPACAO,DATA_NASCIMENTO,NUM_TITULO_ELEITORAL_CANDIDATO,IDADE_DATA_ELEICAO,CODIGO_SEXO,DESCRICAO_SEXO,COD_GRAU_INSTRUCAO,DESCRICAO_GRAU_INSTRUCAO,CODIGO_ESTADO_CIVIL,DESCRICAO_ESTADO_CIVIL,CODIGO_NACIONALIDADE,DESCRICAO_NACIONALIDADE,SIGLA_UF_NASCIMENTO,CODIGO_MUNICIPIO_NASCIMENTO,NOME_MUNICIPIO_NASCIMENTO,DESPESA_MAX_CAMPANHA,COD_SIT_TOT_TURNO,DESC_SIT_TOT_TURNO" > tmp_header.csv

#Informação sobre Bens dos Candidatos
#echo "DATA_GERACAO,HORA_GERACAO,ANO_ELEICAO,DESCRICAO_ELEICAO,SIGLA_UF,SQ_CANDIDATO,CD_TIPO_BEM_CANDIDATO,DS_TIPO_BEM_CANDIDATO,DS_BEM,VALOR_BEM,DATA_ULTIMA_ATUALIZACAO,HORA_ULTIMA_ATUALIZACAO" > header.csv

#Junta os arquivos em um só e remove os arquivos temporarios (renomeie se necessário)
cat tmp_header.csv tmp_file.csv > clean-compiled.csv
rm tmp_*

# Scripts para o csvkit para preparar os arquivos para o script de normalizar nomes. Descomente se necessário.
#csvcut -c 11,27,18,7,10,42 clean-compiled.csv | csvgrep -c 6 -r "ELEITO" | csvgrep -c 5 -m "SENADOR" > senadocut.csv
#csvcut -c 11,27,18,7,10,42 clean-compiled.csv | csvgrep -c 6 -r "ELEITO" | csvgrep -c 5 -r "DEPUTADO FEDERAL" > deputadocut.csv


