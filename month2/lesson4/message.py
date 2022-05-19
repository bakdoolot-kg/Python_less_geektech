import colorama

_SECRET_KEY = '12345678'
test = 123

fore = colorama.Fore
color = colorama.Style
back = colorama.Back

def paint_my_text(text, color):
    print(color, text)

def message(text, color, font_style, secret_key):
    font_styles = {
        'upper': text.upper(),
        'lower': text.lower()
    }

    if secret_key == _SECRET_KEY and type(secret_key) == str:
        paint_my_text(font_styles[font_style], color)
    else:
        print('You dont have permissions!')


