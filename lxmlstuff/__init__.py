#!/usr/bin/python3

import requests
from lxml import html
from functools import partial

session = requests.Session()

def getTree(url, *a, **kw):
    result = session.get(url, *a, **kw)
    return html.fromstring(result.content)

def postTree(url, *a, **kw):
    result = session.post(url, *a, **kw)
    return html.fromstring(result.content)

def joinPath(paths):
    return '/'.join(paths)

def xpathN(tree, *paths):
    ''' Alias for tree.xpath('//<PATH>') '''
    return tree.xpath('//' + joinPath(paths))

def xpathF(tree, *path):
    ''' Alias for tree.xpath('.//<PATH>') '''
    return tree.xpath('.//' + joinPath(paths))

def xpathN0(tree, *path):
    ''' Alias for tree.xpath('//<PATH>')[0] '''
    return tree.xpath('//' + joinPath(paths))[0]

def xpathF0(tree, *path):
    ''' Alias for tree.xpath('.//<PATH>')[0] '''
    return tree.xpath('.//' + joinPath(paths))[0]

def Tag(name, *args, **kwargs):
    conditions = []

    for arg in args:
        conditions.append(arg)

    for attr, value in kwargs.items():
        if attr == 'Class':
            attr = 'class'
        conditions.append("@%s = '%s'" % (attr, value))

    if conditions:
        return "%s[%s]" % (name, ' and '.join(conditions))
    else:
        return "%s" % name

def Following(tag):
    return "following-sibling::%s" % (tag)

def Contains(**kwargs):
    conditions = []
    for attr, value in kwargs.items():
        if attr == 'Class':
            attr = 'class'
        conditions.append("contains(@%s, '%s')" % (name, value))
    return ' and '.join(conditions)

def dumpElements(elements):
    for element in elements:
        print(element, element.attrib)

A        = partial(Tag, "a")
Div      = partial(Tag, "div")
Span     = partial(Tag, "span")
Input    = partial(Tag, "input")
Textarea = partial(Tag, "textarea")

