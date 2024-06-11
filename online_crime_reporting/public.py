from flask import Flask,Blueprint,render_template,request,redirect,url_for,session,flash 	
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('public_home.html')
@public.route('/public_login',methods=['post','get'])	
def public_login():
	if "login" in request.form:
		u=request.form['uname']
		p=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(u,p)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['type']=="admin":
				return redirect(url_for('admin.admin_home'))
			elif res[0]['type']=="police":
				return redirect(url_for('police.police_home'))	

			elif res[0]['type']=="user":
				q="select * from user where login_id='%s'"%(session['lid'])
				res=select(q)
				if res:
					session['uid']=res[0]['user_id']
					
				return redirect(url_for('user.user_home'))
	return render_template('public_login.html')
@public.route('/public_registration',methods=['post','get'])	
def public_registration():
	if "registration" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		a=request.form['address']
		p=request.form['place']
		pi=request.form['pincode']
		n=request.form['number']
		e=request.form['email']
		u=request.form['uname']
		p=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(u,p)
		res=select(q)
		if res:
			flash('already exist')
		else: 	

			q="insert into login values(null,'%s','%s','user')"%(u,p)
			id=insert(q)
			q="insert into user values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(id,f,l,a,p,pi,n,a)
			insert(q)
			flash('insert successfully')
			return redirect(url_for('public.public_registration'))
	return render_template('public_registration.html')

	
	
	