#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'BuGoNee'


'''
Some Explaination should be in here.
'''

import os
import sys
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])

import json
import falcon
import numpy as np
from sklearn.externals import joblib

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

def max_body(limit):

    def hook(req, resp, resource, params):
        length = req.content_length
        if length is not None and length > limit:
            msg = ('The size of the request is too large. The body must not '
                   'exceed ' + str(limit) + ' bytes in length.')

            raise falcon.HTTPRequestEntityTooLarge(
                'Request body is too large', msg)

    return hook

class ThingsResource(object):
    def __init__(self):
        self.model = MBTI_Test()

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')



    @falcon.before(max_body(64 * 1024))
    def on_post(self, req, resp):
        try:
            data = req.stream.read(req.content_length or 0)
        except KeyError:
            raise falcon.HTTPBadRequest(
                'Missing thing',
                'A thing must be submitted in the request body.')

        resp.status = falcon.HTTP_200
        data = json.loads(data)
        result = self.model.model_predict(data)
        resp.body = json.dumps(result)


class MBTI_Test(object):
    Personality_fields = [
        'Mind-Extraverted', 'Mind-Introverted',
        'Energy-Intuitive', 'Energy-Observant',
        'Nature-Thinking', 'Nature-Feeling',
        'Tactics-Judging', 'Tactics-Prospecting',
        'Identity-Assertive', 'Identity-Turbulent'
    ]
    # personality_translate = {
    #     'Mind-Extraverted':     u'精神-外向型',
    #     'Mind-Introverted':     u'精神-内向型',
    #     'Energy-Intuitive':     u'精力-直觉型',
    #     'Energy-Observant':     u'精力-现实型',
    #     'Nature-Thinking':      u'本性-逻辑型',
    #     'Nature-Feeling':       u'本性-感受型',
    #     'Tactics-Judging':      u'对策-计划型',
    #     'Tactics-Prospecting':  u'对策-展望型',
    #     'Identity-Assertive':   u'特性-坚决',
    #     'Identity-Turbulent':   u'特性-谨慎',
    # }
    def __init__(self):
        local = os.path.abspath(os.path.dirname(__file__))
        model_pickle = os.path.join(local, 'model', 'mbti_models.pkl')
        self.regrs = joblib.load(model_pickle)
        print 'initializing regrs:', self.regrs

    def model_predict(self, data):
        data = np.array(data) if isinstance(data, list) else data
        data = data.reshape(1, -1)
        result = {}

        for f in self.Personality_fields:
            if f != 'acronym':
                Personality_value = self.regrs[f].predict(data)
                result[f] = Personality_value

        clf = self.regrs['acronym']
        X = np.array([result[f] for f in self.Personality_fields]).reshape(1, -1)
        result['acronym'] = clf.predict(X)
        result = {k:result[k][0] for k in result}
        if ' (' in result['acronym']:
            result['acronym'] = result['acronym'].replace(' (', '').replace(')','')
        return result

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/mbti', things)

# Useful for debugging problems in your API; works with pdb.set_trace(). You
# can also use Gunicorn to host your app. Gunicorn can be configured to
# auto-restart workers when it detects a code change, and it also works
# with pdb.
if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
