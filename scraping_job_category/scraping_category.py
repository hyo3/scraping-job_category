from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

# Chromeドライバのパスとオプションを設定
chrome_path = 'webdriver/chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument('--headless')  # ヘッドレスモードで起動
# service = Service(executable_path=chrome_path)

# Chromeドライバを起動
with webdriver.Chrome(options=chrome_options) as driver:

    # 指定したURLのページを開く
    url = 'https://www.soumu.go.jp/toukei_toukatsu/index/seido/shokgyou/kou_h21.htm#grp_e'
    driver.get(url)
    driver.implicitly_wait(2)

    major_category = driver.find_element(By.XPATH, "//*[@id=\"contentsWrapper\"]/div[2]/div/div/div[1]")

    major_category_list = list(map(lambda category: category.text.split("－")[1] ,major_category.find_elements(By.TAG_NAME, "li")))

    sleep(3)
    
    sub_category = driver.find_elements(By.TAG_NAME, "h3")
    sub_category_list = list(map(lambda category: category.text.split("－")[1], sub_category))
    print(sub_category_list)

    sleep(3)
    
    sub_classification = driver.find_elements(By.CSS_SELECTOR, "h3 + ul > li")
    sub_classification_list = list(map(lambda category: category.text.split("　")[1], sub_classification))
    print(sub_classification_list)