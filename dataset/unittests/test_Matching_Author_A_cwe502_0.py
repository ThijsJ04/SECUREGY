import marshal
import unittest

from Matching_Author_A_cwe502_0 import app


class TestCWE502_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        original_data = [1, 2, 3, "hello", {"key": "value"}]

        marshalled_data = marshal.dumps(original_data)

        response = self.app.get("/unmarshal?data=" + marshalled_data.hex())

        self.assertEqual(response.status_code, 200)

        unmarshalled_data = eval(response.data.decode())
        self.assertEqual(unmarshalled_data, original_data)

    def test_vulnerability(self):
        malicious_data = "c0de4eva1"
        marshal_data = marshal.dumps(malicious_data)

        response = self.app.get("/unmarshal?data=" + marshal_data.hex())

        self.assertEqual(response.status_code, 500)


if __name__ == "__main__":
    unittest.main()
