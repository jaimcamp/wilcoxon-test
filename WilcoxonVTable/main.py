import math
import sys
sys.path.append('lib')
import vTable
import pTable
import matrixUtils
import calculateGraphs
import calculateApproximateTable

__author__ = 'stenver'

n = 10

vValuesFileName = 'vTable' + str(n) + '.txt'
pValuesFileName = 'pTable' + str(n) + '.txt'
gaussianPValuesFileName = 'gaussianPvalues' + str(n) + '.txt'

#Calculate the v and p tables. Create files
'''
vTable = vTable.calculate(n)

matrixUtils.show(vTable)
matrixUtils.write(vValuesFileName, vTable)

vTable = matrixUtils.read(vValuesFileName)
pTable = pTable.calculate(vTable)
matrixUtils.show(pTable)
matrixUtils.write(pTable, pValuesFileName)
'''

#Read the already calculated files in
'''
gaussianPTable = matrixUtils.read(gaussianPValuesFileName)
pTable = matrixUtils.read(pValuesFileName)
'''

#Do various calculations or graphs on the tables
'''
(table1, table2) = findWhenGaussianIsEffective(pTable, gaussianPTable)
table = findHighestApproximationError(pTable, gaussianPTable)
printHighestApproxPTable(table)

calculateGraphs.printPvsPdata(pTable, gaussianPTable, 50)
calculateGraphs.printPvsPdata(pTable, gaussianPTable, 25)

matrixUtils.read(vValuesFileName, vTable)
calculateVtableStandardDeviations(vTable)

calculateGraphs.printDifference(pTable, gaussianPTable, 49)
calculateGraphs.printPandPapprox(pTable, gaussianPTable, 30)

printKRelativeValues(499, pTable, gaussianPTable)
approximateTable = calculateApproximateTable.calculateApproximateTable(pTable, gaussianPTable)
calculateApproximateTable.writeApproximateTableFile(approximateTable, n)
'''
