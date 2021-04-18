from flask import Flask, render_template, url_for, request, redirect
import mysql.connector
import queries
username=""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ishu@123",
  database='AVAAS2'
)
mycursor = mydb.cursor()
app = Flask(__name__)

@app.route('/' , methods=['POST','GET'])
def index():
    if request.method=='POST': 
        task_content = request.form['content']
        hje=task_content
        global username
        username= task_content
        print(task_content)
        if task_content[0:3]=="BNK":
            return render_template('finance.html', hje = hje )
        if task_content[0:4]=="Cont":
            return render_template('contractor.html', hje= hje )
        if task_content[0:4]=="GOVT":
            return render_template('govt.html', hje= hje )
        if task_content[0:3]=="PUB":
            return render_template('public.html',hje=hje)
            


    else:
        return render_template('signin.html')



    
################################################Government#########################################################




@app.route('/govt' , methods=['POST','GET'])
def add_projects():
    if request.method=='POST':
        if request.form['submit_button'] == 'Add new project':
            return render_template('newproject.html')
        if request.form['submit_button'] == 'View ongoing projects':
            return render_template('ongoingProj1.html', projects=[])
        if request.form['submit_button'] == 'View completed projects':

            mycursor.execute("SELECT DISTINCT cp.name AS 'Project Name', c.contractor_name AS 'Project Contractor', COUNT(project_id) AS 'No. of Houses' FROM Completed_Projects cp INNER JOIN contractors c ON cp.p_contractor_id = c.contractor_id INNER JOIN houses_in_one_project h ON cp.completed_project_id = h.project_id WHERE govt_add_id=%s GROUP BY(project_id)",(username,))
            data = mycursor.fetchall()
            return render_template('view_completed.html', value=data)
        if request.form['submit_button'] == 'Check for the transactions':
            return render_template('transaction_govt_cover.html')



@app.route('/ongoingProj' , methods=['POST','GET'])
def ongoing_Govt():
    if request.method=='POST':
        if request.form['submit_button'] == 'View Upcoming Projects':
            mycursor.execute("SELECT name AS 'Project Name',location AS 'Location',size AS 'size' FROM ongoing_projects WHERE assigned='NO'AND govt_add_id=%s",(username,))
            data = mycursor.fetchall()
            return render_template('UpcomingGovt.html', value=data)
        if request.form['submit_button'] == 'View Live Projects':
            mycursor.execute("SELECT op.name AS 'Project Name', op.completion_percentage AS 'Project Completion', c.contractor_name AS 'Assigned Contractor' FROM ongoing_projects op JOIN contractors c ON op.p_contractor_id = c.contractor_id AND op.govt_add_id=%s",(username,))
            data = mycursor.fetchall()
            return render_template('LiveGovt.html', value=data)





@app.route('/govt_transc' , methods=['POST','GET'])
def govt_transactions():
    if request.method=='POST':
        if request.form['submit_button'] == 'House Payments from Public':
            mycursor.execute(    "SELECT t.date_of_transaction AS 'Date of Transaction', t.sender_id AS 'Sender ID', g.govt_name AS 'Govt. Name', t.receiver_id AS 'Public ID', fc.name AS 'Public Name', t.amount as 'Amount' FROM Transactions t INNER JOIN Government g ON t.receiver_id = g.f_customer_id INNER JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id WHERE govt_id =%s",(username,))
            data = mycursor.fetchall()
            return render_template('Govt_Transac_Public.html', value=data)
        if request.form['submit_button'] == 'Payments to Contractors':
            mycursor.execute(

            "SELECT t.date_of_transaction AS 'Date of Transaction', t.sender_id AS 'Sender ID', g.govt_name AS 'Govt. Name', t.receiver_id AS 'Contractor ID', fc.name AS 'Contractor Name', t.amount as 'Amount' FROM Transactions t INNER JOIN Government g ON t.sender_id = g.f_customer_id INNER JOIN Financial_Customers fc ON t.receiver_id = fc.f_customer_id WHERE govt_id =%s",(username,)
            )
            data = mycursor.fetchall()
            return render_template('Govt_Transac_Contr.html', value=data)


