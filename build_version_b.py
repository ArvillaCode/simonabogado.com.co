"""Genera exclusivamente dist/b/. Conserva intacta la versión A y sus recursos."""
from pathlib import Path
from html import escape
import re
from local_content import LOCAL_CONTENT
from local_sections import PROFILE, seo_head, location, legal_context, related_services, credentials

DIST = Path(__file__).parent / 'dist'
OUT = DIST / 'b'
GENERAL = 'https://wa.link/2dj89b'
SOURCE = (DIST / 'index.html').read_text(encoding='utf-8')

SERVICES = [
 dict(slug='deudas-insolvencia',name='Deudas e insolvencia',image='01-deudas-insolvencia',wa='fyr063',
 title='Las deudas pesan. Enfréntalas con una estrategia.',
 brief='Estudio tus obligaciones y tu capacidad de pago para definir contigo cómo abordar tu situación.',
 intro='Trabajas, pagas y aun así las cuentas siguen acumulándose. Las llamadas de cobro ocupan tu día y las preocupaciones llegan contigo a casa. Pongo tu situación sobre la mesa, reviso tus obligaciones y defino una estrategia para actuar.',
 situations=['Tus pagos mensuales están superando lo que puedes asumir.', 'Debes a varios acreedores y necesitas organizar tus obligaciones.', 'Quieres estudiar una negociación o un proceso de insolvencia con acompañamiento jurídico.'],
 steps=[('Estudio tu situación','Reviso tus deudas, ingresos, pagos y documentos para identificar el punto de partida.'),('Defino la estrategia','Analizo las vías de negociación y los requisitos de una posible insolvencia. Te explico el camino propuesto y lo que implica.'),('Te acompaño al actuar','Adelanto las gestiones acordadas, atiendo tus preguntas y te mantengo informado durante el servicio.')],
 prepare='Cuéntame cuánto debes, a quiénes y qué pagos estás realizando. Reúne los estados de cuenta, las comunicaciones de cobro y la información sobre tus ingresos. Te indicaré qué documentos adicionales necesito.',
 faq=[('¿Puedo consultar antes de dejar de pagar?','Sí. Estudio tu situación actual y tus compromisos para definir cómo abordar las dificultades que estás enfrentando.'),('¿Cómo sé si la insolvencia corresponde a mi caso?','Reviso tus obligaciones y las condiciones de tu situación. Con ese análisis te explico si cumples los requisitos y qué implicaría avanzar por esa vía.'),('¿Qué pasa si me faltan documentos?','Empieza por contarme lo que ocurre. Organizo contigo la información y te indico qué soportes hacen falta.')],
 cta='Necesito ayuda con mis deudas',close='Da el primer paso para enfrentar tus deudas.'),
 dict(slug='reportes-crediticios',name='Reportes crediticios',image='02-reportes-crediticios',wa='ss6ua4',
 title='Tu reporte crediticio merece una revisión a fondo.',
 brief='Reviso la información reportada, identifico inconsistencias y fundamento las reclamaciones que correspondan.',
 intro='Necesitas avanzar, pero aparece una obligación que no reconoces o un dato que no refleja lo ocurrido. Las respuestas de la entidad no resuelven tus dudas. Reviso los antecedentes y sustento las solicitudes que correspondan con documentos y argumentos.',
 situations=['Aparece una obligación que no reconoces en tu historial.', 'Realizaste un pago y necesitas aclarar la información que sigue reportada.', 'Has solicitado explicaciones y necesitas respaldo jurídico para continuar la reclamación.'],
 steps=[('Reviso el reporte','Estudio la información de la obligación, sus antecedentes y las comunicaciones de la entidad.'),('Fundamento la reclamación','Identifico las inconsistencias y organizo los soportes para las solicitudes que correspondan.'),('Doy seguimiento','Adelanto la gestión acordada, reviso las respuestas y te explico el siguiente paso.')],
 prepare='Reúne el reporte, los comprobantes de pago y las respuestas que hayas recibido. Cuéntame qué dato cuestionas. Para revisar tu caso no necesito tus contraseñas ni códigos de acceso.',
 faq=[('¿Puedo consultar si no reconozco la deuda?','Sí. Reviso el reporte y las comunicaciones para identificar qué antecedentes deben solicitarse y qué actuación corresponde.'),('¿También revisas reportes después de un pago?','Sí. Estudio el comprobante, la información reportada y la respuesta de la entidad para definir la gestión.'),('¿La gestión incluye solicitar un crédito?','Mi servicio se centra en revisar la información y tramitar las reclamaciones acordadas. La evaluación de una solicitud de crédito corresponde a la entidad financiera.')],
 cta='Quiero revisar mi reporte',close='Actúa sobre la información que te está afectando.'),
 dict(slug='embargos-cobros',name='Embargos y cobros',image='03-embargos-cobros',wa='0nro66',
 title='Recibiste una notificación. Responde con respaldo jurídico.',
 brief='Reviso el proceso, defino las actuaciones y asumo la representación acordada para defender tus intereses.',
 intro='Piensas en tu sueldo, tu cuenta o los bienes que has construido con esfuerzo. Leer una notificación sin entender qué sigue aumenta la preocupación. Estudio el documento y el expediente, identifico lo que requiere atención y defino la estrategia de defensa.',
 situations=['Recibiste una notificación de cobro o de un proceso judicial.', 'Existe una medida sobre tus ingresos o tus bienes que necesitas revisar.', 'Necesitas un abogado que estudie el expediente y asuma tu representación.'],
 steps=[('Estudio el expediente','Reviso los documentos, los antecedentes de la obligación y el estado del proceso.'),('Defino la respuesta','Identifico las actuaciones que corresponden, sus requisitos y los puntos que requieren atención.'),('Asumo la gestión','Adelanto las actuaciones contratadas y te mantengo informado sobre los avances del caso.')],
 prepare='Envíame una explicación de lo ocurrido y ten a mano la notificación completa, la fecha en que la recibiste y el número del proceso si lo conoces. Te indicaré cómo compartir los documentos necesarios.',
 faq=[('¿Qué hago si no entiendo la notificación?','Cuéntame cuándo la recibiste y comparte el documento completo por el medio que acordemos. Lo reviso y te explico su alcance.'),('¿Puedes revisar un proceso que ya está en curso?','Sí. Estudio el expediente y las actuaciones realizadas para definir el alcance de mi intervención.'),('¿Cómo me informarás sobre el caso?','Te explico las actuaciones, los avances y la información que necesito de ti durante la representación acordada.')],
 cta='Quiero revisar esta notificación',close='Enfrenta el proceso con una defensa organizada.'),
 dict(slug='recuperacion-cartera',name='Recuperación de cartera',image='04-recuperacion-cartera',wa='l2mzg4',
 title='Te deben dinero. Es momento de exigir el pago.',
 brief='Reviso las pruebas, estructuro la reclamación y dirijo la gestión de cobro para defender tu derecho al pago.',
 intro='Has insistido, has esperado y sigues recibiendo excusas. Mientras tanto, tus obligaciones continúan. Las promesas de pago no cubren tus gastos ni sostienen tu negocio. Reviso las pruebas que respaldan la deuda y estructuro una reclamación para defender tu derecho al pago.',
 situations=['Entregaste un producto o prestaste un servicio y aún no te pagan.', 'Prestaste dinero y los compromisos de pago siguen sin cumplirse.', 'Has intentado cobrar y necesitas darle respaldo jurídico a tu reclamación.'],
 steps=[('Estudio las pruebas','Reviso contratos, facturas, comprobantes y conversaciones relacionados con la deuda.'),('Defino la estrategia de cobro','Te explico las actuaciones que propongo, el alcance de la gestión y los costos del acompañamiento.'),('Dirijo la reclamación','Adelanto las actuaciones acordadas y te mantengo informado sobre los avances y las decisiones del caso.')],
 prepare='Reúne los soportes de la deuda, el monto pendiente, las fechas acordadas y las comunicaciones con quien te debe. Indícame si hubo abonos o acuerdos posteriores para organizar la reclamación.',
 faq=[('¿Puedo consultar sin un contrato firmado?','Sí. Reviso los documentos, comprobantes y comunicaciones que tengas para determinar qué respaldan y cómo estructurar la gestión.'),('¿La gestión siempre empieza con una demanda?','Primero estudio la obligación y sus soportes. Defino la estrategia de cobro y te explico las vías de acuerdo o reclamación que corresponden.'),('¿Cómo conoceré el avance del cobro?','Te mantengo informado sobre las actuaciones realizadas, las respuestas recibidas y los pasos que siguen dentro del servicio contratado.')],
 cta='Quiero reclamar mi dinero',close='Dale respaldo jurídico a tu reclamación.'),
 dict(slug='contratos-patrimonio',name='Contratos y patrimonio',image='05-contratos-patrimonio',wa='j3wo34',
 title='Lo que has construido merece una firma bien respaldada.',
 brief='Reviso las condiciones, detecto riesgos y estructuro acuerdos que defiendan tus intereses.',
 intro='Una cláusula que pasaste por alto puede comprometer más de lo que imaginabas. Tu dinero, tus bienes y tus compromisos merecen una revisión cuidadosa. Estudio el documento, te explico las obligaciones y planteo los ajustes necesarios antes de que decidas.',
 situations=['Vas a firmar un contrato que compromete tu dinero o tus bienes.', 'Necesitas dejar por escrito las condiciones de un acuerdo.', 'Ya firmaste y tienes una dificultad con los compromisos asumidos.'],
 steps=[('Reviso las condiciones','Estudio el contrato, los anexos y el propósito de la operación.'),('Identifico los puntos decisivos','Te explico las obligaciones, los riesgos y las condiciones que deben aclararse.'),('Estructuro el acuerdo','Redacto o propongo los ajustes contratados y te acompaño en la revisión de los compromisos.')],
 prepare='Ten a mano el contrato completo y sus anexos. Cuéntame qué quieres lograr, qué te preocupa y en qué momento se encuentra la negociación o la operación.',
 faq=[('¿Puedes elaborar un contrato desde cero?','Sí. Estudio el acuerdo que necesitas, reúno la información y defino contigo el alcance de su elaboración.'),('¿Puedo consultar si ya firmé?','Sí. Reviso lo que acordaste y la dificultad concreta para explicarte las actuaciones que corresponden.'),('¿También revisas cambios que propone la otra parte?','Sí. Dentro del alcance acordado, estudio las modificaciones y te explico cómo afectan tus compromisos e intereses.')],
 cta='Quiero revisar mi contrato',close='Firma con conocimiento de lo que estás acordando.'),
 dict(slug='familia-sucesiones',name='Familia y sucesiones',image='06-familia-sucesiones',wa='ikk5zu',
 title='En los momentos difíciles, defiendo lo que importa para ti.',
 brief='Te escucho, organizo los asuntos jurídicos y te represento con firmeza, sensibilidad y discreción.',
 intro='Un conflicto familiar ocupa tu cabeza incluso cuando intentas concentrarte en otra cosa. Se mezclan las emociones, las decisiones sobre tus hijos y las preocupaciones por los bienes. Escucho tus prioridades, estudio la situación y te acompaño para actuar con una dirección clara.',
 situations=['Necesitas acompañamiento para una separación o un divorcio.', 'Debes resolver asuntos de alimentos, custodia o acuerdos sobre tus hijos.', 'Tras el fallecimiento de un familiar, necesitas avanzar con una sucesión.'],
 steps=[('Escucho tus prioridades','Entiendo qué ocurre, qué necesitas resolver y qué asuntos requieren atención.'),('Organizo la estrategia','Reviso documentos, acuerdos y diferencias para definir las actuaciones.'),('Te represento y acompaño','Adelanto la gestión contratada, manejo el asunto con discreción y te mantengo informado.')],
 prepare='Cuéntame qué está ocurriendo y qué necesitas resolver. Reúne los acuerdos anteriores y los documentos que tengas. Yo te indico qué información es relevante para estudiar tu situación.',
 faq=[('¿Puedo consultar si todavía no hay un acuerdo?','Sí. Estudio tu situación y las diferencias existentes para definir las vías de actuación y los puntos que requieren atención.'),('¿Puedes abordar asuntos de hijos y bienes en una misma consulta?','Sí. Identifico los temas relacionados y organizo la revisión para definir el alcance del acompañamiento.'),('¿Cómo empezamos una consulta sobre sucesión?','Cuéntame quién falleció, qué familiares están involucrados y qué bienes conocen. Te explico qué documentos necesito y cómo organizar la revisión.')],
 cta='Quiero hablar de mi situación familiar',close='Cuenta conmigo para afrontar este momento.')
]

