# Lab 4 - Git and GitHub Collaboration

## Project Overview

This project was developed for Lab 4 for EECE435L.

The objective of this project is to practice collaborative development using Git and GitHub by developing two graphical user interfaces for the same School Management System.

The project includes:

- A Tkinter interface
- A PyQt interface
- Shared Python classes used by the application

Both interfaces were developed on separate branches and later merged into the `main` branch.

## Team Members

- Rawan El Anouti
- Hanaa Ballout

## Branches

- `main` - Final integrated project
- `feature-tkinter` - Tkinter implementation
- `feature-pyqt` - PyQt implementation

## Project Features

The School Management System supports:

- Adding students
- Adding instructors
- Adding courses
- Editing records
- Deleting records
- Searching for records
- Registering students in courses
- Assigning instructors to courses

## Project Files

- `tkinter_app.py` - Tkinter graphical user interface
- `part3_pyqt.py` - PyQt graphical user interface
- `part1_oop.py` - Shared object-oriented classes used by the application
- `README.md` - Project documentation

## How to Run the Project

Make sure Python is installed on your computer.

### Run the Tkinter Interface

Open a terminal inside the project folder and run:

```bash
python tkinter_app.py

### Run the PYQT Interface

Open a terminal inside the project folder and run:

```bash
python part3_pyqt.py
