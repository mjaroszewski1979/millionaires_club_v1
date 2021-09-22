from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


# Ensures that the application instance exists
def test_app_exists():
    assert app != None

# Ensures that index page loads correctly
def test_index_get():
    response = client.get("/")
    assert response.status_code == 200
    assert '<title>Millionaires Club - Home</title>' in response.text 
   
# Ensures that about page loads correctly
def test_about():
    response = client.get("/about")
    assert response.status_code == 200
    assert '<title>Millionaires Club - About</title>' in response.text 

# Ensures that countries page loads correctly
def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert '<title>Millionaires Club - G5 Members</title>' in response.text

# Ensures that g5 page loads correctly
def test_g5():
    response = client.get("/g5")
    assert response.status_code == 200
    assert '<title>Millionaires Club - G5 CPI</title>' in response.text 

# Ensures that form works correctly given valid country name
def test_index_post_success():
    response = client.post('/', data = dict(country='poland'))
    assert response.status_code == 200
    assert 'THE LATEST CPI READING FOR POLAND' in response.text

# Ensures that form behaves as expected given invalid country name
def test_index_post_failure():
    response = client.post('/', data = dict(country='wrong'))
    assert response.status_code == 200
    assert 'PLEASE TRY A DIFFERENT COUNTRY!' in response.text


