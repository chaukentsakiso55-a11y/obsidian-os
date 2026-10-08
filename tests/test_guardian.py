import unittest
from obsidian import assess_url, scan_text

class GuardianTests(unittest.TestCase):
    def test_empty_message(self):
        self.assertEqual(scan_text("")["risk"], "unknown")

    def test_high_risk_message(self):
        result = scan_text("Act immediately and send your password")
        self.assertEqual(result["risk"], "high")

    def test_normal_message(self):
        self.assertEqual(scan_text("See you tomorrow")["signals"], [])

    def test_http(self):
        self.assertIn("unencrypted_http", assess_url("http://example.org")["signals"])

    def test_https(self):
        self.assertEqual(assess_url("https://example.org")["risk"], "unknown")

    def test_invalid(self):
        self.assertEqual(assess_url("not a url")["risk"], "invalid")

if __name__ == "__main__":
    unittest.main()
