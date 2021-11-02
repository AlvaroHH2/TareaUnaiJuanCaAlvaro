from paquete3.cuentas import sumar


class Pechun(sumar):
    def sumas(numero1,numero2):
        print("claseb")
        return numero1*numero2

    sumas = sumar(20, 20)
    print(sumas)
