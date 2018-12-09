import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import src.main as main_module

class MainTest(unittest.TestCase):

    def test_simple(self):
        res = main_module.main1()
        self.assertEqual(res, "real result")
    
    def test_simple_patch_in(self):
        with patch('src.main.some_method', return_value="mocked resp"):
            res = main_module.main1()
        self.assertEqual(res, "mocked resp")

    @patch('src.main.some_method', return_value="mocked resp")
    def test_simple_patch_on_method(self, some_method_mocked):
        res = main_module.main1()
        self.assertEqual(res, "mocked resp")
    
    @patch('src.main.some_method')
    def test_simple_patch_on_method_internal(self, some_method_mocked):
        some_method_mocked.return_value="mocked resp"
        res = main_module.main1()
        self.assertEqual(res, "mocked resp")
    
    @patch('src.main.some_method')
    @patch('src.main.om')
    def test_simple_patch_on_method_internal(self, om_mock, some_method_mocked):
        om_mock.other_method.return_value = "am_mocked"
        some_method_mocked.return_value="mocked resp"
        res = main_module.main4()
        self.assertEqual(res["a"], "mocked resp")
        self.assertEqual(res["b"], "am_mocked")
    
    @patch('src.main.some_method')
    def test_mock_exception(self, some_method_mocked):
        some_method_mocked.side_effect = Exception()
        res = main_module.code_with_exception_check()
        self.assertEqual(res, "error")


    


    def test_othermodule_patch_in(self):
        with patch('src.main.om') as om_mock:
            om_mock.other_method.return_value = "mocked it"
            res = main_module.main2()
        self.assertEqual(res, "mocked it")

    def test_othermodule_method_with_params(self):
        with patch('src.main.om') as om_mock:
            om_mock.method_with_param.return_value = "mocked it"
            res = main_module.main3()
        
        om_mock.method_with_param.assert_called_once()
        self.assertEqual(om_mock.method_with_param.call_count, 1)
        self.assertEqual(om_mock.method_with_param.call_args[0][0], "a_param")
        self.assertEqual(om_mock.method_with_param.call_args[0][1], "b_param")
        self.assertEqual(res, "mocked it")