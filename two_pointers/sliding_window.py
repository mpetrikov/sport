#!/bin/python3

import math
import os
import random
import re
import sys

# 8
# GAAATAAA


def balanced(n, d):
    if d['A'] <= n and d['C'] <= n and d['G'] <= n and d['T'] <= n:
        return True

    return False

# Complete the steadyGene function below.
def steadyGene(gene):
    lgene = len(gene)
    norm = lgene//4
    d = {
        'A': gene.count('A'),
        'C': gene.count('C'),
        'G': gene.count('G'),
        'T': gene.count('T'),
    }

    i = 0
    j = 0
    m = 100000000

    while i < lgene and j < lgene:
        print(i, j, d)
        if not balanced(norm, d):
            d[gene[j]] = d[gene[j]] - 1
            j += 1
        else:
            m = min(m, j-i)
            d[gene[i]] = d[gene[i]] + 1
            i += 1

    return m

if __name__ == '__main__':
    n = int(input())

    gene = input()

    result = steadyGene(gene)
    print(result)

