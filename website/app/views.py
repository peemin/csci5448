
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
		gListName = int(request.form['gListName'])

		user.updateCurrentListIndex(gListName)

		return redirect(url_for('ListPage'))
	else: 
		#return glists
		return render_template('index.html', glist = glists, name = username, gnames = gListNames)
@app.route('/ListPage.html', methods = ['GET', 'POST'])
def ListPage(): 

	gListName = user.getCurrentGlistName()
	glists = user.getGLists()
	glist = user.getCurrentGList()
	index = user.getCurrentListIndex()

	if request.method == 'POST':

		if request.form['delete'] == 'deletelist': 
			glists.pop(index)
			user.updateGLists(glists)
			return redirect(url_for('index'))
		elif request.form['delete'] == 'deleteitem':
			if request.form.get('items'):
				glist.remove(item)
				glists[index] = gListName
				user.updateGLists(glists)
				return redirect(url_for('index'))
	else: 	
		return render_template('ListPage.html', glistname = gListName, glist = glist)
@app.route('/NewList.html', methods = ['GET', 'POST'])
def NewList(): 

	if request.method == 'POST':
		glists = user.getGLists()

		newListName = str(request.form['newlistname'])
		newListitem = str(request.form['firstitem'])
		user.addNewGroceryList(newListName, newListitem)


		return redirect(url_for('index'))
	else: 

		return render_template('NewList.html')
@app.route('/AddItem.html', methods =['GET', 'POST'])
def AddItem():

	if request.method == 'POST': 
		newItem = str(request.form['newitem'])
		user.addNewCurrentListItem(newItem)
		return redirect(url_for('ListPage'))
	else: 
		return render_template('AddItem.html')