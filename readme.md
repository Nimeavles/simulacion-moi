# Simulación `Masa en railes parabólicos giratorios`

Realizado por Juan María Tejero y Pablo Rodríguez Laguna

## Requisitos

- Python 3 instalado.
- Git, si se quiere clonar el repositorio.

## Instalación

Clona el repositorio y entra en su carpeta:

```bash
git clone <URL_DEL_REPOSITORIO>
cd simulacion-moi
```

Crea un entorno virtual en la raíz del proyecto:

```bash
python -m venv venv
```

Activa el entorno virtual:

**Linux/macOS**

```bash
source venv/bin/activate
```

**Windows (PowerShell)**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (símbolo del sistema)**

```bat
venv\Scripts\activate.bat
```

Instala las dependencias:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Ejecución del programa

Desde la raíz del proyecto, con el entorno virtual activado, ejecuta:

```bash
python src/main.py
```

Para salir del entorno virtual cuando termines:

```bash
deactivate
```
