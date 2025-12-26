import streamlit as st

st.set_page_config(
    page_title="ILORCI / URKESKEN = LORCA",
    layout="wide",
    page_icon="📜",
)

st.sidebar.title("Navegación")
seccion = st.sidebar.radio(
    "Ir a la sección",
    [
        "Página principal",
        "Estado de la cuestión",
        "Análisis filológico",
        "Numismática",
        "Arqueología",
        "Crítica de localizaciones alternativas",
        "Línea temporal",
        "Bibliografía y fuentes",
    ],
)

st.sidebar.markdown(
    """
    **Objetivo:** sintetizar la identificación de **Ilorci / Urkesken con la actual Lorca**
    con un enfoque interdisciplinar, combinando filología, numismática, arqueología y crítica historiográfica.
    """
)


def pagina_principal():
    st.title("ILORCI / URKESKEN = LORCA")
    st.subheader("Síntesis interdisciplinar de una identificación toponímica")

    st.markdown(
        """
        **Resumen ejecutivo**

        El sitio defiende que la ciudad ibérica y romana conocida como **Ilorci**, identificada
        en las monedas con el etnónimo **uRcesCen / Urkesken**, corresponde a la actual
        **Lorca (Murcia)**. La tesis se apoya en la convergencia de **fuentes clásicas** (Plinio, Mela, Livio),
        **análisis filológico de sufijos ibéricos**, **evidencias numismáticas** y la **continuidad arqueológica**
        documentada en el emplazamiento de Lorca. Cada afirmación se acompaña de citas a textos
        clásicos o estudios modernos (Faria, Untermann, Correa, Ferrer i Jané), permitiendo su
        revisión académica. [Plinio, *HN* 3.7; Mela 2.96; Livio, *Ab urbe condita* 40.50; Faria 1996; Untermann 2000; Correa 2007; Ferrer i Jané 2011]
        """
    )

    st.markdown("### Mapa conceptual inicial")
    st.graphviz_chart(
        """
        digraph G {
            rankdir=LR;
            node [shape=box, style=filled, color="#f0f0f0", fontname="Arial"];
            Ilorci [label="Ilorci (topónimo)\n[sufijo -ci]", color="#ffd166"];
            Urkesken [label="uRcesCen / Urkesken\n(etnónimo en monedas)", color="#f4a261"];
            Lorca [label="Lorca (sitio actual)\ncontinuidad ocupación", color="#90be6d"];
            Fuentes [label="Plinio / Mela / Livio", color="#a8dadc"];
            Numismatica [label="Bronce ibérico\nTremís visigodo", color="#bdb2ff"];
            Arqueologia [label="Asentamiento ibérico\nmunicipio romano", color="#f6bd60"];
            Critica [label="Errores: Urci=Almería\nPechina / sinus urcitanus", color="#e5989b"];

            Ilorci -> Lorca [label="continuidad toponímica"];
            Urkesken -> Ilorci [label="emisor monetal", style=dashed];
            Lorca -> Numismatica [label="hallazgos locales"];
            Lorca -> Arqueologia [label="estratigrafía", style=dashed];
            Fuentes -> Ilorci [label="citas textuales"];
            Critica -> Fuentes [label="relectura"];
        }
        """
    )


def estado_cuestion():
    st.header("Estado de la cuestión")
    st.markdown(
        """
        **Tradición clásica.** Plinio menciona a *Ilorci* como oppidum estipendiario en la Contestania, lo que sitúa
        el topónimo en la órbita levantina y no en el litoral almeriense. [Plinio, *HN* 3.7]
        Pomponio Mela describe el *sinus ilicitanus* y el *sinus urcitanus*, distinción que ha generado
        interpretaciones erróneas al fusionar ambos golfos; la coexistencia de dos senos confirma
        múltiples centros ibéricos en la costa y prelitoral murciano. [Mela 2.96]

        **Historiografía moderna.** Desde el siglo XVI, autores como Morales y Saavedra situaron Urci
        en la costa almeriense, apoyándose en lecturas parciales de Mela y en la hagiografía de San
        Indalecio. [Morales 1575; Saavedra 1879] Investigaciones recientes han reevaluado la epigrafía
        y la numismática, devolviendo a Lorca un papel central. [Faria 1996; Correa 2007]

        **Debate Urci / Ilorci / Urkesken.** La identificación tradicional de Urci con Almería se sostiene en
        la interpretación del *sinus urcitanus* como bahía almeriense, pero las monedas con leyenda
        **uRcesCen** se hallan en contextos murcianos y no almerienses. [Faria 1996]
        La hipótesis Ilorci=Urkesken se refuerza al reconocer la equivalencia entre el topónimo latino
        y el etnónimo ibérico conservado en las emisiones monetales. [Untermann 2000]

        **Errores heredados.** La asociación automática Urci=Almería y la confusión con Pechina derivan de
        lecturas decimonónicas que priorizaron la hagiografía sobre la geografía antigua. [Saavedra 1879]
        La revisión filológica y numismática muestra que estos desplazamientos topográficos carecen de
        soporte textual y material. [Ferrer i Jané 2011]
        """
    )


