
from flask import render_template, request, redirect, url_for
from app import app
from flask.ext.session import Session
from grocery import GroceryLists
from user import User 

user = User('Magic1@unicorn.com', 'awesomesauce')
groceryLists = GroceryLists(user.getName())

#uses flask here and jinja2 in index.html

@app.route('/')
@app.route('/index.html', methods=['GET', 'POST'])
def index():
	glists = groceryLists.getLists()
	if request.method == 'POST':
		gListName = int(request.form['gListName'])
		user.updateCurrentList(gListName)

		#return render_template('index.html', glist = glists)
		return redirect(url_for('ListPage'))
	else: 
		return render_template('index.html', glist = glists)
@app.route('/ListPage.html', methods = ['GET', 'POST'])
def ListPage(): 

	gListName = user.getCurrentList()

	if request.method == 'POST':
		newItem = str(request.form['newitem'])
		
		glists = groceryLists.getLists()
		glist = glists[gListName]
		glist.append(newItem)

		glists[gListName] = glist
		groceryLists.updateLists(glists)

		return redirect(url_for('ListPage'))
	else: 

		glists = groceryLists.getLists()
		glist = glists[gListName]   

		return render_template('ListPage.html', glistname = gListName, glist = glist)
@app.route('/NewList.html', methods = ['GET', 'POST'])
def NewList(): 

	if request.method == 'POST': 
		newListName = str(request.form['newlistname'])
		firstItem = str(request.form['firstitem'])

		glists = groceryLists.getLists()

		newList = []
		newList.append(firstItem)

		glists.append(newList)
		groceryLists.updateLists(glists)

		return redirect(url_for('index'))
	else: 

		return render_template('NewList.html')