# Tres asuntos del lado de quien enfrenta deudas se presentan como un solo servicio.
_by_slug = {service['slug']: service for service in SERVICES}
_debt_service = dict(_by_slug['deudas-insolvencia'])
_debt_service.update(
    name='Deudas, reportes y embargos',
    title='¿Una deuda, un reporte o un embargo te preocupa?',
    brief='Revisa tus deudas, tu historial crediticio o una notificación y conoce el siguiente paso.',
    intro='Si las deudas se acumulan, aparece un dato que no reconoces o recibiste una notificación, revisamos tu situación y te explico cómo actuar.',
    situations=['Necesitas ordenar deudas o evaluar una negociación o insolvencia.', 'Hay un dato incorrecto o una obligación que no reconoces en tu historial.', 'Recibiste un cobro, una demanda o una medida sobre tus bienes.'],
    steps=[('Reviso tu caso','Estudio tus documentos, pagos, reporte o notificación.'),('Aclaro tus opciones','Te explico qué vías pueden aplicar y qué documentos hacen falta.'),('Definimos el siguiente paso','Conoces el alcance, los honorarios y la gestión que acordemos.')],
    prepare='Cuéntame qué ocurrió y comparte los documentos que tengas: reporte, comprobantes o notificación. No necesitas tener todo para empezar.',
    cta='Revisar mi caso', close='Aclaremos qué está pasando y cómo puedes actuar.',
)
_collection_service = dict(_by_slug['recuperacion-cartera'])
_collection_service.update(
    name='Cobro de deudas pendientes',
    title='¿Te deben dinero y no te pagan?',
    brief='Revisa las pruebas y define cómo reclamar el pago pendiente.',
    intro='Si ya cumpliste y el pago no llega, reviso qué respalda la deuda y te explico las vías para reclamarla.',
    situations=['Te deben por un producto, servicio o préstamo.', 'Has cobrado varias veces y no cumplen el acuerdo.', 'Necesitas valorar una negociación o reclamación formal.'],
    steps=[('Reviso los soportes','Estudio contratos, facturas, comprobantes y conversaciones.'),('Defino la vía','Te explico las opciones de acuerdo o reclamación.'),('Acordamos el alcance','Conoces los pasos, costos y condiciones antes de avanzar.')],
    prepare='Ten a mano el monto pendiente, las fechas y los soportes que tengas. Si hubo abonos o acuerdos, cuéntamelo.',
    cta='Reclamar un pago pendiente', close='Dale rumbo a tu reclamación.',
)
_contract_service = dict(_by_slug['contratos-patrimonio'])
_contract_service.update(
    title='¿Vas a firmar o proteger un bien?',
    brief='Revisa contratos y acuerdos antes de asumir compromisos.',
    intro='Antes de firmar, entiende tus obligaciones, los riesgos y las condiciones del acuerdo.',
    situations=['Vas a firmar y algo no te queda claro.', 'Necesitas redactar o negociar un acuerdo.', 'Ya firmaste y surgió un incumplimiento.'],
    steps=[('Reviso el documento','Identifico obligaciones, pagos, plazos y condiciones.'),('Te explico los riesgos','Señalo qué conviene aclarar o negociar.'),('Acordamos los ajustes','Definimos la revisión, redacción o gestión que necesitas.')],
    prepare='Comparte el contrato completo y cuéntame qué quieres lograr o qué te preocupa.',
    cta='Revisar mi contrato', close='Firma con claridad sobre lo que acuerdas.',
)
_family_service = dict(_by_slug['familia-sucesiones'])
_family_service.update(
    title='¿Un asunto familiar necesita una solución?',
    brief='Orientación y representación para asuntos de familia y sucesiones.',
    intro='Te escucho, ordeno lo que necesitas resolver y te explico cómo avanzar con sensibilidad y discreción.',
    situations=['Estás considerando una separación o un divorcio.', 'Necesitas resolver alimentos, custodia o acuerdos sobre tus hijos.', 'Debes iniciar una sucesión.'],
    steps=[('Te escucho','Aclaro tus prioridades y los temas que requieren atención.'),('Reviso las opciones','Estudio documentos, acuerdos y diferencias.'),('Te acompaño','Definimos las actuaciones y el alcance del servicio.')],
    prepare='Cuéntame qué ocurre y comparte los acuerdos o documentos que ya tienes.',
    cta='Hablar de mi situación familiar', close='Hablemos con claridad y discreción.',
)
SERVICES = [_debt_service, _collection_service, _contract_service, _family_service]

