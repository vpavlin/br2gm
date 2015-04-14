#!/usr/bin/env python

from __future__ import print_function
import os,sys
from bs4 import BeautifulSoup
import urllib2

class Parser():
    soup = None
    __songs_list = []
    def __init__(self, url):
        content = self.loadHtml(url)
        self.soup = BeautifulSoup(content)

    def loadHtml(self, url):
        print("Pulling content from %s" % url)
        response = urllib2.urlopen(url)
        content = response.read()

        return content

    def getSongsList(self):
        get_info = {"artist": self.getArtist, "title": self.getSongTitle}
        for item in self.soup.find_all("div", class_="cht-entry-details"):
            item_data = {"artist": None, "title": None}
            for key, func in get_info.iteritems():
                item_data[key] = func(item)
            self.__songs_list.append(item_data)

        return self.__songs_list

    def getArtist(self, data):
        return data.find("div", class_="cht-entry-artist").get_text().strip()

    def getSongTitle(self, data):
        return data.find("div", class_="cht-entry-title").get_text().strip()
            

        
