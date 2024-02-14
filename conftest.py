import pytest
from module import Site
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture
def path_login():
    x_selector1 = '//*[@id="login"]/div[1]/label/input'
    return x_selector1
  
@pytest.fixture
def path_password():
    x_selector2 = '//*[@id="login"]/div[2]/label/input'
    return x_selector2

@pytest.fixture
def button_selector():
    btn_selector = "button"
    return btn_selector
    
@pytest.fixture
def err_label_selector():
    x_selector3 = '//*[@id="app"]/main/div/div/div[2]/h2'
    return x_selector3

@pytest.fixture
def err_label_text():
    return "401"

@pytest.fixture
def site(scope = "session"):
    site_instance = Site(testdata["address"])
    yield site_instance
    site_instance.close()
    
@pytest.fixture
def btn_home_selector():
    home_text = '//*[@id="app"]/main/nav/a/span'
    return home_text

@pytest.fixture
def btn_home_text():
    return "Home"

#HW fixtures
@pytest.fixture
def btn_create_blog():
    create_btn = '//*[@id="create-btn"]'
    return create_btn

@pytest.fixture
def path_title():
    title_path = '//*[@id="create-item"]/div/div/div[1]/div/label/input'
    return title_path

@pytest.fixture
def btn_save_blog():
    save_btn = '//*[@id="create-item"]/div/div/div[7]/div/button/span'
    return save_btn

@pytest.fixture
def title_after_creation():
    title_ac_path = '//*[@id="app"]/main/div/div[1]/h1'
    return title_ac_path

@pytest.fixture
def title_text():
    return "New post creation"