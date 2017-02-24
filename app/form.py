#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'BuGoNee'


'''
Some Explaination should be in here.
'''

from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import NumberRange

class QuestionsForm(FlaskForm):
    not_none = u'不能为空'
    nr = NumberRange(min=-3, max=3, message=u'答案在-3到3之间')

    q1  = u'Q1 :你发现在向别人做自我介绍时有困难。'
    q2  = u'Q2 :你经常陷入沉思，忽视或忘记了周围。'
    q3  = u'Q3 :你总想尽快回复电子邮件，无法忍受杂乱的收件箱。'
    q4  = u'Q4 :你发现，即便有些压力，你也能轻易保持放松和专注。'
    q5  = u'Q5 :你通常不会主动跟人交谈。'
    q6  = u'Q6 :你很少出于纯粹的好奇心做什么事。'
    q7  = u'Q7 :你觉得自己比别人优越。'
    q8  = u'Q8 :对你来说，有条理比能适应更重要。'
    q9  = u'Q9 :你通常都很有动力和活力。'
    q10 = u'Q10:对你来说，不让别人感到不愉快比赢得辩论更重要。'
    q11 = u'Q11:你经常觉得必须向别人解释你行为的理由。'
    q12 = u'Q12:你的家和工作环境都很整洁。'
    q13 = u'Q13:你不介意成为别人注意的中心。'
    q14 = u'Q14:你认为自己更现实，而不是更有创造力。'
    q15 = u'Q15:人们很少令你不快。'
    q16 = u'Q16:你的旅行计划通常经过深思熟虑。'
    q17 = u'Q17:你常常很难感受到别人的感受。'
    q18 = u'Q18:你的情绪变化很快。'
    q19 = u'Q19:在与人讨论时，你更看重事实，而不是人们敏感的情绪。'
    q20 = u'Q20:你很少担心你的行为对别人有什么影响。'
    q21 = u'Q21:你的工作风格遵循不定期出现的能量高峰，而不是采用有系统有组织的方法。'
    q22 = u'Q22:你经常嫉妒别人。'
    q23 = u'Q23:有趣的书或电子游戏常比社交活动更有吸引力。'
    q24 = u'Q24:每个项目最关键的是能够制定和遵守计划。'
    q25 = u'Q25:你很少沉溺于幻想或想法。'
    q26 = u'Q26:在自然环境中散步时，你常发现自己陷入沉思。'
    q27 = u'Q27:如果有人没迅速回复你的电子邮件，你会担心是不是自己说错了话。'
    q28 = u'Q28:为人父母，你更愿意看到孩子成为善良的人，而不是聪明人。'
    q29 = u'Q29:你不让你的行为受别人影响。'
    q30 = u'Q30:你的梦常是有关真实世界和事件的。'
    q31 = u'Q31:在新的工作单位，你没多久就开始参加社交活动。'
    q32 = u'Q32:你更多是天生的即兴表现者，而不是周密计划者。'
    q33 = u'Q33:你更多受情绪控制，而不是控制情绪。'
    q34 = u'Q34:你喜欢参加需盛装或化妆出席的社交活动。'
    q35 = u'Q35:你经常花时间探索不现实、不可行，但会触发灵感的想法。'
    q36 = u'Q36:你更愿意即兴发挥，而不是花时间制定详细的计划。'
    q37 = u'Q37:你是个相对拘谨、安静的人。'
    q38 = u'Q38:如果你是企业主，你会觉得解雇忠诚但绩效不佳的员工是件难事。'
    q39 = u'Q39:你经常思考人类存在的意义。'
    q40 = u'Q40:在做重要决定时，逻辑通常比心愿更重要。'
    q41 = u'Q41:保持开放的选择比列出行动计划更重要。'
    q42 = u'Q42:如果你的朋友为什么事伤心，你更可能在情感上支持他，而不是向他建议处理问题的办法。'
    q43 = u'Q43:你很少有不安全感。'
    q44 = u'Q44:在制定个人时间表并坚持执行这方面，你没什么困难。'
    q45 = u'Q45:在团队工作中，正确做事比合作态度更重要。'
    q46 = u'Q46:你认为，每个人的看法都应得到尊重，无论是否有事实根据。'
    q47 = u'Q47:在与一群人共度时光之后，你感到更有活力。'
    q48 = u'Q48:你经常把东西放错地方。'
    q49 = u'Q49:你认为自己情绪很稳定。'
    q50 = u'Q50:你的头脑常塞满未经探索的想法和计划。'
    q51 = u'Q51:你不会叫自己梦想家。'
    q52 = u'Q52:面对很多人发言，你通常觉得难以放松。'
    q53 = u'Q53:一般说来，你更多依赖自己的经验而非想象力。'
    q54 = u'Q54:你过于担心人们怎么想。'
    q55 = u'Q55:如果房间里有很多人，你会靠近墙边，避免处于中心位置。'
    q56 = u'Q56:你总爱拖延，直到没有足够的时间做每件事。'
    q57 = u'Q57:你在面对压力情境时感到很焦虑。'
    q58 = u'Q58:你认为，自己被别人喜欢比拥有权势更值得。'
    q59 = u'Q59:你总是对非常规和含义不明的东西感兴趣，比如书籍、艺术或电影。'
    q60 = u'Q60:在社交场合，你经常很主动。'
    question1  = IntegerField(q1,  validators=[nr])
    question2  = IntegerField(q2,  validators=[nr])
    question3  = IntegerField(q3,  validators=[nr])
    question4  = IntegerField(q4,  validators=[nr])
    question5  = IntegerField(q5,  validators=[nr])
    question6  = IntegerField(q6,  validators=[nr])
    question7  = IntegerField(q7,  validators=[nr])
    question8  = IntegerField(q8,  validators=[nr])
    question9  = IntegerField(q9,  validators=[nr])
    question10 = IntegerField(q10, validators=[nr])
    question11 = IntegerField(q11, validators=[nr])
    question12 = IntegerField(q12, validators=[nr])
    question13 = IntegerField(q13, validators=[nr])
    question14 = IntegerField(q14, validators=[nr])
    question15 = IntegerField(q15, validators=[nr])
    question16 = IntegerField(q16, validators=[nr])
    question17 = IntegerField(q17, validators=[nr])
    question18 = IntegerField(q18, validators=[nr])
    question19 = IntegerField(q19, validators=[nr])
    question20 = IntegerField(q20, validators=[nr])
    question21 = IntegerField(q21, validators=[nr])
    question22 = IntegerField(q22, validators=[nr])
    question23 = IntegerField(q23, validators=[nr])
    question24 = IntegerField(q24, validators=[nr])
    question25 = IntegerField(q25, validators=[nr])
    question26 = IntegerField(q26, validators=[nr])
    question27 = IntegerField(q27, validators=[nr])
    question28 = IntegerField(q28, validators=[nr])
    question29 = IntegerField(q29, validators=[nr])
    question30 = IntegerField(q30, validators=[nr])
    question31 = IntegerField(q31, validators=[nr])
    question32 = IntegerField(q32, validators=[nr])
    question33 = IntegerField(q33, validators=[nr])
    question34 = IntegerField(q34, validators=[nr])
    question35 = IntegerField(q35, validators=[nr])
    question36 = IntegerField(q36, validators=[nr])
    question37 = IntegerField(q37, validators=[nr])
    question38 = IntegerField(q38, validators=[nr])
    question39 = IntegerField(q39, validators=[nr])
    question40 = IntegerField(q40, validators=[nr])
    question41 = IntegerField(q41, validators=[nr])
    question42 = IntegerField(q42, validators=[nr])
    question43 = IntegerField(q43, validators=[nr])
    question44 = IntegerField(q44, validators=[nr])
    question45 = IntegerField(q45, validators=[nr])
    question46 = IntegerField(q46, validators=[nr])
    question47 = IntegerField(q47, validators=[nr])
    question48 = IntegerField(q48, validators=[nr])
    question49 = IntegerField(q49, validators=[nr])
    question50 = IntegerField(q50, validators=[nr])
    question51 = IntegerField(q51, validators=[nr])
    question52 = IntegerField(q52, validators=[nr])
    question53 = IntegerField(q53, validators=[nr])
    question54 = IntegerField(q54, validators=[nr])
    question55 = IntegerField(q55, validators=[nr])
    question56 = IntegerField(q56, validators=[nr])
    question57 = IntegerField(q57, validators=[nr])
    question58 = IntegerField(q58, validators=[nr])
    question59 = IntegerField(q59, validators=[nr])
    question60 = IntegerField(q60, validators=[nr])
    submit = SubmitField(u'提交')


if __name__ == '__main__':
    pass


