import requests, bs4, sys, webbrowser
res = requests.get('https://www.douban.com/group/shanghaizufang/')
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.select('tr .title')
nums=len(elems)
target='徐家汇'
elems_targets=[]
for i in range(nums):
    if target in elems[i].getText():
        elems_targets.append(elems[i].find('a').get('href'))
#print(len(elems_targets))
numOpen = min(5, len(elems_targets))
for i in range(numOpen):
    webbrowser.open(elems_targets[i])
