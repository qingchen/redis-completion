# -*- coding:utf-8 -*-

import mmseg 
from pinyin import Pinyin
from redis_completion import RedisEngine

pinyin = Pinyin()
engine = RedisEngine()

def store_movie(movie):
    phrase = movie["title"]
    seg_phrase = " ".join(mmseg.seg_txt(phrase))
    _pinyin_phrase = pinyin.get_pinyin(phrase)
    py_phrase = "".join([p[0] for p in _pinyin_phrase]).encode("utf-8")
    pinyin_phrase = "".join(_pinyin_phrase).encode("utf-8")
    phrase = "%s %s %s %s" % (phrase, seg_phrase, pinyin_phrase, py_phrase)
    engine.store_json(movie["id"], phrase, movie)

def load_datas():
    movies = [
        {"id":20513051, "title": "被偷走的那五年", "director":"黄真真"}
      , {"id":20513052, "title": "十面埋伏", "director":"张艺谋"}
      , {"id":20513053, "title": "龙门镖局", "director":"王勇"}
      , {"id":20513054, "title": "致我们终将逝去的青春", "director":"赵薇"}
      , {"id":20513055, "title": "金枝欲孽2", "director":"戚其义"}
    ]
    for movie in movies:
        store_movie(movie)

load_datas()
for phrase in ["偷", "lmb", "jinzhi"]:
    print "Search for:", phrase
    for i in engine.search_json(phrase):
        print i["title"], i
