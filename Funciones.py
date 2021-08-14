# TAREA 1 - MT7003
# Diego marenco Chaves
# Leonenardo Calderon Monge
import math

class Array_ops:
    def multiple_op(self, num):
        if isinstance(num, int):
            return [num * num, 2 ** num, math.factorial(num)]
        else:
            return "ERROR_INVALID_PARAMETER"

    def verify_array_op(self, array):
        if isinstance(array, list):
            i = 0
            while i < len(array):
                if not isinstance(array[i], int):
                    return "	ERROR_INVALID_FUNCTION: the input array does not contain integers only"
                else:
                    array[i] = self.multiple_op(array[i])
                    i = i + 1
            return array
        else:
            return "	ERROR_INVALID_FUNCTION: The input param is not an array."


    def test_verify_1():
        assert verify_array_op(A_A) == [
            [A_A[0]*A_A[0], pow(2, A_A[0]), math.factorial(A_A[0])],
            [A_A[1]*A_A[1], pow(2, A_A[1]), math.factorial(A_A[1])],
            [A_A[2]*A_A[2], pow(2, A_A[2]), math.factorial(A_A[2])]
            ]
    def test_verify_2():
        assert verify_array_op(random.choice) == 123
array_ops = Array_ops()
#print(array_ops.verify_array_op([4, 3, 6]))