TESTIMONIAL_NAMES = ['Andres Rodrigez', 'Gabriel Aristizabal', 'Milena Diaz', 'Robert Ruiz', 'Josefa Dominguez']

TESTIMONIALS = [
 ('Recuperación de cartera','Cada vez que cobraba me daban una excusa distinta. Klende revisó los soportes y se hizo cargo del cobro. Fue directo desde el principio: me explicó qué se podía hacer y me mantuvo informado mientras avanzaba el caso.'),
 ('Deudas','Tenía varias deudas y no sabía por dónde empezar. Klende puso las cosas en orden, me habló claro y definió cómo abordar mi situación. Lo que más valoré fue que respondió mis preguntas sin juzgarme.'),
 ('Embargos y cobros','Recibí una notificación y me preocupaba dejar pasar algún plazo. Klende revisó el proceso, asumió mi representación y me explicó qué seguía. Siempre supe qué necesitaba de mí y qué estaba haciendo con el caso.'),
 ('Contratos y patrimonio','Pensaba que el contrato estaba listo para firmar. Klende encontró puntos que podían comprometerme más de lo que había entendido y pidió que se aclararan. Esa revisión hizo que me tomara la firma con otros ojos.'),
 ('Familia','Era un asunto familiar difícil y necesitaba hablar con confianza. Klende me escuchó, fue firme al representarme y cuidadoso con los detalles personales. Nunca me quedé con una duda por miedo a preguntar.')
]

