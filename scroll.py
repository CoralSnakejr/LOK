import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_rolling_scroll(scroll_width, text, new_text):
    border_char = '|'

    # Create the text section
    text_lines = text.split('\n')
    new_text_lines = new_text.split('\n')

    # Create top and bottom borders with the specified scroll width
    top_border = f'{border_char * (scroll_width + 4)}'
    bottom_border = f'{border_char * (scroll_width + 4)}'

    clear_console()
    print(top_border)
    for line in text_lines:
        lines = [line[i:i+scroll_width] for i in range(0, len(line), scroll_width)]
        for line in lines:
            line = line.ljust(scroll_width)
            print(f'{border_char} {line} {border_char}')
    print(top_border)

    input("Press Enter to switch the text...")

    clear_console()
    print(top_border)
    for line in new_text_lines:
        lines = [line[i:i+scroll_width] for i in range(0, len(line), scroll_width)]
        for line in lines:
            line = line.ljust(scroll_width)
            print(f'{border_char} {line} {border_char}')
    print(bottom_border)

    input("Press Enter to continue...")

if __name__ == "__main__":
    scroll_width = 30  # Adjust the scroll width as desired

    scroll_text = """
This is a smaller rolling medieval-style scroll
created using Python.

You can adjust the number of rolled lines
to make the scroll roll even smaller.

Have fun!
    """

    new_text = """
Here's some new text with a fading effect.
This text will replace the previous text after you press Enter.
"""

    create_rolling_scroll(scroll_width, scroll_text, new_text)
