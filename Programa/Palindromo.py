import math

class Palindromo():

    def __init__(self):
        pass

    def capturaPalindromo(self):

        palabra = raw_input("Inserte la palabra: ")

        return palabra

    def verificaPalindromo(self):

        palabra = self.capturaPalindromo()

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
                    return varPal

                inf+=1
                sup-=1

            return varPal

    def imprime(self):

        if self.verificaPalindromo():
            print("La palabra es palindromo")

        else:
            print("La palabra NO es palindromo")



