import os, sys
sys.path.append(os.path.dirname(__file__)) #相対パスを指定する
from introduce import Intro

class IntroFam(Intro):
    def __init__(self, name, age, pet):
        super().__init__(name, age)
        # print(os.path.dirname(__file__))
        # print(os.getcwd())
        self.pet = pet

    def cat_out(self):
        '''猫の名前を出力'''
        cattxt = f"飼い猫の名前は、{self.pet}です"
        return cattxt