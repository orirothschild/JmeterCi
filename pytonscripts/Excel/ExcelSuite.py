import unittest 
from  ProdExcelFile import EXCELPROD
from  PreExcelFile import EXCELPRE
import ExcelCompare 
# get all tests from SearchText and HomePageTest class
excel_pre_res= unittest.TestLoader().loadTestsFromTestCase(EXCELPRE)
excel_prod_res= unittest.TestLoader().loadTestsFromTestCase(EXCELPROD)
# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([excel_pre_res,excel_prod_res])
# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
ExcelCompare.main()