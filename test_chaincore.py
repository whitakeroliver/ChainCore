# test_chaincore.py
"""
Tests for ChainCore module.
"""

import unittest
from chaincore import ChainCore

class TestChainCore(unittest.TestCase):
    """Test cases for ChainCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainCore()
        self.assertIsInstance(instance, ChainCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
