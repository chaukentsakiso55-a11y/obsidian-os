import unittest
from obsidian.scoring import analyze, score_signals

class ScoringTests(unittest.TestCase):
    def test_deduplicate(self):
        self.assertEqual(score_signals(["pressure", "pressure"])["score"], 30)

    def test_cap(self):
        self.assertEqual(score_signals(["credential_request", "pressure", "payment"])["score"], 100)

    def test_text(self):
        self.assertEqual(analyze("text", "Act immediately and send your password")["risk"], "high")

    def test_url(self):
        self.assertEqual(analyze("url", "http://example.org")["score"], 25)

    def test_invalid_url(self):
        self.assertIsNone(analyze("url", "invalid")["score"])

    def test_unknown(self):
        self.assertEqual(analyze("text", "hello")["risk"], "unknown")

    def test_kind(self):
        with self.assertRaises(ValueError):
            analyze("file", "abc")

    def test_input_limit(self):
        with self.assertRaises(ValueError):
            analyze("text", "a" * 10001)
