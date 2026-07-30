# Flask Docker CI/CD Integration

![CI/CD Pipeline](https://github.com/jrcordovag/flask-docker-cicd/actions/workflows/ci.yml/badge.svg)

Pipeline completo de Integración y Despliegue Continuo (CI/CD) para una API en Flask usando Docker, PostgreSQL, Pytest y GitHub Actions.

## 🚀 Características del Pipeline
- **Linting:** Análisis de buenas prácticas en `Dockerfile` con Hadolint.
- **Seguridad:** Análisis de vulnerabilidades CVE en la imagen con Trivy.
- **Pruebas de Integración:** Entorno multi-contenedor con Docker Compose y PostgreSQL probado con `pytest`.
- **Registry:** Publicación de imágenes inmutables etiquetadas por Git SHA en GitHub Container Registry (GHCR).
- **Despliegue Continuo (CD):** Despliegue automatizado con verificación de salud (Health Check HTTP 200).
