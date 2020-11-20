# Ron Raifer

class Functions:
    KEY_SIZE = 2
    N = 26

    def cvt_char_to_int(self, ch):
        # lower case
        cvt_char = ord(ch)
        if 97 <= cvt_char <= 122:
            return cvt_char - 97
        # upper case
        if 65 <= cvt_char <= 90:
            return cvt_char - 65
        return -1

    def cvt_int_to_char(self, n):
        return chr(n+97)

    def string_to_key_matrix(self, key):
        keymatrix = [[self.cvt_char_to_int(key[0]), self.cvt_char_to_int(key[1])],
                     [self.cvt_char_to_int(key[2]), self.cvt_char_to_int(key[3])]]
        return keymatrix

    def keymatrix_calculation(self, keymatrix):
        tmp_mat1 = [[0] * self.KEY_SIZE for i in range(self.KEY_SIZE)]
        tmp_mat2 = [[0] * self.KEY_SIZE for i in range(self.KEY_SIZE)]
        res_mat = [[0] * self.KEY_SIZE for i in range(self.KEY_SIZE)]
        # A^2
        for i in range(self.KEY_SIZE):
            for j in range(self.KEY_SIZE):
                for k in range(self.KEY_SIZE):
                    tmp_mat1[i][j] += keymatrix[i][k] * keymatrix[k][j]
        # A^3
        for i in range(self.KEY_SIZE):
            for j in range(self.KEY_SIZE):
                for k in range(self.KEY_SIZE):
                    tmp_mat2[i][j] += tmp_mat1[i][k] * keymatrix[k][j]
        # A^3+2A
        for i in range(self.KEY_SIZE):
            for j in range(self.KEY_SIZE):
                res_mat[i][j] = tmp_mat2[i][j] + 2 * keymatrix[i][j]
        # ((A^3+2A) % N + N) % N
        for i in range(self.KEY_SIZE):
            for j in range(self.KEY_SIZE):
                res_mat[i][j] = self.modulo_n(res_mat[i][j])
        return res_mat

    def determinant_calculation(self, matrix):
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    def inverse_num_calculation(self, number):
        number = self.modulo_n(number)
        i = 1
        while i < self.N:
            i += 1
            if self.modulo_n(number * i) == 1:
                return i
        return -1

    def modulo_n(self, number):
        return (number % self.N + self.N) % self.N

    def vec_mat_mul_calculation(self, v, matrix):
        vec = [0, 0]
        for i in range(self.KEY_SIZE):
            for j in range(self.KEY_SIZE):
                vec[i] += v[j] * matrix[j][i]
        vec[0] = self.modulo_n(vec[0])
        vec[1] = self.modulo_n(vec[1])
        return vec

    def inverse_mat_calculation(self, matrix):
        res_mat = [[0] * self.KEY_SIZE for i in range(self.KEY_SIZE)]
        inverse_num = self.inverse_num_calculation(self.determinant_calculation(matrix))  # get inverse num of det
        if inverse_num == -1:
            print("\n\nKey Matrix is not invertible!\n")
            print(matrix)
            exit(1)
        res_mat[0][0] = self.modulo_n(inverse_num * matrix[1][1])
        res_mat[0][1] = self.modulo_n(inverse_num * matrix[0][1] * (-1))
        res_mat[1][0] = self.modulo_n(inverse_num * matrix[1][0] * (-1))
        res_mat[1][1] = self.modulo_n(inverse_num * matrix[0][0])
        return res_mat