@app.route('/transactionfilterGovtCon' , methods=['POST','GET'])
def govt_transactions1():
    if request.method=='POST':
        if request.form['submit_button'] == 'Sort by date':
            mycursor.execute(    "SELECT t.date_of_transaction AS 'Date of Transaction', t.sender_id AS 'Sender ID', g.govt_name AS 'Govt. Name', t.receiver_id AS 'Contractor ID', fc.name AS 'Contractor Name', t.amount as 'Amount' FROM Transactions t INNER JOIN Government g ON t.sender_id = g.f_customer_id INNER JOIN Financial_Customers fc ON t.receiver_id = fc.f_customer_id WHERE govt_id =%s ORDER BY t.date_of_transaction",(username,))
            data = mycursor.fetchall()
            return render_template('Govt_Transac_Contr.html', value=data)
        if request.form['submit_button'] == 'Sort by amount':
            mycursor.execute(    "SELECT t.date_of_transaction AS 'Date of Transaction', t.sender_id AS 'Sender ID', g.govt_name AS 'Govt. Name', t.receiver_id AS 'Contractor ID', fc.name AS 'Contractor Name', t.amount as 'Amount' FROM Transactions t INNER JOIN Government g ON t.sender_id = g.f_customer_id INNER JOIN Financial_Customers fc ON t.receiver_id = fc.f_customer_id WHERE govt_id =%s ORDER BY t.amount",(username,))
            data = mycursor.fetchall()
            return render_template('Govt_Transac_Contr.html', value=data)


            #Other 2 sortings left
@app.route('/transactionfilterGovtPub' , methods=['POST','GET'])
def govt_transactions2():
    if request.method=='POST':
        if request.form['submit_button'] == 'Sort by date':
            mycursor.execute(    "SELECT t.date_of_transaction AS 'Date of Transaction', t.sender_id AS 'Sender ID', g.govt_name AS 'Govt. Name', t.receiver_id AS 'Public ID', fc.name AS 'Public Name', t.amount as 'Amount' FROM Transactions t INNER JOIN Government g ON t.receiver_id = g.f_customer_id INNER JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id WHERE govt_id =%s ORDER BY t.date_of_transaction",(username,))
            data = mycursor.fetchall()
            return render_template('Govt_Transac_Public.html', value=data)
        if request.form['submit_button'] == 'Sort by amount':
            mycursor.execute(    "SELECT t.date_of_transaction AS 'Date of Transaction', t.sender_id AS 'Sender ID', g.govt_name AS 'Govt. Name', t.receiver_id AS 'Public ID', fc.name AS 'Public Name', t.amount as 'Amount' FROM Transactions t INNER JOIN Government g ON t.receiver_id = g.f_customer_id INNER JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id WHERE govt_id =%s ORDER BY t.amount",(username,))
            data = mycursor.fetchall()
            return render_template('Govt_Transac_Public.html', value=data)



            #Other 2 sortings left


          
          
          

@app.route('/newproject' , methods=['POST','GET'])
def finaliseprojects():
    if request.method=='POST': 
        if request.form['submit_button'] == 'finalisedetails':
            return render_template('govt.html', hje= "New project Added")
          
          
@app.route('/complaintssort' , methods=['POST','GET'])
def complaintssort():
    if request.method=='POST': 
        if request.form['submit_button'] == 'Filter by Name':
            task_content = request.form['projectname']
            print( task_content)
            mycursor.execute('Select name, actual_query, date_posted  , resolved from completed_projects , 	queries  where name="'+ task_content + '" AND queries.project_id=completed_project_id  And resolved = "No" AND  p_contractor_id="'+username+'"') 
            data = mycursor.fetchall() #data from database 


            return render_template('complaints.html',value = data,  hje= "New project Added")
        

        if request.form['submit_button'] == 'Sort by Date':
            
            
            mycursor.execute('Select name, actual_query, date_posted  , resolved from completed_projects , 	queries  where  queries.project_id=completed_project_id  And resolved = "No" AND  p_contractor_id="'+username+'" order by(date_posted)') 
            data = mycursor.fetchall() #data from database 


            return render_template('complaints.html',value = data,  hje= "New project Added")    
    
          
            
