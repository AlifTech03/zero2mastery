from flask import Flask, render_template,url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def hello_world1():
    return render_template('index.html')

@app.route('/about.html')
def hello_world():
    return render_template('about.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n {email},{subject},{message}')


def save_data(data):
	with open('database.csv', 'a', newline='') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_file = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_file.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		save_data(data)
		return redirect('/thank you.html')
	else:
		return'something went wrong'
	

   
   
