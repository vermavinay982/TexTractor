from extract_text import *

def show():
    print("Showing the text")


def find_text(file, search, ctr, debug):
    print("Extracting the text from",file, search, ctr, debug)
    op_file, ctr = find_text_video(file, search, ctr, debug)
    return op_file, ctr

def extract_video_text(file, debug):
    print("Extracting the text from",file, debug)
    op_file, text = extract_text(file, debug)
    return op_file, text
