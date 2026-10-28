import unittest

from obsidian.eden_policy import Decision, SecurityEvent, evaluate


class EdenPolicyTests(unittest.TestCase):
    def test_unknown_usb_blocked(self):
        self.assertEqual(evaluate(SecurityEvent("usb", False, False)), Decision.BLOCK)

    def test_unverified_network_reviewed(self):
        self.assertEqual(evaluate(SecurityEvent("network", True, False)), Decision.REVIEW)

    def test_unauthorized_red_team_blocked(self):
        self.assertEqual(evaluate(SecurityEvent("red_team", False, True)), Decision.BLOCK)

    def test_high_severity_requires_review(self):
        self.assertEqual(evaluate(SecurityEvent("application", True, True, 9)), Decision.REVIEW)

    def test_verified_approved_event_allowed(self):
        self.assertEqual(evaluate(SecurityEvent("archive", True, True, 1)), Decision.ALLOW)

    def test_invalid_severity_rejected(self):
        with self.assertRaises(ValueError):
            evaluate(SecurityEvent("usb", True, True, 11))


if __name__ == "__main__":
    unittest.main()
