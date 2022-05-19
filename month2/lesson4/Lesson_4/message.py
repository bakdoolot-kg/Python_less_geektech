import colorama

_SECRET_KEY = "12345678"
test = 123

fore = colorama.Fore
style = colorama.Style
back = colorama.Back


def paint_my_text(text, color):
    print(color, text)


def message(
        text: str,
        color,
        font_style: str,
        secret_key: str
) -> str:
    font_styles = {
        "upper": text.upper(),
        "lower": text.lower()
    }
    if secret_key == _SECRET_KEY:
        paint_my_text(font_styles[font_style], color)
    else:
        print("You dont have permissions!")

    return ''
