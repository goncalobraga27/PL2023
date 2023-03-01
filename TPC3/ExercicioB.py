import re
class ExercicioB:

    def determinaSeculo(self, number):
        if number[2] == 0 and number[3] == 0:
            auxsec = number[0:2]
            sec = int(auxsec)
        else:
            auxsec = number[0:2]
            sec = int(auxsec) + 1
        return sec
    def calculaFrequenciaSeculos(self, file):
        dic = dict()
        for line in file:
            expRegex = re.search(r'\:\:[0-9]{4}\-', line)
            if expRegex:
                exp = expRegex.group()
                number = exp[2:6]
                sec = self.determinaSeculo(number)
                if sec not in dic:
                    dic[sec] = dict()
                    dic[sec]["nome"] = dict()
                    dic[sec]["apelido"] = dict()
        return dic

    def calculaFrequenciaNomes_Apelidos(self, dic, file): #{19: {'nome': {}, 'apelido': {}}, 20: {'nome': {}, 'apelido': {}}, 18: {'nome': {}, 'apelido': {}}, 17: {'nome': {}, 'apelido': {}}}
        for line in file:
           expRegex1 = re.search(r'(\:\:[0-9]{4}\-)', line)
           expRegex2 = re.findall(r'(\:\:[a-zA-Z]+\s)', line)
           expRegex3 = re.findall(r'(\s[a-zA-Z]+\:\:)|(\s[a-zA-Z]+\,)', line)
           if expRegex1 and expRegex2 and expRegex3:
               ano = expRegex1.group()[2:6]
               sec = self.determinaSeculo(ano)
               for exp in expRegex2:
                   nameAux = exp[2:]
                   name = nameAux[:-1]
                   if name not in dic[sec]['nome']:
                       dic[sec]['nome'][name] = 1
                   else:
                       dic[sec]['nome'][name] += 1
               for pair in expRegex3:
                   if pair[0] != '':
                       namePair = pair[0]
                       if namePair[-1] == ',':
                           nameAuxApelido = namePair[:-1]
                           nameApelido = nameAuxApelido[:1]
                       else:
                           nameAuxApelido = namePair[:-2]
                           nameApelido = nameAuxApelido[1:]
                           if nameApelido not in dic[sec]['apelido']:
                               dic[sec]['apelido'][nameApelido] = 1
                           else:
                               dic[sec]['apelido'][nameApelido] += 1
                   else :
                       namePair = pair[1]
                       if namePair[-1] == ',':
                           nameAuxApelido = namePair[:-1]
                           nameApelido = nameAuxApelido[:1]
                       else:
                           nameAuxApelido = namePair[:-2]
                           nameApelido = nameAuxApelido[1:]
                           if nameApelido not in dic[sec]['apelido']:
                               dic[sec]['apelido'][nameApelido] = 1
                           else:
                               dic[sec]['apelido'][nameApelido] += 1

        return dic
    def calculaResultadoNomes(self, dic):
        resultado = ""
        for key in dic:
            resultado+="--------Século "+str(key)+"----------\n"
            sorted_NamePerson = sorted(dic[key]['nome'].items(), key=lambda x: x[1], reverse=True)
            sorted_ApelidoPerson = sorted(dic[key]['apelido'].items(), key=lambda x: x[1], reverse=True)
            nomes = sorted_NamePerson[:5]
            apelidos = sorted_ApelidoPerson[:5]
            resultado += "--Nomes--\n"
            for pair in nomes:
                resultado += str(pair[0])+"->"+str(pair[1])+"\n"
            resultado += "--Apelidos--\n"
            for pair in apelidos:
                resultado += str(pair[0])+"->"+str(pair[1])+"\n"
        return resultado







