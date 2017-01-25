"""Instagram Follow Bot"""
import pyautogui

mouse_cood = " " #Mouse co-ordinate 
flag = 0
def followBot(address, index):
    """Locates the follow button and clicks it"""
    global flag
    global mouse_cood
    mouse_cood = pyautogui.locateCenterOnScreen(address)
    if mouse_cood != None:
        print("Follow icon found at " + str(index + 1) + \
              "  : " + str(mouse_cood))
        pyautogui.moveTo(mouse_cood, duration=0.4)
        pyautogui.click(mouse_cood)
        flag = 1


follow_icon_array1 = ['C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow1.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow2.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow3.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow4.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow5.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow6.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow7.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow8.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow9.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow10.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow11.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow12.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow13.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow14.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow14.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow14.png']

follow_icon_array2 = ['C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow15v.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow16.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow17.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow18.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow19.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow20.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow21.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow22.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow23.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow24.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow25.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow26.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow27.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow28.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow29.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow30.png']

follow_icon_array3 = ['C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow31v.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow32.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow33.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow34.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow35.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow36.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow37.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow38.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow39.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow40.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow41.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow42.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow43.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow44.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow45.png'\
                    , 'C:\\Users\\mayan_dx0nues\\Pictures\\instafollow\\follow45.png']


while True:
    for x in range(16):
        flag = 0
        buffer_array = []
        buffer_array.append(follow_icon_array1[x])
        buffer_array.append(follow_icon_array2[x])
        buffer_array.append(follow_icon_array3[x])
        for y in range(3):
            followBot(buffer_array[y], x)
            if flag == 1:
                break
    for x in range(15):
        pyautogui.press('down')
