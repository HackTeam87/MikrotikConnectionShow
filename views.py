
#! /usr/bin/python3
from app import app, db
from flask import render_template, request, redirect, jsonify
from ssh_test import Mikrotik
from databse.models import MIKAUTH


@app.route("/")
def index():
    device = MIKAUTH.query.all() 
    return render_template('index.html',device=device)

@app.route("/add/device", methods=['POST', 'GET'])
def add_device():
    if request.method == 'POST':
        router_ip = request.form.get('router_ip')
        router_port = request.form.get('router_port')
        router_name = request.form.get('router_name')
        router_timeout = request.form.get('router_timeout')
        router_login = request.form.get('router_login') 
        router_passwd = request.form.get('router_passwd') 

        d = MIKAUTH(device_type='mikrotik_routeros', ip=router_ip, port=router_port, 
                    name=router_name, login=router_login, passwd=router_passwd, timeout=router_timeout)
        db.session.add(d)
        db.session.commit()

    return redirect('/')

@app.route("/delete/device/<int:id>")
def delete_device(id):
    d = MIKAUTH.query.filter(MIKAUTH.id == id).delete()
    db.session.commit()
    return redirect('/')


@app.route("/info/<int:id>")
def info(id):
    return render_template('info.html')
        

@app.route("/get-infos/<int:router_id>/<string:direction>/<string:test_ip>")
def get_infos(router_id, direction,test_ip):
    my_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    
    device = MIKAUTH.query.filter(MIKAUTH.id == router_id).first()
    try:
        identity = Mikrotik().send_show_command(
        device.ip, device.login, device.passwd, 
        device.port, device.device_type, device.timeout,'system identity print')

        ma = Mikrotik().send_show_command(
        device.ip, device.login, device.passwd, 
        device.port, device.device_type, device.timeout,
        f'ip firewall connection print without-paging  where {direction}~"{test_ip}"'
        )
       
        return jsonify({
            'my_ip': my_ip,
            'router_ip': device.ip, 
            'identity': identity.split(':')[1],
            'test_ip': test_ip,
            'data': ma})
    except:
        return jsonify({'data': ma})
            
             

    

   
