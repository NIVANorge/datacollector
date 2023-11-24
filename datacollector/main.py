import PySimpleGUI as sg

sg.user_settings_filename(path=".")

def main():
    

    # Notice that the Input element has a default value given (first parameter) that is read from the user settings
    layout = [
        [sg.Text("Enter a filename2:")],
        [
            sg.Input(sg.user_settings_get_entry("-filename-", ""), key="-IN-"),
            sg.FileBrowse(),
        ],
        [
            sg.B("Save"),
            sg.B("Exit Without Saving", key="Exit"),
            sg.T("(or click X to close without saving)"),
        ],
    ]

    window = sg.Window("Filename Example", layout)
    window.maximize()
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        elif event == "Save":
            sg.user_settings_set_entry("-filename-", values["-IN-"])

    window.close()


if __name__ == "__main__":
    main()