@app.route('/viewproject/<int:id>',)
def update(id):
    # // get the project details using this id
    # // display the project details here
    #// i have removed the for loop in the parent page 
    print( "cxnhfjd"+ str(id))
    return render_template('projectdetails_ongoing.html')

  
  
  
  ######### Government Over ###########
          
          
          
          
          
          
          
          
          
          
          
          
          
          
@app.route('/fin_insti' , methods=['POST','GET'])
def do_something():
    if request.method=='POST': 
        if request.form['submit_button'] == 'View lender details':
            mycursor.execute("select * from loans where id_lender ='"+ username + "'" )  
            data = mycursor.fetchall()
            mycursor.execute("select COUNT(borrower) from loans where id_lender ='"+ username + "'" )  
            dat = mycursor.fetchall()
            return render_template('FIlenderdetails.html', value=data, val2 = dat)

        if request.form['submit_button'] == 'Check Interested Contractors':
            mycursor.execute("select  c.contractor_name , c.competency_score from loan_applicants l  Join Contractors c  ON c.f_customer_id= l.f_customer_id  Join loans_offered o  ON o.loan_offer_id = l.loan_id Where  o.f_institution_id='"+username+"'")
            data = mycursor.fetchall()
            return render_template('FIcontractorCompetency.html', value=data)

        if request.form['submit_button'] == 'Check Intetested Public':
            mycursor.execute("select  c.name , c.competence_score from loan_applicants l  Join public c  ON c.f_customer_id= l.f_customer_id  Join loans_offered o   ON o.loan_offer_id = l.loan_id Where  o.f_institution_id='"+username+"'")

            
            data = mycursor.fetchall()
            return render_template('FIprojectimpact.html', value=data)

        if request.form['submit_button'] == 'Check payments':
            mycursor.execute("select f_customer_id from Banks where f_institution_id=%s",(username,))
            val=mycursor.fetchall() 
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            mycursor.execute("SELECT   t. id_transaction , t.date_of_transaction, t.sender_id, fc.name , t.receiver_id, fd.name , t.amount FROM Transactions t JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id JOIN Financial_Customers fd ON t.receiver_id= fd.f_customer_id where   sender_id= '" +f_cust_id +"'or receiver_id= '" +f_cust_id + "'")

            data = mycursor.fetchall()
            print( data)




            return render_template("transaction_page_user.html",value=data)
        



# not maded the functions for implement this       

        





####################Contractors#####################

@app.route('/notdecided' , methods=['POST','GET'])
def decided():
    if request.method=='POST': 
        task_content= request.form['Projectname']
        mycursor.execute(   'Select name, location , bid_value , application_time , application_status from project_applicants , 	ongoing_projects   where project_applicants.ongoing_project_id=ongoing_projects.ongoing_project_id     AND project_applicants.p_contractor_id="'+username + '" AND name = "' + task_content + '"') 
        data = mycursor.fetchall() #data from database 
        return render_template('bidstatus.html',value=data)





        

    





