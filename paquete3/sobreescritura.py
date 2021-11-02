from paquete3.cuentas import Sumar


class Pechun(Sumar):
    def sumar(numero1,numero2):
        return numero1+numero2

    sumas = sumar(20, 20)
    print(sumas)
