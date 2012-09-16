# Monitor da Banca Ruralista Exandida

## Objetivo
Criar um site que permita visualizar os parlamentares e suas relações com a bancada ruralista e com o agronegócio brasileiro.

## Os Dados
Para construir o app delineamos algumas analíses possíveis em cima dos dados disponíveis
* Histórico e Mini-bio
	* Excelências
	* Wikipedia
	* DIAP
	* Ocupação declarada (TSE)
* Bens declarados (TSE)
	* Cabeças de gado
	* Posse de terras
	* Uso da terra (uma razão entre HAs e cabeças de gado)
	* Maquinário agricola
	* Participação em empresas agricolas (ainda não encontramos um jeito de identificar essas empresas)
* Votação (XML da Câmara e do Senado)
	* Código Florestal
	* PEC do Trabalho Escravo
	* MP da Grilagem
	* Lei da Anistia de Dívida
	* Lei Complementar 140
	* Resultados das votações	
	* Relatores dos projetos de lei
* Processos (Várias fontes)
	* Muitas fontes diferentes, estão sendo levantados na mão para os ~80 candidatos com cartão vermelho (2x votaram a favor do código florestal)
* Doações (TSE)
	* Cruzamento com as 100 maiores empresas de agronegócio do país

## Desafios
* Criar identificar único entre as bases do TSE e os dados da Câmara e do Senado
** Criei um script que usa fuzzy match para procurar os nomes, mas ainda existem ~200 deputados federais que vão precisar ser pareados e os outros precisam de revisão. A mesma coisa com o Senado.
* Criar um parser para extrair dados estruturados da declaração de bens de campanha
** Criei um script que usa expressões regulares, ainda não testei a eficácia dele e nem olhei para falsos posítivos... mas esta no caminho
* Criar um sistema de georeferenciamento para as terras localizadas na declaração de bens
** O ideal, creio, é bater essa lista com uma lista de nomes de munícipios - vamos perder coisas, mas vai pegar bastante coisa. Da pra usar o compare.py para isso também.
* Localizar o CNPJ e/ou Razão Social das empresas levantadas. A lista montada só possui o nome 'fantasia' - aquele conhecido pelas pessoas. Rodei o compare .py ainda assim e não consegui achar bons matches.
* Aglutinar as bases do TSE em um único banco de dados. A sugestão é usar um banco de dados orientado a objetos, como Mongo ou CouchDB - não da muito trabalho, mas também não é muito rápido - então já é hora de por a mão na massa.


## Links e outros
(XML da Câmara)[http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ObterVotacaoProposicao?tipo=PL&numero=1876&ano=1999]

(XML do Senado)[http://legis.senado.gov.br/dadosabertos/materia/100475]

(Scraper da Câmara)[https://scraperwiki.com/scrapers/camara-codigo-florestal/] - by Dani

(Scraper da Câmara)[https://github.com/barraponto/brazilian-camara-voting] - by Capi

(Scripts váriados)[https://github.com/pmarkun/bancadaruralista] - by Pedro

(Estrutura JSON)[https://gist.github.com/3730317] - by Daniel

(Planilha de organização)[https://docs.google.com/spreadsheet/ccc?key=0At9GzGQkNUDndEgyWGhGb2wxSXBlSnQ2V2d6VnVtZ1E] - by um monte de gente

(Dados no TSE)[http://www.tse.jus.br/eleicoes/repositorio-de-dados-eleitorais] - by TSE