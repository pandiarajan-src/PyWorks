import time
import json

def to_json(python_object):
    if isinstance(python_object, time.struct_time):          #①
        return {'__class__': 'time.asctime',
                '__value__': time.asctime(python_object)}    #②
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': list(python_object)}
    raise TypeError(repr(python_object) + ' is not JSON serializable')


def from_json(json_object):                                  #①
    if '__class__' in json_object:                           #②
        if json_object['__class__'] == 'time.asctime':
            return time.strptime(json_object['__value__'])   #③
        if json_object['__class__'] == 'bytes':
            return bytes(json_object['__value__'])           #④
    return json_object

entry = {'comments_link': None,
            'internal_id': b'\xDE\xD5\xB4\xF8',
            'title': 'Dive into history, 2009 edition',
            'tags': ('diveintopython', 'docbook', 'html'),
            'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
            'published': True
        }

with open('entry.json', 'w', encoding='utf-8') as f:
     json.dump(entry, f, default=to_json)

with open('entry.json', 'r', encoding='utf-8') as f:
     entry = json.load(f, object_hook=from_json)

print (entry['tags'] )                                                     #②
#('diveintopython', 'docbook', 'html')

print(entry['internal_id'])