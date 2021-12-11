import unittest

from app.settings import Database, Settings

Settings.TESTING = True

from app.controllers.product_controller import ProductController
from generators.product_generator import ProductGenerator
from shared.tests.test_printer import TestPrinter


def main():
    ProductGenerator.populate_database(amount=10)
    pass


if __name__ == "__main__":
    main()
