# Proyecto Flask - D´CARPI (Salsas y Condimentos)

## 1) Crear entorno virtual
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
```

## 2) Instalar dependencias
```bash
pip install -r requirements.txt
```

## 3) Ejecutar en local
```bash
python app.py
```
Abrir: http://127.0.0.1:5000/

## 4) Rutas
- `/` → Página principal con el nombre del sistema/negocio.
- `/producto/<nombre>` → Ruta dinámica (ej: `/producto/aji`)

## 5) GitHub (resumen)
```bash
git init
git add .
git commit -m "Primer avance D´CARPI Flask"
git branch -M main
# luego conectar con el repo y subir
git push -u origin main
```

## 6) Render (recomendado)
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- (Opcional) también existe un `Procfile` por si lo necesitas.
