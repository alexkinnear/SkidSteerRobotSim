# Mobility for Wheeled Ground Systems

### Part A
(10 pts) plot the following commanded path in global (x,y) space:
| Duration of command | Left Wheel Velocity | Right Wheel Velocity |
|---------------------|---------------------|----------------------|
| 5s                  | 1m/s                | 1.5m/s               |
| 3s                  | -1m/s               | -1.5m/s              |
| 10s                 | 2m/s                | 2m/s                 | 

The solution to part A can be seen by running the function a() in SSR_sim.py. The graph will appear, and can also be seen in the file a, included in the zip folder. 

### Part B
(10 pts) Make a list of commands that will allow this robot to cover a space of 5m x 5m. Plot the resulting path (x, y) and trajectory (x, y, and angular velocities).

The solution to part B can be seen by running the function b() in SSR_sim.py. The graph will appear, and can also be seen in the file b, included in the zip folder.
The solution works like this:

1. Move forward 5 meters; Θ = 0 degrees, vel_left = 1m/s, vel_right = 1m/s, duration = 5s
2. Turn in place 90 degrees to the right. The velocity slows down to increase accuracy in turning exactly 90 degrees; 	Θ = 0 → -90 degrees, vel_left = 0.5m/s, vel_right = -0.5, duration = 0.471s. I calculated that the Θ value would be at -90 degrees if the wheels were at the described values for 0.471s.
3. Move forward 0.25m. We could move forward as far as the width of the robot (0.3m), however, since we want to cover a space of 5x5m, we are going to move 0.25m at a time since 5 is divisible by 0.25, and not 0.3. Θ = -90 degrees, vel_left = 1/s, vel_right = 1, duration = 0.25s
4. Turn in place 90 degrees to the right; Θ = -90 → 180 degrees, vel_left = 0.5m/s, vel_right = -0.5, duration = 0.471s
5. Move forward 5 meters; Θ = 180 degrees, vel_left = 1m/s, vel_right = 1m/s, duration = 5s
6. Turn in place 90 degrees to the left; Θ = 180 → -90 degrees, vel_left = -0.5m/s, vel_right = 0.5, duration = 0.471s
7. Move forward 0.25m; Θ = -90, vel_left = 1m/s, vel_right = 1m/s, duration = 0.25s
8. Turn in place 90 degrees to the left; Θ = -90 → 0 degrees, vel_left = -0.5m/s, vel_right = 0.5, duration = 0.471s

After steps 1-8, our heading of the robot is back to 0 degrees, and we can repeat steps 1-8 10 more times (Done in a for loop in the code). Once that is done, we move forward 5 meters again as we do in step 1 to complete the final stretch of covering the 5x5m space.

### Part C
(10 pts) Do the same as the above but assume that you have swedish wheels. What has changed? What are the problems we can expect to see if we try to implement your commands on either skid-steered or swedish wheel systems?

The solution to part C can be seen by running the function c() in SSR_sim.py. The graph will appear, and can also be seen in the file c, included in the zip folder.
The graph appears the same as the graph from part b. The path that the robot takes is the same, however, the advantage of swedish wheels is that the robot is holonomic, meaning that it can turn in any direction at any time. For part be, we had to set the left wheel velocity and right wheel velocity opposite each other, and then calculate how long they had to spin until a 90 degree turn had been made before we could move the robot forward again. In the case of part C, this was no longer necessary. We could simply set the Θ value to the direction we needed to go, and then proceed to move forward. This can be seen by in the code for part C. Essentially, the steps where we make a turn in part B (steps 2, 4, 6, and 8), we can just set the value of Θ to -90, 180, or 0 degrees depending on the direction we need to go. 

The problems that could be seen if my code were to be run on an actual skid steer or swedish wheeled robot is the code is not flexible to run on any environment. It is intended for a flat surface with no friction or other outside factors that influence the movement of a robot in authentic situations. The reading also explains that there are more sophisticated and accurate models for obtaining descrete-time models than Euler's integreation method which I used in my code.