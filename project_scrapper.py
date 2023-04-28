from bs4 import BeautifulSoup
import requests
import time
import csv

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

response = requests.get(url)

# print(response.text)

# f = open("data.txt", "w+")
# f.writelines(response.text)
# f.close()

def main():
    headers = ['V. Mag', 'Proper Name', 'Bayer designation', 'Distance', 'Spectral class', 'Mass', 'Radius', 'Luminosity']
    # print(response.text)
    star_data = []
    for i in range(0, 10):
        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all('table', attrs={'class':"wikitable sortable"})
        # print(tables)
        for table in tables:
            # print("table")
            tbody_tags = table.find_all('tbody')
            for tbody_tag in tbody_tags:
                # print("tbody")
                tr_tags = tbody_tag.find_all('tr')
                for tr_tag in tr_tags:
                    temp_list = []
                    # print("tr")
                    td_tags = tr_tag.find_all('td')
                    for td_tag in td_tags:
                        temp_list.append(td_tag.text)
                    star_data.append(temp_list)
    star_data.pop(0)
 
    with open("project_scrapper.csv", "w", encoding="utf-8") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)




main()