def link(url, label, cls='button gold'):
    return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener noreferrer">{label}</a>'

def adapt_shared(markup):
    markup = markup.replace('https://wa.link/h2jnnc', GENERAL)
    markup = re.sub(r'(href|src)="(assets/[^" ]+|[a-z-]+\.(?:css|js))"', r'\1="/\2"', markup)
    markup = markup.replace('href="./"','href="/b/"')
    markup = markup.replace('Klende Simon Villa', 'Klende Simón Villa')
    for anchor in ('servicios','simon'):
        markup = markup.replace(f'href="#{anchor}"',f'href="/b/#{anchor}"')
    return markup

def header(title, description, path='/b/', service=None):
    markup = adapt_shared(SOURCE.split('<main id="contenido">',1)[0])
    markup = re.sub(r'<title>.*?</title>',f'<title>{escape(title)} · Simón Abogado</title>',markup)
    markup = re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{escape(description,quote=True)}">',markup)
    markup = markup.replace('<link rel="stylesheet" href="/motion.css">', '')
    markup = re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="index,follow">', markup)
    if '<meta name="robots"' not in markup:
        markup = markup.replace('</head>', '<meta name="robots" content="index,follow"></head>')
    markup = markup.replace('src="/assets/logo.png"', 'src="/b/assets/logo.webp"')
    markup = markup.replace('Encuentra orientación', 'Servicios').replace('Cuéntame tu situación', 'Hablar con un abogado')
    markup = markup.replace('<a class="nav-cta"', '<a href="/b/#ubicacion">Ubicación</a><a class="nav-cta"')
    markup = markup.replace('</head>', seo_head(title + ' · Simón Abogado', description, path, service) + '</head>')
    return markup.replace('</head>','<link rel="stylesheet" href="/b/variant.css"><link rel="stylesheet" href="/b/scroll-effects.css"><link rel="stylesheet" href="/b/optimization.css"></head>')

