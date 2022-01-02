
from twocaptcha import TwoCaptcha
from selenium import webdriver
#This is an example how to use the TwoCaptcha Api with Selenium. Note a better way to submit your form is to use js with submit(). But when you have a clear button selenium works just fine. 
api_key = "insertAPIkey"
url = "website_url"


web=webdriver.Chrome()
web.get(url)

solver = TwoCaptcha(api_key)
result = solver.recaptcha('insertSitekeyhere',
                          'insertWebsitehere',
                        )

token=str(result["code"])
##JS script that inserts the token
web.execute_script("document.getElementById('g-recaptcha-response').innerHTML='"+token+"';") 
##submits the form
web.find_element_by_id("recaptcha-demo-submit").click()

