import requests
from bs4 import BeautifulSoup
from datetime import datetime


covid_website = requests.get('https://www.mygov.in/covid-19/',timeout =5)
covid_tracker = BeautifulSoup(covid_website.text,'html.parser')
covid_kerala = BeautifulSoup(covid_website.text,'html.parser')
checking_kerala_cases = covid_kerala.tbody

print(covid_website.status_code)
# print(checking_kerala_cases.prettify())
kerala_case = checking_kerala_cases.find_all("tr") 

for kerala in kerala_case :
    if kerala.find("td").text == 'Kerala':
        # Kerala_text = json.loads(str(kerala.text))
        kerala_name =str(kerala.text)[0:7]
        kerala_total_cases = str(kerala.text)[7:11]
        kerala_active_cases = str(kerala.text)[11:14]
        # # x = list(kerala.text.split(','))
    # if kerala.find(class_="st_name").text == 'Kerala':
    #     kerala_case = kerala.text
print(f"State Name : {kerala_name}")
print(f"Kerala Total Cases : {kerala_total_cases}")
print(f"Kerala Active Cases : {kerala_active_cases}")
# print(len(all_states[1]))
# print('COVID19 Cases in Kerala')
# print(kerala_case)
# print(checking_kerala_cases.prettify())

checking_span = covid_tracker.find_all("span",class_="icount")

print('')
print("COVID19 Cases in India")
print('')
print(f"Date : {datetime.now().strftime('%x')}")
print(f"Active Cases : {checking_span[0].text}")
print(f"Discharged/Cured Case : {checking_span[1].text}")
print(f"Number of Deaths : {checking_span[2].text}")
total_cases = int(checking_span[0].text)+int(checking_span[1].text)+int(checking_span[2].text)

print(f"Total Cases in India : {total_cases}")




