from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

class web_scrapping_data():

    def get_data_all_players(website):
        _website = website
        driver = webdriver.Chrome()
        driver.get(_website)

        statistic_players_button = driver.find_element(By.XPATH,'//div[@data-tabid="2"]')
        statistic_players_button.click()

        data_players = driver.find_elements(By.TAG_NAME,'tr')
        data_players = data_players[1:33]

        nomes = []
        gols = []
        assist = []
        desarmes = []
        passes_certos = []
        duelos_ganhos = []
        duelos_ganhos_chao = []
        duelos_ganhos_aereo = []
        min_jogados = []
        nota_sofa = []

        for data_player in data_players:
            nomes.append(data_player.find_element(By.XPATH,'./td[2]').text)
            gols.append(data_player.find_element(By.XPATH,'./td[3]').text)
            assist.append(data_player.find_element(By.XPATH,'./td[4]').text)
            desarmes.append(data_player.find_element(By.XPATH,'./td[5]').text)
            passes_certos.append(data_player.find_element(By.XPATH,'./td[6]').text)
            duelos_ganhos.append(data_player.find_element(By.XPATH,'./td[7]').text)
            duelos_ganhos_chao.append(data_player.find_element(By.XPATH,'./td[8]').text)
            duelos_ganhos_aereo.append(data_player.find_element(By.XPATH,'./td[9]').text)
            min_jogados.append(data_player.find_element(By.XPATH,'./td[10]').text)
            nota_sofa.append(data_player.find_element(By.XPATH,'./td[12]').text)

        driver.quit()
        
        list_of_data = [nomes,gols,assist,desarmes,passes_certos,duelos_ganhos,duelos_ganhos_chao,duelos_ganhos_aereo,min_jogados,nota_sofa]
    
        return list_of_data 
    
 
    
    def create_csv(datas):
        df = pd.DataFrame({'Nome': datas[0], 'Gols': datas[1], 'Assistencia': datas[2], 'Desarmes': datas[3] , 'Passes certos': datas[4] ,'Duelos ganhos': datas[5], 'Duelos no chao (ganho)': datas[6], 'Duelos areos (ganho)': datas[7], 'Minutos jogados': datas[8], 'Nota Sofascore': datas[9]})
        df.to_csv('statistics game.csv', index=False)
        return df
    

    def get_data_team_players(website):
        _website = website
        driver = webdriver.Chrome()
        driver.get(_website)

        statistic_players_button = driver.find_element(By.XPATH,'//div[@data-tabid="2"]')
        statistic_players_button.click()

        time.sleep(10)

        teams_name = _website.split('/')[-2]

        if('vasco' in teams_name):
            team_name = 'Vasco da Gama' 
        elif('flamengo' in teams_name):
            team_name = 'Flamengo'   
        elif('fluminense' in teams_name):
            team_name = 'Fluminense'
        elif('botafogo in teams_name'):
            team_name = 'Botafogo'
        else:
            return print("Tente outro link")

        home_team = driver.find_element(By.CLASS_NAME,'sc-jEACwC.kXttfL').text.split('-')[0]
        print(team_name)
        print(home_team)
        if(team_name == home_team):
            team_statistic_players_button = driver.find_elements(By.CLASS_NAME,'sc-eDPEul eEgeRl')
            print(team_statistic_players_button)
           #team_statistic_players_button[2].click()
        else:
            team_statistic_players_button = driver.find_elements(By.CLASS_NAME,'sc-eDPEul eEgeRl')
            print(team_statistic_players_button)
           # team_statistic_players_button[0].click()

        data_players = driver.find_elements(By.TAG_NAME,'tr')
        data_players = data_players[1:33]

        nomes = []
        gols = []
        assist = []
        desarmes = []
        passes_certos = []
        duelos_ganhos = []
        duelos_ganhos_chao = []
        duelos_ganhos_aereo = []
        min_jogados = []
        nota_sofa = []

        for data_player in data_players:
            nomes.append(data_player.find_element(By.XPATH,'./td[2]').text)
            gols.append(data_player.find_element(By.XPATH,'./td[3]').text)
            assist.append(data_player.find_element(By.XPATH,'./td[4]').text)
            desarmes.append(data_player.find_element(By.XPATH,'./td[5]').text)
            passes_certos.append(data_player.find_element(By.XPATH,'./td[6]').text)
            duelos_ganhos.append(data_player.find_element(By.XPATH,'./td[7]').text)
            duelos_ganhos_chao.append(data_player.find_element(By.XPATH,'./td[8]').text)
            duelos_ganhos_aereo.append(data_player.find_element(By.XPATH,'./td[9]').text)
            min_jogados.append(data_player.find_element(By.XPATH,'./td[10]').text)
            nota_sofa.append(data_player.find_element(By.XPATH,'./td[12]').text)

        driver.quit()
        
        list_of_data = [nomes,gols,assist,desarmes,passes_certos,duelos_ganhos,duelos_ganhos_chao,duelos_ganhos_aereo,min_jogados,nota_sofa]
    
        return list_of_data 


game_data = web_scrapping_data.get_data_team_players('https://www.sofascore.com/pt/madureira-vasco-da-gama/zOsFOc#id:11873049')
print(web_scrapping_data.create_csv(game_data))