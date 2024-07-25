time.sleep(20)
for i in range(len(android_dev_messages)):
    pg.click()
    pg.write(android_dev_messages[i])

    # pg.press("enter") 
    pg.hotkey('ctrl', 'enter')
    time.sleep(5)
