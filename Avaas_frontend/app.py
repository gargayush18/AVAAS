from flask import Flask, render_template, url_for, request, redirect
import mysql.connector
from datetime import datetime
import queries
username=""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ishu@123",
  database='AVAAS2',
  autocommit = True
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
def navigate():
    if request.method=='POST':
        if request.form['submit_button'] == 'Add new project':
            return render_template('newproject.html')
        if request.form['submit_button'] == 'View ongoing projects':
            return render_template('ongoingProj1.html', projects=[])
        if request.form['submit_button'] == 'View completed projects':

            mycursor.execute("SELECT DISTINCT cp.completed_project_id, cp.name AS 'Project Name', c.contractor_name AS 'Project Contractor', COUNT(project_id) AS 'No. of Houses' FROM Completed_Projects cp INNER JOIN contractors c ON cp.p_contractor_id = c.contractor_id INNER JOIN houses_in_one_project h ON cp.completed_project_id = h.project_id WHERE govt_add_id=%s GROUP BY(project_id)",(username,))
            data = mycursor.fetchall()
            return render_template('view_completed.html', value=data)
        if request.form['submit_button'] == 'Check for the transactions':
            return render_template('transaction_govt_cover.html')



@app.route('/ongoingProj' , methods=['POST','GET'])
def ongoing_Govt():
    if request.method=='POST':
        if request.form['submit_button'] == 'View Upcoming Projects':
            mycursor.execute("SELECT ongoing_project_id AS 'Project ID', name AS 'Project Name',location AS 'Location',size AS 'size' FROM ongoing_projects WHERE assigned='NO'AND govt_add_id=%s",(username,))
            data = mycursor.fetchall()
            return render_template('UpcomingGovt.html', value=data)
        if request.form['submit_button'] == 'View Live Projects':
            mycursor.execute("SELECT op.ongoing_project_id AS 'Project ID', op.name AS 'Project Name', op.completion_percentage AS 'Project Completion', c.contractor_name AS 'Assigned Contractor' ,c.contractor_id AS 'Contractor ID' FROM ongoing_projects op JOIN contractors c ON op.p_contractor_id = c.contractor_id AND op.govt_add_id=%s",(username,))
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
        if request.form['submit_button'] == 'Filter by Receiver id':
            content = request.form['receiver_id']
            print(content)
            mycursor.execute("SELECT t.date_of_transaction AS 'Date of Transaction', t.sender_id AS 'Sender ID', g.govt_name AS 'Govt. Name', t.receiver_id AS 'Contractor ID', fc.name AS 'Contractor Name', t.amount as 'Amount' FROM Transactions t INNER JOIN Government g ON t.sender_id = g.f_customer_id INNER JOIN Financial_Customers fc ON t.receiver_id = fc.f_customer_id WHERE govt_id =%s AND t.receiver_id=%s",(username,content,))
            data = mycursor.fetchall()
            return render_template('Govt_Transac_Contr.html', value=data)
        if request.form['submit_button'] == 'Check transcation between these dates':
            startDate =request.form['startDate']
            endDate = request.form['endDate']
            print(startDate, endDate)
            mycursor.execute("SELECT t.date_of_transaction AS 'Date of Transaction', t.sender_id AS 'Sender ID', g.govt_name AS 'Govt. Name', t.receiver_id AS 'Contractor ID', fc.name AS 'Contractor Name', t.amount as 'Amount' FROM Transactions t INNER JOIN Government g ON t.sender_id = g.f_customer_id INNER JOIN Financial_Customers fc ON t.receiver_id = fc.f_customer_id WHERE govt_id =%s AND (date_of_transaction>=%s AND date_of_transaction<=%s);",(username,startDate,endDate,))
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
        if request.form['submit_button'] == 'Filter by Sender id':
            content = request.form['receiver_id']
            print(content)
            mycursor.execute("SELECT t.date_of_transaction AS 'Date of Transaction', t.sender_id AS 'Sender ID', g.govt_name AS 'Govt. Name', t.receiver_id AS 'Public ID', fc.name AS 'Public Name', t.amount as 'Amount' FROM Transactions t INNER JOIN Government g ON t.receiver_id = g.f_customer_id INNER JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id WHERE g.govt_id =%s AND t.sender_id=%s;",(username,content,))
            data = mycursor.fetchall()
            return render_template('Govt_Transac_Public.html', value=data)
        if request.form['submit_button'] == 'Check transcation between these dates':
            startDate =request.form['startDate']
            endDate = request.form['endDate']
            print(startDate, endDate)
            mycursor.execute("SELECT t.date_of_transaction AS 'Date of Transaction', t.sender_id AS 'Sender ID', g.govt_name AS 'Govt. Name', t.receiver_id AS 'Public ID', fc.name AS 'Public Name', t.amount as 'Amount' FROM Transactions t INNER JOIN Government g ON t.receiver_id = g.f_customer_id INNER JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id WHERE g.govt_id =%s AND (date_of_transaction>=%s AND date_of_transaction<=%s);",(username,startDate,endDate,))
            data = mycursor.fetchall()
            return render_template('Govt_Transac_Public.html', value=data)



            #Other 2 sortings left


