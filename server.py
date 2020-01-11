from flask import Flask, render_template,url_for,request,redirect
from passcheck import check
import csv
app = Flask(__name__)
import datetime
now = datetime.datetime.now()
today_date = now.strftime("%Y-%m-%d")



@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def go_page(page_name):
    if page_name == 'components.html':
        return render_template(page_name,date=today_date)
    else:
        return render_template(page_name)

def writing(data):      #Currently
    with open('../database.txt', mode='a') as datum:
        fullname = data['full name']
        email = data['email']
        password = data['password']
        file = datum.write(f'\n {fullname } {email} {password}')

def csvwriting(data):
    with open('../datasheet.csv',newline='',mode='a') as datum1:
        fullname = data['full name']
        email = data['email']
        password = data['password']
        csv_writer = csv.writer(datum1,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([fullname,email,password])

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            dataa = dict(request.form)
            csvwriting(dataa)
            return render_template('thank.html',name = dataa['full name'])
        except:
            return 'Not found on database'
    else:
        return 'something just went wrong, Try again'

@app.route('/finding', methods=['POST', 'GET'])
def findout():
    if request.method == 'POST':
        try:
            data_a = dict(request.form)
            print(data_a)
            print(check(data_a['inppassword']))
            return render_template('result.html',x = check(data_a['inppassword']))
        except:
            return 'Not found on database'
    else:
        return 'something just went wrong, Try again'

