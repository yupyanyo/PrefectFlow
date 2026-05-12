# test_prefectflow.py
"""
Tests for PrefectFlow module.
"""

import unittest
from prefectflow import PrefectFlow

class TestPrefectFlow(unittest.TestCase):
    """Test cases for PrefectFlow class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrefectFlow()
        self.assertIsInstance(instance, PrefectFlow)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrefectFlow()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
