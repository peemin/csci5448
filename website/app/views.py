
from flask import render_template, request, redirect, url_for
from app import app

#imports the user class from the libraries folder to be
#able to use the user methods
from lib.user import User 

#Creates a new user and checks if the user exists
user = User('Magic1@unicorn.com', 'awesomesauce')
user.exist()

#gets username
username = user.getName()

#The following code uses flask methods to communicate between
#the database via the user class and the html pages using Jinja2 
#variables 

@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():

	#gets the grocery lists associated
	#with the user
	glists = user.getGListsItemList()

	#gets a lists of names for all the user's grocery lists
	gListNames = user.getGListsNames()
	
	#Post requests in flask mean that the user has clicked on a button or link 
	#that we would like to handle and send specific information for
	#Here, the following code handles when a user selects a specific lists
	if request.method == 'POST':

		#Gets the name of the grocery lists the user clicked on
		gListName = int(request.form['gListName'])

		#updates the current list the user is working with
		user.updateCurrentListIndex(gListName)

		#sends user to the list page
		return redirect(url_for('ListPage'))
	else: 
		#If the user hasn't clicked on a link, render the home page, sending in 
		#all the glists associated with the user, the name of the user, and the
		#names of all the grocery lists 
		return render_template('index.html', glist = glists, name = username, gnames = gListNames)

#code for the page involving the specific grocery lists 
@app.route('/ListPage.html', methods = ['GET', 'POST'])
def ListPage(): 

	#Gets the name of the list the user clicked on, all glists, the current grocery
	#list and the index spot for the current grocery list
	gListName = user.getCurrentGlistName()
	glists = user.getGLists()
	glist = user.getCurrentGList()
	index = user.getCurrentListIndex()

	if request.method == 'POST':
		#If the user has clicked on the delete list button
		if request.form['delete'] == 'deletelist': 
			
			#remove the grocery list from the glists object
			glists.pop(index)

			#update the glists object in the database to reflect the 
			#changed information
			user.updateGLists(glists)

			#send user back to the home page
			return redirect(url_for('index'))
		elif request.form['delete'] == 'deleteitem':
			#if the user has clicked on the delete item button, dont' 
			#do anything
			return redirect(url_for('ListPage'))
				
	else: 	
		#otherwise, upload the list page with the name of the list clicked on and 
		#the specific grocery list object for that list clicked on 
		return render_template('ListPage.html', glistname = gListName, glist = glist)

#code for the new list form 
@app.route('/NewList.html', methods = ['GET', 'POST'])
def NewList(): 

	#code to handle when the user presses the submit button
	if request.method == 'POST':

		#gets the new list name and the first item in the list
		#that the user submittted
		newListName = str(request.form['newlistname'])
		newListitem = str(request.form['firstitem'])

		#adds a new grocery list to the database
		user.addNewGroceryList(newListName, newListitem)

		#sends user back to home page
		return redirect(url_for('index'))
	else: 

		#otherwise renders the New list form page
		return render_template('NewList.html')

#code for add item form 
@app.route('/AddItem.html', methods =['GET', 'POST'])
def AddItem():

	#If the user presses the submit button on the add item page
	if request.method == 'POST': 

		#gets the new item name
		newItem = str(request.form['newitem'])

		#adds new item to the list
		user.addNewCurrentListItem(newItem)

		#sends user back to list page
		return redirect(url_for('ListPage'))
	else: 
		#otherwise send user to add item page
		return render_template('AddItem.html')