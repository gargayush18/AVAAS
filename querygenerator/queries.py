# Program to extract a particular row value

import openpyxl 
import random
from datetime import datetime, timedelta
  
# Give the location of the file 

  
# workbook object is created 
  
# Loop will print all columns name 

path = "queries.xlsx"
wb_obj = openpyxl.load_workbook(path) 
  
sheet_obj = wb_obj.active 



#INSERT INTO ongoing_projects VALUES('CP001', 'GOVT006', null, 'Godrej Prime', '2020-02-25', 'AGRA', 28, 123.56);

#INSERT INTO queries VALUES('QR001', 'PUB001', 'CP001', 'xyzw', '2020-12-12','YES')


mainans=""

xx=1 
xy=1
xz=1

count=0
proj = 0

for i in range(1,121):
	
	date='2020'+"-"+str(random.randint(1,12))+"-"+str(random.randint(1,30))
	
	
	a = sheet_obj.cell(row = i, column = 1).value


	lol=random.randint(0,1)


	if(lol==0):
		p='YES'
	else:
		p='NO'	

	mainans+="INSERT INTO queries VALUES('QR00"+str(xy)+"', 'CP00"+str(xx)+"', 'PUB00"+str(random.randint(1,57))+"', '"+str(a)+"', '"+date+"', '"+p+"');\n"
	xy+=1


	if(i%3==0):
		xy=1
		xx+=1

print(mainans)	


