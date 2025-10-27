import math
import os

# Constants
G = 6.67430e-11  # gravitational constant, m³/kg/s²
g0 = 9.81        # standard gravity, m/s²

# Planets considered for habitation and Earth
planets = {
    "Earth": {"mass": 5.972e24, "radius": 6371e3},
    "Mars": {"mass": 6.417e23, "radius": 3389e3},
    "Venus (upper atmosphere)": {"mass": 4.867e24, "radius": 6052e3}
}

# Moons considered for habitation
moons = {
    "Moon (Earth)": {"mass": 7.35e22, "radius": 1737e3},
    "Europa (Jupiter)": {"mass": 4.8e22, "radius": 1561e3},
    "Callisto (Jupiter)": {"mass": 1.08e23, "radius": 2410e3},
    "Ganymede (Jupiter)": {"mass": 1.48e23, "radius": 2634e3},
    "Titan (Saturn)": {"mass": 1.35e23, "radius": 2575e3},
    "Enceladus (Saturn)": {"mass": 1.08e20, "radius": 252e3}
}

# Ensure result folder exists
os.makedirs("result", exist_ok=True)

print("Hello, choose an option:")
print("a) Type data and see if your rocket can escape Earth")
print("b) See Escape Velocities of planets and moons")

choice = input("Type a or b and press enter: ")

if choice == "a":
    def delta_v_from_masses(m0: float, mf: float, ve: float) -> float:
        """Δv = ve * ln(m0 / mf)"""
        if m0 <= 0 or mf <= 0:
            raise ValueError("Masses must be positive")
        if m0 <= mf:
            raise ValueError("Initial mass must be greater than final mass")
        if ve <= 0:
            raise ValueError("ve must be positive")
        return ve * math.log(m0 / mf)


    m0 = float(input("Enter initial mass (kg): "))         # m0 is the initial mass of the rocket (including propellant)
    mf = float(input("Enter final mass (kg): "))           # mf is the final mass of the rocket (after propellant is burned).
    ve = float(input("Enter exhaust velocity (m/s): "))    # ve is the effective exhaust velocity
    delta_v = delta_v_from_masses(m0, mf, ve)              # Δv is the change in velocity

    # Escape velocity for Earth
    v_escape_velocity = math.sqrt(2 * G * planets["Earth"]["mass"] / planets["Earth"]["radius"])

    print(f"Delta_v = {delta_v:.2f} m/s")
    print(f"v_escape_velocity = {v_escape_velocity:.2f} m/s")

    # Save results to file
    with open("result/Delta_v.txt", "w") as f:
        f.write(f"Initial mass: {m0} kg")
        f.write(f"Final mass: {mf} kg")
        f.write(f"Exhaust velocity: {ve} m/s")
        f.write(f"Delta-v = {delta_v:.2f} m/s")

    # Calculating thrust
    tb = float(input("Enter burn time (sec):"))            # tb is burn time
    m = (m0 - mf) / tb                                     # m is the mass flow rate of propellant
    F = m * ve                                             # F is thrust

    # Calculating acceleration
    m_dot = F / ve
    t = tb / 2
    current_mass = m0 - m_dot * t
    a = (F - current_mass * g0) / current_mass
    # a = (F - m * g) / m
    with open("result/rocket_output.txt", "w") as f:
        f.write(f"Acceleration at t={t:.2f} s: {a:.2f} m/s^2")
    print(f"Acceleration at t={t:.2f} s: {a:.2f} m/s^2")

    # Calculating maximum altitude
    vb = delta_v - (g0 * tb) - 200     # Approximate drag loss
    h = (vb ** 2) / (2 * g0) / 1000    # Converts to km

    # Translunar Injection Calculation (vis-viva Equation)
    mu_earth = G * planets["Earth"]["mass"]
    r_earth = planets["Earth"]["radius"]
    r_moon = 384400e3 # distance from Earth to Moon center (m)

    # Semi-major axis of transfer orbit
    a_transfer = (r_earth + r_moon) / 2

    # Velocity in circular orbit near Earth (LEO)
    v_leo = math.sqrt(mu_earth / r_earth)

    v_to = math.sqrt(mu_earth * (2 / r_earth - 1 / a_transfer))

    delta_v_transfer_orbit = v_to - v_leo
    print(f"Delta-v needed for translunar injection: {delta_v_transfer_orbit:.2f} m/s")

    # Time to reach Moon (half on orbit)
    t_transfer = math.pi * math.sqrt(a_transfer**3 / mu_earth)
    print(f"Estimated travel time to Moon: {t_transfer / 3600 / 24:.2f} days")

    if delta_v >= 11200:
        print("===Rocket can escape Earth's gravity completely.===")
    elif delta_v >= 10800:
        print("===Rocket can perform translunar injection and reach the Moon.===")
    elif delta_v >= 9400:
        print("===Rocket can reach low Earth orbit (LEO), but not the Moon.===")
    else:
        print("===Suborbital flight only.===")

    with open("result/rocket_output.txt", "a") as f:
        f.write(f"Thrust: {F:.2f} N")
        f.write(f"Maximum Altitude: {h:.2f} km")
        f.write(f"Delta-v needed for translunar injection: {delta_v_transfer_orbit:.2f} m/s")
        f.write(f"Rocket delta_v: {delta_v:.2f} m/s")
        f.write(f"Estimated travel time to Moon: {t_transfer / 3600 / 24:.2f} days")
    print(f"Thrust: {F:.2f} N")
    print(f"Maximum Altitude: {h:.2f} km")

elif choice == "b":
    def escape_velocity(mass, radius):
        return math.sqrt(2 * G * mass / radius)

    print("Escape velocities of potential human habitat worlds")

    with open("result/Escape_velocity.txt", "w") as f:
        f.write("Escape velocities of potential human habitat worlds")

        print("Planets:")
        f.write("Planets:")
        for planet, values in planets.items():
            v = escape_velocity(values["mass"], values["radius"])
            print(f"{planet:30}: {v / 1000:.2f} km/s")
            f.write(f"{planet:30}: {v / 1000:.2f} km/s")

        print("Moons:")
        f.write("Moons:")
        for moon, values in moons.items():
            v = escape_velocity(values["mass"], values["radius"])
            print(f"{moon:30}: {v / 1000:.2f} km/s")
            f.write(f"{moon:30}: {v / 1000:.2f} km/s")

        print("Results saved to result/Escape_velocity.txt")
