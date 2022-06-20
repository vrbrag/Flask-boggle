from unittest import TestCase, skip
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def setUp(self):
        """Before each test..."""
        print('\n***INSIDE SET UP CLASS***')
        app.config['TESTING'] = True
        
    # @skip('skip for now')
    def test_homepage(self):
        """Make sure info is in the session and HTML are showing/displayed"""
        with app.test_client() as client:
            response = client.get('/')

            self.assertIn('board', session)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Timer:', response.data)

    # @skip('skip for now')
    def test_valid_word(self):
        """Test if word is in dictionary"""
        with app.test_client() as client:
            client.get('/')
            with client.session_transaction() as change_session:
                change_session['board'] = [
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
            with client.session_transaction() as change_session:
                change_session['board'] = [
                    ["C", "A", "T", "T", "T"],
                    ["C", "A", "T", "T", "T"],
                    ["C", "A", "T", "T", "T"],
                    ["C", "A", "T", "T", "T"],
                    ["C", "A", "T", "T", "T"]
                ]
            
            response = client.get('/check-word?word=dog')
            self.assertEqual(response.json['result'], 'not-on-board')

    # @skip('skip for now')
    def test_not_word(self):
        """Test if word is not a word"""
        with app.test_client() as client:
            client.get('/')
            response = client.get('/check-word?word=adsjfks')
            self.assertEqual(response.json['result'], 'not-word')