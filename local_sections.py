"""SEO local y secciones reutilizables de la propuesta B."""
from pathlib import Path
from html import escape
import json

PROFILE = json.loads((Path(__file__).parent / 'business_profile.json').read_text(encoding='utf-8'))
ORIGIN = PROFILE['canonical_origin']
GENERAL = 'https://wa.link/2dj89b'

def seo_head(title, description, path, service=None):
    url = ORIGIN + path
    business = {
        '@type': 'LegalService', '@id': ORIGIN + '/b/#despacho',
        'name': PROFILE['name'], 'url': ORIGIN + '/b/',
        'image': ORIGIN + '/b/assets/simon-900.webp',
        'address': {'@type': 'PostalAddress', 'streetAddress': PROFILE['street_address'],
                    'addressLocality': PROFILE['city'], 'addressRegion': PROFILE['region'], 'addressCountry': 'CO'},
        'areaServed': {'@type': 'City', 'name': 'Medellín'},
        'hasMap': PROFILE['maps_url'],
        'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification',
            'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
            'opens': PROFILE['opens'], 'closes': PROFILE['closes']}],
        'founder': {'@type': 'Person', 'name': PROFILE['lawyer'], 'jobTitle': 'Abogado'},
        'sameAs': ['https://www.facebook.com/profile.php?id=61595132795227', 'https://www.tiktok.com/@garantiacol_abogados']
    }
    page = {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': title,
            'description': description, 'inLanguage': 'es-CO', 'about': {'@id': business['@id']}}
    graph = [business, page]
    if service:
        graph.append({'@type': 'Service', '@id': url + '#servicio', 'name': service['name'],
            'serviceType': service['name'], 'provider': {'@id': business['@id']},
            'areaServed': {'@type': 'City', 'name': 'Medellín'}, 'url': url})
        graph.append({'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Inicio', 'item': ORIGIN + '/b/'},
            {'@type': 'ListItem', 'position': 2, 'name': service['name'], 'item': url}]})
    return f'''<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:locale" content="es_CO">
<meta property="og:title" content="{escape(title, quote=True)}"><meta property="og:description" content="{escape(description, quote=True)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{ORIGIN}/b/assets/simon-900.webp">
<meta property="og:image:alt" content="Klende Simón Villa, abogado en Medellín">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('<', chr(92)+'u003c')}</script>'''

def location(contact_url=GENERAL):
    return f'''<section class="section location" id="ubicacion" aria-labelledby="location-title">
<div><p class="eyebrow">ATENCIÓN JURÍDICA EN MEDELLÍN</p><h2 id="location-title">Hablemos de tu caso.<br>Estoy en Medellín.</h2><p class="location-intro">Escríbeme para explicar qué necesitas resolver y coordinar la asesoría. Te indico los documentos iniciales y las condiciones de la atención.</p></div>
<div class="location-card"><p class="location-city">Medellín · Antioquia · Colombia</p><h3>Simón Abogado</h3><address>{escape(PROFILE['street_address'])}<br>Medellín, Colombia</address><p class="location-hours"><strong>Horario de atención</strong><br>{escape(PROFILE['hours_label'])}<br><small>Hora de Colombia</small></p><div class="location-actions"><a class="button navy" href="{contact_url}" target="_blank" rel="noopener noreferrer">Coordinar mi asesoría</a><a class="text-link" href="{PROFILE['maps_url']}" target="_blank" rel="noopener noreferrer">Cómo llegar · Google Maps ↗</a></div></div></section>'''

def legal_context(service, content):
    cards = ''.join(f'<article><span class="step-label">0{i}</span><h3>{escape(title)}</h3><p>{escape(text)}</p></article>' for i,(title,text) in enumerate(content['options'],1))
    sources = ''.join(f'<li><a href="{escape(url,quote=True)}" target="_blank" rel="noopener noreferrer">{escape(title)} ↗</a></li>' for title,url in content['sources'])
    return f'''<section class="section legal-context"><div class="section-heading"><div><p class="eyebrow">{escape(content['heading'].upper())}</p><h2>Actuar con estrategia<br>empieza por tu caso.</h2></div><p>Defino la intervención a partir de los hechos, los documentos y lo que necesitas resolver.</p></div><aside class="risk-note"><h3>{escape(content['risk'][0])}</h3><p>{escape(content['risk'][1])}</p></aside><div class="legal-options">{cards}</div><div class="section-action"><a class="button navy" href="https://wa.link/{service['wa']}" target="_blank" rel="noopener noreferrer">{escape(service['cta'])}</a><p>Cuéntame qué ocurre. Te indico cómo organizar la revisión de tu caso.</p></div><details class="legal-sources"><summary>Fuentes jurídicas y alcance de esta información</summary><p>Información general sobre Colombia. La actuación concreta se define al estudiar los documentos y las circunstancias de tu caso.</p><ul>{sources}</ul><p>Contenido actualizado el <time datetime="2026-10-09">9 de octubre de 2026</time>.</p></details></section>'''

def related_services(content, services):
    selected = [s for slug in content['related'] for s in services if s['slug'] == slug]
    links = ''.join(f'<a href="/b/servicios/{s["slug"]}/"><span>{escape(s["name"])}</span><span aria-hidden="true">↗</span></a>' for s in selected)
    return f'<nav class="related-services section" aria-label="Servicios relacionados"><p class="eyebrow">OTROS ASUNTOS QUE PUEDEN ESTAR RELACIONADOS</p><div>{links}</div></nav>'

def credentials():
    items = [('Formación jurídica', 'Abogado de la Universidad Libre.'), ('Experiencia', 'Más de cinco años de experiencia, con atención directa en cada etapa del servicio.'), ('Áreas de enfoque', 'Experiencia especializada en asuntos de familia y finanzas.'), ('Estrategia y comunicación', 'Análisis, negociación y representación con información clara sobre tu caso.')]
    if PROFILE['professional_card']:
        items.append(('Tarjeta profesional', str(PROFILE['professional_card'])))
    items.extend((x['title'], x['description']) for x in PROFILE['documented_experience'])
    cards = ''.join(f'<div><strong>{escape(title)}</strong><p>{escape(text)}</p></div>' for title,text in items)
    verify = ''
    if PROFILE['professional_card'] and PROFILE['professional_verification_url']:
        verify = f'<a class="text-link" target="_blank" rel="noopener noreferrer" href="{escape(PROFILE["professional_verification_url"],quote=True)}">Consultar registro profesional ↗</a>'
    cases = ''.join(f'<article><h3>{escape(case["title"])}</h3><p>{escape(case["description"])}</p></article>' for case in PROFILE['authorized_case_studies'])
    return f'<div class="credentials" aria-label="Formación y experiencia de Klende Simón Villa">{cards}{verify}{cases}</div>'
