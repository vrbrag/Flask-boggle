from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    # @classmethod
    def setUp(self):
        """Before each test..."""

        print('***INSIDE SET UP CLASS***')

    # @classmethod
    def tearDown(self):
        """After each test...."""

        print('***INSIDE TEARDOWN CLASS***')

    def test_homepage(self):
        """Make sure info is in the session and HTML are showing/displayed"""
        with app.test_client() as client:
            response = client.get('/')

            self.assertIn('board', session)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Timer:', response.data)

    def test_valid_word(self):
        """Make sure word is valid"""
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['board'] = [
                    ["C", "A", "T", "T", "T"],
                    ["C", "A", "T", "T", "T"],
                    ["C", "A", "T", "T", "T"],
                    ["C", "A", "T", "T", "T"],
                    ["C", "A", "T", "T", "T"]
                ]
                response = client.get('/check-word?word=cat')
                self.assertEqual(response.json['result'], 'ok')

    def test_invalid_word(self):
        """Test if word is in dictionary"""
        with app.test_client() as client:
            client.get('/')
            response = client.get('/check-word?word=dog')
            self.assertEqual(response.json['result'], 'not-on-board')

    def test_not_word(self):
        """Test if word is not a word"""
        with app.test_client() as client:
            client.get('/')
            response = client.get('/check-word?word=adsjfks')
            self.assertEqual(response.json['result'], 'not-word')