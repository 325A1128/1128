import streamlit as st

from random import randint

if 'page' not in st.session_state:
    st.session_state.page = 'home'
    
if 'cnt' not in st.session_state:
    st.session_state.cnt = 0
    
if 'juu' not in st.session_state:
    st.session_state.juu = 0
    
if 'henkan' not in st.session_state:
    st.session_state.henkan = 0
    
if 'seigo' not in st.session_state:
    st.session_state.seigo = ''
    
#基数変換プログラム
def henkan(juu,hen):
    if juu == 0:
        return '0'
    chars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    ret = '' 
    while juu > 0:
        ret = chars[int(juu % hen)] + ret
        juu = int(juu / hen)
    return ret

#選択肢のボタンの位置を毎回変える
def ran_button():
    b_list = list()
    while len(b_list) < 4:
        num = randint(0,3)
        if num not in b_list:
            b_list.append(num)
    return b_list

#正誤判定
def seigo(but):
    if but == st.session_state.juu:
        st.session_state.cnt += 1
        st.session_state.seigo = '〇正解'
    else:
        st.session_state.seigo = '✕不正解'
        
#ホーム画面
def home():
    st.title('基数変換クイズ')
    if st.button('10➡2'):
        st.session_state.henkan = 2
        st.session_state.page = 'page1'
    if st.button('10➡8'):
        st.session_state.henkan = 8
        st.session_state.page = 'page1'
    if st.button('10➡16'):
        st.session_state.henkan = 16
        st.session_state.page = 'page1'
    if st.button('2➡10'):
        st.session_state.henkan = 2
        st.session_state.page = 'page4'
    if st.button('8➡10'):
        st.session_state.henkan = 8
        st.session_state.page = 'page4'
    if st.button('16➡10'):
        st.session_state.henkan = 16
        st.session_state.page = 'page4'
    
#問題ページ
#一問目(10➡)
def page1():
    st.session_state.juu = randint(1,15)
    st.title(st.session_state.juu)
    but = [st.session_state.juu,
           st.session_state.juu+1,
           st.session_state.juu+2,
           st.session_state.juu-1]
    ranbut = ran_button()
    
    if st.button(henkan(but[ranbut[0]],st.session_state.henkan)):
        seigo(but[ranbut[0]])
        st.session_state.page = 'page1_ans'
    if st.button(henkan(but[ranbut[1]],st.session_state.henkan)):
        seigo(but[ranbut[1]])
        st.session_state.page = 'page1_ans'
    if st.button(henkan(but[ranbut[2]],st.session_state.henkan)):
        seigo(but[ranbut[2]])
        st.session_state.page = 'page1_ans'
    if st.button(henkan(but[ranbut[3]],st.session_state.henkan)):
        seigo(but[ranbut[3]])
        st.session_state.page = 'page1_ans'

#二問目(10➡)
def page2():
    st.session_state.juu = randint(16,63)
    st.title(st.session_state.juu)
    but = [st.session_state.juu,
           st.session_state.juu+1,
           st.session_state.juu+2,
           st.session_state.juu-1]
    ranbut = ran_button()
    
    if st.button(henkan(but[ranbut[0]],st.session_state.henkan)):
        seigo(but[ranbut[0]])
        st.session_state.page = 'page2_ans'
    if st.button(henkan(but[ranbut[1]],st.session_state.henkan)):
        seigo(but[ranbut[1]])
        st.session_state.page = 'page2_ans'
    if st.button(henkan(but[ranbut[2]],st.session_state.henkan)):
        seigo(but[ranbut[2]])
        st.session_state.page = 'page2_ans'
    if st.button(henkan(but[ranbut[3]],st.session_state.henkan)):
        seigo(but[ranbut[3]])
        st.session_state.page = 'page2_ans'
    
    
#三問目(10➡)
def page3():
    st.session_state.juu = randint(64,127)
    st.title(st.session_state.juu)
    but = [st.session_state.juu,
           st.session_state.juu+1,
           st.session_state.juu+2,
           st.session_state.juu-1]
    ranbut = ran_button()
    
    if st.button(henkan(but[ranbut[0]],st.session_state.henkan)):
        seigo(but[ranbut[0]])
        st.session_state.page = 'page3_ans'
    if st.button(henkan(but[ranbut[1]],st.session_state.henkan)):
        seigo(but[ranbut[1]])
        st.session_state.page = 'page3_ans'
    if st.button(henkan(but[ranbut[2]],st.session_state.henkan)):
        seigo(but[ranbut[2]])
        st.session_state.page = 'page3_ans'
    if st.button(henkan(but[ranbut[3]],st.session_state.henkan)):
        seigo(but[ranbut[3]])
        st.session_state.page = 'page3_ans'

