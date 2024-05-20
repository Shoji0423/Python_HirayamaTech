# introduce.pyのIntroクラスを継承したIntroFamを作成
# 猫の名前を設定、返す処理

from module.introduce import Intro

class IntroFam(Intro):
    def __init__(self, name, age, cat_name):
        super().__init__(name,age)
        self.cat_name = cat_name
    
    def cat_out(self):
        nametxt = "飼い猫の名前は、" + self.cat_name + "です"
        return nametxt


