#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'BuGoNee'


'''
Some Explaination should be in here.
'''

import pandas as pd
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.linear_model import LogisticRegressionCV, LogisticRegression, LinearRegression, Ridge
from sklearn import linear_model

df = pd.read_csv('mbti_data.csv')

result_fields =[
                'type_nice',
                'type_acronym',
                'result',
                'result1',
                'result2',
                'result3',
                'result4',
                'Mind-Extraverted',
                'Mind-Introverted',
                'Energy-Intuitive',
                'Energy-Observant',
                'Nature-Thinking',
                'Nature-Feeling',
                'Tactics-Judging',
                'Tactics-Prospecting',
                'Identity-Assertive',
                'Identity-Turbulent']


# def total_ptype_score():
#     X_fields = [
#         'Mind-Extraverted',
#         'Mind-Introverted',
#         'Energy-Intuitive',
#         'Energy-Observant',
#         'Nature-Thinking',
#         'Nature-Feeling',
#         'Tactics-Judging',
#         'Tactics-Prospecting',
#         'Identity-Assertive',
#         'Identity-Turbulent'
#     ]
#     X = df[X_fields].values
#     y = df[['type_acronym']].values.ravel()
#     clf1 = linear_model.LogisticRegression(n_jobs=-1)
#     scores = cross_val_score(clf1, X, y, cv=5, n_jobs=-1)
#     print scores
#     print("Accuracy: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))
#     return clf1

# def LogisticR():
#     X = df.drop(result_fields, axis=1).values
#     y = df[['type_acronym']].values.ravel()
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=0)
#     clf1 = linear_model.LogisticRegression()
#     clf1.fit(X_train, y_train)
#     print clf1.score(X_train, y_train)
#     print clf1.score(X_test, y_test)
#     print clf1.coef_.ravel().copy()
#     return clf1

def LinearR(X, y):
    regr = linear_model.LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=4)
    regr.fit(X_train, y_train)
    print 'train Accuracy:', regr.score(X_train, y_train)
    print 'test Accuracy:', regr.score(X_test, y_test)
    return regr

def LinearRCV(X, y):
    lr = linear_model.LinearRegression(n_jobs=-1)
    scores = cross_val_score(lr, X, y, cv=5, n_jobs=-1)
    print scores
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    return lr

def personalitys():
    y_field = [
        'Mind-Extraverted',
        'Mind-Introverted',
        'Energy-Intuitive',
        'Energy-Observant',
        'Nature-Thinking',
        'Nature-Feeling',
        'Tactics-Judging',
        'Tactics-Prospecting',
        'Identity-Assertive',
        'Identity-Turbulent'
    ]
    regrs = {}
    X = df.drop(result_fields, axis=1).values
    for col in y_field:
        y = df[[col]].values.ravel()
        print col, ':'
        regr = LinearR(X, y)
        regrs[col] = regr
    return regrs

def acronym():
    X_fields = [
        'Mind-Extraverted',
        'Mind-Introverted',
        'Energy-Intuitive',
        'Energy-Observant',
        'Nature-Thinking',
        'Nature-Feeling',
        'Tactics-Judging',
        'Tactics-Prospecting',
        'Identity-Assertive',
        'Identity-Turbulent'
    ]
    X = df[X_fields].values
    y = df[['type_acronym']].values.ravel()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=3)
    lrcv = linear_model.LogisticRegressionCV(n_jobs=-1, cv=5)
    lrcv.fit(X_train, y_train)
    print lrcv.score(X_test, y_test)
    return lrcv

def train_test():
    clf = acronym()
    regrs = personalitys()

    regrs["acronym"] = clf
    joblib.dump(regrs, 'mbti_models.pkl')

    test(regrs)

def test(regrs):
    test_data = [-3 for i in range(60)]
    X = {}
    for name, regr in regrs.items():
        if name != 'acronym':
            result = regr.predict(test_data)
            X[name] = result
    X_fields = [
        'Mind-Extraverted',
        'Mind-Introverted',
        'Energy-Intuitive',
        'Energy-Observant',
        'Nature-Thinking',
        'Nature-Feeling',
        'Tactics-Judging',
        'Tactics-Prospecting',
        'Identity-Assertive',
        'Identity-Turbulent'
    ]
    X = pd.DataFrame(X, columns=X_fields)
    print X
    clf = regrs['acronym']
    print clf.predict(X.values)
    return regrs

def predict_test():
    regrs = joblib.load('mbti_models.pkl')
    test(regrs)