#一問目(➡10)
def page4():
    st.session_state.juu = randint(1,15)
    but = [st.session_state.juu,
           st.session_state.juu+1,
           st.session_state.juu+2,
           st.session_state.juu-1]
    st.title(henkan(st.session_state.juu,st.session_state.henkan))
    ranbut = ran_button()
    
    if st.button(but[ranbut[0]]):
        seigo(but[ranbut[0]])
        st.session_state.page = 'page4_ans'
    if st.button(but[ranbut[1]]):
        seigo(but[ranbut[1]])
        st.session_state.page = 'page4_ans'
    if st.button(but[ranbut[2]]):
        seigo(but[ranbut[2]])
        st.session_state.page = 'page4_ans'
    if st.button(but[ranbut[3]]):
        seigo(but[ranbut[3]])
        st.session_state.page = 'page4_ans'
        
#二問目(➡10)
def page5():
    st.session_state.juu = randint(16,63)
    but = [henkan(st.session_state.juu,st.session_state.henkan),
           henkan(st.session_state.juu+1,st.session_state.henkan),
           henkan(st.session_state.juu+2,st.session_state.henkan),
           henkan(st.session_state.juu-1,st.session_state.henkan)]
    st.title(henkan(st.session_state.juu,st.session_state.henkan))
    ranbut = ran_button()
    
    if st.button(but[ranbut[0]]):
        seigo(but[ranbut[0]])
        st.session_state.page = 'page5_ans'
    if st.button(but[ranbut[1]]):
        seigo(but[ranbut[1]])
        st.session_state.page = 'page5_ans'
    if st.button(but[ranbut[2]]):
        seigo(but[ranbut[2]])
        st.session_state.page = 'page5_ans'
    if st.button(but[ranbut[3]]):
        seigo(but[ranbut[3]])
        st.session_state.page = 'page5_ans'
        
#三問目(➡10)
def page6():
    st.session_state.juu = randint(64,127)
    but = [st.session_state.juu,
           st.session_state.juu+1,
           st.session_state.juu+2,
           st.session_state.juu-1]
    st.title(henkan(st.session_state.juu,st.session_state.henkan))
    ranbut = ran_button()
    
    if st.button(but[ranbut[0]]):
        seigo(but[ranbut[0]])
        st.session_state.page = 'page6_ans'
    if st.button(but[ranbut[1]]):
        seigo(but[ranbut[1]])
        st.session_state.page = 'page6_ans'
    if st.button(but[ranbut[2]]):
        seigo(but[ranbut[2]])
        st.session_state.page = 'page6_ans'
    if st.button(but[ranbut[3]]):
        seigo(but[ranbut[3]])
        st.session_state.page = 'page6_ans'
        
#答えページ
def page1_ans():
    st.title(st.session_state.seigo)
    st.title(f'{st.session_state.juu}➡{henkan(st.session_state.juu,2)}')
    if st.button('次へ'):
        st.session_state.page = 'page2'
        
def page2_ans():
    st.title(st.session_state.seigo)
    st.title(f'{st.session_state.juu}➡{henkan(st.session_state.juu,2)}')
    if st.button('次へ'):
        st.session_state.page = 'page3'
        
def page3_ans():
    st.title(st.session_state.seigo)
    st.title(f'{st.session_state.juu}➡{henkan(st.session_state.juu,2)}')
    if st.button('次へ'):
        st.session_state.page = 'page7'
        
def page4_ans():
    st.title(st.session_state.seigo)
    st.title(f'{st.session_state.juu}➡{henkan(st.session_state.juu,2)}')
    if st.button('次へ'):
        st.session_state.page = 'page5'
        
def page5_ans():
    st.title(st.session_state.seigo)
    st.title(f'{st.session_state.juu}➡{henkan(st.session_state.juu,2)}')
    if st.button('次へ'):
        st.session_state.page = 'page6'

def page6_ans():
    st.title(st.session_state.seigo)
    st.title(f'{st.session_state.juu}➡{henkan(st.session_state.juu,2)}')
    if st.button('次へ'):
        st.session_state.page = 'page7'
        
#最終結果ページ
def page7():
    st.title('結果')
    st.write(f'{st.session_state.cnt}/3!')
    if st.button('ホームに戻る'):
        st.session_state.cnt = 0
        st.session_state.page = 'home'
        
#メイン実行文
if st.session_state.page == 'home':
    home()
elif st.session_state.page == 'page1':
    page1()
elif st.session_state.page == 'page1_ans':
    page1_ans()
elif st.session_state.page == 'page2':
    page2()
elif st.session_state.page == 'page2_ans':
    page2_ans()
elif st.session_state.page == 'page3':
    page3()
elif st.session_state.page == 'page3_ans':
    page3_ans()
elif st.session_state.page == 'page4':
    page4()
elif st.session_state.page == 'page4_ans':
    page4_ans()
elif st.session_state.page == 'page5':
    page5()
elif st.session_state.page == 'page5_ans':
    page5_ans()
elif st.session_state.page == 'page6':
    page6()
elif st.session_state.page == 'page6_ans':
    page6_ans()
elif st.session_state.page == 'page7':
    page7()