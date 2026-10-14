import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import solve_ivp

# Definir constantes
g = 9.8             # gravedad
a = 8.0             # amplitud paraboloide
c = 2.0             # momento angular
m = 4.0             # masa de la partícula

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
t_eval = np.linspace(0.0, 10.0, 500)

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

# Configuración inicial de la figura 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Dibujar la superficie del paraboloide (opcional pero recomendado)
rho_max = np.max(sol_edo.y[0])  # Máxima distancia radial alcanzada
rho_grid = np.linspace(0, rho_max * 1.2, 50)
phi_grid = np.linspace(0, 2 * np.pi, 50)
R, P = np.meshgrid(rho_grid, phi_grid)
X_surf = R * np.cos(P)
Y_surf = R * np.sin(P)
Z_surf = a * R**2

# Sombra del paraboloide
ax.plot_surface(X_surf, Y_surf, Z_surf, alpha=0.3, color='cyan', edgecolor='none')

# Inicializar los elementos animados (vacíos al principio)
linea_trayectoria, = ax.plot([], [], [], lw=2, color='r', label='Trayectoria')
punto_particula, = ax.plot([], [], [], 'ko', markersize=6, label='Masa m') # 'ko' = punto negro

# Configurar los límites de los ejes para que la cámara no salte
ax.set_xlim(-rho_max, rho_max)
ax.set_ylim(-rho_max, rho_max)
ax.set_zlim(0, a * rho_max**2 * 1.2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Animación de la partícula en el paraboloide')
ax.legend()

# Función de actualización fotograma a fotograma
def update(num):
    # Dibuja la estela desde el instante 0 hasta el frame actual 'num'
    linea_trayectoria.set_data(x_t[:num], y_t[:num])
    linea_trayectoria.set_3d_properties(z_t[:num])
    
    # El punto de la partícula se mantiene en el instante actual 'num'
    punto_particula.set_data([x_t[num]], [y_t[num]])
    punto_particula.set_3d_properties([z_t[num]])
    
    return linea_trayectoria, punto_particula

# Crear la animación
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, len(t), 5), interval=60, blit=False)

plt.show()