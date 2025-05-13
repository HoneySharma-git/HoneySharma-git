### File REad write and error handlingTask 8 ###


with open("output.txt", "a") as file:
     inputdata = input("Enter your data")
     file.write(inputdata)
     print("Enter additional data")
     inputdata = input("Enter your data")
     file.write('\n'+inputdata)
     print("Data has been added")
     file.close()
     file1=open('output.txt','r')
     reading_file = file1.read()
     print('\n'+reading_file)
     file1.close()



#