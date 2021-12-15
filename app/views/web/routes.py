import flask

from app.settings import Settings

Settings.TESTING = True

from app.controllers.customer_controller import CustomerController
from app.controllers.employee_controller import EmployeeController
from app.controllers.product_controller import ProductController
from app.controllers.store_controller import StoreController

bp = flask.Blueprint("main", __name__, template_folder="templates")


@bp.route("/")
def index():
    return flask.render_template("index.html")


@bp.route("/products")
def products_page():
    products = ProductController.find_all()
    return flask.render_template("items/product/content.html", products=products)


@bp.route("/stores")
def stores_page():
    stores = StoreController.find_all()
    return flask.render_template("items/store/content.html", stores=stores)


@bp.post("/products/create")
def create_store():
    data = {key: (value if value else None) for key, value in flask.request.form.items()}
    try:
        StoreController.create(**data)
    except Exception as error:
        print(error)
    return flask.redirect(flask.url_for("main.stores_page"))


@bp.route("/employees")
def employees_page():
    employees = EmployeeController.find_all()
    return flask.render_template("items/employee/content.html", employees=employees)


@bp.route("/customers")
def customers_page():
    customers = CustomerController.find_all()
    return flask.render_template("items/customer/content.html", customers=customers)
