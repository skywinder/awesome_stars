import requests
import json

awesome_url = "https://raw.githubusercontent.com/vinta/awesome-python/master/README.md"
response = requests.get(awesome_url)
open('source.md', "wb").write(response.content)
source_md = open('source.md')
result = open('result.md', 'w')
result = open('result.md', 'a', encoding='utf-8')

linktext = ''
stars = ''
jsonrep = {}

for line in source_md:
    s = line
    # TODO: add exception handling
    if (s.find('![') == -1) and (s.find('//github.com') != -1):
        link = s[s.find('//github.com/') + 13:s.find(')')]
        print(link)
        # TODO: add github api token
        res = requests.get('https://api.github.com/repos/' + link)
        print(res.status_code)
        # TODO: check status_code == 200  or res.json()['stargazers_count'] != None
        if res.status_code:
            jsonrep = json.loads(res.text)
            print(jsonrep["stargazers_count"], '\n')
            stars = str(jsonrep["stargazers_count"])
            linktext = s[s.find('[') + 1:s.find(']')]
            line_with_stars = s[0:s.find('[') + 1] + linktext + ' ★ ' + stars + s[s.find(']'):]
            result.write(line_with_stars)
    else:
        result.write(s)
result.close()
print('complete')