@app.route('/banksot' , methods=['POST','GET'])
def banksot():
    if request.method=='POST': 
        if request.form['submit_button'] == 'Fiter by ROI ':
            mycursor.execute("SELECT loan_offer_id,name,ROI,max_loan_amount,max_duration,no_of_installments FROM loans_offered INNER JOIN Banks ON loans_offered.f_institution_id=Banks.f_institution_id WHERE loan_type='contractor'order by(ROI)") 
            data = mycursor.fetchall() #data from database 
            return render_template('bankpagecont.html',value=data)
        if request.form['submit_button'] == 'Filter by Amount  ':
            mycursor.execute("SELECT loan_offer_id,name,ROI,max_loan_amount,max_duration,no_of_installments FROM loans_offered INNER JOIN Banks ON loans_offered.f_institution_id=Banks.f_institution_id WHERE loan_type='contractor'order by(max_loan_amount)") 
            data = mycursor.fetchall() #data from database 
            return render_template('bankpagecont.html',value=data)
        if request.form['submit_button'] == 'Filter by time':
            mycursor.execute("SELECT loan_offer_id,name,ROI,max_loan_amount,max_duration,no_of_installments FROM loans_offered INNER JOIN Banks ON loans_offered.f_institution_id=Banks.f_institution_id WHERE loan_type='contractor'order by(max_duration)") 
            data = mycursor.fetchall() #data from database 
            return render_template('bankpagecont.html',value=data)
        if request.form['submit_button'] == 'Calculate maximum future value':
            mycursor.execute("SELECT loan_offer_id,name,ROI,max_loan_amount,max_duration,no_of_installments FROM loans_offered INNER JOIN Banks ON loans_offered.f_institution_id=Banks.f_institution_id WHERE loan_type='contractor' order by(no_of_installments)") 
            data = mycursor.fetchall() #data from database 
            return render_template('bankpagecont.html',value=data)


@app.route('/contractortransact' , methods=['POST','GET'])
def contractortransact():
    if request.method=='POST': 
        if request.form['submit_button'] == 'General Payments':
            mycursor.execute("select f_customer_id from contractors where contractor_id=%s",(username,))
            val=mycursor.fetchall() 
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            mycursor.execute("SELECT   t. id_transaction , t.date_of_transaction, t.sender_id, fc.name , t.receiver_id, fd.name , t.amount FROM Transactions t JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id JOIN Financial_Customers fd ON t.receiver_id= fd.f_customer_id where  transaction_type = 'general' AND (sender_id= '" +f_cust_id +"'or receiver_id= '" +f_cust_id + "')")

            data = mycursor.fetchall()
            print( data)
            return render_template("transaction_page_user.html",value=data)

    if request.method=='POST': 
        if request.form['submit_button'] == 'Check my loan payments':
            mycursor.execute("select f_customer_id from contractors where contractor_id=%s",(username,))
            val=mycursor.fetchall() 
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            
            mycursor.execute("SELECT   t. id_transaction , t.date_of_transaction, t.sender_id, fc.name , t.receiver_id, fd.name , t.amount FROM Transactions t JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id JOIN Financial_Customers fd ON t.receiver_id= fd.f_customer_id where  transaction_type = 'loan_payment' AND (sender_id= '" +f_cust_id +"'or receiver_id= '" +f_cust_id + "')")

            da = mycursor.fetchall()
            mycursor.execute("select  *  from loans where id_borrower='"+ f_cust_id+ "'")
            data = mycursor.fetchall()
            print( data)
            if ( len( data)==0):
                data=["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", ]

            

            print( da)
            return render_template("loan.html",value=da, val2= data[0] )
            
            
            
            










