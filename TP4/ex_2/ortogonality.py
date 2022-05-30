from ex_2.letters import alphabet
from ex_2.letters import get_patterns
from ex_2.letters import print_with_asterisks
from ex_2.letters import print_patterns_with_asterisks
import itertools
import numpy as np
import sys

def get_ortogonal_combinations(max_combinations, bool_high_avg_dot):
    max_combins = int(max_combinations)
    order = bool_high_avg_dot

    flat_letters = {
        k: np.array(m).flatten() for (k, m) in alphabet.items()
        }
    all_groups = itertools.combinations(flat_letters.keys(), r=4)

    avg_dot_product = []
    max_dot_product = []

    index = 0
    for g in all_groups:
        group = np.array([v for k,v in flat_letters.items() if k in g])
        orto_matrix = group.dot(group.T)
        np.fill_diagonal(orto_matrix, 0)
        row, _ = orto_matrix.shape
        avg_dot_product.append((np.abs(orto_matrix).sum()/(orto_matrix.size-row), g))
        max_dot_product.append((np.abs(orto_matrix).max(), g))
        index+=1

    avg_dot_product = sorted(avg_dot_product, key=lambda x: x[0], reverse=order)

    rta = []
    for i in range(max_combins):
        print("Patterns: {0}, Avg_dot: {1}".format(avg_dot_product[i][1],avg_dot_product[i][0]))
        rta.append(avg_dot_product[i][1])

    return rta


def get_most_different():
    return get_ortogonal_combinations(1, False)

def get_most_alike():
    return get_ortogonal_combinations(1, True)

def most_different_patterns():
    letters = get_most_different()
    return get_patterns(letters[0])

def most_alike_patterns():
    letters = get_most_alike()
    return get_patterns(letters[0])