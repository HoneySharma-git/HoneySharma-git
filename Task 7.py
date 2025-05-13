### File REad write and error handlingTask 7 ###
from asyncore import write
from sre_constants import error


try:
    file1 = open('sample.txt', 'w')
    file2=file1.write("Line 1:This is a sample text file"+"\n"+"Line2 : It contains multiple lines")
    file1 = open('sample.txt', 'r')
    reading_file =  file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError :
    print("Error :Sample.txt File not found")



#