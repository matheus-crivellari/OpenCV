# OpenCV Study
This repository contains a variety of python examples of OpenCV usage. This is intended for study purposes.

# OpenCV Usage
## Requirements
Some of these examples require Python 2.7.15, others require Python 3.6.2. It's highly recommended that you have both installed in your machine along with [pipenv](https://docs.pipenv.org), Python's virtual environment manager and package manager.
- Python 2.7.15 / Python 3.6.2;
- pipenv;
- numpy;
- matplotlib;
- OpenCV Python distribution;

## Installation
(These instructions are for Windows users)
Once you have correctly installed Python and pipenv, you can install this project:
- Run ``` pipenv install ``` to install all of this project's dependencies;
- Run ``` pipenv shell ``` to enter a nested cmd instance with the correct environment setup running;
- Go to [Sourceforge](https://sourceforge.net/projects/opencvlibrary) and download the correct version of OpenCV distribution for your operational system;
- Extract the self extracting .exe;
- Go to the extracted folder, find the correct build version inside it:
  ``` <extracted folder>/build/python/<opencv version>/<os architecture> ```;
- Copy the cv2.pyd inside it file and paste it onto your current working Python installation folder as follows:
  Usually: ``` C:/<python version>/Lib/site-packages ```;
- Run any of these examples with:
  ``` python <file name> ```;

## Important
Before running any of these examples, place a .jpg image on your repository root folder called ``` test.jpg ```, most of the examples will make use of it.
