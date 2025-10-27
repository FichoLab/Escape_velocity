## Velocity calculator ##
This project calculates does your rocket has enough velocity to escape Earth. And it shows you how much Escape velocities is needed to escape potential human habitat worlds

## How this works? ##
At the start user has two options:
a) Type data and see if your rocket can escape Earth
b) See Escape Velocities of planets and moons

User types a or b and presses Enter, than if "a" is selected user types:
m0 = initial mass (kg),
mf = final mass (kg),
ve = exhaust velocity(m/s)
tb = burn time (s)

The program then calculates:
- Whether the rocket can reach **Low Earth Orbit**, **the Moon**, or **escape Earth entirely**
- Estimated **travel time** to the Moon  
- **Thrust**, **acceleration**, and **maximum altitude**

Program uses The Tsiolkovsky Rocket Equation, also known as the ideal rocket equation:
***Δv = ve × ln(m0 / mf)***

Thrust formula:
***F = m * ve***

Acceleration formula:
***a = (F - m * g) / m***

Vis-Viva Equation:
***v^2 = GM (2/r - 1/a)***

## Constants
G = 6.67430e-11  # gravitational constant, m³/kg/s²
g0 = 9.81        # standard gravity, m/s²

## Planets considered for habitation and Earth
planets:

    "Earth": {"mass": 5.972e24, "radius": 6371e3},
    
    "Mars": {"mass": 6.417e23, "radius": 3389e3},
    
    "Venus (upper atmosphere)": {"mass": 4.867e24, "radius": 6052e3}

## Moons considered for habitation
moons:

    "Moon (Earth)": {"mass": 7.35e22, "radius": 1737e3},
    
    "Europa (Jupiter)": {"mass": 4.8e22, "radius": 1561e3},
    
    "Callisto (Jupiter)": {"mass": 1.08e23, "radius": 2410e3},
    
    "Ganymede (Jupiter)": {"mass": 1.48e23, "radius": 2634e3},
    
    "Titan (Saturn)": {"mass": 1.35e23, "radius": 2575e3},
    
    "Enceladus (Saturn)": {"mass": 1.08e20, "radius": 252e3}

***In Python (and most programming languages), the e notation is just a shorthand for scientific notation.***

## Results
Run program.
Results saved to result/Escape_velocity.txt

## How to run
Install Python and pandas 'pip install pandas'
You can install IDE of your choice, in my case, I used PyCharm


*Created by Filip, a high school mechatronics student passionate about space industry*




