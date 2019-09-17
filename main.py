from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#  Abrir pagina
driver = webdriver.Chrome()
driver.get('https://webtrader.binary.com/')  # site da binary
driver.maximize_window()
action = ActionChains(driver)
sleep(3)
user = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/button').click()
sleep(10)

#  Fazer Login
btn_login = driver.find_element_by_xpath(
    "/html/body/nav/div[3]/div/div[2]/ul[1]/li[2]/button").click()  # Primeiro botao de login
sleep(4)
btn_login2 = driver.find_element_by_xpath('//*[@id="windows-dialog-3"]/div/div[1]/button').click()  # segundo Botao
sleep(5)
txt_email = driver.find_element_by_id('txtEmail').send_keys('Mudar antes de Rodar')
txt_senha = driver.find_element_by_id('txtPass').send_keys('Mudar antes de Rodar')
entrar = driver.find_element_by_name('login').click()
sleep(10)

#  mudar para conta virtual
conta = driver.find_element_by_id('main-account').click()
conta_virtual = driver.find_element_by_class_name('login-id-list').click()
sleep(5)
# configurar workspace
janela_fechar = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/button/span[1]').click()
janela_abrir = driver.find_element_by_xpath('/html/body/nav/div[3]/div/ul/li[1]/a')
janela_abrir.click()
sleep(2)
janela_abrir = driver.find_element_by_xpath('/html/body/nav/div[3]/div/ul/li[1]/ul/li[4]/div')  # Volatility
action.move_to_element(janela_abrir).perform()
janela_abrir = driver.find_element_by_xpath('/html/body/nav/div[3]/div/ul/li[1]/ul/li[4]/ul/li[1]')  # Continuos
action.move_to_element(janela_abrir).perform()
janela_abrir = driver.find_element_by_xpath('/html/body/nav/div[3]/div/ul/li[1]/ul/li[4]/ul/li[1]/ul/li[4]')  # 10
janela_abrir.click()
sleep(2)
metodo_entrada = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/ul[9]/li[1]/span/span[2]')
metodo_entrada.click()
metodo_entrada = driver.find_element_by_xpath('/html/body/div[6]/div[7]/ul/li[2]/div').click()
payout = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/ul[9]/li[3]/input')
payout.clear()
payout.send_keys(input('Qual o valor da sua entrada: '))
# olhar o tick e dar entradas
azul = 0
tick = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/ul[1]/li[4]/span')
tick_atual = 0
vermelho = 0
comprado = False
VelasVermelhas = int(input('Quantos velas vermelhas para entrar de compra? '))
while True:

    if tick.text != tick_atual:
        cor = tick.value_of_css_property('background-color')
        if cor == 'rgba(204, 0, 51, 1)':
            print('Vermelho')
            vermelho += 1
            print(f'Ja foram {vermelho} ticks vermelhos em sequencia')
        elif cor == 'rgba(41, 171, 226, 1)':
            print('Azul')
            vermelho = 0
        tick_atual = tick.text
        print(f'Tick na variavel {tick_atual}, tick no site {tick.text}')
    if vermelho >= VelasVermelhas and not comprado:
        comprar = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/ul[16]/li[2]/button').click()
        comprado = True
        sleep(15)
        fechar_compra = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/span').click()
        comprado = False
        vermelho = 0
    sleep(0.5)
