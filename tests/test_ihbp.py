import unittest
from app.config import APIConfig
from flask import Flask
from flask_smorest import Api
from app.database import db
from app.services import check_if_password_is_leaked
from app.routes import blueprint_hibp


class TestHIBPApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup the application and test client
        # Replace 'testing' with your test configuration if needed

        server = Flask(__name__)
        server.config.from_object(APIConfig)
        api = Api(server)
        server.app_context().push()
        db.init_app(server)
        api.register_blueprint(blueprint_hibp)

        cls.app = server
        cls.client = cls.app.test_client()

    def setUp(self):
        # Setup any necessary state before each test
        pass

    def tearDown(self):
        # Cleanup the database or any state after each test
        pass

    def test_check_password_leaked(self):
        # Test GET /api/hibp/check/<password> with a leaked password
        leaked_password = "password123"  # Example of a commonly leaked password
        response = self.client.get(f'/api/hibp/check/{leaked_password}')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("leaked", data)
        # Assuming this password is considered leaked in the mock or real service
        self.assertTrue(data["leaked"])

    def test_check_password_not_leaked(self):
        # Test GET /api/hibp/check/<password> with a non-leaked password
        non_leaked_password = "UniquePassword123!"  # Example of a non-leaked password
        response = self.client.get(f'/api/hibp/check/{non_leaked_password}')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("leaked", data)
        # Assuming this password is considered safe in the mock or real service
        self.assertFalse(data["leaked"])

    def test_check_password_invalid(self):
        # Test GET /api/hibp/check/<password> with an invalid password format
        invalid_password = ""  # An empty string or other invalid format could be tested
        response = self.client.get(f'/api/hibp/check/{invalid_password}')
        # Assuming invalid password format returns a 400 error
        self.assertEqual(response.status_code, 400)

        data = response.get_json()
        # Customize error message based on your implementation
        self.assertEqual(data["message"], "Invalid password format")


if __name__ == "__main__":
    unittest.main()
