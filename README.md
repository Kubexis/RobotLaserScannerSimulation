# Robot Laser Scanner Simulation


This project implements a program that simulates a laser scanner for a robot, designed to measure distances in a predefined environment. The environment, containing obstacles, is provided as a PNG file, and the robot's current position and orientation are specified in a text file. The program visualizes the laser beams on the environment image and calculates the lengths of the beams, saving the results to a text file.



## Execution / Usage

Before running the program, make sure you have the following installed:

- Python 3.10+
- Required Python libraries (install from requirements.txt):

1. **Clone the repository**:

   If you haven't already, clone the repository to your local machine:

   ```bash
   git clone https://github.com/Kubexis/RobotLaserScannerSimulation.git

2. **Navigate to the project directory**:

   Go into the project directory:

        cd RobotLaserScannerSimulation

3. **Create and activate a virtual environment (optional but recommended)**:

    For Python 3.10+:

        python -m venv venv

        On Windows:

        venv\Scripts\activate

        On macOS/Linux:

        source venv/bin/activate

4. **Install the required dependencies**:

   Install the dependencies from the requirements.txt file:

        pip install -r requirements.txt


5. **Prepare your input files**:

    Environment file (otoczenie.png):

        A 320x240 PNG image file with obstacles (black pixels).

    Parameters file (parametry.txt):

        A text file containing the robot's position and orientation:

        x, y, angle - Where x and y are the coordinates (ranging from [0, 320] and
        [0, 240], respectively), and angle is the orientation of the robot
        in degrees (ranging from [0, 360]). Separated by spaces.
        File format should look like this:
        x y angle


6. **Run the simulation**:

    Execute the simulation by running the Python script:

        python main.py
## Author

Jakub Mierzejewski – jakubmierzejewski3@icloud.com
