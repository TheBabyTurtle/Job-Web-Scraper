# https://www.geeksforgeeks.org/user-input-in-pysimplegui/
import PySimpleGUI as sg

# Add some color to the window
sg.theme('SandyBeach')

# Very basic window.
# Return values using automatic-numbered keys
layout = [
    [sg.Text('Please enter specifications')],
    [sg.Text('Job Field', size=(25, 1)), sg.InputText()],
    [sg.Text('Location', size=(25, 1)), sg.InputText()],
    [sg.Text('Experience Level (e.g, Entry Level)', size=(25, 1)), sg.InputText()],
    [sg.Text('Position (e.g, Full-time)', size=(25, 1)), sg.InputText()],
    [sg.Submit()]
]

window = sg.Window('Web Scraper', layout)
event, values = window.read()
window.close()

# The input data looks like a simple list when automatic numbered
print(event, values[0], values[1], values[2], values[3])
