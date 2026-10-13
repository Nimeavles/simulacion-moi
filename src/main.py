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
"""

def edo_paraboloide(t, y):
    # parametros del sistema
    rho = y[0]
    rho_punto = y[1]

    # evitar división por cero cuando la masa está en el vértice
    if rho < 1e-6:
        rho = 1e-6

    numerador = -2*a*g*rho + (c**2/(m**2*rho**3)) - 4*a**2*rho*rho_punto**2
    denominador = (1 + 4*a**2 * rho ** 2)

    # EDO
    rho_dos_puntos = numerador/denominador

    # necesario para resolver la edo con scipy
    return [rho_punto, rho_dos_puntos]

# Condiciones iniciales
y0 = [1.0, 0.0]         # rho = 1, rho_punto = 0

t_span = (0.0, 10.0)
t_eval = np.linspace(0.0, 10.0, 1000)

sol_edo = solve_ivp(edo_paraboloide, t_span, y0, t_eval=t_eval)

# función posición en función del tiempo
rho_t = sol_edo.y[0]

t = sol_edo.t

plt.figure(figsize=(8, 4))
plt.plot(t, rho_t, label=r'$\rho(t)$')
plt.xlabel('Tiempo (s)')
plt.ylabel(r'Distancia al eje $\rho$ (m)')
plt.title('Simulación del movimiento radial en el paraboloide')
plt.grid(True)
plt.legend()
plt.show()