def usage(data):
    regrs = joblib.load('mbti_models.pkl')
    X = {}
    for name, regr in regrs.items():
        if name != 'acronym':
            result = regr.predict(data)
            X[name] = result
    X_fields = [
        'Mind-Extraverted',
        'Mind-Introverted',
        'Energy-Intuitive',
        'Energy-Observant',
        'Nature-Thinking',
        'Nature-Feeling',
        'Tactics-Judging',
        'Tactics-Prospecting',
        'Identity-Assertive',
        'Identity-Turbulent'
    ]
    X = pd.DataFrame(X, columns=X_fields)
    print X
    clf = regrs['acronym']
    df = X
    df['acronym'] = clf.predict(X.values)
    if len(df) == 0:
        return df.loc[0].to_dict()
    else:
        return {'error': 'df length'}

def myRidgeCV():
    y_field = [
        'Mind-Extraverted',
        'Mind-Introverted',
        'Energy-Intuitive',
        'Energy-Observant',
        'Nature-Thinking',
        'Nature-Feeling',
        'Tactics-Judging',
        'Tactics-Prospecting',
        'Identity-Assertive',
        'Identity-Turbulent'
    ]
    regs = {}
    X = df.drop(result_fields, axis=1).values
    for col in y_field:
        y = df[[col]].values.ravel()
        print col, ':'
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=3)
        reg = linear_model.RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0])
        reg.fit(X_train, y_train)
        print 'train Accuracy:', reg.score(X_train, y_train)
        print 'test Accuracy:', reg.score(X_test, y_test)
        regs[col] = reg

    return regs

def myLasso():
    y_field = [
        'Mind-Extraverted',
        'Mind-Introverted',
        'Energy-Intuitive',
        'Energy-Observant',
        'Nature-Thinking',
        'Nature-Feeling',
        'Tactics-Judging',
        'Tactics-Prospecting',
        'Identity-Assertive',
        'Identity-Turbulent'
    ]
    regs = {}
    X = df.drop(result_fields, axis=1).values
    for col in y_field:
        y = df[[col]].values.ravel()
        print col, ':'
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=3)
        reg = linear_model.Lasso(alpha = 0.1)
        reg.fit(X_train, y_train)
        print 'train Accuracy:', reg.score(X_train, y_train)
        print 'test Accuracy:', reg.score(X_test, y_test)
        regs[col] = reg

    return regs

def myBayes():
    y_field = [
        'Mind-Extraverted',
        'Mind-Introverted',
        'Energy-Intuitive',
        'Energy-Observant',
        'Nature-Thinking',
        'Nature-Feeling',
        'Tactics-Judging',
        'Tactics-Prospecting',
        'Identity-Assertive',
        'Identity-Turbulent'
    ]
    regs = {}
    X = df.drop(result_fields, axis=1).values
    for col in y_field:
        y = df[[col]].values.ravel()
        print col, ':'
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=3)
        reg = linear_model.BayesianRidge()
        reg.fit(X_train, y_train)
        print 'train Accuracy:', reg.score(X_train, y_train)
        print 'test Accuracy:', reg.score(X_test, y_test)
        regs[col] = reg

    return regs
def myTest():
    y_field = [
        'Mind-Extraverted',
        'Mind-Introverted',
        'Energy-Intuitive',
        'Energy-Observant',
        'Nature-Thinking',
        'Nature-Feeling',
        'Tactics-Judging',
        'Tactics-Prospecting',
        'Identity-Assertive',
        'Identity-Turbulent'
    ]
    bayes = {}
    lassos = {}
    ridges = {}
    linearr = {}
    X = df.drop(result_fields, axis=1).values
    for col in y_field:
        y = df[[col]].values.ravel()
        print col, ':'
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=3)

        print 'bayes:'
        reg = linear_model.BayesianRidge()
        reg.fit(X_train, y_train)
        print 'train Accuracy:', reg.score(X_train, y_train),
        print 'test Accuracy:', reg.score(X_test, y_test)
        bayes[col] = reg


        print 'lasso:'
        reg = linear_model.Lasso(alpha = 0.1)
        reg.fit(X_train, y_train)
        print 'train Accuracy:', reg.score(X_train, y_train),
        print 'test Accuracy:', reg.score(X_test, y_test)
        lassos[col] = reg

        print 'ridge:'
        reg = linear_model.RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0])
        reg.fit(X_train, y_train)
        print 'train Accuracy:', reg.score(X_train, y_train),
        print 'test Accuracy:', reg.score(X_test, y_test)
        ridges[col] = reg


        print 'linearR:'
        regr = linear_model.LinearRegression()
        regr.fit(X_train, y_train)
        print 'train Accuracy:', regr.score(X_train, y_train),
        print 'test Accuracy:', regr.score(X_test, y_test)
        linearr[col] = reg
if __name__ == '__main__':
    # train_test()
    # predict_test()
    pass
