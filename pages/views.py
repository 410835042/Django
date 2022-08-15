from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse

from .script.GetHand import Hand
from .script.camera import VideoCamera, gen

import mediapipe as mp
import numpy as np
import math
import cv2

# Create your views here.


def home_view(request, *args, **kwargs):
    print(request.user)  # 在終端機中輸出提出請求的使用者是誰（不安全）
    # return HttpResponse("<h1>Home Page</h1>") #HTML的寫法。 此寫法較不完善，後面改用下行樣式
    return render(request, "home.html", {})  # 從名為home.html模板中抓取此頁應有樣貌


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def threed_model_view(request):
    return render(request, "3D_model/3d_js.html")


def button(request):
    return render(request, 'med_hand.html')


# def get_hand(request):
#     # return render(request, 'med_hand.html')
#     return HttpResponse(request, 'med_hand.html')


def get_hand(request):
    Hand()
    return HttpResponse(request, 'get_hand.html')


# def get_hand(request):
#     mp_drawing = mp.solutions.drawing_utils  # 繪製方法、工具。將座標繪製到螢幕上
#     mp_drawing_styles = mp.solutions.drawing_styles  # mediapipe 繪圖樣式。匯入手模型
#     mp_hands = mp.solutions.hands  # mediapipe 偵測手掌方法
#     cap = cv2.VideoCapture(0)  # 建立一個VideoCapture物件，物件會連接到一隻網路攝影機，0代表第一支攝影機
#     # 用攝像頭即時拍照傳到後台(即時攝影)
#     with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5,
#                         min_tracking_confidence=0.5) as hands:  # 啟動偵測和追蹤
#         if not cap.isOpened():
#             print("Cannot open camera")
#             exit()
#         while True:  # 原本是while cap.isOpened()，怕一直判斷會拖慢速度
#             ret, frame = cap.read()
#             # 每次呼叫cap.read()就會讀取一張畫面，第一個傳回值ret代表成功與否（True成功False失敗)，第二個傳回值frame是攝影機的單張畫面。
#             if not ret:
#                 print("Cannot receive frame")
#                 break
#             image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # BGR轉RGB #轉換顏色設定順序：mediapipe讀法為bgr python為rgb
#             image = cv2.flip(image, 1)  # 螢幕左右翻轉
#             image.flags.writeable = False  # 為了提高效率，將圖像標記改為不可寫入模式
#             results = hands.process(image)  # 在圖像上偵測和追蹤，results就是偵測和追蹤的結果(result會記錄手部關節點的位置(xy軸)和關節點編號)
#             image.flags.writeable = True
#             image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#
#             if results.multi_hand_landmarks:  # 檢查手座標是否有輸出
#                 for num, hand in enumerate(results.multi_hand_landmarks):  # num:左手是0右手是1。hand是21個關節點的座標
#                     mp_drawing.draw_landmarks(
#                         image, hand, mp_hands.HAND_CONNECTIONS,  # 在圖像上實際繪製landmark(改解釋)
#                         mp_drawing.DrawingSpec(color=(121, 87, 76), thickness=1, circle_radius=4),
#                         # 關節點顏色 color:(藍，綠，紅)
#                         mp_drawing.DrawingSpec(color=(255, 255, 25), thickness=2, circle_radius=2),  # 關節顏色
#                     )
#
#
#                 joint_list1 = [[5], [9]]  # 量指寬
#                 joint_list2 = [[9], [12]]  # 量指長
#                 joint_list3 = [[0], [9]]  # 量手掌高度
#                 joint_list4 = [[5], [17]]  # 量手掌寬度
#                 subX = subY = subA = subB = subC = subD = subE = subF = 0.00
#                 for hand in results.multi_hand_landmarks:
#                     for joint in joint_list1:
#                         a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y])
#                         subX = abs(subX - round(a[0], 2))
#                         subY = abs(subY - round(a[1], 2))
#                     for joint in joint_list2:
#                         a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y])
#                         subE = abs(subE - round(a[0], 2))
#                         subF = abs(subF - round(a[1], 2))
#                     for joint in joint_list3:
#                         a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y])
#                         subA = abs(subA - round(a[0], 2))
#                         subB = abs(subB - round(a[1], 2))
#                     for joint in joint_list4:
#                         a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y])
#                         subC = abs(subC - round(a[0], 2))
#                         subD = abs(subD - round(a[1], 2))
#                 XY2 = round(math.sqrt(pow(subX, 2) + pow(subY, 2)), 2)
#                 EF2 = round(math.sqrt(pow(subE, 2) + pow(subF, 2)), 2)
#                 AB2 = round(math.sqrt(pow(subA, 2) + pow(subB, 2)), 2)
#                 CD2 = round(math.sqrt(pow(subC, 2) + pow(subD, 2)), 2)
#                 print("finger width size:" + str(XY2 * 34.5) + "cm")
#                 print("middle finger length:" + str((EF2 * 34.5) - 2.0) + "cm")
#                 print("palm height:" + str((AB2 * 34.5) - 1.5) + "cm")
#                 print("palm width:" + str((CD2 * 34.5) + 1.5) + "cm")
#
#             cv2.imshow("Hand Tracking", image)  # 開新視窗顯示圖片
#             if (cv2.waitKey(10) & 0xFF == ord('q')):  # 按鍵盤Q跳出循環
#                 break
#
#     cap.release()  # 把攝像頭和彈出視窗一併關掉
#     cv2.destroyAllWindows()
#     return HttpResponse(request, 'med_hand.html')


# ~~~~ outside ~~~~

def video_stream(request):
    vid = StreamingHttpResponse(gen(VideoCamera(), False),
    content_type='multipart/x-mixed-replace; boundary=frame')
    return vid


def video_input(request):
    return render(request, 'med_hand.html')

