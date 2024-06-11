from flask import Flask,Blueprint,render_template,request,url_for,session,redirect,flash
from database import*
import uuid


user=Blueprint('user',__name__)

@user.route('/user_home')
def user_home():
	return render_template('user_home.html')
@user.route('/user_viewstations')
def user_viewstations():
	data={}
	q="select * from stations"
	res=select(q)
	data['sta']=res
	return render_template('user_viewstations.html' ,data=data)
@user.route('/user_viewcrimetypes')	
def user_viewcrimetypes():
	data={}
	q="select * from crime_types"
	res=select(q)
	data['type']=res

	return render_template('user_viewcrimetypes.html',data=data)
@user.route('/user_viewcrimes')
def user_viewcrimes():
	data={}
	q="select *,concat(crimes.place) as cplace from crimes inner join crime_types using (crime_type_id) inner join stations using(station_id)"
	res=select(q)
	data['cr']=res
	return render_template('user_viewcrimes.html',data=data)
@user.route('/user_viewcriminals')
def user_viewcriminals():
	data={}
	q="select * from criminals"
	res=select(q)
	data['crim']=res

	return render_template('user_viewcriminals.html',data=data)
@user.route('/user_reportcriminal',methods=['post','get'])	
def user_reportcriminal():
	data={}
	q="select * from criminals"
	res=select(q)
	data['cr']=res
	q="select *,CONCAT (criminals.first_name) AS cname ,CONCAT(user.first_name) AS uname  from foundreport inner join criminals using(criminal_id) inner join user using(user_id)"
	res=select(q)
	data['rep']=res

	if "report" in request.form:
		c=request.form['cri']
		uid=session['uid']
		p=request.form['place']
		dat=request.form['date']
		des=request.form['des']
		q="insert into foundreport values(null,'%s','%s','%s','%s','%s')"%(c,uid,p,dat,des)
		insert(q)
		return redirect(url_for('user.user_reportcriminal'))
		
	return render_template('user_reportcriminal.html',data=data)
@user.route('/user_sendfeedback',methods=['post','get'])
def user_sendfeedback():
	data={}
	q="select * from feedback inner join user using(user_id)"
	res=select(q)
	data['fee']=res
	if "feedback" in request.form:
		uid=session['uid']
		f=request.form['fee']
		q="insert into feedback values(null,'%s','%s','pending',curdate())"%(uid,f)
		insert(q)
		return redirect(url_for('user.user_sendfeedback'))
	
	return render_template('user_sendfeedback.html',data=data)
@user.route('/user_makecomplaint',methods=['post','get'])
def user_makecomplaint():
	data={}
	q="select * from stations"
	res=select(q)
	data['sta']=res
	q="select * from complaints inner join user using(user_id) inner join stations using(station_id)"
	res=select(q)
	data['comp']=res

	if "complaint" in request.form:
		uid=session['uid']
		s=request.form['sta']
		des=request.form['des']
		q="insert into complaints values(null,'%s','%s','%s',curdate(),'pending')"%(uid,s,des)
		insert(q)
		return redirect(url_for('user.user_makecomplaint'))
	

	return render_template('user_makecomplaint.html',data=data)
@user.route('/user_uploadevidence',methods=['post','get'])
def user_uploadevidence():
	data={}
	q="select *,concat (complaints.description)as cd ,concat (evidences.description) as ed from evidences inner join complaints using(complaint_id)"
	res=select(q)
	data['ev']=res

	if "evi" in request.form:
		cid=request.args['cid']
		i=request.files['imgg']
		d=request.form['des']
		path="static/images/"+str(uuid.uuid4())+i.filename
		i.save(path)
		q="insert into evidences values(null,'%s','%s','%s',curdate())"%(cid,path,d)
		insert(q)
		print(q)
		return redirect(url_for('user.user_uploadevidence'))

	return render_template('user_uploadevidence.html',data=data)
@user.route('/user_viewmessage',methods=['post','get'])
def user_viewmessage():
	data={}
	q="select * from message inner join user using(user_id)"
	res=select(q)
	data['mess']=res


	return render_template('user_viewmessage.html',data=data)
@user.route('/user_sendreply',methods=['post','get'])	
def user_sendreply():
	if "sreply" in request.form:
		m=request.args['mid']
		r=request.form['rep']
		q="update message set reply='%s' where message_id='%s'"%(r,m)
		update(q)
		return redirect(url_for('user.user_viewmessage'))
		
	return render_template('user_sendreply.html')
	
			
		

			 
			


	
	
	
			
	
	
	