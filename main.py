from flask import render_template, Flask, url_for,request
import sqlite3
from flask_sqlalchemy import SQLAlchemy


from sent_email import sent_for_email


app = Flask(__name__)
app.static_folder = 'static'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Baza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
	__abstract__ = True
	__tablename__ = 'bars'
	Name = db.Column(db.String())
	Email = db.Column(db.String())
	Phone = db.Column(db.String())
	File = db.Column(db.String())

class Products(db.Model):
	ID = db.Column(db.Integer(), primary_key=True)
	Brand = db.Column(db.String())
	Name = db.Column(db.String())
	Price = db.Column(db.String())
	Image = db.Column(db.String())


@app.route('/')
def index():
	title = 'Женя'
	return render_template('index.html', title=title)

@app.route('/about', methods=['POST','GET'])
def about():
	title = 'Про меня'
	return render_template('about.html', title=title)



@app.route('/indew')
def indew():
	title = 'Фото'
	p_root = '/static/images/'
	v_root = '/static/vidios/'
	photos = [p_root+'1.jpg',p_root+'12.jpg',p_root+'1.jpg',p_root+'12.jpg',p_root+'1.jpg',p_root+'12.jpg']
	vidios = [v_root+'3.mp4', v_root+'3.mp4']
	return render_template('indew.html', title=title, photos=photos,vidios=vidios)

@app.route('/admin')
def admin():
	title = 'Admin'
	if request.method == 'POST':
		name_form = request.form['name']
		email_form = request.form['email']
		phone_form = request.form['phone']
		file_form = request.form['file']
		if name_form is not None and email_form is not None and phone_form is not None and fail_form is not None:
			new_tasks = Tour(Name=name_form, Email=email_form, Phone=phone_form, File=file_form)
			try:
				db.session.add(new_tasks)
				db.session.commit()
			except:
				pass


@app.route('/product/<brand>')
def products(brand):
	brand_p = Products.query.filter_by(Brand=brand).all()
	print(brand_p)
	title = brand
	return render_template('brand.html', title=title, brand_p=brand_p)


@app.route('/product/adidas/<product>', methods=['POST','GET'])
def name_product(product):
	about_product = Products.query.filter_by(ID=int(product))[0]
	if request.method == 'POST':
		name = request.form['name']
		phone = request.form['phone']
		email = request.form['email']
		address = request.form['address']
		sent_for_email(f'Имя - {name}\nТелефон - {phone}\nEmail - {email}\nАдрес - {address} ')
	title = about_product.Name
	return render_template('name_product.html', title=title , product=product, about_product=about_product)

	

app.run(debug=True)