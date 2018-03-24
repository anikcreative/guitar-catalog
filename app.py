#!/usr/bin/env python

# -------------------------------------------------
#       guitar_catalog - by Anik Bhattacharya
#                  version 1.1.07
# -------------------------------------------------

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbsetup import Base, Category, Guitar
from flask import Flask, render_template, request, redirect, url_for


# Flask application
app = Flask(__name__)


# Database session setup
engine = create_engine('sqlite:///gtrcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def catalogRedirect():
    return redirect(url_for('catalogHome'))


@app.route('/catalog/')
def catalogHome():
    all_categories = session.query(Category).all()
    most_popular = session.query(Guitar).order_by(Guitar.views.desc()).limit(10).all()
    return render_template('catalog.html',
                           categories=all_categories,
                           most_popular=most_popular)


@app.route('/catalog/<category_name>/')
def categoryRedirect(category_name):
    return redirect(url_for('viewCategory', category_name=category_name))


@app.route('/catalog/<category_name>/items')
def viewCategory(category_name):
    all_categories = session.query(Category).all()
    category = session.query(Category).filter_by(name = category_name).one()
    all_items = session.query(Guitar).filter_by(category_id = category.id).order_by(Guitar.views.desc()).all()
    return render_template('category.html',
                           categories=all_categories,
                           category=category,
                           items=all_items)


@app.route('/catalog/<category_name>/<guitar_slug>')
def viewGuitar(category_name, guitar_slug):
    all_categories = session.query(Category).all()
    category = session.query(Category).filter_by(name = category_name).one()
    guitar = session.query(Guitar).filter_by(slug = guitar_slug).one()
    # add to the view counter for this item...
    guitar.views += 1
    # ...then, render html
    return render_template('item.html',
                           categories=all_categories,
                           category=category,
                           item=guitar)


@app.route('/catalog/<int:category_id>/<guitar_slug>')
def viewGuitarWithCategoryId(category_id, guitar_slug):
    category = session.query(Category).filter_by(id = category_id).one()
    return redirect(url_for('viewGuitar',
                            category_name=category.name,
                            guitar_slug=guitar_slug))


if __name__ == '__main__':
    print "\n\n------------------------------------------------------\n"
    print "\nguitar-catalog - by Anik Bhattacharya - v1.1.07\n"
    print "==> Server operational, running on port 5000. Access via localhost."
    print "    Press Ctrl+C at any time to cease operation.\n"
    print "------------------------------------------------------\n\n"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
