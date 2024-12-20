import sys
import numpy as np
import cv2
 
# goal: circuit 이미지에서 crystal 이미지의 위치를 찾기 
#%% 입력 영상 & 템플릿 영상 불러오기
src = cv2.imread(r'd:\NewImageName.bmp', cv2.IMREAD_GRAYSCALE)
templ = cv2.imread(r'd:\NewImageName2.bmp', cv2.IMREAD_GRAYSCALE)
 
if src is None or templ is None:
    print('Image load failed!')
    sys.exit()
 
#%% 입력영상을 약간 변경해 보자 
noise = np.zeros(src.shape, np.int32)
cv2.randn(noise, 50, 10) # 입력 영상 밝기 50증가,가우시안 잡음(sigma=10) 추가
src = cv2.add(src, noise, dtype=cv2.CV_8UC3)
 
# 템플릿 매칭 & 결과 분석
res = cv2.matchTemplate(src, templ, cv2.TM_CCOEFF_NORMED) # res의 범위: -1~0
res_norm = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U) 
# res_norm: res의 범위를 0~255로 변경 
 
_, maxv, _, maxloc = cv2.minMaxLoc(res) # minMaxLoc: 최소값, 최대값의 값, 위치를 반환
print('maxv:', maxv)
print('maxloc:', maxloc)
 
#%% 매칭 결과를 빨간색 사각형으로 표시
th, tw = templ.shape[:2]
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
cv2.rectangle(dst, maxloc, (maxloc[0] + tw, maxloc[1] + th), (0, 0, 255), 2)
 
# 결과 영상 화면 출력
cv2.imshow('src', src)
cv2.imshow('templet', templ)
cv2.imshow('res_norm', res_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()