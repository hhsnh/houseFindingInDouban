import requests, bs4, sys, webbrowser
# a function to find nextlink or prelink in current page
def findReltLink(currentUrl,flag='n'):
    if flag=='p':
        direct='prev'
    else:
        direct='next'
    res = requests.get(currentUrl)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    nextLink = soup.select('link[rel='+direct+']')[0]
    return nextLink.get('href')
