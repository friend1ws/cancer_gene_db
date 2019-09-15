#! /usr/bin/env python

from __future__ import print_function
import xlrd, re

hOUT = open("LawrenceEtAl2014/LawrenceEtAl2014.proc.txt", "w")

book = xlrd.open_workbook("LawrenceEtAl2014/nature12912-s3.xlsx")

main_sheet = book.sheet_by_index(0)

gene2type = {}
for row in range(2, main_sheet.nrows):
    gene = main_sheet.cell(row, 0).value.encode('ascii', 'ignore')
    if gene != "":
        if gene not in gene2type:
            gene2type[gene] = "PANCAN"
        else:
            gene2type[gene] = gene2type[gene] + ';' + "PANCAN"


book = xlrd.open_workbook("LawrenceEtAl2014/nature12912-s4.xlsx")
main_sheet = book.sheet_by_index(0)

for row in range(1, main_sheet.nrows):

    type = main_sheet.cell(row, 1).value.encode('ascii', 'ignore')
    genes1 = main_sheet.cell(row, 3).value.encode('ascii', 'ignore').split(',')
    genes2 = main_sheet.cell(row, 4).value.encode('ascii', 'ignore').split(',')

    for gene in genes1 + genes2:
        if gene == "": continue
        match = re.search(r'([\w\-]+) \(\d+', gene)
        mgene = match.group(1)
        if mgene not in gene2type:
            gene2type[mgene] = type
        else:
            gene2type[mgene] = gene2type[mgene] + ';' + type


for gene in sorted(gene2type):
    print(gene + '\t' + gene2type[gene], file = hOUT)

hOUT.close()
