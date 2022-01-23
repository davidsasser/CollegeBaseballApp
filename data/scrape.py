from bs4 import BeautifulSoup
import os
import csv
import requests
import pandas as pd
import re
from selenium import webdriver
import time

count = 1
for x in range(2016, 2022):
    fr = open(f'./parse.txt', "r")
    lines = fr.readlines()

    for i in lines:
        if(count % 100 == 0):
            time.sleep(10)
        else:
            time.sleep(2)
        if(i == '\n'):
            continue
        else:
            URL = i.format(x)
            DRIVER_PATH = r"C:\Users\David\Downloads\chromedriver_win32 (1)\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=DRIVER_PATH)
            driver.get(URL)
            # print(driver.page_source)
            # print(URL)
            # page = requests.get(URL, headers=headers)
            # print(page.request.headers)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            # print(soup)
            try:
                batting_total = soup.findAll('tr', {"class": "totalsRow"})[0]
                pitching_total = soup.findAll('tr', {"class": "totalsRow"})[1]

                batStats = batting_total.findAll('td', {"class": "align_right"})
                df_batting = pd.read_csv('./batting.csv')
                df_len = len(df_batting)
                t_ids = re.findall(r"\d\d\d\d\d",i)
                if(type(t_ids) == str):
                    t_id = t_ids
                else:
                    t_id = t_ids[0]
                team_list_bat = [t_id, x]
                for stat in batStats:
                    team_list_bat.append(stat.text.strip())
                df_batting.loc[df_len] = team_list_bat
                df_batting.to_csv('./batting.csv', index=False)

                pitStats = pitching_total.findAll('td', {"class": "align_right"})
                df_pitching = pd.read_csv('./pitching.csv')
                df_len = len(df_pitching)
                t_ids = re.findall(r"\d\d\d\d\d",i)
                if(type(t_ids) == str):
                    t_id = t_ids
                else:
                    t_id = t_ids[0]
                team_list_pitch = [t_id, x]
                for stat in pitStats:
                    team_list_pitch.append(stat.text.strip())
                df_pitching.loc[df_len] = team_list_pitch
                df_pitching.to_csv('./pitching.csv', index=False)
            except:
                f = open("missing.txt", "a")
                t_ids = re.findall(r"\d\d\d\d\d",i)
                if(type(t_ids) == str):
                    t_id = t_ids
                else:
                    t_id = t_ids[0]
                f.write("Team: {}, Year: {}\n".format(t_id, x))
                f.close()

        driver.quit()
