import requests
import json
import urllib3
import string
import random
from __colors__.colors import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class EduHelper:
    def __init__(self, id):
        self.url = 'https://www.openccc.net/f-vs-stand-I-hat-of-yout-ands-Banquoh-Cumberland?d=www.openccc.net'
        self.h = {
            'accept': 'application/json; charset=utf-8',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
            'content-type': 'text/plain; charset=utf-8',
            'origin': 'https://www.openccc.net'
        }

        self.url1 = 'https://www.openccc.net/cccacct-proxy/createAccount?locale=en&source=https://www.opencccapply.net/SSOLogin/{idd}/false/en'.format(idd=id)

        
        self.urlxd = 'https://www.openccc.net/cccacct-proxy/createAccount?locale=en&source=https://www.opencccapply.net/SSOLogin/{idd}/false/en'.format(idd=id)

        self.url2 = 'https://www.openccc.net/f-vs-stand-I-hat-of-yout-ands-Banquoh-Cumberland?d=www.openccc.net'

        self.h2 = {
            'accept': 'application/json; charset=utf-8',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
            'content-type': 'text/plain; charset=utf-8',
            'origin': 'https://www.openccc.net',
            'sec-fetch-site': 'same-origin'
        }
        
        self.url3 = 'https://www.openccc.net/uPortal/p/AccountCreation.ctf1/max/action.uP?pP_execution=e1s1'
        self.h3 = {
            'origin': 'https://www.openccc.net',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin'
        }
        self.cookie = {
            'reese84': None
        }

        self.session = requests.Session()
    
    def getAuthToken(self):
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Fetching Token', end='')
        data = {
            'solution': {
                'interrogation': {
                    'p': ''.join(random.choices(string.ascii_lowercase + string.digits, k=40)),
                    'st': 1627823618,
                    'sr': 9090987876,
                    'cr': 678989098
                },
                'version': 'stable'
            },
            'old_token': None,
            'error': None,
            'performance': {
                'interogation': 248
            }
        }

        res = self.session.post(url=self.url, data=json.dumps(data), headers=self.h, verify=False)
        
        js = res.json()
        token = js['token']
        self.cookie['reese84'] = token
        print(fg + ' (success)')
        return token
    
    def _tryHarder(self):
        token = self.getAuthToken()
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Fetching Cookies', end='')
        self.session.get(url=self.url1, cookies=self.cookie, headers=self.h, verify=False)
        print(fg + ' (success)')

        data2 = '"{tok}"'.format(tok=token)
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Sending Custom Fields and Token to Server', end='')
        resp = self.session.post(url=self.url2, data=data2, headers=self.h2, verify=False)
        print(fg + ' (success)')
        js = resp.json()
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Setting Incap Token', end='')
        token = js['token']
        self.cookie['reese84'] = token
        print(fg + ' (success)')

        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Sending Custom Cookies', end='')
        data3 = '_eventId_continue=&flowId=e1s1'
        resp3 = self.session.post(url=self.url3, data=data3, headers=self.h3, cookies=self.cookie, verify=False)
        print(fg + ' (success)')

        return resp3.url, self.session.cookies, token