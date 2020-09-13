import scrapy
from scrapy.http import JsonRequest

import json


class Ecp2Spider(scrapy.Spider):
    name = 'ecp2f'
    allowed_domains = ['https://ecp.sgcc.com.cn/ecp2.0/']
    sum = 0

    # https://ecp.sgcc.com.cn/ecp2.0/ecpwcmcore//index/downLoad?fileId=2020032342120992&a=b
    # https://ecp.sgcc.com.cn/ecp2.0/ecpwcmcore//index/downLoadWin?notice=2020090869625830
    def start_requests(self):
        urls = [
            'https://ecp.sgcc.com.cn/ecp2.0/portal/#/doc/',
            'https://ecp.sgcc.com.cn/ecp2.0/ecpwcmcore//index/getNoticeWin',
            'https://ecp.sgcc.com.cn/ecp2.0/ecpwcmcore//index/getDoc',
        ]
        with open('notelist.json', 'r', encoding='utf-8') as jf:
            data = json.load(jf)
            for note in data['resultValue']['noteList']:
                noteurl = "{}{}/{}_2018060501171111".format(urls[1], note['doctype'], note['noticeId'])
                param = note['noticeId']
                nurl = urls[1]
                if note['doctype'] == 'doc-com':
                    noteurl = "{}{}/{}_2018060501171111".format(urls[0], note['doctype'], note['firstPageDocId'])
                    param = note['firstPageDocId']
                    nurl = urls[2]
                print(noteurl)
                # yield scrapy.Request(url=noteurl, callback=self.parse)
                yield JsonRequest(url=nurl, data=param)
        # data = 2020091177137366
        # yield JsonRequest(url='https://ecp.sgcc.com.cn/ecp2.0/ecpwcmcore//index/getNoticeWin', data=data)

    def parse(self, response):
        data = json.loads(response.body)
        print(data['successful'])
        # attach = response.css('a[_ngcontent-c10] span[_ngcontent-c10]::text').extract_first()
        # attach = response.css('h1::text').extract_first()
        # if attach:
            # self.sum += 1
        # print(attach)
        # print(self.sum)
