import os
import ctypes
import sys

def change_wallpaper(image_path):
    if not os.path.isfile(image_path):
        print(f"File {image_path} does not exist.")
        return

    try:
        image_path = os.path.abspath(image_path)
        result = ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        if result:
            print("Wallpaper changed successfully.")
        else:
            print("Failed to change wallpaper.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if os.name != 'nt':
        print("This script only works on Windows.")
        sys.exit(1)
    
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        image_path = os.path.join(os.path.dirname(__file__), "src", "sung-jinwoo.jpg") # AQUI DEBES DE PONER LA RUTA LOCAL/RELATIVA DE LA IMAGEN QUE DESEAS PONER DE FONDO DE PANTALLA
    
    print(f"Attempting to change wallpaper to: {image_path}")
    change_wallpaper(image_path)
