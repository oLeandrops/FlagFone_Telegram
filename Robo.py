from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


urlPrincipal = 'https://web.telegram.org/z/'
browser = Firefox()
browser.get(urlPrincipal)
qr = input('Realizou o QRCode').upper()

if qr == 'SIM':
    print('Feito')
consultados = []
dados = {}

WDW = WebDriverWait(browser,10)


telefones = ['11986828520','11932481472','11984914952','11958067827','47999555900']
for tel in telefones:
    urlConversa = f'https://t.me/+55{tel}'
    browser.get(urlConversa)

#CLICAR NO ICONE OPEN IN WEB

    ancoras = browser.find_elements(By.CSS_SELECTOR,'a')
    ancoras[3].click()

    #locator = By.CSS_SELECTOR,'[class*="status"]>span'
    #locator = By.CSS_SELECTOR,'[class="ChatInfo"]'
    locator = By.CSS_SELECTOR,'#editable-message-text'
    #browser.find_elements(By.CSS_SELECTOR,'#editable-message-text')

    status = None

    try:
        WDW.until(
        presence_of_element_located(locator=locator),
        message='Telefone Não existe')
        aguardando = browser.find_element(By.CSS_SELECTOR,'[class*="status"]>span').text
        while aguardando == '':
             aguardando = browser.find_element(By.CSS_SELECTOR,'[class*="status"]>span').text
        status = browser.find_element(By.CSS_SELECTOR,'[class*="status"]>span').text
        fullNome = browser.find_element(By.CSS_SELECTOR,'[class="ChatInfo"] h3').text
        print(status)
    except:
        status = 'Telefone Inexistente No Telegram'
        fullNome = None
    finally:
        dados = {'tel':tel,'status':status,'nome':fullNome}
        consultados.append(dados)
        del status