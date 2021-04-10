# Program to extract a particular row value

import openpyxl 
import random
  
mainans=""

# for i in range(1,32):
# 	x = random.randint(1,2)
# 	gt= ""
# 	if ( x==2):
# 		gt="YES"
# 	else:
# 		gt="NO"
# 	mainans+="INSERT INTO contractor_competency VALUES('Cont00"+str(i)+"',"+str(random.randint(5,20))+","+str(random.randint(10,40))+",'"+gt+"');\n"
# # Give the location of the file 




for i in range(1,41):
	x = random.randint(1,2)
	gt= ""
	if ( x==2):
		gt="YES"
	else:
		gt="NO"
	mainans+="INSERT INTO project_requirements VALUES('ONGP00"+str(i)+"',"+str(random.randint(5,20))+",'"+gt+"',"+str(random.randint(50,200 ))+","+str(random.randint(10,40))+");\n"


  
# workbook object is created 
  
# Loop will print all columns name 



print(mainans)