def footer(contact_url=GENERAL):
    markup = adapt_shared('<footer>'+SOURCE.split('<footer>',1)[1])
    markup = markup.replace('<p>©', f'<div class="footer-location"><address>{PROFILE["street_address"]} · Medellín, Colombia</address><span>{PROFILE["hours_label"]}</span><a href="{PROFILE["maps_url"]}" target="_blank" rel="noopener noreferrer">Ver ubicación en Google Maps ↗</a></div><p>©')
    return markup.replace(GENERAL,contact_url).replace('src="/app.js"', 'src="/b/scroll-effects.js"')

def steps(items):
    return '<div class="steps">'+''.join(f'<article><span class="step-label">0{i}</span><h3>{title}</h3><p>{text}</p></article>' for i,(title,text) in enumerate(items,1))+'</div>'

def faq(items):
    return '<div class="faq-list">'+''.join(f'<details><summary>{q}<span class="plus" aria-hidden="true"></span></summary><p>{a}</p></details>' for q,a in items)+'</div>'

cards=''.join(f'''<article class="service-card"><a class="service-cover" href="/b/servicios/{s['slug']}/" aria-label="Conocer el servicio de {s['name'].lower()}"><img src="/assets/servicios/{s['image']}.webp" alt="Escena ilustrativa de {s['name'].lower()}" width="1536" height="1024" loading="lazy" decoding="async"></a><div class="card-copy"><p class="card-label">{s['name'].upper()}</p><h3>{s['title']}</h3><p>{s['brief']}</p><a class="button navy service-button" href="/b/servicios/{s['slug']}/" aria-label="Conocer el servicio de {s['name'].lower()}">Ver cómo puedo ayudarte</a></div></article>''' for s in SERVICES)
reviews=''.join(f'<figure class="review-card"><span class="review-mark" aria-hidden="true">“</span><blockquote>{text}</blockquote><figcaption><img class="review-avatar" src="/b/assets/portrait-sample-{i}.webp" alt="Retrato generado con IA para la propuesta" width="56" height="56" loading="lazy"><span><strong>{escape(TESTIMONIAL_NAMES[i-1])}</strong></span></figcaption></figure>' for i,(service,text) in enumerate(TESTIMONIALS,1))
home=header('Abogado en Medellín · familia y finanzas','Atención jurídica en Medellín para asuntos de familia, finanzas, deudas y contratos. Habla directamente con Klende Simón Villa.')+f'''
<main id="contenido"><section class="hero" id="inicio"><div class="hero-copy"><p class="eyebrow light">MÁS DE 5 AÑOS DE EXPERIENCIA · FAMILIA Y FINANZAS</p><h1>Tu problema merece<br><em>una respuesta clara.</em></h1><p class="hero-intro">¿Una deuda, una notificación o un conflicto familiar? Te explico tus opciones y el siguiente paso.</p><div class="hero-actions">{link(GENERAL,'Cuéntame qué ocurre')}<a class="button outline-light" href="#servicios">Ver servicios</a></div><p class="contact-expectation">Atención directa por WhatsApp.</p><div class="hero-note"><span class="short-line" aria-hidden="true"></span><p>Cuando asumo tu caso,<br>cuentas con mi atención directa.</p></div></div><figure class="portrait"><img src="/b/assets/simon-900.webp" srcset="/b/assets/simon-480.webp 480w, /b/assets/simon-900.webp 900w" sizes="(max-width:760px) 100vw, 48vw" alt="Klende Simón Villa, abogado" width="1086" height="1448" fetchpriority="high"><figcaption><span>Experiencia en familia y finanzas.</span><small>KLENDE SIMÓN VILLA · ABOGADO</small></figcaption></figure></section>
<div class="principles" aria-label="Mi compromiso contigo"><span>Estudio tu caso a fondo</span><span>Defino la estrategia</span><span>Te acompaño en cada etapa</span></div>
<section class="section services" id="servicios"><div class="section-heading"><div><p class="eyebrow">SERVICIOS JURÍDICOS</p><h2>¿Qué necesitas resolver?</h2></div><p>Elige el asunto que te preocupa. Si no sabes cuál es, cuéntamelo.</p></div><div class="service-grid">{cards}</div><div class="service-footer"><p>¿No encuentras tu situación?</p>{link(GENERAL,'Cuéntame qué pasa','button navy service-button')}</div></section>
<section class="approach section" id="simon"><div class="approach-statement"><p class="eyebrow">EXPERIENCIA Y ATENCIÓN DIRECTA</p><h2>Familia y finanzas.<br>Una ruta clara<br><em>para avanzar.</em></h2><p class="signature">Klende Simón Villa</p><span class="signature-caption">ABOGADO · MÁS DE CINCO AÑOS DE EXPERIENCIA</span></div><div class="approach-copy"><p class="lead">Experiencia enfocada en lo que necesitas proteger.</p><p>Soy <strong>Klende Simón Villa</strong>, abogado con más de cinco años de experiencia y práctica especializada en asuntos de <strong>familia y finanzas</strong>.</p><p>Reviso tu caso, te explico tus opciones y definimos el siguiente paso. Hablas directamente conmigo y conoces el alcance y los honorarios antes de contratar.</p>{credentials()}<div class="commitment">Atención clara, directa y cercana.</div><div class="section-action">{link(GENERAL,'Cuéntame qué ocurre','button navy')}</div></div></section>
<section class="section testimonials" id="testimonios"><div class="section-heading"><div><p class="eyebrow">EXPERIENCIAS DE MIS CLIENTES</p><h2>La confianza se construye<br>acompañando cada caso.</h2></div><p>Esto cuentan quienes han trabajado conmigo.</p></div><div class="review-viewport" tabindex="0" role="region" aria-label="Testimonios de clientes" aria-describedby="reviews-help"><div class="review-track"><div class="review-group">{reviews}</div></div></div><p class="reviews-help" id="reviews-help">Desliza para explorar. Pausa el movimiento al colocar el cursor encima o seleccionar esta sección con el teclado. Retratos de muestra generados con IA para esta propuesta.</p><div class="section-action">{link(GENERAL,'Quiero contar mi caso','button navy')}</div></section>
<section class="questions section"><div><p class="eyebrow">ANTES DE EMPEZAR</p><h2>Respuestas rápidas.</h2></div>{faq([('¿Tengo que saber qué servicio necesito?','No. Cuéntame qué ocurre y te ayudo a identificar por dónde empezar.'),('¿Qué documentos debo enviar?','Empieza con lo que tienes. Te indicaré si hace falta algo más.'),('¿Cuánto cuesta la asesoría?','Depende del servicio. Conocerás el alcance y los honorarios antes de contratar.')])}</section>
{location()}<section class="contact" id="consulta"><p class="eyebrow light">TU SIGUIENTE PASO</p><h2>Cuéntame qué necesitas resolver.</h2><p>Te explico cómo empezar y qué información hace falta.</p>{link(GENERAL,'Hablar con Klende por WhatsApp')}<span class="contact-note">Atención directa · Honorarios claros antes de contratar</span></section></main>'''+footer()
OUT.mkdir(parents=True,exist_ok=True)
home=home.replace('</body>', '<script src="/b/testimonials.js" defer></script></body>')
(OUT/'index.html').write_text(home,encoding='utf-8',newline='\n')

