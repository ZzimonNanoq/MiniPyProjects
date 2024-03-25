import win32api, win32con
import mss
import cv2 as cv, numpy as np
from matplotlib import pyplot as plt
#help(win32api)

output_filename = 'screenshot.png'
image=cv.imread('screenshot.png')

with mss.mss() as mss_instance:  # Create a new mss.mss instance
    monitor_1 = mss_instance.monitors[1]  # Identify the display to capture
    screenshot = mss_instance.grab(monitor_1)  # Take the screenshot
    mss_instance.shot(output=output_filename)

img_rgb = cv.imread('screenshot.png')
assert img_rgb is not None, "file could not be read, check with os.path.exists()"
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('G:\Gadgetz\Photoshop\CookieClicker_Rabbit1.png', cv.IMREAD_GRAYSCALE)
template2 = cv.imread('G:\Gadgetz\Photoshop\CookieClicker_Rabbit2.png', cv.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"
assert template2 is not None, "file could not be read, check with os.path.exists()"
w, h = template.shape[::-1]
w, h = template2.shape[::-1]
 
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
res = cv.matchTemplate(img_gray,template2,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
 cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
 
cv.imwrite('res.png',img_rgb)




def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#click(100,100)