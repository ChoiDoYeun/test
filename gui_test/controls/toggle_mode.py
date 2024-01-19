    def toggle_mode(button, mode, mode_name):
        mode['state'] = not mode['state']
        new_state = "ON" if mode['state'] else "OFF"
        button.config(bg='green' if mode['state'] else 'SystemButtonFace')
        print(f"{mode_name} mode is now {new_state}")
