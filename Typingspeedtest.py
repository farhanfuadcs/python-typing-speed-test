import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to typing test!")
    stdscr.addstr("\nPress any key to start.")
    stdscr.refresh()
    stdscr.getkey()

def load_text():
    with open("text.txt","r") as f:
        lines=f.readlines()
        return random.choice(lines).strip()

def text_display(stdscr,target,current,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0,f"WPM: {wpm}")
    for i,char in enumerate(current):
        current_char=target[i]
        color=curses.color_pair(1)
        if char!=current_char:
            color=curses.color_pair(2)
        stdscr.addstr(0,i,char,color)


def wpm_test(stdscr):
    target_text=load_text()
    current_text=[]
    wpm=0
    start_time=time.time()
    stdscr.nodelay(True)
    while True:
        time_total=max(time.time()-start_time,1)
        wpm=round((len(current_text)/((time_total)/60))/5)
        stdscr.clear()
        text_display(stdscr,target_text,current_text,wpm)
        stdscr.refresh()
        if "".join(current_text)==target_text:
            stdscr.nodelay(False)
            break
        try:
            key=stdscr.getkey()
        except:
            continue
        if ord(key)==27:
            break
        if key in ("KEY_BACKSPACE","\b","\x7f"):
            if len(current_text)>0:
                current_text.pop()
        elif len(target_text)>len(current_text):
            current_text.append(key)
        




def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0,"You completed the test!\nPress any key to start again")
        key=stdscr.getkey()
        if ord(key)==27:
            break


wrapper(main)