import scrapy

import json


class Ecp2Spider(scrapy.Spider):
    name = 'ecp2f'
    allowed_domains = ['https://ecp.sgcc.com.cn/ecp2.0/']
    sum = 0

    def start_requests(self):
        urls = [
            'https://ecp.sgcc.com.cn/ecp2.0/portal/#/doc/',
        ]
        with open('notelist.json', 'r', encoding='utf-8') as jf:
            data = json.load(jf)
            # n = 0
            for note in data['resultValue']['noteList']:
                # n += 1
                # print(n)
                # print(note['publishOrgName'])
                noteurl = "{}{}/{}_2018060501171111".format(urls[0], note['doctype'], note['noticeId'])
                if note['doctype'] == 'doc-com':
                    noteurl = "{}{}/{}_2018060501171111".format(urls[0], note['doctype'], note['firstPageDocId'])
                # print(noteurl)
                yield scrapy.Request(url=noteurl, callback=self.parse)

    def parse(self, response):
        # attach = response.css('a[_ngcontent-c10] span[_ngcontent-c10]::text').extract_first()
        attach = response.css('h1::text').extract_first()
        # if attach:
            # self.sum += 1
        print(attach)
        # print(self.sum)
