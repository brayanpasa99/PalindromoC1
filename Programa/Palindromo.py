import math

class Palindromo():

    def __init__(self):
        pass

    def capturaPalindromo(self):
        print "PROGRAMA PARA PALABRAS PALINDROMAS"
        print ""
        palabra = raw_input("Inserte la palabra: ")
        return palabra

    def verificaPalindromo(self, palabra):

        medio = int(math.ceil(len(palabra)/2))

        varPal = True

        if len(palabra)>0:

            inf = 0
            sup = len(palabra)-1

            for i in range(0, medio):

                if palabra[inf] == palabra[sup]:
                    varPal = True

                elif palabra[inf] != palabra[sup]:
                    varPal = False
                    return [varPal, inf, sup]

                inf+=1
                sup-=1

            return varPal

    def imprime(self):

        if self.conviertePalindromo():
            print("")

    def conviertePalindromo(self):

        palabra = self.capturaPalindromo()


        if len(palabra)>1:

            continua = self.verificaPalindromo(palabra)

            if (self.verificaPalindromo(palabra) is True):
                print"La palabra ya es palindroma..."
                state = False


            while type(continua)==list and not continua[0]:
                
                auxpalabra = palabra[::-1]
                auxpalabra = auxpalabra.replace(palabra[continua[2]], palabra[continua[1]]+palabra[continua[2]], 1)
                palabra = auxpalabra[::-1]
                continua = self.verificaPalindromo(palabra)
                state = True

            if state == True:
                print "La palabra no es palindroma..."
                print("Palabra palindroma generada: " + palabra)
                return True

        elif len(palabra)>0:
            print("La palabra " + palabra + " ya es palindroma...")




