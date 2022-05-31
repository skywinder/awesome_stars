import requests
import json

file_md = open('test.md')
result = open('result.md', 'w')
result = open('result.md', 'a', encoding='utf-8')

linktext = ''
stars = ''
jsonrep = {}

for line in file_md:
    s = line
    if ((s.find('![') == -1) and (s.find('//github.com') != -1)):
        link = s[s.find('//github.com/') + 13:s.find(')')]
        print(link)
        res = requests.get('https://api.github.com/repos/' + link)
        print(res.status_code)
        if res.status_code :
            #print(res.text)
            jsonrep = json.loads(res.text)
            print(jsonrep["stargazers_count"], '\n')
            stars = str(jsonrep["stargazers_count"])
            linktext = s[s.find('[') + 1:s.find(']')]
            result.write(s[0:s.find('[') + 1] + linktext + ' ★ ' + stars + s[s.find(']'):])
    else:
        result.write(s)
result.close()
print('complete')