@app.route('/contractor' , methods=['POST','GET'])
def search_projects():
    if request.method=='POST': 
        if request.form['submit_button'] == 'Search for projects':
            mycursor.execute('select name, location , size , ongoing_project_id  from ongoing_projects where assigned="NO"') 
            
            data = mycursor.fetchall() #data from database 
            
            return render_template('projectsearch.html', value = data)
        if request.form['submit_button'] == "Search for Banks":
            mycursor.execute("SELECT loan_offer_id,name,ROI,max_loan_amount,max_duration,no_of_installments FROM loans_offered INNER JOIN Banks ON loans_offered.f_institution_id=Banks.f_institution_id WHERE loan_type='contractor'") 
            data = mycursor.fetchall() #data from database 
            return render_template('bankpagecont.html',value=data)
        if request.form['submit_button'] == "Check Complaints":
            mycursor.execute('Select name, actual_query, date_posted  , resolved from completed_projects , 	queries  where queries.project_id=completed_project_id  And resolved = "No" AND  p_contractor_id="'+username+'"') 
            data = mycursor.fetchall() #data from database 
            return render_template('complaints.html',value=data)
        if request.form['submit_button'] == "Check Bid status":
            mycursor.execute(   'Select name, location , bid_value , application_time , application_status from project_applicants , 	ongoing_projects   where project_applicants.ongoing_project_id=ongoing_projects.ongoing_project_id  AND project_applicants.p_contractor_id="'+username + '"') 
            data = mycursor.fetchall() #data from database 
            return render_template('bidstatus.html',value=data)

            


        if request.form['submit_button'] == 'Check for the transactions':
            return render_template('Contractorpayments.html')
            
        
        
        
        
        
        
        
        if request.form['submit_button'] == 'Current project':
            mycursor.execute('Select * from ongoing_projects where p_contractor_id="' + username + '"') 

            data = mycursor.fetchall() #data from database 
            print ( data)
            if ( len( data) ==0 ):
                dat = "Oho! you have no current project going on"
            else:
                dat= "\nName =" + str(data[0][3])+  " \nLocation  =" + str(data[0][4])+ "\n Size  =" +str( data[0][5])+   "\n Completion Percentage  =" + str(data[0][6])
                mycursor.execute('Select * from supplies where project_supplies_id="' + data[0][0] + '"') 
                da = mycursor.fetchall() #data from database 
                dat= dat +" \n Supplies Data \n"
                dat= dat +"Material Cost  " + str(da[0][1]) + "Crs..\n"
                dat= dat +"Labour Cost  " + str(da[0][2]) + "Crs..\n"
                dat= dat +"Engineers Cost  " + str(da[0][2]) + "Crs..\n"
                


                
                
    
                

            print( dat)

            return render_template('freepage.html', value = dat)

@app.route('/finalbid' , methods=['POST','GET'])

def thisfunc():
    if request.method=='POST': 
        task_content= request.form['bidvalue']
        # mycursor.execute("INSERT INTO project_applicants VALUES(" + "'"+username+"',"+  "'"+idd+"',"+" 'Under review','2021-05-29 23:39:36',16.14);") 
        
        
@app.route('/projectsort' , methods=['POST','GET'])
def sortproject():
    if request.method=='POST':
        if request.form['submit_button'] == 'Filter by location': 
            
            task_content = request.form['locname']
            
            mycursor.execute('select name, location , size , ongoing_project_id  from ongoing_projects where assigned="NO" AND location= "'+ task_content+'"' ) 
            
            data = mycursor.fetchall() #data from database 
            return render_template('projectsearch.html',value=data)





@app.route('/putbid/<id>',)
def display_project_bid(id):
    # // get the project details using this id
    # // display the project details here
    #// i have removed the for loop in the parent page 
    print( "cxnhfjd"+ str(id))
    global idd
    print (id)
    idd = id 

    mycursor.execute('select *  from project_requirements where project_req_id ='+"'"+ idd +"'" ) 
    data = mycursor.fetchall() #data from database 
    
    mycursor.execute('select *  from contractor_competency where c_competency_id ='+"'"+ username +"'" ) 
    dataf = mycursor.fetchall() #data from database 
    print(dataf)
    insp= "No"
    if ( dataf[0][1]>= data[0][1]  and dataf[0][2]>= data[0][4]):
        if( data[0][2]=="NO"):
            insp="Yes"
        if( dataf[0][3]==data[0][2]):
            insp="Yes"
    


    return render_template('bidpage.html' , value = data , val2 = insp) 







####################General Public #####################

