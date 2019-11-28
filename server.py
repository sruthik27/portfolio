from flask import Flask, render_template,url_for,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def go_page(page_name):
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
    error = None
    if request.method == 'POST':
        try:
            dataa = dict(request.form)
            csvwriting(dataa)
            return render_template('thank.html',name = dataa['full name'])
        except:
            return 'Not found on database'
    else:
        return 'something just went wrong, Try again'


