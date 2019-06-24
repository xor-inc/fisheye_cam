# You should replace these 3 lines with the output in calibration step
import cv2
assert cv2.__version__[0] == '3', 'The fisheye module requires opencv version >= 3.0.0'

import numpy as np
import os
import glob
import sys
DIM=(1280, 720)
K=np.array([[526.1294858739368, 0.0, 635.4168192781472], [0.0, 528.5213555116729, 329.44239083966767], [0.0, 0.0, 1.0]])
D=np.array([[-0.027813474371374894], [0.028948692665810603], [0.03496661454701722], [-0.06135759529623624]])

def undistort(img_path):

    img = cv2.imread(img_path)
    h,w = img.shape[:2]

    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)

    cv2.imshow("undistorted", undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    for p in sys.argv[1:]:
        undistort(p)
