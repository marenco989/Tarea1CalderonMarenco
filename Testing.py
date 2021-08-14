# TAREA 1 - MT7003
# Diego marenco Chaves
# Leonenardo Calderon Monge

#Pruebas por medio de Pytest
import math
#se importan las librerias extra a utilizar
import pytest
import random
import string

a,a=[] #arreglo aleatorio
Arreglo_random = [] #arreglo para caso de error
class Array_ops:
    def multiple_op(self, num):
        if isinstance(num, int):
            return [num * num, 2 ** num, math.factorial(num)]
        elif num < 0:
            return "ERROR_INVALID_PARAMETER"
        else:
            return "ERROR_INVALID_PARAMETER"

    def verify_array_op(self, array):
        if isinstance(array, list):
            i = 0
            while i < len(array):
                if not isinstance(array[i], int):
                    return "Error: the input array does not contain integers only"
                else:
                    array[i] = self.multiple_op(array[i])
                    i = i + 1
            return array
        else:
            return "Error: The input param is not an array."

p = random.randint(0,20) #Elige un numero al azar entre 0 y 20

# MULTIPLE_OP EXITOSO   
def test_multiple_op_1():
    assert multiple_op(p)==[p*p,2**p,math.factorial(p)]

#MULTIPLE_OP FALLO CON STRING
def test_multiple_op_2():
    assert multiple_op(random.choice(string.ascii_letters))== 87
    
#VERIFY_ARRAY_OP FALLO
def test_verify_1():
    assert verify_array_op(a,a) == [
        [a,a[9]*a,a[9], pow(2, a,a[9]), math.factorial(a,a[9])],
        [a,a[12]*a,a[12], pow(2, a,a[12]), math.factorial(a,a[12])],
        [a,a[15]*a,a[15], pow(2, a,a[15]), math.factorial(a,a[15])]
        ]

#VERIFY_ARRAY_OP FALLO CON STRING
def test_verify_2():
    assert verify_array_op(Arreglo_random) == 123