@app.route('/ShowCont' , methods=['POST','GET'])
def show_contr():

    if request.method=='POST':


        content = request.form['submit_button']
        mycursor.execute("SELECT pa.ongoing_project_id, pa.application_time, c.contractor_name, c.dob, c.phone_number, c.contactdetails, cc.exp_years, cc.no_of_completed_projects, cc.personal_workforce_available, c.competency_score, pa.bid_value, pa.application_status, pa.p_contractor_id FROM project_applicants pa INNER JOIN Contractors c ON pa.p_contractor_id = c.contractor_id INNER JOIN contractor_competency cc ON pa.p_contractor_id = cc.c_competency_id WHERE pa.ongoing_project_id =%s AND pa.application_status <> 'Assigned'",(content,))


        data = mycursor.fetchall()
        return render_template('InterestedContr.html', value=data)





@app.route('/AssignCont' , methods=['POST','GET'])
def Assign_Contractor():
    if request.method=='POST':
        content = request.form['submit_button']
        lol1= content.index('-')
        lol2= content.index('-', lol1+1)

        p1=content[:lol1]
        p2=content[lol2+1:]
        print(p1,p2)
        mycursor.execute("UPDATE AVAAS2.project_applicants SET application_status = 'Assigned' WHERE (p_contractor_id = %s) AND (ongoing_project_id=%s);", (p1,p2,))
        mycursor.execute("UPDATE AVAAS2.Contractors SET booked = 'YES' WHERE (contractor_id = %s) ;", (p1,))
        mycursor.execute("UPDATE AVAAS2.ongoing_projects SET p_contractor_id =%s, assigned = 'YES', completion_percentage = '0.00' WHERE (ongoing_project_id =%s);", (p1,p2,))
        mycursor.execute("INSERT INTO AVAAS2.supplies VALUES(%s, %s ,%s ,%s);", (p2, random.randint(1,50), random.randint(1,50), random.randint(1,50)))
        return render_template('UpcomingGovt.html')




@app.route('/MoreDetailsProj' , methods=['POST','GET'])
def more_details_proj():
    if request.method=='POST':


            content = request.form['submit_button']
            mycursor.execute("SELECT op.name, op.location, op.size, s.construction_material, s.labour, s.engineers FROM supplies s INNER JOIN ongoing_projects op ON s.project_supplies_id = op.ongoing_project_id WHERE s.project_supplies_id =%s",(content,))


            data = mycursor.fetchall()
            return render_template('Project_Other_Details.html', value=data)


@app.route('/MoreDetailsContr' , methods=['POST','GET'])
def more_details_contr():
    if request.method=='POST':

            content = request.form['submit_button']

            mycursor.execute("SELECT contractor_id, contractor_name, dob, phone_number, contactdetails, exp_years, no_of_completed_projects, personal_workforce_available, competency_score FROM Contractors c INNER JOIN contractor_competency cc ON c.contractor_id = cc.c_competency_id WHERE contractor_id =%s", (content,))


            data = mycursor.fetchall()
            return render_template('Contractor_Other_Details.html', value=data)




@app.route('/MoreCDetailsProj' , methods=['POST','GET'])
def more_details_comp_proj():

    if request.method=='POST':


        content = request.form['submit_button']
        mycursor.execute("SELECT name, location, size, price, date_of_completion, p_contractor_id, completed_project_id FROM Completed_Projects cp WHERE completed_project_id=%s", (content,))


        data = mycursor.fetchall()
        return render_template('Completed_Proj_Other_Details.html', value=data)


