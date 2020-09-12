import scrapy
from scrapy.http import JsonRequest

import json


class Ecp2Spider(scrapy.Spider):
    name = 'ecp2'
    allowed_domains = ['https://ecp.sgcc.com.cn/ecp2.0/']

    def start_requests(self):
        urls = [
            'https://ecp.sgcc.com.cn/ecp2.0/ecpwcmcore//index/noteList/',
        ]
        data = {
            "index": 1,
            "size": 800,
            "firstPageMenuId": "2018060501171111",
            "orgId": "",
            "key": "",
            "year": ""
        }
        yield JsonRequest(url=urls[0], data=data)

    def parse(self, response):
        data = json.loads(response.body)
        if not data['successful']:
            print('Data fetch error!')
            return
        
        with open('notelist.json', 'w', encoding='utf-8') as jf:
            json.dump(data, jf, ensure_ascii=False)
        # for note in data['resultValue']['noteList']:
        #     print(note['publishOrgName'])
        #     noteurl = "https://ecp.sgcc.com.cn/ecp2.0/portal/#/doc/{}/{}_2018060501171111".format(note['doctype'], note['noticeId'])
        #     print(noteurl)
        
        # print(data['resultValue']['noteList'][0]['publishOrgName'])
