#! /usr/bin/env python

hout = open("CancerGeneCensus/CancerGeneCensus.proc.txt", "w")

with open("CancerGeneCensus/Census_allWed Nov  4 06_55_16 2015.tsv.txt", 'r') as hin:
    for line in hin:
        F = line.rstrip('\n').split('\t')
        if F[0].startswith("Gene"): continue
        print >> hout, F[0] + '\t' + F[12]

hout.close()
