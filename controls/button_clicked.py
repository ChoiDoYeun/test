# button_clicked.py
selected_location = None

def button_clicked(button_text, callback=None):
    global selected_location
    selected_location = button_text
    if callback:
        callback(selected_location)

def get_selected_location():
    return selected_location