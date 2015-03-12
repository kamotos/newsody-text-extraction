import json
import unittest
import urllib

import newsody_text_extraction as nte


class TextExtractionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = nte.app.test_client()
        nte.app.config['TESTING'] = True

    def test_get_text_and_title(self):
        html = open('test.html', 'r').read()
        params = urllib.urlencode({'html': html})
        response = self.app.get('/v1/?' + params)
        import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        expected_title = "Ireland closing a tax loophole that saved " \
                         "billions for Apple, Google, and Facebook"
        json_response = json.loads(response.data)
        self.assertIn('title', json_response)
        self.assertEqual(json_response['title'], expected_title)

    def test_should_raise_400_if_no_html_or_url_provided(self):
        response = self.app.get('/v1/')
        self.assertEqual(response.status_code, 400)

        json_response = json.loads(response.data)
        self.assertEqual(
            json_response['message'],
            "You should provide either an `url` or `html` parameter")


if __name__ == '__main__':
    unittest.main()

