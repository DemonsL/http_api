# coding:utf-8
import time
from selenium import webdriver
from bs4 import BeautifulSoup

def login(username, password):
    browser = webdriver.Chrome()
    # 用户登录
    browser.get('https://www.wish.com')
    browser.find_element_by_xpath('//*[@id="signup-form"]/div[4]').click()
    browser.find_element_by_xpath('//*[@id="test-le"]').send_keys(username)
    browser.find_element_by_xpath('//*[@id="test-lp"]').send_keys(password)
    browser.find_element_by_xpath('//*[@id="test-elf"]/button').submit()
    cookies = browser.get_cookies()
    # requests 请求
    # req = requests.Session()
    # for cookie in cookies:
    #     req.cookies.set(cookie['name'], cookie['value'])
    # time.sleep(10)
    # resp = req.get('https://www.wish.com/product/5a23bdaef707ed54052e06bb', headers=headers).text
    # selenium 请求 (渲染页面)
    for item in cookies:
        browser.add_cookie({
        'domain': 'www.wish.com',
        'name': item['name'],
        'value': item['value'],
        'path': '/',
        'expiry': None
    })
    time.sleep(10)
    browser.get('https://www.wish.com/product/5a23bdaef707ed54052e06bb')
    return browser


if __name__ == '__main__':
    user = '245576908@qq.com'
    pswd = 'test123'
    browser = login(user, pswd)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    title = soup.find(attrs={'class': 'PurchaseContainer__Name-ghgluL crzchL'}).text
    print(title)
    img = soup.find('img', attrs={'class': 'ProductImageContainer__StripImage-jMdYib fjlNJj'}).get('src')
    print(img)
    price = soup.find(attrs={'class': 'PurchaseContainer__ActualPrice-liXyad cRbBob'}).text
    print(price)
    browser.find_element_by_xpath('//div[@class="PurchaseContainer__RatingWrapper-ebrehg fkCrvt"]').click()
    soup = BeautifulSoup(browser.page_source, 'lxml')
    star = soup.find(attrs={'class': 'ProductReviewContainer__AverageRationgScoreSection-enkDzN hiwWxQ'}).text
    print(star)
    reviews = soup.find(attrs={'class': 'ProductReviewContainer__TotalRating-jITvxa fFhsZP'}).text
    print(reviews)
