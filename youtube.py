import os
import sys
import requests

def main():
    name = ""
    for i in range(len(sys.argv)):
        if (i==0):
            continue
        else:
            name = name + " " + sys.argv[i]
    name = name.strip()
    name = name.replace(" ","+")
    if (name == ""):
        print("Nothing to Search")
        exit()
    url = "https://www.googleapis.com/youtube/v3/search/?key=AIzaSyCPpjgXrEJcPFm1PuxEfmwWKH1u2s-7H6s&part=snippet&type=video&maxResults=1&order=relevance&q=" + name
    resp = requests.get(url)
    resp=resp.json()
    vid=resp['items'][0]['id']['videoId']
    print(vid)

if __name__ == "__main__":
    main()