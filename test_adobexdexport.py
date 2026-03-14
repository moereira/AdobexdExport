# test_adobexdexport.py
"""
Tests for AdobexdExport module.
"""

import unittest
from adobexdexport import AdobexdExport

class TestAdobexdExport(unittest.TestCase):
    """Test cases for AdobexdExport class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AdobexdExport()
        self.assertIsInstance(instance, AdobexdExport)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AdobexdExport()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
