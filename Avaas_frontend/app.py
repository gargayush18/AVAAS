from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/' , methods=['POST','GET'])
def index():
    if request.method=='POST': 
        task_content = request.form['content']
        hje= task_content

        
        print(task_content)
        if task_content=="bank":
            return render_template('bank.html')
        if task_content=="contractor":
            return render_template('contractor.html', hje= hje )
        if task_content=="govt":
            return render_template('govt.html', hje= hje )
        if task_content=="public":
            return render_template('public.html')
            


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
            print("hellp i m clicked")
            return render_template('house_search.html')
        if request.form['submit_button'] == 'Search for Banks':
            print("hellp i m clicked")
            return render_template('bankpage.html')
        if request.form['submit_button'] == 'Search for the home requests status':
            print("hellp i m clicked")
            
            return render_template('homerequeststatus.html')
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
        if request.form['submit_button'] == 'Check my Hosue payments':
            return render_template("view_transactions.html")
        if request.form['submit_button'] == 'Check my loan payments':
            return render_template("loan.html")
        







if __name__ == '__main__':
    app.run(debug="true")
    