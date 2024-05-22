import datetime
from database import session
from table_vend_mer import merchandise
from table_vend_mes import message
from table_vend_mon import money
from table_vend_sto import stock
import sys

mer=session.query(merchandise).all()
drink_list={}

      
yn="Y"
# drink_list={"お茶":110,"コーヒー":100,"ソーダ":160,"コンポタージュ":130}

for item in mer:
    sto=session.query(stock).filter_by(id=item.id).first()
    if sto.stock!=0:
        print(item.name+"："+str(item.price)+"円")
mon=int(input("投入金額を入力してください"))
for item in mer:
    drink_list.update({item.name:item.price})
#金額入力フェーズ
while True :
    #何も買えない場合
    if min(drink_list.values()) > mon :
        mon=int(input(str(mon)+"円では購入できる商品がありません。再度投入金額を入力してください"))
    #10000以上を入力した場合
    elif mon > 10000 :
        mon=int(input("10000円を超える金額は投入できません。再度投入金額を入力してください"))
    #1円玉もしくは5円玉を投入しようとしている場合
    elif mon%10!=0:
        mon=int(input("1円玉、5円玉は使用できません。再度金額を入力してください"))
    else:
        break
mon_st=mon 
if mon >= 1000:
    m=session.query(money).filter_by(price=1000).first()
    m.number=int(m.number)+int(mon/1000)
    session.add(m)
    session.commit()
    mon=mon%1000
if mon >= 500:
    m=session.query(money).filter_by(price=500).first()
    m.number=int(m.number)+int(mon/500)
    session.add(m)
    session.commit()
    mon=mon%500
if mon >= 100:
    m=session.query(money).filter_by(price=100).first()
    m.number=int(m.number)+int(mon/100)
    session.add(m)
    session.commit()
    mon=mon%100
if mon >= 50:
    m=session.query(money).filter_by(price=50).first()
    m.number=int(m.number)+int(mon/50)
    session.add(m)
    session.commit()
    mon=mon%50
if mon >= 10:
    m=session.query(money).filter_by(price=10).first()
    m.number=int(m.number)+int(mon/10)
    session.add(m)
    session.commit()
    
mon=mon_st
#購入フェーズ
while True:
    input_syo=input("何を購入しますか（商品名/cancel）")
    #cancelが入力された場合購入フェーズを抜ける
    if input_syo=="cancel" :
        break
    else:
        syo_id=session.query(merchandise.id).filter_by(name=input_syo).first()
        sto=session.query(stock).filter_by(id=syo_id.id).first()
        sto.stock=int(sto.stock)-1
        session.add(sto)
        session.commit()
        mon=mon-drink_list[input_syo]
    #最安値以上残高が残っている場合
    if min(drink_list.values())<=mon:
        print("残金："+str(mon)+"円")
        yn=input("続けて購入しますか(Y/N)")
    else:
        break
    if yn=="N":
        break
    for name in drink_list:
        print(name+str(drink_list[name])+"円")
        
#おつりフェーズ 
print("おつり")
if mon >= 1000:
    m=session.query(money).filter_by(price=1000).first()
    m.number=int(m.number)-int(mon/1000)
    if m.number <=10:
        seq=session.query(message.seq).count()
        mes=message(
            seq=seq+1,
            Message="1000円の残枚数が{0}枚になりました。確認してください".format(m.number),
            datetime=datetime.datetime.today()
        )
        session.add(mes)
        session.commit()
    session.add(m)
    session.commit()
    print("1000円札："+str(int(mon/1000))+"枚")
    mon=mon%1000
if mon >= 500:
    m=session.query(money).filter_by(price=500).first()
    m.number=int(m.number)-int(mon/500)
    if m.number <=10:
        seq=session.query(message.seq).count()
        mes=message(
            seq=seq+1,
            Message="500円の残枚数が{0}枚になりました。確認してください".format(m.number),
            datetime=datetime.datetime.today()
        )
        session.add(mes)
        session.commit()
    session.add(m)
    session.commit()
    print("500円玉："+str(int(mon/500))+"枚")
    mon=mon%500
if mon >= 100:
    m=session.query(money).filter_by(price=100).first()
    m.number=int(m.number)-int(mon/100)
    if m.number <=10:
        seq=session.query(message.seq).count()
        mes=message(
            seq=seq+1,
            Message="100円の残枚数が{0}枚になりました。確認してください".format(m.number),
            datetime=datetime.datetime.today()
        )
        session.add(mes)
        session.commit()
    session.add(m)
    session.commit()
    print("100円玉："+str(int(mon/100))+"枚")
    mon=mon%100
if mon >= 50:
    m=session.query(money).filter_by(price=50).first()
    m.number=int(m.number)-int(mon/50)
    if m.number <=10:
        seq=session.query(message.seq).count()
        mes=message(
            seq=seq+1,
            Message="50円の残枚数が{0}枚になりました。確認してください".format(m.number),
            datetime=datetime.datetime.today()
        )
        session.add(mes)
        session.commit()
    session.add(m)
    session.commit()
    print("50円玉："+str(int(mon/50))+"枚")
    mon=mon%50
if mon >= 10:
    m=session.query(money).filter_by(price=10).first()
    m.number=int(m.number)-int(mon/10)
    if m.number <=10:
        seq=session.query(message.seq).count()
        mes=message(
            seq=seq+1,
            Message="10円の残枚数が{0}枚になりました。確認してください".format(m.number),
            datetime=datetime.datetime.today()
        )
        session.add(mes)
        session.commit()
    session.add(m)
    session.commit()
    print("10円玉："+str(int(mon/10))+"枚")
      
    


    