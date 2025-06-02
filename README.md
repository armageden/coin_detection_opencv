# coin_detection_opencv

A simple coin detection project using OpenCV on Python.

## Requirements
- Python 3+
- OpenCV
- NumPy

On Arch Linux:
```bash
sudo pacman -S python-opencv python-numpy
```
Or install inside a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
pip install opencv-python numpy
```
## Usage
Clone or download this repository.
Update the image path in main.py as needed:
```bash
img_path = "/home/farhan/coin_detection_opencv/istockphoto-92890281-612x612.jpg"
```
Run the script:
```bash
python main.py
```
## Description
This script reads an image, applies Gaussian blur and Canny edge detection, then locates coins by finding contours. The algorithm checks each contour’s area, circularity, and polygon approximation to confirm if it’s a coin. Finally, the program draws green outlines around detected coins and displays the total count.

