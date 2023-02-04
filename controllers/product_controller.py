from flask import Flask , render_template, request, redirect
from repositories import manufacturer_repository
from repositories import product_repository
from models.product import Product
from models.manufacturer import Manufacturer

from flask import Blueprint

product_blueprint = Blueprint("products", __name__)

@product_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", all_products = products)

@product_blueprint.route("/products/<id>")
def show_product(id):
    product = product_repository.select(id)
    return render_template("products/show.html", product = product)

@product_blueprint.route("/products/new")
def new_product():
    products = product_repository.select_all()
    return render_template("products/new.html", products = products)


