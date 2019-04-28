import math
from string import join


class Palindromo():

    def __init__(self):
        pass

    def corriendo(self):
        palabra = self.capturaPalindromo()

        if self.verificaPalindromo(palabra) is True:
            print ("La palabra es palindroma")
        else:
            print("")
            print("La palabra NO es palindroma, se transformara")
            self.conviertePalindromoAdd(palabra)
            self.conviertePalindromoRem(palabra)

    def conviertePalindromoAdd(self, palabra):
        print("")
        print"Probando agregando las letras"

        abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"
                      ,"o","p","q","r","s","t","u","v","w","x","y","z"]

        i = 0
        j = 0
        k = 0
        l = 0
        cont_pal_add = 0

        palabra_sep = list(palabra)

        '''print(''.join(palabra_sep))'''

        while k < len(palabra_sep):
            l = 0

            while l < 26:
                palabra_sep = list(palabra)
                palabra_sep[k] = abecedario[l] + palabra[k]
                palabra_aux = ''.join(palabra_sep)
                if self.verificaPalindromo(palabra_aux):
                    print("Palabra palindroma por agregacion: " + palabra_aux)
                    cont_pal_add =+ 1
                l+=1


            if k == len(palabra_sep) - 1:
                while i < 26:
                    palabra_sep = list(palabra)
                    palabra_sep[k] = palabra[k] + abecedario[i]
                    palabra_aux = ''.join(palabra_sep)
                    if self.verificaPalindromo(palabra_aux):
                        print("Palabra palindroma por agregacion: " + palabra_aux)
                        cont_pal_add = + 1
                    i += 1
            k += 1

    def conviertePalindromoRem(self, palabra):
        print("")
        print "Probando removiendo las letras"
        i = 0
        j = 0
        k = 0
        l = 0
        cont_pal_rem = 0

        palabra_sep = list(palabra)


        while k < len(palabra_sep):

            if k==0:
                palabra_aux = palabra[1:]
                if self.verificaPalindromo(palabra_aux):
                    print("Palabra palindroma (removiendo): " + palabra_aux)
                    cont_pal_add = + 1

            palabra_sep = list(palabra)

            palabra_sep[k] = palabra_sep.pop(k)
            palabra_aux = ''.join(palabra_sep)
            if self.verificaPalindromo(palabra_aux):
                print("Palabra palindroma (removiendo): " + palabra_aux)
                cont_pal_rem = + 1
            k += 1

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

                '''print ("Comparacion de letras: " + palabra[inf]+palabra[sup])'''

                if palabra[inf] == palabra[sup]:
                    varPal = True

                elif palabra[inf] != palabra[sup]:
                    varPal = False
                    return varPal

                inf+=1
                sup-=1

            return varPal

    def conviertePalindromo(self, palabra):
        palabra = self.capturaPalindromo()


    '''def conviertePalindromo(self):

        palabra = self.capturaPalindromo()

        if len(palabra)>1:

            continua = self.verificaPalindromo(palabra)

            auxpalabra = palabra.replace(palabra[continua[2]], palabra[continua[2]]+palabra[continua[1]])
            palabra = palabra[0:continua[2]] + auxpalabra[continua[2]+1:]
            print(palabra +"AUX"+ auxpalabra)

            while type(continua)==list and not continua[0]:
                auxpalabra = palabra.replace(palabra[continua[2]], palabra[continua[2]] + palabra[continua[1]])
                palabra = palabra[0:continua[2]] + auxpalabra[continua[2] + 1:]
                print ("AQUI "+palabra)
                continua = self.verificaPalindromo(palabra)
            

            print(palabra)

        elif len(palabra)>0:
            print(palabra)

            inf += 1
                sup -= 1
            for i in range(0, medio):

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





