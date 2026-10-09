# Simón Abogado

Sitio de presentación de Klende Simon Villa. Incluye inicio, seis páginas de servicios, enlaces de WhatsApp por servicio y redes sociales.

## Archivos

- `dist/`: sitio completo listo para cualquier alojamiento estático.
- `dist/assets/`: logo, retrato y portadas optimizadas en WebP.
- `build_content.py`: contenido y plantillas para generar las siete páginas HTML.
- `dist/app.js` y archivos CSS: navegación, WhatsApp flotante, estilos y efectos.
- `.github/workflows/pages.yml`: publicación automática con GitHub Pages al actualizar `main`.

## Editar

Se requiere Python 3 únicamente para regenerar el contenido:

```sh
python build_content.py
```

Los estilos y el JavaScript se editan directamente dentro de `dist/`. Las imágenes ya están preparadas: no se requieren paquetes ni herramientas de compilación.

Para una vista local:

```sh
python -m http.server 8765 --directory dist
```

Abrir `http://localhost:8765/`. Las rutas relativas permiten servir el sitio desde un dominio propio o desde una ruta de GitHub Pages.

## Publicar con GitHub Pages

En el repositorio, abrir **Settings → Pages → Build and deployment → Source → GitHub Actions**. El flujo **Publicar sitio web** despliega exclusivamente `dist/`; también puede ejecutarse desde **Actions → Run workflow**.

Documentación: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

Para otro proveedor, subir el contenido de `dist/` a su directorio público. No necesita Node.js, base de datos ni variables secretas.

## Dominio propio

El nombre del repositorio no conecta automáticamente `simonabogado.com.co`. Primero se debe confirmar el control del dominio y configurar sus registros DNS y el dominio personalizado en el alojamiento. No se incluye un CNAME que cambie el destino sin esa configuración.

La propuesta conserva `noindex,nofollow` mientras el cliente decide su versión final. Antes del lanzamiento para buscadores, retirar esa etiqueta desde `build_content.py`, regenerar las páginas y publicar.

## Interacciones y accesibilidad

- WhatsApp permanece visible y utiliza un enlace diferente para cada servicio.
- Volver arriba se mantiene en el pie de página.
- Las apariciones se reproducen una sola vez; el parallax funciona solo en escritorio.
- Se respeta `prefers-reduced-motion`; el contenido permanece disponible sin JavaScript.
- Los enlaces externos abren una pestaña nueva; no se envían mensajes automáticamente.
