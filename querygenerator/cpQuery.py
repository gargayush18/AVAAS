# Program to extract a particular row value

import openpyxl 
import random
from datetime import datetime, timedelta
  
# Give the location of the file 

  
# workbook object is created 
  
# Loop will print all columns name 

path = "ongoing_projects.xlsx"
wb_obj = openpyxl.load_workbook(path) 
  
sheet_obj = wb_obj.active 







mainans=""

xx=1 ;

for i in range(1,41):
	ans1=""
	ans2=""
	ans3=0
	ans4=""

	date='2020'+"-"+str(random.randint(1,12))+"-"+str(random.randint(1,30))
	lol= round(random.uniform(50.00, 150.00),2)

	for j in range(1,5):
		a = sheet_obj.cell(row = i, column = j).value

		if(j==1):
			ans1=a
		
		if(j==2):
			ans2=a
		
		if(j==3):
			ans3=int(a)
		
		if(j==4):
			ans4=a
		
		
		
	
	mainans+="INSERT INTO Completed_Projects VALUES('CP00"+str(xx)+"', '"+ans4+"', null, '"+ans1+"', '"+date+"', '"+ans2+"', "+str(ans3)+", "+str(lol)+");\n"
	xx+=1


    

print(mainans)