@app.route('/ShowIntrPublic' , methods=['POST','GET'])
def show_intr_public():

    if request.method=='POST':


        content = request.form['submit_button']
        k=content.index('-')
        p=content[:k]
        mycursor.execute("SELECT ha.application_time, p.name, p.location, pc.financial_category, pc.no_of_female_members, pc.loans_cleared, p.competence_score, ha.application_status FROM house_applicants ha INNER JOIN PUBLIC p ON ha.public_id = p.public_id INNER JOIN public_competence pc ON p.public_id = pc.public_id WHERE ha.application_status <> 'Alloted' AND ha.completed_project_id=%s;", (p,)      )


        data = mycursor.fetchall()
        return render_template('Interested_Public.html', value=data)



@app.route('/ShowReviews' , methods=['POST','GET'])
def show_reviews():

    if request.method=='POST':


        content = request.form['submit_button']
        k=content.index('-')
        p=content[:k]
        mycursor.execute("SELECT p.name, p.location, r.review_score, r.review_comment FROM reviews r INNER JOIN public p ON r.public_id = p.public_id WHERE r.project_id = %s ", (p,))


        data = mycursor.fetchall()
        return render_template('Show_Reviews.html', value=data)

@app.route('/newproject' , methods=['POST','GET'])
def add_new_projects():

    if request.method=='POST':

        name = request.form['project_name']
        area = request.form['location_area']
        size = request.form['proj_size']

        minExp = request.form['experience']
        minCost = request.form['cost_handled']
        projComp = request.form['proj_completed']
        preWork = request.form['workforce']



        if request.form['submit_button'] == 'Finalise Details':

            mycursor.execute("SELECT COUNT(*) FROM ongoing_projects;")

            data=mycursor.fetchall()

            k = data[0][0]

            p="ONGP00"+str(k+1)

            print(username)

            mycursor.execute("INSERT INTO ongoing_projects VALUES(%s, null, %s, %s, %s, %s,'NO',0.00);", (p,username,name,area,size,))
            mycursor.execute("INSERT INTO project_requirements VALUES(%s,%s,%s,%s,%s);",(p,minExp, preWork, minCost,projComp,))


            return render_template('newproject.html')

  
  ######### Government Over ###########
          
          
          
          
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
                data=[["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]]        
                da=[["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA"]]        
                das = "Oho! you have no current project going on"
            else:
                das=""
                dat= "\nName =" + str(data[0][3])+  " \nLocation  =" + str(data[0][4])+ "\n Size  =" +str( data[0][5])+   "\n Completion Percentage  =" + str(data[0][7])
                mycursor.execute('Select * from supplies where project_supplies_id="' + data[0][0] + '"') 
                da = mycursor.fetchall() #data from database 
                dat= dat +" \n Supplies Data \n"
                dat= dat +"Material Cost  " + str(da[0][1]) + "Crs..\n"
                dat= dat +"Labour Cost  " + str(da[0][2]) + "Crs..\n"
                dat= dat +"Engineers Cost  " + str(da[0][2]) + "Crs..\n"
                


                
                
    
                

            

            return render_template('freepage.html', value = data , val2 = da ,  val3 = das)

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

        if request.form['submit_button'] == 'Apply for the entered loan id':

            task_content = request.form['loanid']
            
            mycursor.execute("select f_customer_id from Public where public_id=%s",(username,))
            val=mycursor.fetchall() 
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(task_content)
            print(username)
            print(f_cust_id)
            now = datetime.now()
            loan_application_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
            print(loan_application_datetime)
            mycursor.execute("insert into loan_applicants values(%s,%s,'Under review',%s)",(task_content,f_cust_id,loan_application_datetime,)) 
            mydb.commit()
            mycursor.execute("select * from Completed_Projects") 
            data = mycursor.fetchall() #data from database 
            return render_template('house_search.html',value=data)

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
            now = datetime.now()
            house_application_datetime = now.strftime("%Y-%m-%d")
            mycursor.execute("insert into house_applicants values(%s,%s,'Under review',%s)",(username,task_content,house_application_datetime)) 
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
            mycursor.execute("SELECT   t. id_transaction , t.date_of_transaction, t.sender_id, fc.name , t.receiver_id, fd.name , t.amount FROM Transactions t JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id JOIN Financial_Customers fd ON t.receiver_id= fd.f_customer_id where  transaction_type = 'general' AND (sender_id= '" +f_cust_id +"'or receiver_id= '" +f_cust_id + "')")

            data = mycursor.fetchall()
            print( data)
            return render_template("transaction_page_user.html",value=data)
        
        

        if request.form['submit_button'] == 'Check my loan payments':
            mycursor.execute("select f_customer_id from Public where public_id=%s",(username,))
            val=mycursor.fetchall() 
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            
            mycursor.execute("SELECT   t. id_transaction , t.date_of_transaction, t.sender_id, fc.name , t.receiver_id, fd.name , t.amount FROM Transactions t JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id JOIN Financial_Customers fd ON t.receiver_id= fd.f_customer_id where  transaction_type = 'loan_payment' AND (sender_id= '" +f_cust_id +"'or receiver_id= '" +f_cust_id + "')")

            da = mycursor.fetchall()
            mycursor.execute("select  *  from Loans where id_borrower='"+ f_cust_id+ "'")
            data = mycursor.fetchall()
            print( data)
            if ( len( data)==0):
                data=["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", ]

            

            print( da)
            return render_template("loan.html",value=da, val2= data[0] )
        
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
            mycursor.execute("SELECT   t. id_transaction , t.date_of_transaction, t.sender_id, fc.name , t.receiver_id, fd.name , t.amount FROM Transactions t JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id JOIN Financial_Customers fd ON t.receiver_id= fd.f_customer_id where  transaction_type = 'general' AND (sender_id= '" +f_cust_id +"'or receiver_id= '" +f_cust_id + "') order by(t.date_of_transaction)")

            data = mycursor.fetchall()
            print( data)
            return render_template("transaction_page_user.html",value=data)
        if request.form['submit_button'] == 'sort by amount':
            mycursor.execute("select f_customer_id from Public where public_id=%s",(username,))
            val=mycursor.fetchall() 
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            mycursor.execute("SELECT   t. id_transaction , t.date_of_transaction, t.sender_id, fc.name , t.receiver_id, fd.name , t.amount FROM Transactions t JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id JOIN Financial_Customers fd ON t.receiver_id= fd.f_customer_id where  transaction_type = 'general' AND (sender_id= '" +f_cust_id +"'or receiver_id= '" +f_cust_id + "') order by(t.amount)")

            data = mycursor.fetchall()
            print( data)
            return render_template("transaction_page_user.html",value=data)
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
            
            mycursor.execute("SELECT   t. id_transaction , t.date_of_transaction, t.sender_id, fc.name , t.receiver_id, fd.name , t.amount FROM Transactions t JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id JOIN Financial_Customers fd ON t.receiver_id= fd.f_customer_id where  transaction_type = 'loan_payment' AND (sender_id= '" +f_cust_id +"'or receiver_id= '" +f_cust_id + "') order by (t.date_of_transaction)")

            da = mycursor.fetchall()
            mycursor.execute("select  *  from Loans where id_borrower='"+ f_cust_id+ "'")
            data = mycursor.fetchall()
            print( data)
            if ( len( data)==0):
                data=["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", ]

            

            print( da)
            return render_template("loan.html",value=da, val2= data[0] )
        if request.form['submit_button'] == 'sort by amount':
            mycursor.execute("select f_customer_id from Public where public_id=%s",(username,))
            val=mycursor.fetchall() 
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            
            mycursor.execute("SELECT   t. id_transaction , t.date_of_transaction, t.sender_id, fc.name , t.receiver_id, fd.name , t.amount FROM Transactions t JOIN Financial_Customers fc ON t.sender_id = fc.f_customer_id JOIN Financial_Customers fd ON t.receiver_id= fd.f_customer_id where  transaction_type = 'loan_payment' AND (sender_id= '" +f_cust_id +"'or receiver_id= '" +f_cust_id + "') order by (t.amount)")

            da = mycursor.fetchall()
            mycursor.execute("select  *  from Loans where id_borrower='"+ f_cust_id+ "'")
            data = mycursor.fetchall()
            print( data)
            if ( len( data)==0):
                data=["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", ]

            

            print( da)
            return render_template("loan.html",value=da, val2= data[0] )



if __name__ == '__main__':
    app.run(debug="true")
    
