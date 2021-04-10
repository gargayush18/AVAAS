# Program to extract a particular row value

import openpyxl 
import random
  
# Give the location of the file 

  
# workbook object is created 
  
# Loop will print all columns name 

path = "ongoing_projects.xlsx"
wb_obj = openpyxl.load_workbook(path) 
  
sheet_obj = wb_obj.active 




#INSERT INTO loans VALUES(1,'Tapan Roy','SBI',4.8,'2016-12-14',500000.0,200000.0);
#INSERT INTO contractors VALUES (1,'Boris Singh','1960-01-01',12456889,50,'NO',null,null);

mainans=""

xx=1 ;
xy =  52; 
for i in range(1,100):
	ans=""

	for j in range(1,3):
		cell_obj = sheet_obj.cell(row = i, column = j) 
		oho=cell_obj.value
		trr=oho
		oho= str(oho)
		if(isinstance(trr, int)):
			ans+=str(cell_obj.value)+","
		
		else:
			oho=oho.replace("\n"," ")
			oho=oho.replace("  ","")
			oho=oho.replace("00:00:00","")
			ans+="'"+str(oho)+"'"+","
	
	mainans+="INSERT INTO ongoing_projects VALUES('ONGP00"+str(xx)+"',null,'GOVT00"+str(random.randint(1,7))+"',"+ans[:-1]+","+str(random.randint(20,40))+",'NO',0 "+");\n"
	xx+=1
	xy+=1

    

print(mainans)



