from flask import render_template, session, request, redirect, url_for, flash
from shop import db, app, photos
from .model import Brand, Category
from .forms import Addproducts
from sqlalchemy.exc import IntegrityError

@app.route('/addbrand', methods=['GET','POST'])
def addbrand():
    if request.method=="POST":
        getbrand = request.form.get('brand')
        brand= Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The Brand {getbrand} was added to your database', 'success')
      
        db.session.commit()
    
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', brand='brand')


@app.route('/addcat', methods=['GET','POST'])
def addcat():
    if request.method=="POST":
        getcat = request.form.get('category')
        cat = Category(name=getcat)
        db.session.add(cat)
        flash(f'The Category {getcat} was added to your database', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addbrand.html', cat='cat')


@app.route('/addproduct', methods=['GET','POST'])
def addproduct():
    brands=Brand.query.all()
    categories = Category.query.all()
    form= Addproducts(request.form)
    if request.method =="POST":
        photos.save(request.files.get(image_1))
        photos.save(request.files.get(image_2))
        photos.save(request.files.get(image_3))
    return render_template('products/addproduct.html', title="Add Product page", form=form, brands=brands, categories=categories)