import PySimpleGUI as sg
import os. path
# window layout of two columns
file_list_column = [
    [

        sg.Text("Input"), sg.In(size=(25, 1),
                                enable_events=True, key="-FOLDER-")],
    [
        sg.Button('SEND', button_color=(
            sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True)
    ]
]


image_viewer_column = [
    [sg.Text("Choose an image from the list on the left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")], ]

layout = [[
    sg.Column(file_list_column), sg.VSeperator(), sg.Column(image_viewer_column)]]


window = sg.Window("Image Viewer", layout)
# event loop
while True:
    event, values = window.read()
    # 'in' elements using event, event is a map
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "SEND":
        textInput = event[""]
        # this is how we check for an event
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # get list of files in folder
            file_list = os. listdir(folder)
        except:
            file_list = []
        fnames = [
            f
            for f in file_list
            if os. path.isfile(os.path.join(folder, f)) and f. lower().endswith((".png", ".gif"))
        ]
        # this is how we update the file list
        window["-FILE LIST-"].update(fnames)
window.close()
