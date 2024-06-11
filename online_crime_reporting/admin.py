from flask import Flask,Blueprint,render_template,request,redirect,url_for,flash
from database import*

admin=Blueprint('admin',__name__)
@admin.route('/admin_home')
def admin_home():
	return render_template('admin_home.html')

@admin.route('/admin_managepolicestation',methods=['post','get'])
def admin_managepolicestation():
	data={}
	q="select * from stations"
	res=select(q)
	data['stations']=res

	if "policestation" in request.form:
		s=request.form['sname']
		pl=request.form['place']
		d=request.form['dis']
		pi=request.form['pincode']
		ph=request.form['number']
		e=request.form['email']
		f=request.form['fx']
		u=request.form['uname']
		p=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(u,p)
		res=select(q)
		if res:
			flash('already exist')
		else:
			
			q="insert into login values(null,'%s','%s','police')"%(u,p)
			id=insert(q)
			q="insert into stations values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(id,s,pl,d,pi,ph,e,f)
			insert(q)
			flash('insert successfully')
			return redirect(url_for('admin.admin_managepolicestation'))
	if "action" in request.args:
		action=request.args['action']
		sid=request.args['sid']
	else:action=None
	if action=='delete':
		q="delete from stations where station_id='%s'"%(sid)
		delete(q)
		print(q)
		flash('delete successfully')
		return redirect(url_for('admin.admin_managepolicestation'))
	if action=='update':
		q="select * from stations where station_id='%s'"%(sid)
		res=select(q)
		data['station']=res

	if "update" in request.form:
		s=request.form['sname']
		pl=request.form['place']
		d=request.form['dis']
		pi=request.form['pincode']
		ph=request.form['number']
		e=request.form['email']
		f=request.form['fx']

		
		q="update stations set station_name='%s',place='%s',district='%s',pincode='%s',phone='%s',email='%s',fax_no='%s'where station_id='%s' "%(s,pl,d,pi,ph,e,f,sid)
		update(q)
		flash('update successfully')
		return redirect(url_for('admin.admin_managepolicestation'))
	return render_template('admin_managepolicestation.html',data=data)

@admin.route('/admin_managecrimetype', methods=['post','get'])	
def admin_managecrimetype():
	data={}
	q="select * from crime_types"
	res=select(q)
	data['crime']=res

	if "crimetype" in request.form:
		c=request.form['ctn']
		m=request.form['mp']
		q="insert into crime_types values(null,'%s','%s')"%(c,m)
		insert(q)
		flash('insert successfully')
		return redirect(url_for('admin.admin_managecrimetype'))
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:action=None
	if action=='delete':
		q="delete from crime_types where crime_type_id='%s'"%(cid)
		delete(q)
		flash('delete successfully')
		return redirect(url_for('admin.admin_managecrimetype'))
	if action=='update':
		q="select * from crime_types"
		res=select(q)
		data['crimes']=res
	if "update" in request.form:
		c=request.form['ctn']
		m=request.form['mp']
		q="update crime_types set crime_type_name='%s',minimum_penalty='%s' where crime_type_id='%s'"%(c,m,cid)
		update(q)
		flash('update successfully')
		return redirect(url_for('admin.admin_managecrimetype'))
	return render_template('admin_managecrimetype.html',data=data)
@admin.route('/admin_viewusers')	
def admin_viewusers():
	data={}
	q="select * from user"
	res=select(q)
	data['user']=res
	return render_template('admin_viewusers.html',data=data)
@admin.route('/admin_viewcomplaints')
def complaints():
	data={}
	q="select * from complaints inner join user using(user_id) inner join stations using(station_id)"
	res=select(q)
	data['comp']=res
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None
	if action=='accept':
		q="update complaints set status='Tracks' where complaint_id='%s' "%(cid)
		update(q)
	if action=='reject':
		q="update complaints set status='Reject' where complaint_id='%s'"%(cid)
		update(q)
		return redirect(url_for('admin.admin_viewcomplaint'))
				
				
		
	return render_template('admin_viewcomplaints.html',data=data)


@admin.route('/admin_viewfeedback')	
def admin_viewfeedback():
	data={}
	q="select * from feedback inner join user using(user_id)"
	res=select(q)
	data['feed']=res
	return render_template('admin_viewfeedback.html',data=data)

@admin.route('/admin_sendreply',methods=['post','get'])	
def admin_sendreply():
	if "sreply" in request.form:
		f=request.args['fid']
		r=request.form['rep']
		q="update feedback set reply='%s' where feedback_id='%s'"%(r,f)
		update(q)
		return redirect(url_for('admin.admin_viewfeedback'))
		
	return render_template('admin_sendreply.html')
	
	


			
	
	