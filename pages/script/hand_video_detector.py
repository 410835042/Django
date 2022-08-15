import cv2
import mediapipe as mp
import numpy as np
import math


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# this method is used to deduce the hand_video method
# plz refer to the hand_video method accordingly
# def hand_image():
#     # For static images:
#     hands = mp_hands.Hands(
#         static_image_mode=True,
#         max_num_hands=2,
#         min_detection_confidence=0.5)
#
#     # feed a video:
#     videoFile = "test_vid.mp4"
#     cap = cv2.VideoCapture(videoFile)
#     flag, frame = cap.read()
#
#     # while cap.isOpened():
#     while flag:
#         image = cv2.flip(frame, 1)
#         frame_ID = cap.get(1)
#         results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#         print('Handedness:', results.multi_handedness)
#         if not results.multi_hand_landmarks:
#             continue
#         image_hight, image_width, _ = image.shape
#         annotated_image = image.copy()
#         for hand_landmarks in results.multi_hand_landmarks:
#             print('hand_landmarks:', hand_landmarks)
#             print(
#                 f'Index finger tip coordinates: (',
#                 f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
#                 f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_hight})'
#             )
#             mp_drawing.draw_landmarks(
#                 annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#         cv2.imwrite(
#             '/tmp/annotated_image_' + str(frame_ID) + '.png', cv2.flip(annotated_image, 1))
#         flag, frame = cap.read()
#     hands.close()


def hand_video(flag, frame):
    times = 0
    # For static images:
    # parameters for the detector
    hands = mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=2,
        min_detection_confidence=0.5)
    # flip it along y axis
    image = cv2.flip(frame, 1)
    # color format conversion
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    # print('Handedness:', results.multi_handedness)
    if not results.multi_hand_landmarks:
        hands.close()
        return frame
    image_hight, image_width, _ = image.shape
    annotated_image = image.copy()

    if times == 10:  # 加上去的
        print_hand_length(results)
    times += 1

    # draw result landmarks
    for hand_landmarks in results.multi_hand_landmarks:
        # print('hand_landmarks:', hand_landmarks)
        # print(
        #     f'Index finger tip coordinates: (',
        #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
        #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_hight})'
        # )
        mp_drawing.draw_landmarks(
            annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    # flip it back and return
    return cv2.flip(annotated_image, 1)

# save the video if user chooese so
# def vid_save():
#     cap = cv2.VideoCapture(0)
#
#     # Define the codec and create VideoWriter object
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
#
#     while(cap.isOpened()):
#         ret, frame = cap.read()
#         if ret==True:
#             frame = cv2.flip(frame,0)
#
#             # write the flipped frame
#             out.write(frame)
#
#             cv2.imshow('frame',frame)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         else:
#             break
#
#     # Release everything if job is finished
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()


def print_hand_length(results):
    joint_list1 = [[5], [9]]  # 量指寬
    joint_list2 = [[9], [12]]  # 量指長
    joint_list3 = [[0], [9]]  # 量手掌高度
    joint_list4 = [[5], [17]]  # 量手掌寬度
    subX = subY = subA = subB = subC = subD = subE = subF = 0.00
    for hand in results.multi_hand_landmarks:
        for joint in joint_list1:
            a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y])
            subX = abs(subX - round(a[0], 2))
            subY = abs(subY - round(a[1], 2))
        for joint in joint_list2:
            a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y])
            subE = abs(subE - round(a[0], 2))
            subF = abs(subF - round(a[1], 2))
        for joint in joint_list3:
            a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y])
            subA = abs(subA - round(a[0], 2))
            subB = abs(subB - round(a[1], 2))
        for joint in joint_list4:
            a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y])
            subC = abs(subC - round(a[0], 2))
            subD = abs(subD - round(a[1], 2))
    XY2 = round(math.sqrt(pow(subX, 2)+pow(subY, 2)), 2)
    EF2 = round(math.sqrt(pow(subE, 2) + pow(subF, 2)), 2)
    AB2 = round(math.sqrt(pow(subA, 2)+pow(subB, 2)), 2)
    CD2 = round(math.sqrt(pow(subC, 2) + pow(subD, 2)), 2)
    print("finger width size:" + str(XY2 * 34.5) + "cm")
    print("middle finger length:" + str((EF2 * 34.5)-2.0) + "cm")
    print("palm height:" + str((AB2 * 34.5)-1.5) + "cm")
    print("palm width:" + str((CD2 * 34.5)+1.5) + "cm")
