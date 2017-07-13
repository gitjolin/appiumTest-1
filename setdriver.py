# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:33:15 2017

@author: Jo_Lin
"""

#import pandas 
#pd.Series()
#pd.show_Versions()

print("===== start =====")

from appium import webdriver
import time



desired_caps={
    'platformName':'Android',
    'deviceName':'H4AZCY00W518XPD',
    'platformVersion':'6.0.1',
    #APK Package Name
    'appPackage':'com.asus.deskclock',
    #APK Launch Activity
    'appActivity':'.DeskClock'
#     'appActivity':'com.asus.deskclock.DeskClock'
#    'appActivity':'com.asus.deskclock',
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

time.sleep(5)


comp=driver.find_element_by_xpath("//*")
print(comp)

#確認上方tab按鈕的元件
#driver.find_element_by_id("com.asus.deskclock:id/tab_icon").click()
#comp=driver.find_element_by_class_name("android.widget.LinearLayout")
#print("type:",type(comp) , "\n","\n","Data:",comp)

#count=0;
#for ob in comp:
#    count+=1
#    print(count ," . ",ob)
#for data in comp:
    


#呼叫new alarm page
#driver.find_element_by_id("com.asus.deskclock:id/bt_add_alarm").click()
#driver.find_element_by_id("com.asus.deskclock:id/asus_commonui_minutes").click()
#driver.press_keycode(7)
#driver.press_keycode(8)
#按下back
#for i in range(0,2): 
#    driver.press_keycode(4)
#    time.sleep(2)
driver.quit()
print("=====end=====")

