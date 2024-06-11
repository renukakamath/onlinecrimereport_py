from flask import Flask,Blueprint,render_template,request,url_for,redirect,flash
from database import*
import uuid

police=Blueprint('police',__name__)
@police.route('/police_home')
def police_home():
	return render_template('police_home.html')

@police.route('/police_managecrime',methods=['post','get'])
def police_managecrime():
	data={}
	q="select * from crime_types"
	res=select(q)
	data['cr']=res

	q="select * from stations"
	res=select(q)
	data['st']=res

	q="select *,concat(crimes.place) as cplace from crimes inner join crime_types using (crime_type_id) inner join stations using (station_id)"
	res=select(q)
	data['cri']=res

	if "crime" in request.form:
		t=request.form['type']
		s=request.form['station']
		c=request.form['crimetitle']
		cr=request.form['crimedes']
		oc=request.form['occ']
		re=request.form['rep']
		st=request.form['status']
		p=request.form['place']
		d=request.form['dob']
		di=request.form['dis']
		i=request.files['imgg']
		path="static/images/"+str(uuid.uuid4())+i.filename
		i.save(path)
		q="insert into crimes values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(t,s,c,cr,oc,re,st,p,d,di,path)
		insert(q)
		flash('insert successfully')
		return redirect(url_for('police.police_managecrime'))
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None


	if action=='delete':
		q="delete from crimes where crime_id='%s'"%(cid)
		delete(q)
		flash('delete successfully')
		return redirect(url_for('police.police_managecrime'))
	if action=='update':
		
		q="select * from crimes inner join crime_types using(crime_type_id) inner join stations using (station_id) where crime_id='%s'"%(cid)
		res=select(q)
		data['crime']=res
	if "update" in request.form:
		t=request.form['type']
		s=request.form['station']
		c=request.form['crimetitle']
		cr=request.form['crimedes']
		oc=request.form['occ']
		re=request.form['rep']
		st=request.form['status']
		p=request.form['place']
		d=request.form['dob']
		di=request.form['dis']
		i=request.files['imgg']
		path="static/images/"+str(uuid.uuid4())+i.filename
		i.save(path)
		q="update crimes set crime_type_id='%s',station_id='%s',crime_title='%s',crime_description='%s',date_time_occurred='%s',date_time_reported='%s',crime_status='%s',place='%s',dob='%s',district='%s',image='%s' where crime_id='%s'"%(t,s,c,cr,oc,re,st,p,d,di,path,cid)
		update(q)
		print(q)
		flash('update successfully')
		return redirect(url_for('police.police_managecrime'))
	return render_template('police_managecrime.html' ,data=data)
@police.route('/police_managecriminals',methods=['post','get'])	
def police_managecriminals():
	data={}
	q="select * from criminals"
	res=select(q)
	data['c']=res
	if "criminals" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		g=request.form['gen']
		da=request.form['date']
		i=request.files['imgg']
		t=request.files['thump']
		id1=request.form['idm1']
		id2=request.form['idm2']
		a=request.form['add']
		fa=request.form['faname']
		p=request.form['place']
		di=request.form['dis']
		path="static/images/"+str(uuid.uuid4())+i.filename
		i.save(path)
		path1="static/images/"+str(uuid.uuid4())+t.filename
		t.save(path1)
		q="insert into criminals values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(f,l,g,da,path,path1,id1,id2,a,fa,p,di)
		insert(q)
		print(q)
		flash('insert successfully')
		return redirect(url_for('police.police_managecriminals'))
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']

	else :
		action=None

	if action=='delete':
		q="delete from criminals where criminal_id='%s'"%(cid)
		delete(q)
		flash('delete successfully')
		return redirect(url_for('police.police_managecriminals'))
	if action=='update':
		q="select * from criminals"
		res=select(q)
		data['up']=res
	if "update" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		g=request.form['gen']
		d=request.form['date']
		i=request.files['imgg']
		t=request.files['thump']
		id1=request.form['idm1']
		id2=request.form['idm2']
		a=request.form['add']
		fa=request.form['faname']
		p=request.form['place']
		di=request.form['dis']
		path="static/images/"+str(uuid.uuid4())+i.filename
		i.save(path)
		path1="static/images/"+str(uuid.uuid4())+t.filename
		t.save(path1)
		q="update criminals set first_name='%s',last_name='%s', genter='%s',dob='%s',photo='%s',thumb_impression='%s',identification_mark1='%s',identification_mark2='%s',address='%s',father_name='%s',place='%s',district='%s' where criminal_id='%s'"%(f,l,g,d,path,path1,id1,id2,a,fa,p,di,cid)
		update(q)
		flash('update successfully')
		return redirect(url_for('police.police_managecriminals'))

	return render_template('police_managecriminals.html',data=data)

@police.route('/police_viewcomplaint')	
def police_viewcomplaint():
		data={}
		q="select * from complaints inner join user using(user_id) inner join stations using(station_id)"
		res=select(q)
		data['compl']=res

		if "action" in request.args:
			action=request.args['action']
			cid=request.args['cid']
		else:
			action=None

		if action=='accept':
			q="update complaints set status='on going' where complaint_id='%s'"%(cid)
			update(q)

		if action=='reject':
			q="update complaints set status='reject' where complaint_id='%s'"%(cid)
			update(q)
			return redirect(url_for('police.police_viewcomplaint'))

		return render_template('police_viewcomplaint.html',data=data)
@police.route('/police_viewusers')	
def police_viewusers():
	data={}

	q="select * from user"
	res=select(q)
	data['us']=res
	return render_template('police_viewusers.html',data=data)
@police.route('/police_viewcrimereport')
def police_viewcrimereport():
	data={}
	q="SELECT *,CONCAT (criminals.first_name) AS cname ,CONCAT(user.first_name) AS uname FROM foundreport INNER JOIN criminals USING(criminal_id) INNER JOIN `user` USING(user_id)"
	res=select(q)
	data['rep']=res

	return render_template('police_viewcrimereport.html',data=data)
@police.route('/police_viewevidence')
def police_viewevidence():
	data={}
	q="select *,concat (complaints.description)as cd ,concat (evidences.description) as ed  from evidences inner join complaints using(complaint_id)"
	res=select(q)
	data['evi']=res

	return render_template('police_viewevidence.html',data=data)
@police.route('/police_sendmessage',methods=['post','get'])	
def police_sendmessage():
	if "message" in request.form:
		u=request.args['uid']
		m=request.form['msg']
		q="insert into message values(null,'%s','%s','pending',curdate())"%(u,m)
		insert(q)
		flash('insert successfully')
		return redirect(url_for('police.police_sendmessage'))

		
	return render_template('police_sendmessage.html')
	
		

		
		
		

