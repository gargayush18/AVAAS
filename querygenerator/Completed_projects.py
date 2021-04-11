# Program to extract a particular row value

import openpyxl 
import random
from datetime import datetime, timedelta
  
# Give the location of the file 

  
# workbook object is created 
  
# Loop will print all columns name 

path = "Completed_Projetcs.xlsx"
wb_obj = openpyxl.load_workbook(path) 
  
sheet_obj = wb_obj.active 



#INSERT INTO ongoing_projects VALUES('CP001', 'GOVT006', null, 'Godrej Prime', '2020-02-25', 'AGRA', 28, 123.56);



mainans=""

xx=1 ;

for i in range(1,41):
	ans1=""
	ans2=""
	

	date='2020'+"-"+str(random.randint(1,12))+"-"+str(random.randint(1,30))
	lol= round(random.uniform(50.00, 150.00),2)

	for j in range(1,3):
		a = sheet_obj.cell(row = i, column = j).value

		if(j==1):
			ans1=a
		
		if(j==2):
			ans2=a
		
		
		
		
		
	
	mainans+="INSERT INTO Completed_Projects VALUES('CP00"+str(xx)+"', 'GOVT00"+str(random.randint(1,6))+"', 'Cont00"+str(random.randint(1,31))+"', '"+ans1+"', '"+date+"', '"+ans2+"', "+str(random.randint(25,60))+", "+str(lol)+");\n"
	xx+=1


    

print(mainans)
