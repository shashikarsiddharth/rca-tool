import unittest, json
from app import *

BASE_URL = 'http://172.17.0.1:5000/rcas'

class testRCAList(unittest.TestCase):
    def setUp(self):
        self.rca = {"title": "Sys Abort", "incident_report_for": "qwerty is good", "incident_datetime": "2020-1-1", "incident_reported_by": "James", "report_datetime": "2020-1-1", "fixed_on": "2020-1-1", "outage_duration": "2020-1-1", "outage_severity": "High", "sre_on_call": "James", "summary": "System crashed due to human error.", "root_cause_analysis": "Human error compromised the system.", "error_message": "failed transactions", "bugs": "none", "recovery": "avoid such mistakes", "workaround": "used second server", "closing_remarks": "issued resolved", "action_items": "none", "comment": "none"}
        self.app = app.test_client()
        self.app.testing = True

    def test_get(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        

    def test_post(self):
        response = self.app.post(BASE_URL, data=self.rca, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