@app.route('/public' , methods=['POST','GET'])
def handle_public_queries():
    if request.method=='POST': 
        if request.form['submit_button'] == 'Search for Houses':
            mycursor.execute("select * from Completed_Projects") 
            data = mycursor.fetchall() #data from database 
            return render_template('house_search.html',value=data)
        if request.form['submit_button'] == 'Search for Banks':
            mycursor.execute("SELECT loan_offer_id,name,ROI,max_loan_amount,max_duration,no_of_installments FROM loans_offered INNER JOIN Banks ON loans_offered.f_institution_id=Banks.f_institution_id WHERE loan_type='public'") 
            data = mycursor.fetchall() #data from database 
            return render_template('bankpage.html',value=data)
        if request.form['submit_button'] == 'Search for the home requests status':
            print("hellp i m clicked")
            print(username,'ghghg')
            mycursor.execute("SELECT * FROM house_applicants WHERE public_id=%s",(username,) )
            data = mycursor.fetchall()
            return render_template('homerequeststatus.html',value=data)
        if request.form['submit_button'] == 'My home':
            return render_template('myhome.html')
        if request.form['submit_button'] == 'Check for the transactions':
            return render_template('publicpayments.html')
        if request.form['submit_button'] == 'Check Loan Application Status':
            mycursor.execute("select f_customer_id from Public where public_id=%s",(username,))
            val=mycursor.fetchall()
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            mycursor.execute("SELECT * FROM loan_applicants WHERE (f_customer_id=%s)",(f_cust_id,)) 
            data = mycursor.fetchall()
            return render_template('loanrequeststatus.html',value=data)
        
@app.route('/banksort' , methods=['POST','GET'])
def banksort():
    if request.method=='POST': 
        if request.form['submit_button'] == 'Fiter by ROI ':
            mycursor.execute("SELECT loan_offer_id,name,ROI,max_loan_amount,max_duration,no_of_installments FROM loans_offered INNER JOIN Banks ON loans_offered.f_institution_id=Banks.f_institution_id WHERE loan_type='public'order by(ROI)") 
            data = mycursor.fetchall() #data from database 
            return render_template('bankpage.html',value=data)
        if request.form['submit_button'] == 'Filter by Amount  ':
            mycursor.execute("SELECT loan_offer_id,name,ROI,max_loan_amount,max_duration,no_of_installments FROM loans_offered INNER JOIN Banks ON loans_offered.f_institution_id=Banks.f_institution_id WHERE loan_type='public'order by(max_loan_amount)") 
            data = mycursor.fetchall() #data from database 
            return render_template('bankpage.html',value=data)
        if request.form['submit_button'] == 'Filter by time':
            mycursor.execute("SELECT loan_offer_id,name,ROI,max_loan_amount,max_duration,no_of_installments FROM loans_offered INNER JOIN Banks ON loans_offered.f_institution_id=Banks.f_institution_id WHERE loan_type='public'order by(max_duration)") 
            data = mycursor.fetchall() #data from database 
            return render_template('bankpage.html',value=data)
        if request.form['submit_button'] == 'Calculate maximum future value':
            mycursor.execute("SELECT loan_offer_id,name,ROI,max_loan_amount,max_duration,no_of_installments FROM loans_offered INNER JOIN Banks ON loans_offered.f_institution_id=Banks.f_institution_id WHERE loan_type='public' order by(no_of_installments)") 
            data = mycursor.fetchall() #data from database 
            return render_template('bankpage.html',value=data)

@app.route('/housesort' , methods=['POST','GET'])
def housesort():
    if request.method=='POST':
        if request.form['submit_button'] == 'Filter by location': 
            task_content = request.form['locname']
            print(task_content)
            mycursor.execute("select * from Completed_Projects where (location= %s)",(task_content,)) 
            print("select * from Completed_Projects where (location= %s)",(task_content,))
            data = mycursor.fetchall() #data from database 
            return render_template('house_search.html',value=data)
        if request.form['submit_button'] == 'Apply for the entered house': 
            task_content = request.form['projectid']
            print(task_content)
            print(username)
            mycursor.execute("insert into house_applicants values(%s,%s,'Under review','2021-03-21')",(username,task_content,)) 
            mydb.commit()
            mycursor.execute("select * from Completed_Projects") 
            data = mycursor.fetchall() #data from database 
            return render_template('house_search.html',value=data)
        
    







@app.route('/housequery/<int:id>',)
def displayhouseinfo(id):
    # // get the project details using this id
    # // display the project details here
    #// i have removed the for loop in the parent page 
    print( "cxnhfjd"+ str(id))
    return render_template('publi_home_requiremnts.html')


