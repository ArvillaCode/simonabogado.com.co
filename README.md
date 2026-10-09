# Simón Abogado

Sitio de presentación de Klende Simon Villa. Incluye inicio, seis páginas de servicios, enlaces de WhatsApp por servicio y redes sociales.

## Archivos

- `dist/`: sitio completo listo para cualquier alojamiento estático.
- `dist/assets/`: logo, retrato y portadas optimizadas en WebP.
- `build_content.py`: contenido y plantillas para generar las siete páginas HTML.
- `dist/app.js` y archivos CSS: navegación, WhatsApp flotante, estilos y efectos.
- `vercel.json`: configuración de Vercel para publicar `dist/` como raíz del sitio.

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

## Publicar con Vercel

Conectar este repositorio a Vercel y utilizar la rama `main`. Configurar **Root Directory** como la raíz del repositorio (vacío o `./`) y **Framework Preset** como **Other**. `vercel.json` establece `dist` como **Output Directory** y omite instalación y compilación porque el sitio ya contiene todos sus HTML, CSS, JavaScript e imágenes.

No usar `dist` simultáneamente como Root Directory y Output Directory. Una actualización de `main` dispara un despliegue cuando la integración Git de Vercel está activa. Si no comienza, ejecutar **Redeploy** sobre el último commit.

Documentación: https://vercel.com/docs/project-configuration/vercel-json

Para otro proveedor, subir el contenido de `dist/` a su directorio público. No necesita Node.js, base de datos ni variables secretas.

## Dominio propio

En el proyecto de Vercel, abrir **Settings → Domains**, añadir `simonabogado.com.co` y `www.simonabogado.com.co`, y elegir el primero como dominio principal con redirección desde `www`. Copiar al proveedor DNS los valores A y CNAME exactos que muestra Vercel para este proyecto. Sustituir los registros web anteriores de GitHub Pages si existen, conservando los registros de correo y verificación.

El archivo `CNAME` de la raíz proviene de la configuración anterior de GitHub Pages; Vercel no lo utiliza. Los dominios se gestionan desde Vercel y el proveedor DNS.

## Versiones A y B

Por ahora solo está implementada la versión A. Se propone conservarla en `https://simonabogado.com.co/` y crear la alternativa en `https://simonabogado.com.co/b/`. La ruta `/b/` aún no existe.

Ambas versiones pueden compartir el mismo proyecto de Vercel y el mismo dominio: no requieren DNS separados. Cada versión deberá mantener sus propios enlaces de navegación y páginas de servicio; por ejemplo, `/servicios/deudas-insolvencia/` para A y `/b/servicios/deudas-insolvencia/` para B. Tener dos rutas permite presentar ambas opciones; una prueba A/B con reparto de visitantes y medición de conversiones se configura por separado.

La propuesta conserva `noindex,nofollow` mientras el cliente decide su versión final. Antes del lanzamiento para buscadores, retirar esa etiqueta desde `build_content.py`, regenerar las páginas y publicar.

## Interacciones y accesibilidad

- WhatsApp permanece visible y utiliza un enlace diferente para cada servicio.
- Volver arriba se mantiene en el pie de página.
- Las apariciones se reproducen una sola vez; el parallax funciona solo en escritorio.
- Se respeta `prefers-reduced-motion`; el contenido permanece disponible sin JavaScript.
- Los enlaces externos abren una pestaña nueva; no se envían mensajes automáticamente.

