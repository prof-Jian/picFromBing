# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests


class Spider:
    def __init__(self):
        self.session = requests.Session()
    
        
        
        
        
    # 下载器    
    def download(self,url):        
            e = self.session.get(url)
            print(e.text)
        

if __name__ == '__main__':
    spider = Spider()
    spider.download('http://photo.hupu.com/nba/tag/%E7%A7%91%E6%AF%94')
