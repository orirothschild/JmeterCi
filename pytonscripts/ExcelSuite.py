import unittest 
from  PreExcelFile import EXCELPRE
from  ./ProdExcelFile import EXCELPROD
# get all tests from SearchText and HomePageTest class
excel_pre_res= unittest.TestLoader().loadTestsFromTestCase(EXCELPRE)
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')
# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([excel_pre_res])


# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)