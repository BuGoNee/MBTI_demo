#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'BuGoNee'


'''
Some Explaination should be in here.
'''
from flask import render_template, flash
from form import QuestionsForm
from app import app, regrs
import numpy as np
import pandas as pd

X_fields = [
    'Mind-Extraverted', 'Mind-Introverted',
    'Energy-Intuitive', 'Energy-Observant',
    'Nature-Thinking', 'Nature-Feeling',
    'Tactics-Judging', 'Tactics-Prospecting',
    'Identity-Assertive', 'Identity-Turbulent'
]
def model_predict(data):
    data = np.array(data) if isinstance(data, list) else data
    data = data.reshape(1, -1)
    global regrs
    X = {}
    for name, regr in regrs.items():
        if name != 'acronym':
            result = regr.predict(data)
            X[name] = result

    X = pd.DataFrame(X, columns=X_fields)
    clf = regrs['acronym']
    df = X
    df['acronym'] = clf.predict(X.values)
    if len(df) == 1:
        return df.loc[0].to_dict()
    else:
        return {'error': 'df length'}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    print regrs
    return 'test'

personality = {
    'Mind-Extraverted':     u'精神-外向型',
    'Mind-Introverted':     u'精神-内向型',
    'Energy-Intuitive':     u'精力-直觉型',
    'Energy-Observant':     u'精力-现实型',
    'Nature-Thinking':      u'本性-逻辑型',
    'Nature-Feeling':       u'本性-感受型',
    'Tactics-Judging':      u'对策-计划型',
    'Tactics-Prospecting':  u'对策-展望型',
    'Identity-Assertive':   u'特性-坚决',
    'Identity-Turbulent':   u'特性-谨慎',
}
@app.route('/mbti', methods=['GET', 'POST'])
def mbti():
    form = QuestionsForm()
    if form.validate_on_submit():
        data = [form.data.get('question'+str(i+1), 0)
                for i in range(60)]
        data = [-d for d in data]
        model_result = model_predict(data)
        for f in X_fields:
            message = u'%s:%0.05s %%'%(personality[f], model_result[f])
            flash(message, 'success')
        flash(u'人格类型:%s'%model_result['acronym'], 'success')
    return render_template('mbti.html', form=form)

if __name__ == '__main__':
    pass
