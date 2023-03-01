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

    def calculaFrequenciaNomes_Apelidos(self, dic, file):
        print(dic)
        for line in file:
           expRegex = re.search(r'(\:\:[0-9]{4}\-)(\:\:[a-zA-Z]+\s)((\s[a-zA-Z]+\:\:)|(\s[a-zA-Z]+\,))', line)
           if expRegex:
               print(expRegex)
               print(expRegex.groups())
               print(expRegex.group())