@app.route('/publictransact' , methods=['POST','GET'])
def publicpayments():
    if request.method=='POST': 
        if request.form['submit_button'] == 'Check my House payments':
            mycursor.execute("select f_customer_id from Public where public_id=%s",(username,))
            val=mycursor.fetchall() 
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            mycursor.execute("SELECT   t. id_transaction , t.date_of_transaction, t.sender_id, fc.name , t.receiver_id, fd.name , t.amount FROM Transactions t JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id JOIN Financial_Customers fd ON t.receiver_id= fd.f_customer_id where  transaction_type = 'general' AND sender_id= '" +f_cust_id +"'or receiver_id= '" +f_cust_id + "'")

            data = mycursor.fetchall()
            print( data)
            return render_template("view_transactions.html",value=data)
        
        
        
        
        if request.form['submit_button'] == 'Check my loan payments':
            mycursor.execute("select f_customer_id from Public where public_id=%s",(username,))
            val=mycursor.fetchall() 
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            mycursor.execute("SELECT   t. id_transaction , t.date_of_transaction, t.sender_id, fc.name , t.receiver_id, fd.name , t.amount FROM Transactions t JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id JOIN Financial_Customers fd ON t.receiver_id= fd.f_customer_id where  transaction_type = 'loan_payment' AND sender_id= '" +f_cust_id +"'or receiver_id= '" +f_cust_id + "'")
            val=mycursor.fetchall()
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            mycursor.execute("SELECT * FROM Transactions WHERE (transaction_type='loan_payment' and (sender_id=%s or receiver_id=%s))",(f_cust_id,f_cust_id,)) 
            data = mycursor.fetchall()
            return render_template("loan.html",value=data)
        
@app.route('/transactionfilter' , methods=['POST','GET'])
def sortpublicpayments():
    if request.method=='POST': 
        if request.form['submit_button'] == 'Sort by date':
            mycursor.execute("select f_customer_id from Public where public_id=%s",(username,))
            val=mycursor.fetchall()
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            mycursor.execute("SELECT * FROM Transactions WHERE (transaction_type='general' and (sender_id=%s or receiver_id=%s)) order by(date_of_transaction)",(f_cust_id,f_cust_id,)) 
            data = mycursor.fetchall()
            return render_template("view_transactions.html",value=data)
        if request.form['submit_button'] == 'sort by amount':
            mycursor.execute("select f_customer_id from Public where public_id=%s ",(username,))
            val=mycursor.fetchall()
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            mycursor.execute("SELECT * FROM Transactions WHERE (transaction_type='general' and (sender_id=%s or receiver_id=%s)) order by(amount)",(f_cust_id,f_cust_id,)) 
            data = mycursor.fetchall()
            return render_template("view_transactions.html",value=data)
@app.route('/transactionfilterloan' , methods=['POST','GET'])
def sortpublicloan():
    if request.method=='POST': 
        if request.form['submit_button'] == 'Sort by date':
            mycursor.execute("select f_customer_id from Public where public_id=%s",(username,))
            val=mycursor.fetchall()
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            mycursor.execute("SELECT * FROM Transactions WHERE (transaction_type='loan_payment' and (sender_id=%s or receiver_id=%s)) order by(date_of_transaction)",(f_cust_id,f_cust_id,)) 
            data = mycursor.fetchall()
            return render_template("loan.html",value=data)
        if request.form['submit_button'] == 'sort by amount':
            mycursor.execute("select f_customer_id from Public where public_id=%s ",(username,))
            val=mycursor.fetchall()
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            mycursor.execute("SELECT * FROM Transactions WHERE (transaction_type='loan_payment' and (sender_id=%s or receiver_id=%s)) order by(amount)",(f_cust_id,f_cust_id,)) 
            data = mycursor.fetchall()
            return render_template("loan.html",value=data)



if __name__ == '__main__':
    app.run(debug="true")
    
