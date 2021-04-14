from flask import Flask, render_template, url_for, request, redirect
import mysql.connector
username=""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Password@1234",
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
            print("hellp i m clicked")
            return render_template('projectsearch.html')
        if request.form['submit_button'] == "Search for Banks":
            return render_template('bankpage.html')
        if request.form['submit_button'] == 'Check for the transactions':
            return render_template('transaction_page_user.html')
        if request.form['submit_button'] == 'Current project':
            return render_template('projectdetails_ongoing.html')






@app.route('/putbid/<int:id>',)
def display_project_bid(id):
    # // get the project details using this id
    # // display the project details here
    #// i have removed the for loop in the parent page 
    print( "cxnhfjd"+ str(id))
    return render_template('bidpage.html')  







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
        







if __name__ == '__main__':
    app.run(debug="true")
    