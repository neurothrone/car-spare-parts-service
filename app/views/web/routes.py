import flask

from app.settings import Database, Settings

from app.controllers.customer_controller import CustomerController
from app.controllers.employee_controller import EmployeeController
from app.controllers.product_controller import ProductController
from app.controllers.storage_controller import StorageController
from app.controllers.store_controller import StoreController
from app.views.web.controller import WebController
from app.views.web.utils import StatusCode

bp = flask.Blueprint("main", __name__, template_folder="templates")


@bp.app_errorhandler(StatusCode.BAD_REQUEST_ERROR)
def bad_request_error_handler(error):
    return flask.render_template("error/400.html"), StatusCode.BAD_REQUEST_ERROR


@bp.app_errorhandler(StatusCode.NOT_FOUND_ERROR)
def not_found_error_handler(error):
    return flask.render_template("error/404.html"), StatusCode.NOT_FOUND_ERROR


@bp.app_errorhandler(StatusCode.INVALID_SERVER_ERROR)
def internal_server_error_handler(error):
    return flask.render_template("error/500.html"), StatusCode.INVALID_SERVER_ERROR


@bp.route("/")
def index():
    return flask.render_template("index.html", database=Settings.DATABASE)


@bp.route("/products")
def products_page():
    products = ProductController.find_all()
    return flask.render_template("items/product/content.html", products=products)


@bp.route("/stores")
def stores_page():
    stores = StoreController.find_all()
    return flask.render_template("items/store/content.html", stores=stores)


@bp.route("/stores/create", methods=["POST"])
def create_store():
    data = {key: (value if value else None) for key, value in flask.request.form.items()}
    try:
        StoreController.create(**data)
        flask.flash("Store created", "success")
    except Exception as error:
        print(error)
        flask.flash(str(error), "error")
    return flask.redirect(flask.url_for("main.stores_page"))


@bp.route("/storages")
def storages_page():
    storages = StorageController.find_all()
    return flask.render_template("items/storage/content.html", storages=storages)


@bp.route("/employees")
def employees_page():
    employees = EmployeeController.find_all()
    return flask.render_template("items/employee/content.html", employees=employees)


@bp.route("/customers")
def customers_page():
    customers = CustomerController.find_all()
    return flask.render_template("items/customer/content.html", customers=customers)


@bp.route("/db/populate", methods=["POST"])
def populate():
    try:
        WebController.populate_mysql_db()
        flask.flash("MySQL database successfully populated", "success")
    except Exception as error:
        print(error)
        flask.flash("Something went wrong when populating MySQL database", "error")
    return flask.redirect(flask.url_for("main.index"))


@bp.route("/db/convert", methods=["POST"])
def convert():
    try:
        WebController.convert_mysql_to_mongo()
        flask.flash("Data in MySQL database successfully converted to data in Mongo database", "success")
    except Exception as error:
        print(error)
        flask.flash("Something went wrong with converting from MySQL to Mongo", "error")
    return flask.redirect(flask.url_for("main.index"))


@bp.route("/db/purge-mysql", methods=["POST"])
def purge_mysql():
    try:
        WebController.delete_data_from_mysql_db()
        flask.flash("MySQL database successfully purged", "success")
    except Exception as error:
        print(error)
        flask.flash("Something went wrong when purging MySQL database", "error")
    return flask.redirect(flask.url_for("main.index"))


@bp.route("/db/purge-mongo", methods=["POST"])
def purge_mongo():
    try:
        WebController.delete_data_from_mongo_db()
        flask.flash("Mongo database successfully purged", "success")
    except Exception as error:
        print(error)
        flask.flash("Something went wrong when purging Mongo database", "error")
    return flask.redirect(flask.url_for("main.index"))


@bp.route("/db/switch", methods=["POST"])
def switch_db():
    if database := flask.request.form.get("database-option", None):
        Settings.DATABASE = Database.MONGO if database == Database.MONGO else Database.MYSQL
        flask.flash(f"Database successfully switched to {Settings.DATABASE.title()}", "success")
    else:
        flask.flash("Something went wrong when switching database", "error")
    return flask.redirect(flask.url_for("main.index"))
