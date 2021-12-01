# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 17:10:26 2021

@author: yuki
"""
import streamlit as st

st.title('～ソウルナンバー診断～')

pic=st.image('girl_title.png',use_column_width=True,)


st.write('ここでは、簡単な心理テストが受けられます。')
st.write('仕事や学問に追われて忙しいそこのあなた！ちょっと息抜きしていきませんか？')


text=st.text_input('１.あなたのニックネームを入力してください。（名前は結果に影響しません。）')
'あなたは, ',text,'です。'

st.write(' ')

gender=st.selectbox(
    '２.あなたの性別を選択してください。',
    list(['男性','女性','その他'])
    )
'あなたは、',gender,'です。'

st.write(' ')

st.write('３.あなたの誕生年の数字を選択してください。')

col1,col2,col3,col4 = st.columns(4)

with col1:
    year1000=st.selectbox(
    '誕生年　千の位',
    list(['1','2'])
    )
    
with col2:
    year100=st.selectbox(
    '誕生年　百の位',
    list(['0','1','2','3','4','5','6','7','8','9'])
    )
    

with col3:
    year10=st.selectbox(
    '誕生年　十の位',
    list(['0','1','2','3','4','5','6','7','8','9'])
    )
    
with col4:
     year1=st.selectbox(
    '誕生年　一の位',
    list(['0','1','2','3','4','5','6','7','8','9'])
    )

st.write('あなたの誕生年は',year1000+year100+year10+year1,'年です。')

st.write(' ')


st.write('4.あなたの誕生月の数字を選択してください。')

col5,col6= st.columns(2)

with col5:
    month10=st.selectbox(
    '誕生月 十の位（１～９月の場合→０、１０～１２月の場合→１）',
    list(['0','1',''])
    )

with col6:
    month1=st.selectbox(
    '誕生月 一の位',
    list(['0','1','2','3','4','5','6','7','8','9'])
    )
    
st.write('あなたの誕生月は',month10+month1,'月です。')

st.write(' ')


st.write('5.あなたの誕生日の数字を選択してください。')

col7,col8= st.columns(2)

with col7:
    day10=st.selectbox(
    '誕生日の十の位（１～９日の場合→０）',
    list(['0','1','2','3'])
    )

with col8:
    day1=st.selectbox(
    '誕生日の一の位',
    list(['0','1','2','3','4','5','6','7','8','9'])
    )
    
st.write('あなたの誕生日は',day10+day1,'日です。')

count=int(year1000)+int(year100)+int(year10)+int(year1)+int(month10)+int(month1)+int(day10)+int(day1)

#aとbに何かしらの数字が入っていないと下のif文でエラーがでてしまうため、最初に0を入れておく
a=0
b=0

point=str(count)
#文字に変換した数字をばらばらにする
array=list(map(int,point))
#二桁以上なら、さっき分解した数字をaとbに分解する
if len(array) >= 2:
    a,b = array
    
elif a==b:
    k = count
else:
    k = sum(array)


st.write('あなたのソウルナンバーは、',k,'です。')


if st.button('結果を見る'):
    if k == 1:
         st.write('素晴らしい行動力の持ち主で、頭の回転も速く周りからよく頼られるでしょう。',
             'ですが、はやとちりや周りを置いて行ってしまうことには注意...',)
         st.image('girl1.png',use_column_width=True)
    
    elif k == 2:
        st.write('さっぱりした性格で、必要に応じて立場を考えて行動が出来るでしょう。',
             'ですが、執着がないことには注意。異性からの好意を得にくいかも...',)
        st.image('girl2.png',use_column_width=True)
    
    elif k == 3:
        st.write('洞察力が高く、周りからも慕われることが多いあなたは、相手の立場に合わせていろんな人と公平に接する事が出来るでしょう。',
             'ですが、たまにお節介とおもわれてしまったり、頼られすぎてしまうことがあるかも...',)
        st.image('girl3.png',use_column_width=True)
        
    elif k == 4:
        st.write('リーダー気質を持っており、周りへの影響力を持っています。常に新たな事に挑戦出来る気持ちも持っています。',
             'しかし、挫折してしまうと内向的になってしまい、言いたいことが言えなくなってしまうことも...',)
        st.image('girl4.png',use_column_width=True)
    
    
    elif k == 5:
        st.write('真面目で曲がったことが嫌いなあなたは、人にだまされることが少ないでしょう。',
             'しかし、突き進みすぎて周りが見えなくなってしまうことも...',)
        st.image('girl5.png',use_column_width=True)
    
    
    elif k == 6:
        st.write('社交的で、あたまの回転も速く、あいてを理解するのうりょくも高いので、話すことで励まされる人がたくさんいるはずです。',
             'しかし、飽きっぽいため、1つのことに集中ができないことがあります。また、自分の心を開くのが苦手な一面もあるでしょう。',)
        st.image('girl6.png',use_column_width=True)
        
    elif k == 7:
        st.write('やさしく、家庭的で探究心の強いあなたは、興味を持ったことに対しては一番を目指していくタイプです。',
             'しかし、逆境に弱く、想定外のトラブルに直面したときに、自分を見失ってしまうことがあるかも...',)
        st.image('girl7.png',use_column_width=True)
    
    
    elif k == 8:
        st.write('穏やかな正確で純粋なあなた。嘘や計算が嫌いで、他人に損得勘定抜きで接するところが魅力です。',
             'しかし、几帳面な部分を相手にも求めてしまうことや、一度イヤになると、イヤなままになってしまうことがあります。')
        st.image('girl8.png',use_column_width=True)
        
    elif k == 9:
        st.write('人とワイワイ楽しむことが好きで、誰からも好かれるタイプです。',
             'ルールに縛られることが嫌いで、反発したくなることもあるでしょう。')
        st.image('girl9.png',use_column_width=True)
    
    elif k == 11:
        st.write('直感が鋭く、あいての仕草や表情から考えていることが察知できてしまう事があります。',
             'また、傷つきやすい一面も持っています。',)
        st.image('girl11.png',use_column_width=True)
    
    elif k == 22:
        st.write('判断力が強く、最後まで諦めないあなたは、目標に向かって一直線に努力できるタイプです。',
             'しかし、周りが見えなくなってしまうこともあるので注意が必要。',)
        st.image('girl22.png',use_column_width=True)
    
    elif k == 33:
        st.write('天才肌の持ち主です！',
             '仕事では、大成功かだ失敗の量驚嘆になりがちで、周りの環境次第で人生が変化するタイプです。',)
        st.image('girl33.png',use_column_width=True)
        
    elif k == 44:
        st.write('問題解決能力が高く、リーダー気質があるでしょう。',
             '全体をまとめる立場となり、組織を引っ張っていくタイプです。',)
        st.image('girl44.png',use_column_width=True)
    
    else:    
        st.write('診断できませんでした')
        st.image('girl_no.png',use_column_width=True)
    
