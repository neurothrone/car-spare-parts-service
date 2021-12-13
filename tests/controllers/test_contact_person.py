import unittest

from app.settings import Database, Settings

Settings.TESTING = True

from app.controllers.contact_person_controller import ContactPersonController
from generators.contact_person_generator import ContactPersonGenerator
from shared.tests.test_printer import TestPrinter


class ContactPersonTestCase(unittest.TestCase):

    def setUp(self) -> None:
        ContactPersonController.delete_all()

    def tearDown(self) -> None:
        ContactPersonController.delete_all()

    @classmethod
    def setUpClass(cls) -> None:
        ContactPersonGenerator.populate_database(amount=100)
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        TestPrinter.print_passed_tests()

    def test_find_by_id_found(self):
        ContactPersonGenerator.populate_database(amount=5)
        contact_person_created = ContactPersonController.find_all()[0]

        if Settings.DATABASE == Database.MONGO:
            contact_person = ContactPersonController.find_by_id(contact_person_created._id)
        else:
            contact_person = ContactPersonController.find_by_id(contact_person_created.contact_person_id)

        self.assertIsNotNone(contact_person)
        TestPrinter.add(self.test_find_by_id_found.__name__)

    def test_find_by_id_not_found(self):
        if Settings.DATABASE == Database.MONGO:
            contact_person = ContactPersonController.find_by_id("61acd805a1dca9c019999999")
        else:
            contact_person = ContactPersonController.find_by_id(9999)

        self.assertIsNone(contact_person)
        TestPrinter.add(self.test_find_by_id_not_found.__name__)

    def test_find_by_first_name(self):
        ContactPersonGenerator.populate_database(amount=1)
        contact_person_created = ContactPersonController.find_all()[0]
        contact_person = ContactPersonController.find_by_first_name(contact_person_created.first_name)
        self.assertIsNotNone(contact_person)
        TestPrinter.add(self.test_find_by_first_name.__name__)

    def test_find_by_first_name_not_found(self):
        contact_person = ContactPersonController.find_by_first_name("DO THIS SHIT")

        self.assertIsNone(contact_person)
        TestPrinter.add(self.test_find_by_first_name_not_found.__name__)

    def test_find_by_last_name(self):
        ContactPersonGenerator.populate_database(amount=1)
        contact_person_created = ContactPersonController.find_all()[0]
        contact_person = ContactPersonController.find_by_last_name(contact_person_created.last_name)
        self.assertIsNotNone(contact_person)
        TestPrinter.add(self.test_find_by_last_name.__name__)

    def test_find_by_last_name_not_found(self):
        contact_person = ContactPersonController.find_by_last_name("DO THIS SHIT")

        self.assertIsNone(contact_person)
        TestPrinter.add(self.test_find_by_last_name_not_found.__name__)

    def test_find_by_phone(self):
        ContactPersonGenerator.populate_database(amount=1)
        contact_person_created = ContactPersonController.find_all()[0]
        contact_person = ContactPersonController.find_by_phone(contact_person_created.phone)

        self.assertIsNotNone(contact_person)
        TestPrinter.add(self.test_find_by_phone.__name__)

    def test_find_by_phone_not_found(self):
        contact_person = ContactPersonController.find_by_phone('070 00 93 71 35 25')

        self.assertIsNone(contact_person)
        TestPrinter.add(self.test_find_by_phone_not_found.__name__)

    def test_find_all_found(self):
        ContactPersonGenerator.populate_database(amount=3)
        contact_persons = ContactPersonController.find_all()
        self.assertIsNotNone(contact_persons)
        TestPrinter.add(self.test_find_all_found.__name__)

    def test_find_all_not_found(self):
        contact_persons = ContactPersonController.find_all()
        self.assertTrue(len(contact_persons) == 0)
        TestPrinter.add(self.test_find_all_not_found.__name__)

    def test_delete_all_found(self):
        ContactPersonGenerator.populate_database(amount=3)
        count_deleted = ContactPersonController.delete_all()
        self.assertTrue(count_deleted >= 3)
        TestPrinter.add(self.test_delete_all_found.__name__)

    def test_delete_all_not_found(self):
        count_deleted = ContactPersonController.delete_all()
        self.assertFalse(count_deleted > 0)
        TestPrinter.add(self.test_delete_all_not_found.__name__)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