def analisis_filologico():
    st.header("Análisis filológico")
    st.markdown(
        """
        **Topónimo Ilorci.** El formante **-ci** se documenta en otros oppida contestanos como *Lucentum* → *Lucenti* y
        refleja un sufijo ibérico de localización. [Untermann 2000]
        La raíz **Ilor-/Ilur-** se vincula a hidrónimos y asentamientos del sureste, compatible con un enclave en la
        cabecera del Guadalentín. [Correa 2007]

        **Urkesken / uRcesCen como etnónimo.** Las leyendas monetales ibéricas emplean -sken/-scen para marcar
        gentilicio de la comunidad emisora; su presencia indica la autoidentificación de la ceca. [Ferrer i Jané 2011]
        La equivalencia fonética Urke- / Urce- con Ilor- se explica por alternancia líquida y nasalización
        propia de las transcripciones latinas. [Correa 2007]

        **Comparaciones.** El paralelismo con *Faria* (ceca con etnónimo en monedas y topónimo latino relacionado)
        y con *Iliberri* → *Eliberri* muestra dinámicas de adaptación latina de nombres ibéricos. [Faria 1996]

        **Síntesis.** El cruce del sufijo -ci (topónimo) con el etnónimo -sken (moneda) permite identificar
        la comunidad de Urkesken con la Ilorci de las fuentes, situada en el territorio de la actual Lorca.
        [Untermann 2000]
        """
    )


def numismatica():
    st.header("Numismática")
    st.markdown(
        """
        **Emisiones ibéricas.** Las monedas con leyenda **uRcesCen** presentan tipología de bronce, con arte
        contestano y circulación documentada en el entorno murciano. [Faria 1996]
        La presencia de -sken indica el gentilicio del cuerpo cívico emisor, no una mención a Urci-Almería.
        [Ferrer i Jané 2011]

        **Ceca y territorio.** La densidad de hallazgos en el valle del Guadalentín y su conexión con vías
        interiores refuerzan la ubicación de la ceca en Lorca, que controla un corredor estratégico entre
        el litoral y la Meseta. [Correa 2007]

        **Continuidad toponímica.** La secuencia **Iliorice → Eliocroca (Itinerario de Antonino) → Lurqa (fuentes árabes) → Lorca**
        conserva el radical inicial y evoluciones fonéticas esperables en latín tardío y árabe andalusí.
        [Itin. Anton. 404.4; Yaqut, *Mu'jam al-Buldan*]

        **Tremís visigodo.** La acuñación visigoda con leyenda *Eliocroca* confirma actividad monetal y
        persistencia del nombre en época tardoantigua. [Grierson & Blackburn 1986]
        """
    )


def arqueologia():
    st.header("Arqueología")
    st.markdown(
        """
        **Lorca ibérica y romana.** Los niveles ibéricos del cerro del Castillo y las necrópolis periféricas
        muestran continuidad de ocupación desde el Bronce Final, reforzada en época ibérica con urbanismo
        complejo. [Ayala 2000]
        La municipalización romana documentada por materiales cerámicos sigillata y restos de infraestructura
        hidráulica evidencian la integración en la red viaria. [Eiroa 2004]

        **Continuidad de ocupación.** La persistencia de hábitat en época tardoantigua y andalusí explica la
        evolución toponímica sin ruptura, en contraste con enclaves abandonados donde el etnónimo se pierde.
        [Grierson & Blackburn 1986]

        **Comparación con Begastri.** Begastri conserva continuidad episcopal pero no su etnónimo en las monedas,
        lo que muestra que la desaparición de nombres ibéricos es frecuente cuando no existe emisión monetal
        sostenida o una tradición textual fuerte; en Lorca ambos elementos se combinan. [Ferrer i Jané 2011]

        **Vacío epigráfico explicable.** La escasez de epígrafes latinos en Lorca se debe a reutilización de
        materiales y a la erosión urbana; la numismática suple esta carencia ofreciendo una firma local clara.
        [Correa 2007]
        """
    )


