import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import src.main as main_module

class MainGlobalMockTest(unittest.TestCase):

    def setUp(self):
        self.patcher = patch('src.main.some_method')
        self.some_method_mock = self.patcher.start()
        
    def tearDown(self):
        self.patcher.stop()

    def test_simple(self):
        self.some_method_mock.return_value="mocked resp"
        res = main_module.main1()
        self.assertEqual(res, "mocked resp")
    
    def test_dependency(self):
        dependency = MagicMock()
        dependency.run.return_value = 55
        res = (main_module.HasDependency(dependency)).run()
        self.assertEqual(res, 55)
