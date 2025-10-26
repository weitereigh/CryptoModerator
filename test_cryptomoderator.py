# test_cryptomoderator.py
"""
Tests for CryptoModerator module.
"""

import unittest
from cryptomoderator import CryptoModerator

class TestCryptoModerator(unittest.TestCase):
    """Test cases for CryptoModerator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoModerator()
        self.assertIsInstance(instance, CryptoModerator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoModerator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
