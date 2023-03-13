import pyautogui as gui
import time

DIR = input('Enter the folder path: ')
totalPages = int(input('Enter the number of pages: '))
page = int(input('Enter the first page: '))

for i in range(totalPages - page):

    gui.moveTo(400, 50)
    time.sleep(0.1)
    gui.click()

    gui.hotkey('ctrl', 'a')
    gui.write(f'https://etext-content.gls.pearson-intl.com/eplayer/pdfassets/prod1/145000/2d0b813a-d3e5-4f13-bcc4-fd544af7914c/pages/page{page}')
    gui.press('enter')

    time.sleep(1)

    gui.click()
    gui.click()
    gui.write(DIR)

    gui.press('enter')
    time.sleep(1)

    gui.moveTo(500, 620)

    gui.click()
    gui.click()

    gui.write(f'page{page}.png')

    gui.press('enter')
    page += 1
    time.sleep(5)
    


