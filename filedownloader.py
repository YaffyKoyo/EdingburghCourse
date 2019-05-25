import requests

lineList = list()
with open('stations.txt') as f:
  for line in f:
    lineList.append(line.rstrip('\n'))

for place in lineList:
    url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/{}data.txt".format(place)
    r = requests.get(url)
    with open('{}data.txt'.format(place),'wb') as f:
        f.write(r.content)
