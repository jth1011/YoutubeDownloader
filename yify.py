import requests
import sys
if True:
    name = ""
    for i in range(len(sys.argv)):
        if (i==0):
            continue
        else:
            name = name + " " + sys.argv[i]
    name = name.strip()
    name = name.replace(" ","+")
    url = "https://yts.am/api/v2/list_movies.json?limit=1&order_by=asc&query_term=" + name
    resp = requests.get(url)
    if (200!=resp.status_code):
        url="this wont work"
        exit()
    data = resp.json()
    if 'movies' not in data['data']:
        url="this wont work"
        exit()
    got_7 = False
    url = ""
    for movie in data['data']['movies']:
       for torrent in movie['torrents']:
            if torrent['quality']=="720p":
                got_7 = True
                url = torrent['url']
                break
    if got_7 == False:
        for movie in data['data']['movies']:
            for torrent in movie['torrents']:
                if torrent['quality']=="1080p":
                    url = torrent['url']
                    break
    print(url)

