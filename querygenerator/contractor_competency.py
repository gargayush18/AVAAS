# Program to extract a particular row value

import openpyxl 
import random

def givedate():
	return str(random.randint(2019,2021))+"-"+str(random.randint(1,12))+"-"+str(random.randint(1,28))
  
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




# for i in range(1,41):
# 	x = random.randint(1,2)
# 	gt= ""
# 	if ( x==2):
# 		gt="YES"
# 	else:
# 		gt="NO"
# 	mainans+="INSERT INTO project_requirements VALUES('ONGP00"+str(i)+"',"+str(random.randint(5,20))+",'"+gt+"',"+str(random.randint(50,200 ))+","+str(random.randint(10,40))+");\n"

# for i in range(1,58):
# 	x = random.randint(1,3)
# 	gt= ""
# 	if ( x==2):
# 		gt="A"
# 	if ( x==1):
# 		gt="B"
# 	if( x==3):
# 		gt="C"
# 	mainans+="INSERT INTO public_competence VALUES('PUB00"+str(i)+"','"+gt+"',"+str(x)+",'"+"YES"+"'"+");\n"

for i in range(11,58):
	chance = random.randint(1,3)
	arr = []
	for j in range(chance):
		house_no=random.randint(6,32)
		while( house_no in arr ):
			house_no= random.randint(6,32)
		arr.append(house_no)
		
		
	
		gt=givedate()
	
		mainans+="INSERT INTO house_applicants VALUES('PUB00"+str(i)+"','CP00"+str(house_no)+"','Under review','"+gt+"'"+");\n"
  
# workbook object is created 
  
# Loop will print all columns name 



print(mainans)



