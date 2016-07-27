from unittest import TestCase
from app import db, create_app
from app.models import Category, Book


class ModelTests(TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def testCategoryModel(self):
        category_fiction = Category(name='Fiction')

        db.session.add(category_fiction)
        db.session.commit()
        self.assertIsNotNone(category_fiction.id)