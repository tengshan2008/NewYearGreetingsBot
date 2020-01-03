import PySimpleGUI as sg
import itchat


button_sign_in = sg.Button('登录',
                           size=(5, 1),
                           key='_SIGNIN_')

button_switch = sg.Button('开始',
                          size=(5, 3),
                          key='_SWITCH_',
                          button_color=('white', 'green'))

# sg.theme('DarkAmber')  # Add a touch of color
layout = [[sg.Text('账号：', size=(15, 1)), button_sign_in],
          [button_switch]]

# Create the Window
window = sg.Window('自动拜年机器人', layout)

switch = True


def signin():
    """
    sign in weixin
    """
    itchat.auto_login()
    pass


def controller():
    """
    start and stop program
    """
    while switch:
        pass


# Event Loop
while True:
    event, values = window.Read()
    if event in (None, 'Quit'):
        break
    if event == '_SWITCH_':
        switch = not switch
        window.Element('_SWITCH_').Update(
            ('停止', '开始')[switch],
            button_color=(('white', ('red', 'green')[switch]))
        )
        controller()
    if event == '_SIGNIN_':
        signin()

window.close()
