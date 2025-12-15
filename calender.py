import PySimpleGUI as sg

sg.theme("SystemDefault")


layout = [[
    sg.Input(key="-DATE-"),
    sg.CalendarButton(
        "Click to open the calendar",
        target="-DATE-",
        format="%m-%d-%Y",
        default_date_m_d_y=(1, 1, 2025),
    ),
    sg.Button("Date Popup"),
    sg.Exit(),
]]

window = sg.Window("Calendar", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event == "Date Popup":
        chosen = sg.popup_get_date()
        if chosen:
            month, day, year = chosen
            window["-DATE-"].update(f"{month:02d}-{day:02d}-{year}")
            sg.popup("You chose", f"{month:02d}-{day:02d}-{year}")
        else:
            sg.popup("No date selected")

window.close()
