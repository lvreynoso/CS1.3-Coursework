#!python

from redact_problem import redact_words
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_redaction(self):
        text = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda"]
        banned = ["kappa", "gamma", "eta"]
        expected_result = ["alpha", "beta", "delta", "epsilon", "zeta", "theta", "iota", "lambda"]
        assert list(redact_words(text, banned)) == expected_result

    def test_no_banned_words(self):
        text = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda"]
        banned = ["uno", "dos", "tres", "cuatro", "cinco", "seis"]
        assert list(redact_words(text, banned)) == text

    def test_all_banned_words(self):
        text = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda"]
        assert list(redact_words(text, text)) == []
