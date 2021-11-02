import math

class tarea:
    def numero(numeros):


     for n in range(2, numeros):
         if numeros % n == 0:
            print("No es primo", n, "es divisor")
            return False
     print("Es primo")
     return True

    #numerosinredon=float(input("Ingrese un numero: "))
    #numeroredon=math.floor(numerosinredon)
    #numero(numeroredon)

    def bisiesto(año):


        if año % 4 != 0:  # no divisible entre 4
             print("No es bisiesto")
        elif año % 4 == 0 and año % 100 != 0:  # divisible entre 4 y no entre 100 o 400
           print("Es bisiesto")
        elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:  # divisible entre 4 y 10 y no entre 400
             print("No es bisiesto")
        elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:  # divisible entre 4, 100 y 400
             print("Es bisiesto")


    #año = int(input("Dime un año: "))
   # bisiesto(año)
    sumDigit, extNum = 0, 0
    numEntero = int(input("Ingrese un numero entero: "))
    while numEntero != 0:
        extNum = numEntero % 10
        numEntero //= 10
        sumDigit += extNum
    print("La suma de los digitos es: {}".format(sumDigit))

from bs4 import BeautifulSoup
import requests
url = "http://quotes.toscrape.com/"
pagina = requests.get(url)
html = BeautifulSoup(pagina.text, 'html.parser')
print(html)
#Sobreescritura




class Sumar:
    def sumar(numero1,numero2):
        return numero1+numero2

    sumas=sumar(20,20)
    print(sumas)

