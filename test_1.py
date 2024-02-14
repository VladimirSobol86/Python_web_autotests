import yaml
import time
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    
# site = Site(testdata["address"])

# def test_with_invalid_values(path_login, path_password, button_selector, 
#                err_label_selector, err_label_text, site):
    
#     input1 = site.find_element("xpath", path_login)
#     input1.send_keys("invalid login")
    
#     input2 = site.find_element("xpath", path_password)
#     input2.send_keys("invalid pass")
    
#     btn = site.find_element("css", button_selector)
#     btn.click()
    
#     error_label = site.find_element("xpath", err_label_selector)
#     assert error_label.text == err_label_text
    
#     time.sleep(3)

def test_with_correct_values(site, path_login, path_password, 
                             button_selector, btn_home_selector, 
                             btn_home_text, btn_create_blog, path_title, 
                             btn_save_blog, title_after_creation, title_text):
    input1 = site.find_element("xpath", path_login)
    input1.send_keys(testdata["login"])
    
    input2 = site.find_element("xpath", path_password)
    input2.send_keys(testdata["password"])
    
    btn = site.find_element("css", button_selector)
    btn.click()
    
    btn_home = site.find_element("xpath", btn_home_selector)
    assert btn_home.text == btn_home_text
#HW code is below______________________________________    
    btn_create = site.find_element("xpath", btn_create_blog)
    btn_create.click()
    time.sleep(2)
    
    title = site.find_element("xpath", path_title)
    title.send_keys(title_text)
    time.sleep(2)
    
    btn_save = site.find_element("xpath", btn_save_blog)
    btn_save.click()
    time.sleep(2)
        
    title_path = site.find_element("xpath", title_after_creation)
    assert title_path.text == title_text
    time.sleep(2)
    
    