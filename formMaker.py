#creating Database
project = {}
component= {}
#importing xlrd to open excel files
import xlrd

#Opening spreadsheet file
workbook = xlrd.openworkbook('DB2018.xls')
sheet1 = workbook.sheet_by_index(1)
sheet2 = workbook.sheet_by_index(2)

#getting data from cells and placing data in database

#project Database
for i in range(21)
partNo = sheet.cell(i,0).value
projectName = sheet.cell(i,1)
count = 0
project[partNo] = projectName

#component Database
for i in range(21)
partNo = sheet.cell(i,0).value
projectName = sheet.cell(i,1)
count = 0
project[partNo] = projectName


# Write Document