import keyboard

with open("ejercicio.txt", "a") as i:

    def entrar(event):
        i.write(event.name + "\n")

keyboard.on_press(entrar)
keyboard.wait("esc")