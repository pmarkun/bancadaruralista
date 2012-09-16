# -*- coding: utf8 -*-
import csv, difflib
from unidecode import unidecode

class Matcher:
    """Um objeto para encontrar strings semelhantes. Passe como parametros o nome do arquivo csv e o campo."""
    def __init__(self, filename, fieldname):
        p_list = csv.DictReader(open(filename, 'r'))
        
        self.fuzzy_index = []
        self.fuzzy_matches = {}

        for p in p_list:
            match_string = unidecode(p[fieldname]).upper()
            self.fuzzy_index.append(match_string)
            self.fuzzy_matches[match_string] = p
            self.fuzzy_matches[match_string]["original_name"] = p[fieldname]
        

    def match(self, parlamentar, sense=0.6):
        """A função de comparação. Recebe uma string e retorna uma lista de possíbilidades ordenada por prioridade. Baseado no difflib."""
        matches = difflib.get_close_matches(unidecode(parlamentar).upper(), self.fuzzy_index, 3, sense)
        return matches
    
    def test(self, compare_list, sense=0.6, print_result=False):
        """Testa uma lista de strings contra o CSV base. E retorna um balanço das respostas encontradas."""
        self.test_count = {
            "0" : 0
        }
        for t in compare_list:
            matched = self.match(t, sense)
            if print_result and matched:
                print t + " = " + str(matched)
                
            if not matched:
                self.test_count['0'] += 1
            elif self.test_count.has_key(str(len(matched))):
                self.test_count[str(len(matched))] += 1
            else:
                self.test_count[str(len(matched))] = 1
        print "Test result with " + str(sense) + " sensitivity: " + str(self.test_count)

    def csv_comparisson(self, compare_list, match_field=None, sense=0.6, outfile="compare.csv"):
        """Gera um CSV para comparação e correção manual.
        Recebe como paramêtro uma lista e o campo único que deve ser incluido no novo CSV.
        Use o parametro 'outfile' para mudar o nome do arquivo de saída."""
        csv_file = open(outfile, 'w')
        w = csv.DictWriter(csv_file, [ "original_string", "matched_string", "id" ])
        w.writeheader()
        for t in compare_list:
            matched = self.match(t, sense)
            if len(matched) > 0:
                match_id = None
                if match_field:
                    try:
                        match_id = self.fuzzy_matches[matched[0]][match_field]
                    except:
                        match_id = "error: field not found"
                w.writerow({ "original_string" : t, "matched_string" : self.fuzzy_matches[matched[0]]['original_name'], "id" : match_id})
            elif len(matched) == 0:
                w.writerow({ "original_string" : t, "matched_string" : "", "id" : ""})
        csv_file.close()
