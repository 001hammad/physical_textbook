---
sidebar_position: 2
title: Chapter 2 - Fundamentals of Physical AI
---

# Chapter 2: Fundamentals of Physical AI

Now that we know what Physical AI and humanoid robots are, let’s understand the **basic building blocks** of Physical AI.  
These are the key ideas that make a robot "smart" in the real world.

### 1. Embodied Intelligence

**Embodied Intelligence** means the AI is inside a physical body (the robot).  
The robot learns by moving, touching, and seeing the real world — not just by reading data.

Example:  
- A baby learns to walk by falling, getting up, and trying again.  
- A robot learns to walk the same way — by trying in simulation or real life.

Without a body, AI stays "digital only". With a body, it becomes **Physical AI**.

### 2. Sensing the World (Perception)

The robot needs "senses" to understand its environment.

Main sensors in humanoid robots:
| Sensor Type       | What it Does                                      | Example Use                           |
|-------------------|---------------------------------------------------|---------------------------------------|
| Cameras           | See colors, shapes, and people                    | Recognize faces, read signs           |
| LiDAR             | Measure distances accurately                      | Avoid walls, map rooms                |
| IMU (Inertial Measurement Unit) | Detect movement, tilt, acceleration       | Keep balance while walking            |
| Force/Torque Sensors | Feel how hard it’s holding something         | Pick up an egg without breaking it    |

These sensors give the robot "eyes", "ears", and "touch".

### 3. Acting in the World (Actuation)

The robot needs to **move** using motors and parts.

Main actuators:
- **Motors** — move arms, legs, hands  
- **Servos** — small motors for fingers  
- **Pneumatics/Hydraulics** — powerful movements (like in big robots)

The robot’s brain (AI) sends commands to these actuators:  
"Move left leg forward 10 cm" → motor rotates.

### 4. The Brain: AI + Control System

The robot’s brain has two parts:
- **Low-level control** — keeps balance, moves legs smoothly (like reflexes)  
- **High-level AI** — decides what to do (like "go to the kitchen and pick up a glass")

We use:
- ROS 2 (for low-level control)  
- LLMs like GPT (for high-level planning)

### 5. Sim-to-Real Gap

Robots learn best in simulation (digital twin).  
But when we move them to the real world, things change (gravity is slightly different, floor is slippery, etc.).

We call this the **sim-to-real gap**.  
To fix it, we use:
- Realistic physics in simulation  
- Random noise (rain, wind)  
- Transfer learning

### Why These Fundamentals Matter

If we understand these basics, we can build robots that:
- Walk without falling  
- See and avoid obstacles  
- Pick up objects gently  
- Talk and understand humans

### Practice Tasks

1. **Task 1**  
   Watch this short video (5–8 minutes):  
   [Embodied Intelligence Explained](https://www.youtube.com/results?search_query=embodied+intelligence+robotics)  
   Write 3 sentences explaining what "embodied" means in AI.

2. **Task 2**  
   Search online: "humanoid robot sensors"  
   Find a picture of a humanoid robot (like Atlas or Optimus) and list 3 sensors you can see.

3. **Task 3**  
   Think of one everyday task (like opening a door).  
   Write which sensors and actuators a robot would need to do it.

4. **Task 4 (Optional)**  
   Search: "sim-to-real gap robotics"  
   Write one sentence explaining what it is in your own words.

Great job! You’ve completed Chapter 2.  
In the next chapter, we will start exploring ROS 2 — the "nervous system" that connects all these parts.