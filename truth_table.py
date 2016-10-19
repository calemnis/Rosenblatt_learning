#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy


class KarnoughTable:

    '''
    A bit too magical of an implementation:
    fills the cells of a matrix with a binary representation of the truth table
    corresponding to given [i,j] coordinates.
    For example a 2 dimension Karnough would look like this:
    [[b'00' b'01']
    [b'10' b'11']]
    '''
    def __init__(self, dimension):
        self.dimension = dimension
        d = dimension/2
        varnum_i = math.floor(d)
        varnum_j = dimension - varnum_i

        varnum_dec_i = varnum_i*'1'
        varnum_dec_j = varnum_j*'1'
        self._i = int(varnum_dec_i, 2)
        self._j = int(varnum_dec_j, 2)
        self.truth_matrix = numpy.empty((self._i + 1, self._j + 1), dtype="S10")
        #result matrix initialization
        self.result_matrix = numpy.zeros((self._i + 1, self._j + 1))

        for i in range(0, self._i + 1):
            ch = '0' + str(varnum_i) + 'b'
            var = format(i, ch)
            for j in range(0, self._j + 1):
                ch2 = '0' + str(varnum_j) + 'b'
                var2 = format(j, ch2)
                self.truth_matrix[i][j] = var + var2
        print('The truth matrix: ')
        print(self.truth_matrix)

    def get_dim(self):
        return self.dimension

    def get_i(self):
        return self._i

    def get_j(self):
        return self._j

    def get_truth_index(self, i, j):
        return self.truth_matrix[i][j]

    '''
    Prompts input from the user to fill up the result Karnough matrix with numbers 1,-1.
    '''
    def input_resultmatrix(self):
        for i in range(0, self._i + 1):
            for j in range(0, self._j + 1):
                while True:
                    num = int(input('Please add the [i,j]=[{},{}]-th result matrix element (row by row form)!'
                                    .format(i, j)))
                    print(num)
                    if num in [-1, 1]:
                        self.result_matrix[i][j] = num
                        break
                    else:
                        print('Incorrect format, please enter only 1 or -1!')

        print(self.result_matrix)

    def get_res_index(self, i, j):
        return self.result_matrix[i][j]






