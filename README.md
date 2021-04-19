# NBA-Ticker
The purpose of this project is to display live NBA scores on an Adafruit 16x32 LED Matrix.

# Hardware
I used [Adafruit's 16x32 LED Matrix](https://www.adafruit.com/product/420), their [MatrixPortal](https://www.adafruit.com/product/4745) and a USB C power supply

# Software
The code is written in Python using Adafruit and CircuitPython's libraries to control the LED Board. The board automatically runs the `code.py` file. `lambda.py` is a lambda function running on AWS that gets live scores from NBA.com. I set it up through API Gateway to be accessible using an API call. The URL and API-KEY are not included in the project but are necessary in a `secrets.py` file to be able to run this code

https://user-images.githubusercontent.com/32146689/115180640-1b6ad900-a0a4-11eb-92f9-a2b3cf7d4238.MOV
