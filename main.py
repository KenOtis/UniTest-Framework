import unittest
from selenium import webdriver
import page 


class PythonOrgSearch(unittest.TestCase):
    # a sample test class to show how page object works 
    def setUp(self):            #this will be run every time the test cases are run 
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.python.org")
    
   # def test_example(self):     #this will be run automatically because it starts with the keyword test (lowercase)
    #    print("test")
    #   assert True
    
    def test_search_python(self):
        #Tests pythn.org search feature. searches for the word 'pycon' then verifies that 
        #some results show up. Note that it does not look for any particular text in search results page, this 
        #test verifies that the results were not empty 

        #load the main page. in this case the homepage of python.org 
        main_Page=page.MainPage(self.driver)
        #checks if the word "python" is in the title 
        assert main_Page.is_title_matches()

        #sets the text of search text box to "pycon"
        main_Page.search_text_element="pycon"
        main_Page.click_go_button()
        Search_Result_Page=page.SearchResultPage(self.driver)
        #verifies that the reults page is not empty 
        assert Search_Result_Page.is_results_found()


    #def tearDown(self):
     #   self.driver.close()

if __name__=="__main__":
    unittest.main()