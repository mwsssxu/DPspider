#coding:utf-8
import os

def checkSVG(path):
    def outter(func):
        def wrapper(*args,**kwargs):
            if os.path.isfile(path):
                with open(path, 'r') as f:
                    svg = f.read()
                res,_ = func(*args,svg=svg,**kwargs)
            else:
                res,svg = func(*args, **kwargs)
                with open(path, 'w') as f:
                    f.write(svg)
            return res
        return wrapper
    return outter

