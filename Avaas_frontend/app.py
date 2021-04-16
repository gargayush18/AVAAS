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
            return render_template('bank.html')
        if task_content[0:4]=="Cont":
            return render_template('contractor.html', hje= hje )
        if task_content[0:4]=="GOVT":
            return render_template('govt.html', hje= hje )
        if task_content[0:3]=="PUB":
            return render_template('public.html',hje=hje)
            


    else:
        return render_template('signin.html')



    
@app.route('/govt' , methods=['POST','GET'])
def add_new_projects():
    if request.method=='POST': 
        if request.form['submit_button'] == 'Add new project':
            return render_template('newproject.html')
        if request.form['submit_button'] == 'View ongoing projects':
            #topresent=get_ongoing_projects(id)  here we add those projects which correspond to this government  id; 

            return render_template('view_ongoing.html', projects=[])
        if request.form['submit_button'] == 'View completed projects':
            return render_template('view_completed.html')
        if request.form['submit_button'] == 'Check for the transactions':
            return render_template('view_transactions.html')



# not maded the functions for implement this       

        



@app.route('/newproject' , methods=['POST','GET'])
def finaliseprojects():
    if request.method=='POST': 
        if request.form['submit_button'] == 'finalisedetails':
            return render_template('govt.html', hje= "New project Added")



            
@app.route('/viewproject/<int:id>',)
def update(id):
    # // get the project details using this id
    # // display the project details here
    #// i have removed the for loop in the parent page 
    print( "cxnhfjd"+ str(id))
    return render_template('projectdetails_ongoing.html')



####################Contractors#####################

@app.route('/contractor' , methods=['POST','GET'])
def search_projects():
    if request.method=='POST': 
        if request.form['submit_button'] == 'Search for projects':
            mycursor.execute('select name, location , size , ongoing_project_id  from ongoing_projects where assigned="NO"') 
            
            data = mycursor.fetchall() #data from database 
            print( data)
            return render_template('projectsearch.html', value = data)
        if request.form['submit_button'] == "Search for Banks":
            mycursor.execute("SELECT loan_offer_id,name,ROI,max_loan_amount,max_duration,no_of_installments FROM loans_offered INNER JOIN Banks ON loans_offered.f_institution_id=Banks.f_institution_id WHERE loan_type='contractor'") 
            data = mycursor.fetchall() #data from database 
            return render_template('bankpage.html',value=data)
        if request.form['submit_button'] == "Check Complaints":
            mycursor.execute('Select name, actual_query, date_posted  , resolved from completed_projects , 	queries  where queries.project_id=completed_project_id  And resolved = "No" AND  p_contractor_id="'+username+'"') 
            data = mycursor.fetchall() #data from database 
            return render_template('complaints.html',value=data)
        if request.form['submit_button'] == "Check Bid status":
            mycursor.execute(   'Select name, location , bid_value , application_time , application_status from project_applicants , 	ongoing_projects   where project_applicants.ongoing_project_id=ongoing_projects.ongoing_project_id  AND project_applicants.p_contractor_id="'+username + '"') 
            data = mycursor.fetchall() #data from database 
            return render_template('bidstatus.html',value=data)

            


        if request.form['submit_button'] == 'Check for the transactions':
            mycursor.execute("select f_customer_id from Contractors where contractor_id=%s",(username,))
            val=mycursor.fetchall() 
            f_cust_id=" "
            for row in val:
                f_cust_id=row[0]
            print(f_cust_id)
            mycursor.execute("SELECT * FROM Transactions WHERE (transaction_type='general' and (sender_id=%s or receiver_id=%s))",(f_cust_id,f_cust_id,)) 
            data = mycursor.fetchall()
            
            
            return render_template('transaction_page_user.html',value =  data)
        
        
        
        
        
        
        
        
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
        task_content = request.form['bidvalue']
        # mycursor.execute("INSERT INTO project_applicants VALUES(" + "'"+username+"',"+  "'"+idd+"',"+" 'Under review','2021-05-29 23:39:36',16.14);") 
        
        



@app.route('/putbid/<int:id>',)
def display_project_bid(id):
    # // get the project details using this id
    # // display the project details here
    #// i have removed the for loop in the parent page 
    print( "cxnhfjd"+ str(id))
    global idd
    idd ="ONGP0010"
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
        if request.form['submit_button'] == 'Fiter by location': 
            task_content = request.form['locname']
            print(task_content)
            mycursor.execute("select * from Completed_Projects where (location= %s)",(task_content,)) 
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
            mycursor.execute("SELECT * FROM Transactions WHERE (transaction_type='general' and (sender_id=%s or receiver_id=%s))",(f_cust_id,f_cust_id,)) 
            data = mycursor.fetchall()
            return render_template("view_transactions.html",value=data)
        if request.form['submit_button'] == 'Check my loan payments':
            mycursor.execute("select f_customer_id from Public where public_id=%s",(username,))
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
    