import pandas
file1 = pandas.read_csv("<filepath_or_buffer>")
print (file1.head())
FinalPrint = file1[(file1['VARIABLE.lenght']>5) & (file1['VARIABLE.width']>3)]
print (FinalPrint)