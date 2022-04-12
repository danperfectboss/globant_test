try:
    from app import app
    import unittest

except Exception as e:
    print('Some Modules are Missing {}'.str(e))

class FlaskTest(unittest.TestCase):
    
    def test_response(self):
        tester = app.test_client(self)
        response = tester.get("/get?city=Mexico&country=mx")
        statuscode = response.status_code
        self.assertEqual(statuscode,  200)
    
    def test_output(self):
        tester = app.test_client(self)
        response = tester.get("/get?city=Mexico&country=mx")
        statuscode = response.status_code
        self.assertEqual(response.content_type,  "application/json")

if __name__ == '__main__':
    unittest.main()