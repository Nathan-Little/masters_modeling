import requests
from bs4 import BeautifulSoup

URL = "https://www.pgatour.com/stats/stat.120.html"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find('table', attrs = {'id':'statsTable'})
data = []
headings = soup.findAll('th')
print(headings)
for row in table.tbody.findAll('tr'):
    playerData = []
    td = row.findAll('td')
    for col in td:
        #playerData.append("".join(col.text.split()))
        playerData.append(col.text)
    data.append(playerData)



print(data[0])
#for row in data:
#    0:9
#for row in table.findAll('td', attrs = {'class':'player-name'}):
    # create list to house player data
    #playerData = []
    # player name
    #playerName = row.a.text
    #playerData.append(playerName)


    #playerName, playerRank, Rounds, Avg., Total Strokes, Total Adjustment, Total Rounds
    ## for every player, add a row of data to the list
    ## scrape from site, add to playerData, add playerData to data
