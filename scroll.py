import time

def create_rolling_scroll(text):
    scroll_width = 30  # Adjust the scroll width as desired
    border_char = '|'

    # Create the text section
    text_lines = text.split('\n')

    # Determine the length of the longest line
    max_line_length = max(len(line) for line in text_lines)

    # Create top and bottom borders with proper length
    top_border = f'{border_char * (max_line_length + 4)}'
    bottom_border = f'{border_char * (max_line_length + 4)}'

    # Assemble the initial scroll with top and bottom borders
    medieval_scroll = f'''
{top_border}
{border_char}{' ' * max_line_length} {border_char}
{border_char}{' ' * max_line_length} {border_char}
{border_char}{' ' * max_line_length} {border_char}
{border_char}{' ' * max_line_length} {border_char}
{border_char}{' ' * max_line_length} {border_char}
{border_char}{' ' * max_line_length} {border_char}
{border_char}{' ' * max_line_length} {border_char}
{border_char}{' ' * max_line_length} {border_char}
{bottom_border}
'''

    num_roll_lines = min(len(text_lines), 1)  # Adjust the number as desired
    rolled_text = '\n'.join([f'{border_char} {line.ljust(max_line_length)} {border_char}' for line in text_lines[:]])
    rolled_scroll = medieval_scroll + rolled_text + medieval_scroll
    print(rolled_scroll)
    time.sleep(0.5)  # Adjust the delay as desired

if __name__ == "__main__":
    scroll_text = """
This is a smaller rolling medieval-style scroll
created using Python.

You can adjust the number of rolled lines
to make the scroll roll even smaller.

Have fun!
    """

    create_rolling_scroll(scroll_text)
