# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json
import collections

def to_utf8(text, errors='strict', encoding='utf8'):
    """Convert a string (unicode or bytestring in `encoding`), to bytestring in utf8."""
    if isinstance(text, unicode):
        return text.encode('utf8')
    # do bytestring -> unicode -> utf8 full circle, to ensure valid utf8
    return unicode(text, encoding, errors=errors).encode('utf8')

def to_unicode(text, encoding='utf8', errors='strict'):
    """Convert a string (bytestring in `encoding` or unicode), to unicode."""
    if isinstance(text, unicode):
        return text
    return unicode(text, encoding, errors=errors)

def convert(data):
    """Convert any type string in list or dict to utf-8."""
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

def cleanify(s):
    if isinstance(s, list):
        return [cleanify(string) for string in s]
    if isinstance(s, dict):
        return {cleanify(k):cleanify(v) for k,v in s.items()}
    return ''.join(s.split())

def jsonify(o):
    return json.dumps(convert(o), encoding='utf-8', ensure_ascii=False)

def get_item(selector, xpath_statement):
    try:
        item = selector.xpath(xpath_statement).extract()
        if len(item) == 1:
            return convert(item[0])
        else:
            return item
    except Exception as e:
        print e
        return ''
