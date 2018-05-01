from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv"
               ).read().decode('ascii', 'ignore')
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)


for row in dictReader:
    print("The album \"" + row["Name"] + "\" was released in " + str(row["Year"]))

# print(dictReader.fieldnames)
# for row in dictReader:
#     print(row)