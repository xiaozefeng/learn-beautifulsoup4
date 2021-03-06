#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc)
print(soup.prettify())
print('title:', soup.title)
print('title.name:', soup.title.name)
print('title.string:', soup.title.string)
print('title.parent.name:', soup.title.parent.name)
print('title.p.class:', soup.p['class'])
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id='link3'))

