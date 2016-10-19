#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import truth_table
import numpy
import math


'''
Gets the corresponding byte array for an x vector for given [i,j] in the Karnough table.
This function is called in every iteration of the Rosenblatt perceptron learning algorithm.
Also inserts a -1 for biaz and handles the zeros in the byte array - swaps them for a -1.
'''

def next_vec_x(truth_table, i, j):
    tt_element = truth_table.get_truth_index(i, j)
    elem_as_str = tt_element.decode('utf-8')
    vec_x = [int(element) for element in elem_as_str]
    vec_x.insert(0, -1)
    vec_x = [-1 if x == 0 else x for x in vec_x]
    vec_x = numpy.array(vec_x)
    return vec_x

'''
Picks the weight vector corresponding to a '1' in the result table for [i,j] Karnough indexes.
The weight vector is appended by a 1 (biaz weight)
'''

def get_ones(tt, i, j):
    tt_element = tt.get_truth_index(i, j)
    elem_as_str = tt_element.decode('utf-8')
    vec_x = [int(element) for element in elem_as_str]
    vec_x.append(1)
    vec_x = numpy.array(vec_x)
    vec_x = [-1 if x == 0 else x for x in vec_x]
    return vec_x

'''
Gets the starting weight vector (all ones!)
'''
def get_starting_weight(tt):
    weight_len = tt.get_dim() + 1
    vec_weight = []
    for i in range(weight_len):
        vec_weight.append(1)
    vec_weight = numpy.array(vec_weight)
    return vec_weight

'''
Gets a starting weight vector and a next x vector for given [i,j] coordinates.
Also gets the result (a d scalar, which may be -1 or 1).
From this the algorithm calculates the y output vector (with sum and sign operations).
Next it calculates scalar e and lastly the next weight vector.
Memorizes the last weight vector to compare with the fresh weight vector.
If weight remains unchanged less than x times (now x is 10),
it recommends the weights for first layer neurons and an OR neuron.
'''
def rosenblatt_algorithm(tt):
    vec_weight = get_starting_weight(tt)

    unchanged_weights = 0
    for k in range(10):
        for i in range(tt.get_i() + 1):
            for j in range(tt.get_j() + 1):
                last_weight = vec_weight
                vec_x = next_vec_x(tt, i, j)
                print('vec_x:', vec_x)

                scalar_d = numpy.array(tt.get_res_index(i,j))
                vec_y = numpy.multiply(vec_x, vec_weight)
                summed = numpy.sum(vec_y)
                sgn_y = math.copysign(1, summed)
                scalar_e = scalar_d - sgn_y

                vec_weight = vec_weight + numpy.multiply(scalar_e, vec_x)
                print('new_weight:', vec_weight, '-\n')
                if numpy.array_equal(last_weight, vec_weight):
                    unchanged_weights += 1
                else:
                    unchanged_weights = 0

    print('{0} unchanged weight vectors in 10*{1}*{2} attempts'.
          format(unchanged_weights, tt.get_i() + 1, tt.get_j() + 1))

    if unchanged_weights < 10:
        print('This function with given Karnough/truth table is not realizable.')
        for i in range(tt.get_i() + 1):
            for j in range(tt.get_j() + 1):
                if tt.get_res_index(i,j) == 1:
                    print('Recommended first layer perceptron with weights', get_ones(tt, i, j))

        or_weight = get_starting_weight(tt)
        or_weight[-1] = -1
        print('Recommended second layer perceptron with weights', or_weight, ' + a -1 biaz')


if __name__ == '__main__':

    while True:
        dim = int(input("How many variables would you like to see in the Karnough table?"))
        if dim > 1:
            var_matrix = truth_table.KarnoughTable(dim)
            var_matrix.input_resultmatrix()
            rosenblatt_algorithm(var_matrix)
            break
        else:
            print('You should not enter less than 2-variables. try again!')



