import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Definir constantes
g = 9.8             # gravedad
a = 2.0             # amplitud paraboloide
c = 4.0             # momento angular
m = 2.0             # masa de la partícula

# Definir la ec. diferencial
"""
d^2p/dt = 1/(1 + 4a^2p^2)*[ -2agp + c^2/(m^2p^3) - 4a^2p*(dp/dt)^2 ]
dphi/dt = c/(m*rho^2)
"""

def edos_paraboloide(t, y):
    # parametros del sistema
    rho = y[0]
    rho_punto = y[1]

    # evitar división por cero cuando la masa está en el vértice
    if rho < 1e-6:
        rho = 1e-6

    numerador = -2*a*g*rho + (c**2/(m**2*rho**3)) - 4*a**2*rho*rho_punto**2
    denominador = (1 + 4*a**2 * rho ** 2)

    phi_punto = c / (m * rho**2)

    # EDO
    rho_dos_puntos = numerador/denominador

    # necesario para resolver las edos con scipy
    return [rho_punto, rho_dos_puntos, phi_punto]

# Condiciones iniciales
y0 = [1.0, 0.0, 0.0]         # rho = 1, rho_punto = 0, phi = 0

t_span = (0.0, 10.0)
t_eval = np.linspace(0.0, 10.0, 1000)

sol_edo = solve_ivp(edos_paraboloide, t_span, y0, t_eval=t_eval)

# funciónes phi y rho en función del tiempo
rho_t = sol_edo.y[0]
phi_t = sol_edo.y[2]

t = sol_edo.t

rho_t = sol_edo.y[0]
phi_t = sol_edo.y[2]

# Conversión de las coordenadas a cartesianas
x_t = rho_t * np.cos(phi_t)
y_t = rho_t * np.sin(phi_t)
z_t = a * rho_t**2

# Representación
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x_t, y_t, z_t, label='Trayectoria de la particula', color='r')

ax.set_xlabel('Eje X (m)')
ax.set_ylabel('Eje Y (m)')
ax.set_zlabel('Eje Z (m)')
ax.set_title('Simulación del movimiento de la partícula en los railes parabólicos giratorios')
ax.legend()

plt.show()