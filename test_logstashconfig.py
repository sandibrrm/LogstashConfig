# test_logstashconfig.py
"""
Tests for LogstashConfig module.
"""

import unittest
from logstashconfig import LogstashConfig

class TestLogstashConfig(unittest.TestCase):
    """Test cases for LogstashConfig class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LogstashConfig()
        self.assertIsInstance(instance, LogstashConfig)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LogstashConfig()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
