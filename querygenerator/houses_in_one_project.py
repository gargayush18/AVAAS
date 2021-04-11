# Program to extract a particular row value

import openpyxl 
import random
from datetime import datetime, timedelta
  
# Give the location of the file 

  
# workbook object is created 
  
# Loop will print all columns name 

path = "ongoing_projects1.xlsx"
wb_obj = openpyxl.load_workbook(path) 
  
sheet_obj = wb_obj.active 



#INSERT INTO ongoing_projects VALUES('CP001', 'GOVT006', null, 'Godrej Prime', '2020-02-25', 'AGRA', 28, 123.56);



mainans=""

xx=1 ;

for i in range(1,41):

	k=0
	if(i<=10):
	
		k=2
	
	elif(i>10 and i<=20):
		k=3
	elif(i>20 and i<=30):
		k=4
	else:
		k=5	

	xy=i

	for j in range(k):
		mainans+="INSERT INTO houses_in_one_project VALUES('HP00"+str(xx)+"', 'CP00"+str(xy)+"', 'NO', null);\n"

		xx+=1
		
		
		
		
	
	xx=1


    

print(mainans)
