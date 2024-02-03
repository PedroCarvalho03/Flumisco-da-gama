from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
import time

# Para usar basta passar a rodada e a funcao ira retornar o print com os resultados da rodada
def print_scoreboard(round):
    driver = webdriver.Chrome()
    driver.get('https://www.sofascore.com/pt/torneio/futebol/brazil/carioca/92')


    # Aperta o botão para aparecer os resultados da rodada
    round_button = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[2]/div[2]')
    round_button.click()

    # referencia para o lugar onde vamos parar no scroll
    scroll_reference = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[2]/div/div[3]/div')

    # Execute um script JavaScript para rolar a página para o elemento
    driver.execute_script("arguments[0].scrollIntoView();", scroll_reference)
    
    time.sleep(10)

    # Localiza o elemento da dropdown
    dropdown_element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[1]/div[2]')

    # Clica no elemento da dropdown para expandi-la
    dropdown_element.click()

    # Aguarda até que as opções da dropdown sejam carregadas (você pode ajustar o tempo conforme necessário)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/ul')))
    
    time.sleep(5)

    # Localiza e clica na opção desejada na dropdown
    option_element = driver.find_element(By.XPATH,f'//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/ul/li[{str(round)}]')
    driver.execute_script("arguments[0].click();", option_element)

    time.sleep(5)
    
    # Captura de tela do elemento
    png = driver.get_screenshot_as_png()
    im = Image.open(BytesIO(png))
    left = 14
    top = 268
    right = 420
    bottom = 700

    #corta a imagem em um retangulo
    im = im.crop((left, top, right, bottom))

    driver.quit()

    return im

def print_lineup(url):
    driver = webdriver.Chrome()
    driver.get(url) 

    scroll = 900
    driver.execute_script(f"window.scrollBy(0, {scroll});")

     # Captura de tela do elemento
    png = driver.get_screenshot_as_png()
    im = Image.open(BytesIO(png))
    left = 470
    top = 230
    right = 1230
    bottom = 800

    #corta a imagem em um retangulo
    im = im.crop((left, top, right, bottom))

    driver.quit()

    return im

def save_image(image, output_file):
    # Salva a imagem em um arquivo
    image.save(output_file, 'PNG')

image = print_lineup('https://www.sofascore.com/pt/nova-iguacu-vasco-da-gama/zOsGOc#id:11873060')
save_image(image, 'print.png')
