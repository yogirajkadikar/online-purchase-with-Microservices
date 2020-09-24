import os
from flask import render_template, session, request, redirect, url_for, flash
from shop import app, db, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User
from shop.products.model import Addproduct, Brand, Category


@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))
    products = Addproduct.query.all()
    return render_template('admin/index.html', title='Vendor Page', products=products)


@app.route('/brands')
def brands():
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html', title='brands',brands=brands)


@app.route('/categories')
def categories():
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/brand.html', title='categories',categories=categories)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)

        user = User(name=form.name.data, username=form.username.data, email=form.email.data, 
                password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.name.data} Thank you for registering.', 'success')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title="Registration Page")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method =="POST" and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Welcome {form.email.data} You are LoggedIn', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('Please check Email-Id and password again or Register if new user','danger')
            return redirect(url_for('login'))   
    return render_template('admin/login.html',form=form, title="Login Page")
