# Questions from Fogarty, C. T., & Brown, J. B. (2002).
# Screening for abuse in Spanish-speaking women. 
# The Journal of the American Board of Family Practice, 15(2), 101-111.

QUESTIONS = {
    1: {
        "text_es": "¿En general, cómo describiría usted su relación con su pareja?",
        "options": [
            {"label": "Mucha tensión", "score": 2},
            {"label": "Alguna tensión", "score": 1},
            {"label": "Sin tensión", "score": 0}
        ]
    },
    2: {
        "text_es": "Usted y su pareja resuelven sus discusiones (argumentos) con...",
        "options": [
            {"label": "Mucha dificultad", "score": 2},
            {"label": "Alguna dificultad", "score": 1},
            {"label": "Sin dificultad", "score": 0}
        ]
    },
    3: {
        "text_es": "Al terminar las discusiones ¿usted se siente decaída o mal con usted misma?",
        "options": [
            {"label": "Muchas veces", "score": 2},
            {"label": "A veces", "score": 1},
            {"label": "Nunca", "score": 0}
        ]
    },
    4: {
        "text_es": "Las discusiones terminan en golpes, patadas, o empujones?",
        "options": [
            {"label": "Muchas veces", "score": 2},
            {"label": "A veces", "score": 1},
            {"label": "Nunca", "score": 0}
        ]
    },
    5: {
        "text_es": "¿Siente miedo de lo que su pareja diga o haga?",
        "options": [
            {"label": "Muchas veces", "score": 2},
            {"label": "A veces", "score": 1},
            {"label": "Nunca", "score": 0}
        ]
    },
    6: {
        "text_es": "¿Su pareja ha abusado de usted físicamente?",
        "options": [
            {"label": "Muchas veces", "score": 2},
            {"label": "A veces", "score": 1},
            {"label": "Nunca", "score": 0}
        ]
    },
    7: {
        "text_es": "¿Su pareja ha abusado de usted emocionalmente?",
        "options": [
            {"label": "Muchas veces", "score": 2},
            {"label": "A veces", "score": 1},
            {"label": "Nunca", "score": 0}
        ]
    },
    8: {
        "text_es": "¿Su pareja ha abusado de usted sexualmente?",
        "options": [
            {"label": "Muchas veces", "score": 2},
            {"label": "A veces", "score": 1},
            {"label": "Nunca", "score": 0}
        ]
    }
}

RISK_LEVELS = [
    {
        "min_score": 0,
        "max_score": 3,
        "level": "Todo Chill / Prevención",
        "title": "¡Parece que tu relación está tranquila! ☀️",
        "color": "success",
        "description": "Tu resultado es bajo, ¡lo cual es genial! No detectamos señales de violencia. Recuerda siempre que la <strong>comunicación efectiva y clara</strong> es la mejor herramienta para una relación tranquila y sana. ¡Sigue así!",
        "resources": []
    },
    {
        "min_score": 4,
        "max_score": 6,
        "level": "¡Ojo Aquí! / Tensión y Control",
        "title": "¡Alerta! Hay <i>señales de humo</i> en tu relación.",
        "color": "warning",
        "description": "El puntaje sugiere que hay <strong>mucha tensión, dificultad para resolver problemas o control</strong>. Esto no es violencia <strong>física</strong>, pero son dinámicas tóxicas que pueden escalar. Busca hablar con alguien de muchísima confianza o con un profesional. ¡No dejes que se normalice!",
        "resources": [
            {"name": "Centros de Emergencia Mujer (CEM)",
             "contact": "Accede al directorio de atención legal y psicológica gratuita y presencial.<br>Recuerda que atienden las 24 horas del día, los 365 días del año.",
             "link": "https://cdn.www.gob.pe/uploads/document/file/3650084/3487068-directorio-cemf-y-cemf-24hr-actualizado-julio-2025.pdf?v=1758557895"}
        ]
    },
    {
        "min_score": 7,
        "max_score": 16,
        "level": "¡Peligro! / Violencia Detectada",
        "title": "¡DETENTE! Este resultado sugiere una situación de violencia de pareja.",
        "color": "danger",
        "description": "El puntaje es alto, lo que indica la presencia de <strong>miedo, abuso o agresión</strong>. ¡Tu seguridad y tu vida son lo más importante! No estás sola. Necesitas buscar apoyo o contactar a las líneas de ayuda <strong>inmediatamente</strong>.",
        "resources": [
            {"name": "Centros de Emergencia Mujer (CEM)",
             "contact": "Accede al directorio de atención legal y psicológica gratuita y presencial.<br>Recuerda que atienden las 24 horas del día, los 365 días del año.",
             "link": "https://cdn.www.gob.pe/uploads/document/file/3650084/3487068-directorio-cemf-y-cemf-24hr-actualizado-julio-2025.pdf?v=1758557895"}
        ]
    }
]

SAFETY_PLAN = [
    "Recuerda ir a tus <strong>'lugares seguros'</strong>, ya sea una persona, familiar, amistad o un lugar en sí.",
    "Ten siempre a la mano tu <strong>DNI</strong> (Documento Nacional de Identidad).",
    "No solo puedes llamar a la <strong>Línea 100</strong>, también hay <strong>Chat 100</strong> en caso prefieras escribir el link es: <a href='https://chat100.warminan.gob.pe/' target='_blank'>Chat 100</a>",
    "Si ves o sientes algo raro, siempre <strong>documenta</strong>. La evidencia siempre ayuda: graba o toma fotos de forma segura. ¡Eso te ayudará muchísimo!"
]
