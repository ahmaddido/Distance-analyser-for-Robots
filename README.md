
# Robot Distance Sensor Analyzer


## Overview

Robot Distance Sensor Analyzer is a Python-based project designed to simulate the processing and analysis of distance sensor measurements for obstacle detection in autonomous robots.

The program accepts distance measurements in centimeters, classifies them according to their proximity, calculates statistical information, and recommends an appropriate robot action based on the detected obstacles.

This project was developed as part of my journey, with a focus on strengthening Python fundamentals, problem-solving skills, and programming logic. 



## Project Structure

- **`analyser.py`** — Main program responsible for collecting, classifying, and displaying sensor measurements.
- **`func.py`** — Contains reusable functions for statistical calculations and robot decision-making.


## Example

**Input measurements:**

`15, 15, 30, 30, 70`

**Expected analysis:**

- Total measurements: 5
- Minimum distance: 15 cm
- Maximum distance: 70 cm
- Average distance: 32 cm
- DANGER readings: 2
- WARNING readings: 2
- SAFE readings: 1
- Final decision: STOP

## Future Improvements

This project is currently a software-based simulation using manually entered measurements. Future developments may include:

- Export measurement statistics, classifications, and robot decisions into a structured PDF report.
- Connect a physical distance sensor, such as an ultrasonic sensor, to collect real measurements.
- Continuously process incoming sensor data instead of relying on manually entered measurements.
- Display distance measurements and classification trends using charts.


## Note

The Python implementation was written independently by me, without using AI generated code. AI was used only for code reviewe and with the README documentation support. All program logic and code changes were by me.
