class Intro:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name_out(self):
        '''名前紹介の文を出力するメソッド'''
        nametxt = f"私の名前、{self.name}です"
        return nametxt
    
    def age_out(self):
        '''年齢紹介の文を出力するメソッド'''
        agetxt = f"年齢は、{self.age}です"
        return agetxt