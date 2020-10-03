from flask import render_template, session, request, redirect, url_for, flash, current_app
from shop import db, app, photos
from shop.products.model import Addproduct
import json

def MergeDicts(dict1,dict2):
    if  isinstance (dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))


@app.route('/addcart', methods=['POST'])
def AddCart():
    try:
        product_id= request.form.get('product_id')
        quantity = request.form.get('quantity')
        colors = request.form.get('colors')
        product = Addproduct.query.filter_by(id=product_id).first()
        if product_id and quantity and colors and request.method =='POST':
            DictItems = {product_id:{'name': product.name, 'price': float(product.price), 'discount': product.discount, 'color':product.colors, 'quantity': quantity,'image':product.image_1}}
            if 'Shoppingcart' in session:
                print(session['Shoppingcart'])
                if product_id in session['Shoppingcart']:
                    print("This product is already in your cart")
                else:
                    session['Shoppingcart'] = MergeDicts(session['Shoppingcart'], Dictitems)
                    return redirect(request.referrer)
            else:
                session['Shoppingcart'] = DictItems
                return redirect(request.referrer) 
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)