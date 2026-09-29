# Python Typing Speed Test

A terminal-based typing speed test built with Python. The program displays a random sentence, tracks the user's typing in real time, highlights incorrect characters, and calculates typing speed in Words Per Minute (WPM).

## Features

* Randomly selects text from a text file
* Real-time typing feedback
* Calculates WPM
* Highlights correct and incorrect characters
* Supports backspace
* Press `ESC` to exit the test
* Allows the user to start another test after completing one

## Example

The program displays a sentence such as:

```text
The quick brown fox jumps over the lazy dog.
```

As you type:

* Correct characters are displayed in green
* Incorrect characters are displayed in red
* WPM is updated in real time

## Technologies Used

* Python
* `curses`
* File handling
* Functions
* Lists
* Loops
* `random`
* `time`

## How to Run

Make sure Python is installed.

The project requires a `text.txt` file containing the sentences used for the typing tests.

Run:

```bash
python typing_test.py
```

### Windows Note

The standard Python `curses` module is primarily designed for Unix-like systems. On Windows, an additional curses-compatible package may be required.

## What I Practiced

This project helped me practice:

* Working with external text files
* Reading and processing file contents
* Using lists to store typed characters
* Real-time keyboard input
* Measuring elapsed time
* Calculating WPM
* Using the `curses` library
* Handling keyboard events
* Using random text selection
* Creating an interactive terminal application

## Known Limitations

* The typing test currently uses randomly selected lines from `text.txt`.
* WPM is calculated using the standard approximation of 5 characters per word.
* The program does not currently calculate accuracy as a percentage.
* The program is terminal-based rather than graphical.

## Future Improvements

* Add typing accuracy percentage
* Add error count
* Add a countdown before the test
* Add a score/history system
* Add difficulty levels
* Add a timer mode
* Add a graphical or web interface
* Store previous results
