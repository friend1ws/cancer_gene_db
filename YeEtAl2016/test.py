#! /usr/bin/env python

import gzip

gene_symbol = []
with gzip.open("refGene.txt.gz", 'r') as hin:
    for line in hin:
        F = line.rstrip('\n').split('\t')
        if F[1].startswith("NR_"): continue
        gene_symbol.append(F[12])

gene_symbol = list(set(gene_symbol))

print '\n'.join(gene_symbol)

