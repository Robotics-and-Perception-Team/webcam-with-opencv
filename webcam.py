# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:08:51 2020

@author: Eren
"""
import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
