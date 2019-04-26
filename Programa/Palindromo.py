import math

class Palindromo():

    def __init__(self):
        pass

    def capturaPalindromo(self):

        palabra = raw_input("Inserte la palabra: ")

        return palabra

    def verificaPalindromo(self, palabra):

        medio = int(math.ceil(len(palabra)/2))

        varPal = True

        if len(palabra)>0:

            inf = 0
            sup = len(palabra)-1

            for i in range(0, medio):

                print (palabra[inf]+palabra[sup])

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
            print("La palabra es palindromo")

        else:
            print("La palabra NO es palindromo")

    def conviertePalindromo(self):

        palabra = self.capturaPalindromo()

        if len(palabra)>1:

            continua = self.verificaPalindromo(palabra)


            while type(continua)==list and not continua[0]:
                
                auxpalabra = palabra[::-1]
                auxpalabra = auxpalabra.replace(palabra[continua[2]], palabra[continua[1]]+palabra[continua[2]], 1)
                palabra = auxpalabra[::-1]
                print palabra.find("a")
                print ("AQUI "+palabra)
                continua = self.verificaPalindromo(palabra)


            print(palabra)

        elif len(palabra)>0:
            print(palabra)

            '''inf += 1
                sup -= 1'''
            '''for i in range(0, medio):

                print (palabra[inf]+palabra[sup])

                if palabra[inf] == palabra[sup]:
                    varPal = True

                elif palabra[inf] != palabra[sup]:
                    varPal = False
                    palabra = palabra + palabra[inf]
                    self.verificaPalindromo(palabra)
                    print (palabra)
                    while not varPal:
                        
                    return varPal'''





