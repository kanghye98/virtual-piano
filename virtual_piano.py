#!/usr/bin/env python
# coding: utf-8

# In[1]:


#훈련시킨 모델 가져오기
from keras.models import load_model
model=load_model('./virtual_piano_model_final.h5')


# model.summary()

# #실시간 웹캠 영상 출력
# import cv2
# from matplotlib import pyplot as plt
# from playsound import playsound
# 
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,720)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1280)
# 
# 
# #현재 웹캠이 연결되어있는지 확인s
# if not cap.isOpened():
#     raise IOError("Cannot open webcam")
#     
# #원래의 영상과 ROI영상 출력    
# while True :
#     ret,frame = cap.read()
#     cv2.rectangle(frame,(20,450),(790,560),(0,0,255),2) #웹캠 화면에 rectangle 그리기
#     img_roi=frame[450:560,20:790] #ROI 생성
#     
#     c=cv2.waitKey(1)
#     if c == 27: #아스키코드 27=ESC키 ,ESC를 누르면 종료
#         break
#         
# #release는 웹캠을 적절하게 마무리시켜줌
# cap.release()
# cv2.destroyAllWindows()

# In[4]:


#실시간 웹캠 영상 출력
import cv2
import numpy as np
from matplotlib import pyplot as plt
from playsound import playsound

cap = cv2.VideoCapture(0)


#현재 웹캠이 연결되어있는지 확인s
if not cap.isOpened():
    raise IOError("Cannot open webcam")
    
#원래의 영상과 ROI영상 출력    
while True :
    ret,frame = cap.read()
    cv2.rectangle(frame,(10,450),(635,330),(0,0,255),2) #웹캠 화면에 rectangle 그리기
    img_roi=frame[330:450,10:635] #ROI 생성

    
    #predict = model.predict_classes(dst)
    
    cv2.imshow('ROI',img_roi)
    cv2.imshow('Webcam', frame)
    #print(predict)
    
    c=cv2.waitKey(1)
    if c == 27: #아스키코드 27=ESC키 ,ESC를 누르면 종료
        break
    elif c == 32: #스페이스바를 누르면 ROI설정
        img=img_roi
    #img=img.resize(105,500,3)
        dst = cv2.resize(img, dsize=(500,105), interpolation=cv2.INTER_AREA)
        dst = cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)
        dst=dst.reshape(1,105,500,3)
        predict = model.predict_classes(dst)
        if predict==[0]:
            playsound("./piano_sounds/a4.wav")
            print("a4")
        elif predict==[1]:
            playsound("./piano_sounds/b4.wav")
            print("b4")
        elif predict==[2]:
            print("c4")
            playsound("./piano_sounds/c4.wav")
        elif predict==[3]:
            print("c5")
            playsound("./piano_sounds/c5.wav")
        elif predict==[4]:
            print("d4")
            playsound("./piano_sounds/d4.wav")
        elif predict==[5]:
            print("e4")
            playsound("./piano_sounds/e4.wav")
        elif predict==[6]:
            print("f4")
            playsound("./piano_sounds/f4.wav")
        elif predict==[7]:
            print("g4")
            playsound("./piano_sounds/g4.wav")
        elif predict==[8]:
            print("no piano")        
        else:
            print("can't play piano")
            print(predict)
        
#release는 웹캠을 적절하게 마무리시켜줌
cap.release()
cv2.destroyAllWindows()


# #실시간 웹캠 영상 출력
# import cv2
# from matplotlib import pyplot as plt
# from playsound import playsound
# 
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,720)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1280)
# 
# 
# #현재 웹캠이 연결되어있는지 확인s
# if not cap.isOpened():
#     raise IOError("Cannot open webcam")
#     
# #원래의 영상과 ROI영상 출력    
# while True :
#     ret,frame = cap.read()
#     if ret == False:
#         break
# 
#     cv2.rectangle(frame,(20,300),(790,560),(0,0,255),2) #웹캠 화면에 rectangle 그리기
#     img_roi=frame[450:560,20:790] #ROI 생성
#     
#     img=img_roi
#     #img=img.resize(105,500,3)
#     dst = cv2.resize(img, dsize=(500,105), interpolation=cv2.INTER_AREA)
#     dst=dst.reshape(1,105,500,3)
#     
#     predict = model.predict_classes(dst)
#     
#     if predict==[0]:
#         playsound("./piano_sounds/a4.wav")
#     elif predict==[1]:
#         playsound("./piano_sounds/b4.wav")
#     elif predict==[2]:
#         playsound("./piano_sounds/c4.wav")
#     elif predict==[3]:
#         playsound("./piano_sounds/c5.wav")
#     elif predict==[4]:
#         playsound("./piano_sounds/d4.wav")
#     elif predict==[5]:
#         playsound("./piano_sounds/e4.wav")
#     elif predict==[6]:
#         playsound("./piano_sounds/f4.wav")
#     elif predict==[7]:
#         playsound("./piano_sounds/g4.wav")
#     elif predict==[8]:
#         print("no piano")        
#     else:
#         print("can't play piano")
# 
#     #cv2.imshow('ROI',img_roi)
#     cv2.imshow('Webcam', frame)   
#     c=cv2.waitKey(1)
#     if c == 27: #아스키코드 27=ESC키 ,ESC를 누르면 종료
#         break
#         
# #release는 웹캠을 적절하게 마무리시켜줌
# cap.release()
# cv2.destroyAllWindows()

# In[ ]:





# In[ ]:




