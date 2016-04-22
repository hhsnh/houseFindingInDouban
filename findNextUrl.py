import requests, bs4, sys, webbrowser
def findNextUrl(currentUrl):
    res = requests.get(currentUrl)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    nextLink = soup.select('link[rel="next"]')[0]
    url= nextLink.get('href')
    return url
