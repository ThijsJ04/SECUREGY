import unittest
from A_cwe209_0 import app, db


class TestCWE306_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.drop_all()
            db.create_all()
