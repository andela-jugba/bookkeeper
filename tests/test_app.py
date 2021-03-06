from unittest import TestCase
from app import create_app, db
from flask import current_app


class TestApp(TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def testAppExist(self):
        self.assertFalse(current_app is None)

    def testAppConfig(self):
        self.assertTrue(self.app.config['TESTING'])