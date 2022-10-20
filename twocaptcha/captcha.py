
from twocaptcha import TwoCaptcha
from twocaptcha import api

def get_captcha(image_path):
    # URL = "https://www.ktbnetbank.com/consumer"
    # webbrowser.open(URL)  # Go to example.com

    # page = requests.get(URL)
    # soup = BeautifulSoup(page.content, "html.parser")
    # results = soup.find(id="imageCodeDisplayId")

    # URL_CAPCHA = "https://www.ktbnetbank.com"+results["src"]
    solver = TwoCaptcha(api.key)
    
    result = solver.normal(image_path)
    return result['code']
    