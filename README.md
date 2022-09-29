# Speed-of-Sound
# Speed-of-Sound
This project is to measure the speed of sound. In order to achieve this, two KY-037 sound sensors will be placed on a
leveled ground and kept in different places.

The distance between the two sound sensors will then be measured.

Working principle:
The python code called timer.py in the repository will be executed. A clap or a loud bang will be made in front of one of the sound sensors. When the clap is made,
the timer starts. The other sound sensor will stop the timer when the sound reaches it. Please note that the microphone of the two sound sensors should be facing
each other for the experiment to work.

Since we have the distance between the sound sensors and the time it takes for sound to travel from the first sound sensor to the other one, the speed of sound
can be calculated.
This can be done by dividing the distance by the time (secs). Be careful of the unit used for measuring the distance.

Also, for this project, a platform was manufactured to hold the two sound sensors. The SolidWorks part file of this structure can be seen in this repository.
The aim of this project was to practically demonstrate how the speed of sound can be obtained.

Design of the platform:
A wooden structure was made and a 1.5l Coca-cola bottle was cut and nailed to the top of the structure. The opening of the bottle will be used to place the sound
sensor.
During the experiment, I noticed that there are errors in the time gotten from the program when the sound sensors are placed very far apart i.e. larger than 5m. 
After trying different solution, it was observed that the sound waves were not concentrating well on the microphone of the sound sensor.
To solve this problem, there has to be an opening that concentrates the sound waves to the microphone. This is why the 1.5l bottle works well for the project.
