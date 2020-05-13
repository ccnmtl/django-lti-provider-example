from django.test import TestCase


class BasicTest(TestCase):

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
