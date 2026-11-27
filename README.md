# Games Ranking

## Motivación

Uno de mis pasatiempos favoritos (por no decir el más) son los videojuegos, y resulta que quería anotar los juegos que terminaba, por ende los anotaba en las notas de mi teléfono, pero luego quise anotar también mi valoración de los mismos juegos, por ende los anotaba en las mismas notas. 

Pasó el tiempo y me di cuenta que era un proceso muy engorroso e incómodo, es por ello que decidí realizar una aplicación web en donde pueda visualizar las valoraciones de cada juego que me terminaba (y también los juegos por sí solos), así surge la idea y motivación de este pequeño proyecto personal.

## Herramientas utilizadas

- Django
- Vue.js

    Utilicé Django porque a la hora de empezar el proyecto tenía manejo básico del mismo, además de querer profundizar mis conocimientos del mismo y aplicarlos de buena forma.

    Y por último utilicé Vue.js porque me sentí motivado para aprender a utilizar un framework de front-end, e indagando me decanté por Vue, ya que se veía sencillo de utilizar y permite tener todos los elementos necesarios para una vista en un solo archivo, como el estilo (CSS), estructura (HTML), y código (Javascript).

## Vistas

- **Home**

    <br>
    <img src="screenshots/home.png">

<br>

- **Game**

    <br>
    <img src="screenshots/game_1.png">
    <br>
    <br>
    <img src="screenshots/game_2.png">

<br>

- **Platforms**

    <br>
    <img src="screenshots/platform_1.png">
    <br>
    <br>
    <img src="screenshots/platform_2.png">

<br>

- **Register**

    <br>
    <img src="screenshots/register_1.png">
    <br>
    <br>
    <img src="screenshots/register_2.png">


<br>

- **Search**

    <br>
    <img src="screenshots/search_1.png">
    <br>
    <br>
    <img src="screenshots/search_2.png">


## Cómo levantar el proyecto localmente

### Backend y Base de Datos (Docker)

1. Copia el archivo de variables de entorno de ejemplo y ajústalo si es necesario:
   ```bash
   cp .env.example .env
   ```
2. Construye y levanta PostgreSQL + Django:
   ```bash
   docker compose up -d --build
   ```
   - API disponible en `http://127.0.0.1:8000/api/`
   - Admin de Django en `http://127.0.0.1:8000/admin/`
   - PostgreSQL expuesto en el puerto definido en `POSTGRES_HOST_PORT` (por defecto `5434`).
3. Para ejecutar comandos de Django dentro del contenedor:
   ```bash
   docker compose exec backend python manage.py createsuperuser
   docker compose exec backend python manage.py makemigrations
   ```

### Frontend (Vue)

```bash
cd ranking/vue-django/vue-ranking
npm install
npm run serve
```

## Disclaimer

Este proyecto es de uso personal, por ende no hay validación en los formularios presentes en la aplicación (en futuro quizás haya).
