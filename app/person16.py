#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'BuGoNee'


'''
Some Explaination should be in here.
'''
import requests
from parsel import Selector

class Person(object):

    def __init__(self):
        self.url = 'https://www.16personalities.com/test-results'
        self.headers = {
            'Origin': 'https://www.16personalities.com',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.73 Chrome/47.0.2526.73 Safari/537.36',
            }
        self.timeout = 15

        self.s = requests.session()
        r = self.s.get('https://www.16personalities.com/', timeout=self.timeout)

        sel = Selector(r.text)
        xp= '//*[@id="login-dialog"]/div/div/div[2]/form/input/@value'
        self.token = sel.xpath(xp).extract()[0]
        print self.token

    def get_result(self, data, timeout=None):
        if not timeout:
            timeout = self.timeout
        if isinstance(data, list):
            payload = {'a'+str(i+1):data[i] for i in range(60)}
        elif isinstance(data, dict):
            payload = data.copy()
        payload['_token'] = self.token
        payload['options'] = 'on'
        payload['code'] = ''

        r = self.s.post(self.url, headers=self.headers, data=payload, timeout=timeout)
        html = r.text

        sel = Selector(html)
        result = {}
        xp = '/html/body/div[2]/div[4]/div[1]/div/div[1]/div/span[1]/text()'
        result['type_nice'] = sel.xpath(xp).extract_first()
        xp = '/html/body/div[2]/div[4]/div[1]/div/div[1]/div/span[2]/text()'
        result['type_acronym'] = sel.xpath(xp).extract_first()

        xp = '/html/body/div[2]/div[4]/div[1]/div/div[2]/div[2]/div'
        div = sel.xpath(xp)[:5]
        for d in div:
            attribute = d.xpath('div[1]/text()').extract()[0]
            left_attribute_score = d.xpath('div[4]/div[1]/div/text()').extract()[0]
            left_attribute_title = d.xpath('div[4]/div[1]/span/text()').extract()[0]
            right_attribute_score = d.xpath('div[4]/div[2]/div/text()').extract()[0]
            right_attribute_title = d.xpath('div[4]/div[2]/span/text()').extract()[0]
            result[attribute+'-'+left_attribute_title] = left_attribute_score
            result[attribute+'-'+right_attribute_title] = right_attribute_score
        result.update(payload)
        del result['code']
        del result['_token']
        del result['options']
        return result

            #             'type_nice',
            #             'type_acronym',
            #             'Mind-Extraverted',
            #             'Mind-Introverted',
            #             'Energy-Intuitive',
            #             'Energy-Observant',
            #             'Nature-Thinking',
            #             'Nature-Feeling',
            #             'Tactics-Judging',
            #             'Tactics-Prospecting',
            #             'Identity-Assertive',
            #             'Identity-Turbulent',

if __name__ == '__main__':
    p = Person()
    data = [-3 for i in range(60)]
    result = p.get_result(data)
    print result
    pass

