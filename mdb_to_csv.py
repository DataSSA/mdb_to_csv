
#Open a terminal

#Install mdbtools 

pip install mdbtools
pip install --upgrade pip

#in the specific location of .mdb files, in my case was

home/Docs$ mbd- # +[tab]

#its suppose to output a list of mbdTools


home/Docs$ mdb-tables 'file.mdb'

#its suppose to print the name of tables inside the file


home/Docs$ mdb-export 'file.mdb' 'name_of_table' > 'file.csv'

#and this is what we are looking for: take all data inside the .mdb and 
#put in the exactly same order in a .csv file, then save it. 

#Now you got a .csv file with all data for be completly examinated by fisical #observation and pandas at least, wich in my case was enought. 
