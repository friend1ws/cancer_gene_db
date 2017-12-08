#! /usr/bin/env python

import xlrd, re

hout = open("VogelsteinEtAl2013/VogelsteinEtAl2013.proc.txt", "w")

book = xlrd.open_workbook("VogelsteinEtAl2013/1235122TablesS1-4.xlsx")

main_sheet = book.sheet_by_index(5)

gene2type = {}
for row in range(2, main_sheet.nrows):
    gene = main_sheet.cell(row, 0).value
    if gene.startswith("*"): continue

    classification = main_sheet.cell(row, 5).value
    print >> hout, gene + '\t' + classification


hout.close()