for s in SERVICES:
    local=LOCAL_CONTENT[s['slug']]
    s['faq']=local['faq']
    url='https://wa.link/'+s['wa']
    page=header(local['seo_title'],local['description'],'/b/servicios/'+s['slug']+'/',s)+f'''<main id="contenido"><section class="detail-hero"><div class="detail-intro"><nav class="breadcrumbs" aria-label="Ruta de navegación"><a href="/b/">Inicio</a><span aria-hidden="true">/</span><span>{s['name']}</span></nav><p class="eyebrow light">KLENDE SIMÓN VILLA · ABOGADO</p><h1>{local['heading']}</h1><p class="detail-promise">{s['title']}</p><p>{s['intro']}</p>{link(url,s['cta'])}<p class="contact-expectation">Cuéntame qué ocurre. Te indico qué información necesito para coordinar la asesoría.</p></div><figure class="detail-image"><img src="/assets/servicios/{s['image']}.webp" alt="Imagen ilustrativa del servicio de {s['name'].lower()}" width="1536" height="1024" fetchpriority="high"></figure></section>
<section class="section detail-context"><div><p class="eyebrow">EMPECEMOS POR LO QUE TE PREOCUPA</p><h2>{local['context_heading']}</h2><p class="intro-text">{local['context']}</p></div><ul class="situation-list">{''.join('<li>'+item+'</li>' for item in s['situations'])}</ul></section>
{legal_context(s,local)}
<section class="section prepare"><div><p class="eyebrow">PRIMER PASO</p><h2>Empieza con lo que tienes.</h2></div><div class="prepare-copy"><p>{s['prepare']}</p><p>Conocerás el alcance y los honorarios antes de contratar.</p>{link(url,s['cta'],'button navy')}</div></section>
<section class="questions section"><div><p class="eyebrow">RESPUESTAS DIRECTAS</p><h2>Lo que necesitas<br>saber para empezar.</h2></div>{faq(s['faq'])}</section>
{related_services(local,SERVICES)}<section class="contact detail-contact"><p class="eyebrow light">ATENCIÓN DIRECTA</p><h2>{s['close']}</h2><p>Cuéntame qué ocurre. Te explico cómo empezar.</p>{link(url,s['cta'])}<span class="contact-note">Hablas directamente con Klende Simón Villa</span><a class="other-service" href="/b/#servicios">Ver los otros servicios</a></section></main>'''+footer(url)
    # On service pages, both the header CTA and floating button use this service's link.
    page=page.replace(GENERAL,url)
    folder=OUT/'servicios'/s['slug']
    folder.mkdir(parents=True,exist_ok=True)
    (folder/'index.html').write_text(page,encoding='utf-8',newline='\n')

redirect = '''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="robots" content="noindex,follow"><link rel="canonical" href="/b/servicios/deudas-insolvencia/"><meta http-equiv="refresh" content="0;url=/b/servicios/deudas-insolvencia/"><title>Servicio actualizado · Simón Abogado</title></head><body><p>Este servicio ahora forma parte de <a href="/b/servicios/deudas-insolvencia/">Deudas, reportes y embargos</a>.</p></body></html>'''
for old_slug in ('reportes-crediticios', 'embargos-cobros'):
    folder = OUT / 'servicios' / old_slug
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'index.html').write_text(redirect, encoding='utf-8', newline='\n')

print('Version B generada en dist/b: inicio y cuatro servicios. Version A conservada.')