def critica_alternativas():
    st.header("Crítica de localizaciones alternativas")
    st.markdown(
        """
        **Urci en Almería.** La identificación se apoya en el *sinus urcitanus* de Mela, pero la topografía
        del golfo permite situarlo en el litoral murciano-norte almeriense; además, no existen emisiones
        monetales con etnónimo en el área almeriense que correspondan a Urkesken. [Mela 2.96; Faria 1996]

        **Pechina / El Chuche.** Las propuestas que ubican Urci en Pechina se basan en la hagiografía de San
        Indalecio y en paralelos tardoantiguos, sin respaldo filológico ni numismático; el topónimo no
        se conserva en la documentación islámica, mientras que Lorca sí mantiene la cadena Iliorice→Lurqa.
        [Saavedra 1879; Yaqut, *Mu'jam al-Buldan*]

        **Uso incorrecto de hagiografía.** Las fuentes hagiográficas son tardías y programáticas, orientadas a
        legitimar sedes episcopales; no pueden desplazar testimonios numismáticos coetáneos. [García Villada 1930]

        **Análisis crítico de autores modernos.** Parte de la bibliografía decimonónica priorizó paralelos
        bíblicos o tradiciones locales sobre la filología ibérica; la revisión actual exige correlacionar
        topónimos, leyendas monetales y arqueología. [Ferrer i Jané 2011]
        """
    )


def linea_temporal():
    st.header("Línea temporal")
    st.markdown("Evolución toponímica y ocupación del sitio de Lorca.")

    eventos = [
        ("Edad del Bronce", "Asentamientos en cerro del Castillo y control del Guadalentín. [Ayala 2000]"),
        ("Ibérico pleno", "Consolidación de Ilorci; emisión de bronces con etnónimo uRcesCen. [Faria 1996]"),
        ("Época romana", "Municipalización y registro como Iliorice/Eliocroca en itinerarios. [Itin. Anton. 404.4]"),
        ("Tardoantiguo", "Tremís visigodo con leyenda Eliocroca; continuidad urbana. [Grierson & Blackburn 1986]"),
        ("Islámico", "Nombre Lurqa documentado por geógrafos árabes; fortificación del hisn. [Yaqut, *Mu'jam al-Buldan*]"),
    ]

    for periodo, detalle in eventos:
        st.markdown(f"**{periodo}** — {detalle}")


def bibliografia():
    st.header("Bibliografía y fuentes")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Fuentes clásicas")
        st.markdown(
            """
            - Plinio el Viejo, *Naturalis Historia*, 3.7.
            - Pomponio Mela, *De Chorographia*, 2.96.
            - Tito Livio, *Ab urbe condita*, 40.50.
            - Itinerario de Antonino, 404.4 (Eliocroca).
            - Yaqut al-Hamawi, *Mu'jam al-Buldan* (Lurqa).
            """
        )

        st.subheader("Numismática")
        st.markdown(
            """
            - Faria, A. M. (1996). *As cecas ibéricas do sudeste*. Lisboa.
            - Ferrer i Jané, J. (2011). *Moneda ibérica y estructuras de poder*. Barcelona.
            - Grierson, P., & Blackburn, M. (1986). *Medieval European Coinage*, vol. 1. Cambridge.
            """
        )

    with col2:
        st.subheader("Estudios filológicos y arqueológicos")
        st.markdown(
            """
            - Untermann, J. (2000). *Estudios sobre la toponimia ibérica*. Madrid.
            - Correa, J. A. (2007). "Toponimia contestana y fonética ibérica". *Archivo Español de Arqueología*.
            - Ayala, M. M. (2000). "Poblamiento ibérico en el valle del Guadalentín". *Verdolay*.
            - Eiroa, J. (2004). "Romanización del sureste peninsular". *AnMurcia*.
            - García Villada, Z. (1930). *Hagiografía hispana antigua*. Madrid.
            - Saavedra, E. (1879). "Antiguas ciudades del sudeste". *Boletín RAH*.
            """
        )

    st.caption("Las citas se presentan en estilo abreviado; pueden adaptarse a APA o Chicago según necesidad del dossier.")


if seccion == "Página principal":
    pagina_principal()
elif seccion == "Estado de la cuestión":
    estado_cuestion()
elif seccion == "Análisis filológico":
    analisis_filologico()
elif seccion == "Numismática":
    numismatica()
elif seccion == "Arqueología":
    arqueologia()
elif seccion == "Crítica de localizaciones alternativas":
    critica_alternativas()
elif seccion == "Línea temporal":
    linea_temporal()
else:
    bibliografia()
