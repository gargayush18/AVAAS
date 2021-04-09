# Program to extract a particular row value

import openpyxl 
import random
  
# Give the location of the file 

  
# workbook object is created 
  
# Loop will print all columns name 

path = "financial_customer.xlsx"
wb_obj = openpyxl.load_workbook(path) 
  
sheet_obj = wb_obj.active 




#INSERT INTO loans VALUES(1,'Tapan Roy','SBI',4.8,'2016-12-14',500000.0,200000.0);
#INSERT INTO contractors VALUES (1,'Boris Singh','1960-01-01',12456889,50,'NO',null,null);

mainans=""

xx=1 ;
xy =  52; 
for i in range(1,130):
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
	
	ft = -1; 
	if( "bank" in ans or "govt" in ans  ):
		pass
	else:
		ft= random.randint(70,94)
	mainans+="INSERT INTO Financial_Customers VALUES('FICT00"+str(xx)+"',"+ans[:-1]+",true,"+str(ft)+");\n"
	xx+=1
	xy+=1

    

print(mainans)



