#! /usr/bin/env python

import xlrd, re

hout = open("YeEtAl2016/YeEtAl2016.proc.txt", "w")

book = xlrd.open_workbook("YeEtAl2016/nm.4002-S7.xlsx")

main_sheet = book.sheet_by_index(0)

gene2type = {}
for row in range(2, main_sheet.nrows):
    gene = main_sheet.cell(row, 0).value

    print >> hout, gene


hout.close()


