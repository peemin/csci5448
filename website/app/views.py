
from flask import render_template, request, redirect, url_for
from app import app
from flask.ext.session import Session
from lib.user import User 

user = User('Magic1@unicorn.com', 'awesomesauce')
user.exist()
username = user.getName()

#uses flask here and jinja2 in index.html

@app.route('/')
@app.route('/index.html', methods=['GET', 'POST'])
def index():
	glists = user.getGListsItemList()
	gListNames = user.getGListsNames()
	if request.method == 'POST':
		gListNames = int(request.form['gListName'])

		user.updateCurrentListIndex(gListName)

		#return render_template('index.html', glist = glists)
		return redirect(url_for('ListPage'))
	else: 
		#return glists
		return render_template('index.html', glist = glists, name = username, gnames = gListNames)
@app.route('/ListPage.html', methods = ['GET', 'POST'])
def ListPage(): 

	gListName = user.getCurrentGlistName()
	glist = user.getCurrentGList()

	if request.method == 'POST':

		if request.form['delete'] == 'deletelist': 
			glists.remove(glist)
			groceryLists.updateLists(glists)
			return redirect(url_for('index'))
		elif request.form['delete'] == "deleteitem": 
			value = str(request.form.get('check'))
			return value
		else: 
			newItem = str(request.form['newitem'])
			
			glist.append(newItem)
			glists[gListName] = glist
			groceryLists.updateLists(glists)
			return redirect(url_for('ListPage'))
	else: 

		return render_template('ListPage.html', glistname = gListName, glist = glist)
@app.route('/NewList.html', methods = ['GET', 'POST'])
def NewList(): 

	if request.method == 'POST':
		glists = groceryLists.getLists()

		newListName = str(request.form['newlistname'])
		firstItem = str(request.form['firstitem'])

		newList = []
		newList.append(firstItem)

		glists.append(newList)
		groceryLists.updateLists(glists)

		return redirect(url_for('index'))
	else: 

		return render_template('NewList.html')