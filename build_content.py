"""Genera el contenido estático de la propuesta B; no requiere dependencias."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent / 'dist'
GENERAL = 'https://wa.link/h2jnnc'
SERVICES = [
    dict(slug='deudas-insolvencia', name='Deudas e insolvencia', image='01-deudas-insolvencia', wa='uwryis',
         title='¿Las deudas superan lo que puedes pagar?',
         brief='Recupera claridad sobre tus obligaciones y conoce las alternativas que podrían aplicar a tu situación.',
         intro='Cuando cada ingreso ya tiene destino y los cobros no paran, decidir se vuelve más difícil. Puedes empezar por poner tus obligaciones en orden y entender qué caminos vale la pena evaluar.',
         situations=['Los pagos mensuales superan tu capacidad actual y no sabes qué priorizar.', 'Tienes obligaciones con varios acreedores y necesitas una visión completa de tu situación.', 'Quieres saber si una negociación o un proceso de insolvencia podría ser una alternativa para ti.'],
         outcomes=[('Tu punto de partida', 'Revisamos deudas, ingresos y documentos para entender tu capacidad de pago y las dificultades que enfrentas.'), ('Las alternativas', 'Evaluamos las opciones de manejo de tus obligaciones y si tiene sentido estudiar una posible insolvencia.'), ('Una ruta para decidir', 'Te explico qué implica cada alternativa, qué información falta y cuál podría ser el siguiente paso.')],
         prepare='Ten a mano una relación de tus deudas, los pagos que realizas, tus ingresos y las comunicaciones de cobro que hayas recibido. Si la información está incompleta, empezamos por identificar qué falta.',
         faq=[('¿La insolvencia es una opción para cualquier persona?', 'Depende de las condiciones de cada situación. Primero se revisan tus obligaciones, tu capacidad de pago y la información necesaria para evaluar si esta vía resulta aplicable.'), ('¿La asesoría garantiza que desaparezcan mis deudas?', 'No. La orientación busca que comprendas las alternativas y sus implicaciones. Cualquier resultado depende de las condiciones del caso y del procedimiento que corresponda.'), ('¿Puedo consultar si todavía estoy pagando?', 'Sí. Puedes solicitar una revisión de tu situación para comprender tus opciones antes de tomar nuevas decisiones sobre tus obligaciones.')],
         cta='Quiero revisar mis deudas', close='Empieza por entender tus opciones.', alt='Mujer organizando facturas y haciendo cuentas en casa'),
    dict(slug='reportes-crediticios', name='Reportes crediticios', image='02-reportes-crediticios', wa='ku1tfy',
         title='¿Un reporte negativo está limitando tus opciones de crédito?',
         brief='Entiende qué información aparece en tu historial y si hay motivos para solicitar una revisión.',
         intro='Que una solicitud de crédito no avance puede dejarte con más preguntas que respuestas. Revisemos el reporte y sus antecedentes para entender qué está ocurriendo y qué puedes hacer.',
         situations=['Encuentras una obligación o un dato que no reconoces en tu historial.', 'Ya realizaste un pago y tienes dudas sobre la información que sigue apareciendo.', 'Necesitas orientación para consultar o reclamar información relacionada con un reporte.'],
         outcomes=[('Qué dice tu reporte', 'Revisamos la información disponible y los documentos relacionados con la obligación.'), ('Qué conviene aclarar', 'Identificamos posibles inconsistencias y los soportes que hacen falta para estudiar una reclamación.'), ('Cómo solicitar la revisión', 'Te explico las gestiones que podrían corresponder y el alcance del acompañamiento en tu caso.')],
         prepare='Reúne el reporte que quieres revisar, los comprobantes de pago y las respuestas de la entidad, si los tienes. No compartas contraseñas ni códigos de acceso: para comenzar basta con contar qué información te preocupa.',
         faq=[('¿Todo reporte negativo se puede eliminar?', 'No se puede asegurar eso. Primero hay que revisar la información, sus antecedentes y si existen fundamentos para solicitar una corrección o realizar otra gestión.'), ('¿Pueden garantizarme que me aprueben un crédito?', 'No. La aprobación depende de la entidad que evalúa la solicitud. El acompañamiento se enfoca en revisar la información reportada y las actuaciones que puedan corresponder.'), ('¿Qué pasa si no reconozco la deuda?', 'Cuéntame qué información aparece y qué comunicaciones has recibido. Eso permite definir qué antecedentes y soportes es necesario revisar.')],
         cta='Quiero revisar mi reporte', close='Entiende qué hay detrás de tu reporte.', alt='Hombre revisando información financiera en un portátil'),
    dict(slug='embargos-cobros', name='Embargos y cobros', image='03-embargos-cobros', wa='twk37q',
         title='¿Recibiste una notificación de cobro o embargo y no sabes qué hacer?',
         brief='Comprende el documento que recibiste, en qué estado está el asunto y qué opciones debes evaluar.',
         intro='Una carta de cobro o una notificación puede hacerte pensar de inmediato en tu sueldo, tu cuenta o tus bienes. El primer paso es entender qué recibiste y qué atención necesita tu situación.',
         situations=['Te llegó una comunicación y no distingues si es un cobro o una actuación judicial.', 'Tienes conocimiento de un proceso y necesitas revisar sus documentos.', 'Te preocupa una medida sobre tus ingresos o tus bienes y buscas orientación para actuar.'],
         outcomes=[('Qué está ocurriendo', 'Revisamos la comunicación, quién la emite y los antecedentes que tengas del asunto.'), ('Qué requiere atención', 'Identificamos el estado de la situación y los puntos que deben revisarse para definir una respuesta.'), ('Qué opciones evaluar', 'Te explico las alternativas que puedan corresponder y el alcance de una eventual representación.')],
         prepare='Ten disponible la notificación completa, la fecha en que la recibiste y los documentos de la obligación. Si conoces el número del proceso o has recibido otras comunicaciones, inclúyelos al explicar tu caso.',
         faq=[('¿Una llamada de cobro significa que ya existe un embargo?', 'Es necesario distinguir entre las comunicaciones de cobro y los documentos de un proceso. Revisar lo que recibiste permite entender tu situación concreta.'), ('¿La asesoría puede levantar un embargo de inmediato?', 'No se puede prometer un levantamiento ni un tiempo de respuesta sin estudiar el caso. Primero se revisan el proceso, los documentos y las actuaciones que puedan corresponder.'), ('¿Qué debo contar en el primer mensaje?', 'Indica qué recibiste, cuándo lo recibiste y qué te preocupa. Con esa información podemos coordinar la revisión de los documentos.')],
         cta='Quiero revisar la notificación', close='Comprende tu situación antes de decidir.', alt='Hombre leyendo una comunicación con documentos y llaves sobre la mesa'),
    dict(slug='recuperacion-cartera', name='Recuperación de cartera', image='04-recuperacion-cartera', wa='b59gk4',
         title='¿Te deben dinero y necesitas reclamar el pago?',
         brief='Revisa los soportes de la deuda y las vías disponibles para reclamar lo que te deben.',
         intro='Has cumplido con tu parte, pero el pago no llega. Mientras insistes, se afectan tus cuentas y tus planes. Revisemos qué respalda la obligación y qué camino puedes considerar para reclamarla.',
         situations=['Entregaste un producto o prestaste un servicio y el pago sigue pendiente.', 'Prestaste dinero y los compromisos de pago no se han cumplido.', 'Has intentado cobrar y necesitas evaluar una gestión formal o una posible reclamación.'],
         outcomes=[('El respaldo de tu cobro', 'Revisamos contratos, facturas, comprobantes y comunicaciones relacionados con la obligación.'), ('Las vías disponibles', 'Evaluamos si conviene considerar un acuerdo, una gestión de cobro o una actuación judicial.'), ('El alcance de la gestión', 'Hablamos de los pasos, los costos del servicio y los factores que pueden influir en la recuperación.')],
         prepare='Reúne los documentos que respaldan la deuda, el monto pendiente, las fechas acordadas y las comunicaciones con la persona o empresa que te debe. Indica también si hubo abonos o acuerdos posteriores.',
         faq=[('¿Puedo consultar si no tengo un contrato firmado?', 'Sí. Podemos revisar qué documentos, comprobantes o comunicaciones existen y qué permiten acreditar. La viabilidad de una gestión depende de esa revisión.'), ('¿Es necesario demandar desde el principio?', 'La vía adecuada depende del caso. Primero se estudian los antecedentes, los soportes disponibles y las posibilidades de acuerdo o reclamación.'), ('¿Se puede garantizar la recuperación del dinero?', 'No. El resultado depende de varios factores, entre ellos los soportes de la obligación y las condiciones del deudor. La revisión permite valorar esas dificultades antes de avanzar.')],
         cta='Quiero revisar una deuda a mi favor', close='Dale una dirección clara a tu reclamación.', alt='Emprendedora revisando facturas en su negocio'),
    dict(slug='contratos-patrimonio', name='Contratos y patrimonio', image='05-contratos-patrimonio', wa='a2imqi',
         title='¿Necesitas claridad antes de firmar o decidir sobre tus bienes?',
         brief='Entiende tus compromisos, identifica puntos de atención y toma decisiones con mejor información.',
         intro='Una firma puede comprometer dinero, tiempo y bienes que has construido con esfuerzo. Antes de decidir, conviene que entiendas qué aceptas y qué necesitas aclarar.',
         situations=['Vas a firmar un contrato y hay condiciones que no entiendes o te generan dudas.', 'Necesitas dejar claros los compromisos de un acuerdo personal o comercial.', 'Tienes una inquietud sobre documentos o acuerdos relacionados con tus bienes.'],
         outcomes=[('Qué estás acordando', 'Revisamos el objeto del contrato, las obligaciones y los puntos relevantes para tu decisión.'), ('Qué merece atención', 'Identificamos ambigüedades, compromisos y condiciones que conviene aclarar o discutir.'), ('Cómo avanzar', 'Definimos si necesitas una revisión, ajustes al documento o acompañamiento para estructurar el acuerdo.')],
         prepare='Ten a mano el contrato o borrador completo, sus anexos y una explicación de lo que quieres lograr. Si se trata de un bien, cuéntame cuál es la operación y qué documentos tienes disponibles.',
         faq=[('¿Puedo consultar antes de tener un contrato listo?', 'Sí. Podemos conversar sobre el acuerdo que necesitas y definir qué información hace falta para establecer el alcance de su elaboración o revisión.'), ('¿También puedo consultar si ya firmé?', 'Sí. La revisión puede ayudarte a comprender los compromisos asumidos y a evaluar una inquietud o dificultad concreta relacionada con el acuerdo.'), ('¿La revisión evita cualquier problema futuro?', 'Ninguna revisión elimina todos los riesgos. Su propósito es ayudarte a identificar puntos relevantes, aclarar compromisos y decidir con mejor información.')],
         cta='Quiero revisar mi contrato o acuerdo', close='Que tu próxima firma sea una decisión informada.', alt='Mujer revisando un contrato junto a un profesional'),
    dict(slug='familia-sucesiones', name='Familia y sucesiones', image='06-familia-sucesiones', wa='0xlmp0',
         title='¿Una situación familiar necesita un camino claro?',
         brief='Encuentra orientación para una separación, un asunto con tus hijos o los trámites de una herencia.',
         intro='Cuando una decisión involucra a tu familia, las dudas jurídicas se mezclan con lo que sientes. Mereces un espacio para explicar lo que ocurre y entender las opciones con calma.',
         situations=['Estás considerando una separación o un divorcio y necesitas entender qué asuntos revisar.', 'Tienes inquietudes sobre alimentos, custodia o acuerdos relacionados con tus hijos.', 'Tras el fallecimiento de un familiar, necesitas orientación sobre una sucesión.'],
         outcomes=[('Lo que necesitas resolver', 'Escuchamos tu situación e identificamos los asuntos familiares y patrimoniales que requieren atención.'), ('Las opciones del caso', 'Revisamos los documentos, los acuerdos existentes y los puntos en los que hay diferencias.'), ('Un siguiente paso claro', 'Te explico las alternativas y definimos el acompañamiento que necesitas para avanzar.')],
         prepare='Empieza por contar qué está pasando y qué necesitas resolver. Si tienes acuerdos anteriores, comunicaciones o documentos relacionados con la situación, podemos definir cuáles conviene revisar.',
         faq=[('¿Puedo consultar aunque mi familia todavía no esté de acuerdo?', 'Sí. La orientación inicial permite entender tu situación, identificar las diferencias y revisar las alternativas disponibles.'), ('¿Puedo recibir orientación sobre varios asuntos a la vez?', 'Sí. Si una separación involucra acuerdos sobre hijos o bienes, podemos identificar los temas relacionados y organizar la revisión de cada uno.'), ('¿Qué información necesito para una sucesión?', 'En la primera conversación identificamos la información sobre el familiar fallecido, las personas involucradas y los bienes conocidos para definir qué documentación hace falta.')],
         cta='Quiero orientación sobre mi familia', close='Un paso claro en un momento sensible.', alt='Tres mujeres de distintas generaciones conversando con una carpeta en la mesa')
]

# Tres asuntos del lado de quien enfrenta deudas se presentan como un solo servicio.
_by_slug = {service['slug']: service for service in SERVICES}
_debt_service = dict(_by_slug['deudas-insolvencia'])
_debt_service.update(
    name='Deudas, reportes y embargos', title='¿Una deuda, un reporte o un embargo te preocupa?',
    brief='Revisa tus deudas, tu historial crediticio o una notificación y conoce el siguiente paso.',
    intro='Si las deudas se acumulan, aparece un dato que no reconoces o recibiste una notificación, revisamos tu situación y te explico cómo actuar.',
    situations=['Necesitas ordenar deudas o evaluar una negociación o insolvencia.', 'Hay un dato incorrecto o una obligación que no reconoces en tu historial.', 'Recibiste un cobro, una demanda o una medida sobre tus bienes.'],
    outcomes=[('Revisamos tu caso', 'Estudio tus documentos, pagos, reporte o notificación.'), ('Aclaramos tus opciones', 'Te explico qué vías pueden aplicar y qué documentos hacen falta.'), ('Definimos el siguiente paso', 'Conoces el alcance, los honorarios y la gestión que acordemos.')],
    prepare='Cuéntame qué ocurrió y comparte los documentos que tengas: reporte, comprobantes o notificación. No necesitas tener todo para empezar.',
    faq=[('¿Debo saber qué servicio necesito?', 'No. Cuéntame qué pasó y organizamos la revisión.'), ('¿Pueden borrar cualquier reporte o levantar un embargo?', 'Cada solicitud depende de sus fundamentos y documentos. Primero estudio el caso y te explico las opciones.'), ('¿Qué hago si recibí una notificación?', 'Guárdala completa y anota cuándo la recibiste. Escríbeme para revisar qué actuación requiere atención.')],
    cta='Revisar mi caso', close='Aclaremos qué está pasando y cómo puedes actuar.',
)
_collection_service = dict(_by_slug['recuperacion-cartera'])
_collection_service.update(
    name='Cobro de deudas pendientes', title='¿Te deben dinero y no te pagan?',
    brief='Revisa las pruebas y define cómo reclamar el pago pendiente.',
    intro='Si ya cumpliste y el pago no llega, reviso qué respalda la deuda y te explico las vías para reclamarla.',
    situations=['Te deben por un producto, servicio o préstamo.', 'Has cobrado varias veces y no cumplen el acuerdo.', 'Necesitas valorar una negociación o reclamación formal.'],
    outcomes=[('Reviso los soportes', 'Estudio contratos, facturas, comprobantes y conversaciones.'), ('Defino la vía', 'Te explico las opciones de acuerdo o reclamación.'), ('Acordamos el alcance', 'Conoces los pasos, costos y condiciones antes de avanzar.')],
    prepare='Ten a mano el monto pendiente, las fechas y los soportes que tengas. Si hubo abonos o acuerdos, cuéntamelo.',
    faq=[('¿Puedo reclamar sin contrato firmado?', 'Reviso comprobantes, mensajes y otros soportes para valorar qué acreditan.'), ('¿Siempre hay que demandar?', 'No necesariamente. Primero estudio la obligación y las opciones disponibles.'), ('¿Se puede garantizar el pago?', 'No. Te explico los factores y el alcance de la gestión antes de contratar.')],
    cta='Reclamar un pago pendiente', close='Dale rumbo a tu reclamación.',
)
_contract_service = dict(_by_slug['contratos-patrimonio'])
_contract_service.update(
    title='¿Vas a firmar o proteger un bien?', brief='Revisa contratos y acuerdos antes de asumir compromisos.',
    intro='Antes de firmar, entiende tus obligaciones, los riesgos y las condiciones del acuerdo.',
    situations=['Vas a firmar y algo no te queda claro.', 'Necesitas redactar o negociar un acuerdo.', 'Ya firmaste y surgió un incumplimiento.'],
    outcomes=[('Reviso el documento', 'Identifico obligaciones, pagos, plazos y condiciones.'), ('Te explico los riesgos', 'Señalo qué conviene aclarar o negociar.'), ('Acordamos los ajustes', 'Definimos la revisión, redacción o gestión que necesitas.')],
    prepare='Comparte el contrato completo y cuéntame qué quieres lograr o qué te preocupa.',
    faq=[('¿Puedo consultar antes de firmar?', 'Sí. Reviso el documento y te explico sus puntos clave.'), ('¿Y si ya firmé?', 'Estudio lo acordado y el problema que surgió para definir opciones.')],
    cta='Revisar mi contrato', close='Firma con claridad sobre lo que acuerdas.',
)
_family_service = dict(_by_slug['familia-sucesiones'])
_family_service.update(
    title='¿Un asunto familiar necesita una solución?', brief='Orientación y representación para asuntos de familia y sucesiones.',
    intro='Te escucho, ordeno lo que necesitas resolver y te explico cómo avanzar con sensibilidad y discreción.',
    situations=['Estás considerando una separación o un divorcio.', 'Necesitas resolver alimentos, custodia o acuerdos sobre tus hijos.', 'Debes iniciar una sucesión.'],
    outcomes=[('Te escucho', 'Aclaro tus prioridades y los temas que requieren atención.'), ('Reviso las opciones', 'Estudio documentos, acuerdos y diferencias.'), ('Te acompaño', 'Definimos las actuaciones y el alcance del servicio.')],
    prepare='Cuéntame qué ocurre y comparte los acuerdos o documentos que ya tienes.',
    faq=[('¿Puedo consultar si aún no hay acuerdo?', 'Sí. Revisamos las diferencias y las vías que pueden aplicar.'), ('¿Qué necesito para una sucesión?', 'Cuéntame quiénes están involucrados y qué bienes conocen. Te indico qué documentos reunir.')],
    cta='Hablar de mi situación familiar', close='Hablemos con claridad y discreción.',
)
SERVICES = [_debt_service, _collection_service, _contract_service, _family_service]

def wa(url, label, cls='button gold'):
    return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener noreferrer">{label}</a>'

def head(title, description, base=''):
    return f'''<!doctype html><html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} · Simón Abogado</title><meta name="description" content="{escape(description, quote=True)}"><meta name="robots" content="noindex,nofollow">
<link rel="icon" href="{base}assets/favicon.ico"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}styles.css"><link rel="stylesheet" href="{base}sections.css"><link rel="stylesheet" href="{base}services.css"><link rel="stylesheet" href="{base}footer.css"><link rel="stylesheet" href="{base}motion.css"></head><body>
<a class="skip" href="#contenido">Ir al contenido</a><header class="header" id="inicio-pagina" tabindex="-1"><a class="brand" href="{base or './'}" aria-label="Simón Abogado, inicio"><img src="{base}assets/logo.png" alt="Simón Abogado. Compromiso que garantiza tu confianza." width="2172" height="724"></a><button class="menu-toggle" aria-expanded="false" aria-controls="menu">Menú <span aria-hidden="true">☰</span></button><nav id="menu" aria-label="Principal"><a href="{base}#servicios">Encuentra orientación</a><a href="{base}#simon">Conoce a tu abogado</a>{wa(GENERAL, 'Cuéntame tu situación', 'nav-cta')}</nav></header>'''

def footer(base='', contact_url=GENERAL):
    return f'''<footer><div class="footer-brand">SIMÓN ABOGADO<span>Compromiso que garantiza tu confianza.</span></div><div class="footer-nav"><a href="{base}#servicios">Encuentra tu servicio</a><a href="{base}#simon">Conoce a tu abogado</a><a class="footer-back-top" href="#inicio-pagina">Volver arriba ↑</a></div><div class="footer-social"><span class="footer-social-label">Conecta con nosotros</span><a href="https://www.facebook.com/profile.php?id=61595132795227" target="_blank" rel="noopener noreferrer" aria-label="Simón Abogado en Facebook (abre en una pestaña nueva)"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 22v-9h3l.5-3.5h-3.5V7.25c0-1 .3-1.75 1.75-1.75H17V2.4c-.3-.05-1.35-.15-2.6-.15-2.6 0-4.4 1.6-4.4 4.55v2.7H7V13h3v9z"/></svg><span>Facebook</span></a><a href="https://www.tiktok.com/@garantiacol_abogados" target="_blank" rel="noopener noreferrer" aria-label="Garantíacol Abogados en TikTok (abre en una pestaña nueva)"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 2h-3v13a3 3 0 1 1-3-3V9a6 6 0 1 0 6 6V8a9 9 0 0 0 5 1.5v-3A5 5 0 0 1 16 2z"/></svg><span>TikTok</span></a></div><p>© 2026 Simón Abogado · Atención jurídica con Klende Simon Villa</p></footer><a class="whatsapp-float" href="{contact_url}" target="_blank" rel="noopener noreferrer" aria-label="Cuéntame tu caso por WhatsApp (abre en una pestaña nueva)" title="Hablar por WhatsApp"><span class="whatsapp-label">Cuéntame tu caso</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.52 3.48A11.86 11.86 0 0 0 12.06 0C5.48 0 .12 5.35.12 11.93c0 2.1.55 4.16 1.6 5.97L0 24l6.26-1.64a11.94 11.94 0 0 0 5.8 1.48h.01C18.65 23.84 24 18.49 24 11.91c0-3.18-1.24-6.18-3.48-8.43ZM12.07 21.83a9.9 9.9 0 0 1-5.05-1.38l-.36-.21-3.72.98.99-3.63-.24-.38a9.89 9.89 0 0 1-1.51-5.28c0-5.46 4.44-9.9 9.91-9.9a9.84 9.84 0 0 1 7 2.9 9.83 9.83 0 0 1 2.9 7c0 5.47-4.44 9.9-9.92 9.9Zm5.44-7.42c-.3-.15-1.76-.87-2.04-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.47-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.18-.3-.02-.46.13-.61.14-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.49s1.07 2.89 1.22 3.09c.15.2 2.1 3.21 5.08 4.5.71.3 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.08 1.76-.72 2.01-1.42.25-.69.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35Z"/></svg></a><script src="{base}app.js"></script></body></html>'''

def faqs(items):
    return '<div class="faq-list">' + ''.join(f'<details><summary>{q}<span class="plus" aria-hidden="true"></span></summary><p>{a}</p></details>' for q,a in items) + '</div>'

def steps(items):
    return '<div class="steps">' + ''.join(f'<article><span class="step-label">0{i}</span><h3>{t}</h3><p>{p}</p></article>' for i,(t,p) in enumerate(items,1)) + '</div>'

cards=[]
for s in SERVICES:
    route=f'servicios/{s["slug"]}/'
    cards.append(f'''<article class="service-card"><a class="service-cover" href="{route}" aria-label="Conocer el servicio de {s['name'].lower()}"><img src="assets/servicios/{s['image']}.webp" alt="{s['alt']}" width="1536" height="1024" loading="lazy" decoding="async"></a><div class="card-copy"><p class="card-label">{s['name'].upper()}</p><h3>{s['title']}</h3><p>{s['brief']}</p><a class="button navy service-button" href="{route}" aria-label="Conocer el servicio de {s['name'].lower()}">Ver cómo puedo ayudarte</a></div></article>''')

home=head('Abogado en Medellín · familia y finanzas', 'Atención jurídica en Medellín para asuntos de familia, finanzas, deudas y contratos. Habla directamente con Klende Simón Villa.')+f'''
<main id="contenido"><section class="hero" id="inicio"><div class="hero-copy"><p class="eyebrow light">MÁS DE 5 AÑOS DE EXPERIENCIA · FAMILIA Y FINANZAS</p><h1>Tu problema merece<br><em>una respuesta clara.</em></h1><p class="hero-intro">¿Una deuda, una notificación o un conflicto familiar? Te explico tus opciones y el siguiente paso.</p>{wa(GENERAL,'Cuéntame qué ocurre')}<div class="hero-note"><span class="short-line" aria-hidden="true"></span><p>Atención directa de Klende Simon Villa.<br>Empecemos por lo que hoy te preocupa.</p></div></div><figure class="portrait"><img src="assets/simon.jpg" alt="Klende Simon Villa, abogado" width="1086" height="1448" fetchpriority="high"><figcaption><span>Experiencia en familia y finanzas.</span><small>KLENDE SIMON VILLA · ABOGADO</small></figcaption></figure></section>
<div class="principles" aria-label="Lo que puedes esperar"><span>Tu situación, escuchada con atención</span><span>Tus opciones, explicadas con claridad</span><span>Tu siguiente paso, con orientación</span></div>
<section class="section services" id="servicios"><div class="section-heading"><div><p class="eyebrow">SERVICIOS JURÍDICOS</p><h2>¿Qué necesitas resolver?</h2></div><p>Elige el asunto que te preocupa. Si no sabes cuál es, cuéntamelo.</p></div><div class="service-grid">{''.join(cards)}</div><div class="service-footer"><p>¿No encuentras tu situación?</p>{wa(GENERAL,'Cuéntame qué pasa','button navy service-button')}</div></section>
<section class="approach section" id="simon"><div class="approach-statement"><p class="eyebrow">EXPERIENCIA Y ATENCIÓN DIRECTA</p><h2>Familia y finanzas.<br>Una ruta clara<br><em>para avanzar.</em></h2><p class="signature">Klende Simon Villa</p><span class="signature-caption">ABOGADO · MÁS DE CINCO AÑOS DE EXPERIENCIA</span></div><div class="approach-copy"><p class="lead">Experiencia enfocada en lo que necesitas proteger.</p><p>Soy <strong>Klende Simon Villa</strong>, abogado con más de cinco años de experiencia y práctica especializada en asuntos de <strong>familia y finanzas</strong>.</p><p>Reviso tu caso, te explico tus opciones y definimos el siguiente paso. Hablas directamente conmigo y conoces el alcance y los honorarios antes de contratar.</p><div class="commitment">Atención clara, directa y cercana.</div></div></section>
<section class="questions section"><div><p class="eyebrow">ANTES DE EMPEZAR</p><h2>Respuestas rápidas.</h2></div>{faqs([('¿Tengo que saber qué servicio necesito?', 'No. Cuéntame qué está pasando y te ayudo a identificar por dónde empezar.'),('¿Qué documentos debo enviar?', 'Empieza por explicar tu situación y compartir lo que ya tienes. Te indicaré si hace falta algo más.'),('¿Cuánto cuesta la asesoría?', 'Depende del servicio. Conocerás el alcance y los honorarios antes de contratar.')])}</section>
<section class="contact" id="consulta"><p class="eyebrow light">TU SIGUIENTE PASO</p><h2>Cuéntame qué necesitas resolver.</h2><p>Te explico cómo empezar y qué información hace falta.</p>{wa(GENERAL,'Hablar con Klende por WhatsApp')}<span class="contact-note">Atención directa · Honorarios claros antes de contratar</span></section></main>'''+footer()
(ROOT/'index.html').write_text(home,encoding='utf-8',newline='\n')

for s in SERVICES:
    base='../../'
    url='https://wa.link/'+s['wa']
    page=head(s['name'],s['brief'],base)+f'''<main id="contenido"><section class="detail-hero"><div class="detail-intro"><a class="back-link" href="../../#servicios">← Explorar todos los servicios</a><p class="eyebrow light">{s['name'].upper()}</p><h1>{s['title']}</h1><p>{s['intro']}</p>{wa(url,s['cta'])}</div><figure class="detail-image"><img src="../../assets/servicios/{s['image']}.webp" alt="{s['alt']}" width="1536" height="1024" fetchpriority="high"></figure></section>
<section class="section detail-context"><div><p class="eyebrow">EMPECEMOS POR LO QUE TE PREOCUPA</p><h2>¿Te pasa algo de esto?</h2><p class="intro-text">No necesitas conocer el trámite. Cuéntame qué ocurrió.</p></div><ul class="situation-list">{''.join('<li>'+v+'</li>' for v in s['situations'])}</ul></section>
<section class="section detail-outcomes"><div class="section-heading"><div><p class="eyebrow">ASÍ PUEDO AYUDARTE</p><h2>Reviso. Te explico. Actuamos.</h2></div><p>Con atención directa y un alcance claro para tu caso.</p></div>{steps(s['outcomes'])}</section>
<section class="section prepare"><div><p class="eyebrow">PRIMER PASO</p><h2>Empieza con lo que tienes.</h2></div><div class="prepare-copy"><p>{s['prepare']}</p><p>Conocerás el alcance y los honorarios antes de contratar.</p>{wa(url,s['cta'],'button navy')}</div></section>
<section class="questions section"><div><p class="eyebrow">RESPUESTAS RÁPIDAS</p><h2>Lo esencial para empezar.</h2></div>{faqs(s['faq'])}</section>
<section class="contact detail-contact"><p class="eyebrow light">ATENCIÓN DIRECTA</p><h2>{s['close']}</h2><p>Cuéntame qué ocurre. Te explico cómo empezar.</p>{wa(url,s['cta'])}<span class="contact-note">Hablas directamente con Klende Simon Villa</span><a class="other-service" href="../../#servicios">Ver los otros servicios</a></section></main>'''+footer(base,url)
    folder=ROOT/'servicios'/s['slug']
    folder.mkdir(parents=True,exist_ok=True)
    (folder/'index.html').write_text(page,encoding='utf-8',newline='\n')

redirect = '''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="robots" content="noindex,follow"><link rel="canonical" href="../deudas-insolvencia/"><meta http-equiv="refresh" content="0;url=../deudas-insolvencia/"><title>Servicio actualizado · Simón Abogado</title></head><body><p>Este servicio ahora forma parte de <a href="../deudas-insolvencia/">Deudas, reportes y embargos</a>.</p></body></html>'''
for old_slug in ('reportes-crediticios', 'embargos-cobros'):
    folder = ROOT / 'servicios' / old_slug
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'index.html').write_text(redirect, encoding='utf-8', newline='\n')

print('Contenido generado: inicio y cuatro páginas de servicios.')
