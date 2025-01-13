region_insular = {"Nombre": "Islas Galápagos",
"Descripción": "Un archipiélago volcánico famoso por su biodiversidad única y su importancia en la teoría de la evolución de Charles Darwin.",
"Actividades": {"Snorkel", "buceo", "observación de tortugas gigantes", "senderismo", "avistamiento de aves"},
"Gastronomía": {"ceviche de camarón", "encebollado", "pescado fresco", "mariscos variados"},
"Ubicación": "Provincia de Galápagos, Ecuador"},

region_costa ={ 
{"Nombre": "Manta",
"Descripción": "Conocida como La Capital Mundial del Atún, Manta es una ciudad costera vibrante con hermosas playas y un puerto importante",
"Actividades": {"playa", "pesca", "observación de ballenas"},
"Gastronomía": {"ceviche de atún", "encocado", "mariscos frescos"},
"Ubicación": "Provincia de Manabí, Ecuador"},

{"Nombre": "Puerto López",
"Descripción":" Un pintoresco pueblo pesquero famoso por los avistamientos de ballenas jorobadas y su cercanía al Parque Nacional Machalilla",
"Actividades": {"Avistamiento de ballenas", "snorkel", "paseos en bote", "exploración del parque nacional"},
"Gastronomía": {"ceviche de camarón", "pescado frito", "mariscos frescos"," batidos de frutas tropicales"},
"Ubicación": "Provincia de Manabí, Ecuador"},

{"Nombres": "Montañita",
"Descripción": "Un popular destino de playa conocido por su ambiente relajado y vibrante, ideal para amantes del surf y la vida nocturna",
"Actividades": {"surf", "yoga", "caminatas por la playa", "fiestas nocturnas"},
"Gastronomía": {"ceviche", "tacos de pescado", "jugos naturales", "comida marítima"},
"Ubicación": "Provincia de Santa Elena, Ecuador"}},

region_sierra = {{"Nombre": "Mitad del Mundo",
"Descripción": "Un monumento que marca la ubicación exacta de la línea ecuatorial, con un museo y varias actividades interactivas",
"Actividades": {"visita al museo", "fotografías en la línea ecuatorial", "experimentos científicos", "compras de recuerdos"},
"Gastronomía": {"cuy asado", "fritada", "empanadas", "locro de papas"},
"Ubicación": "Ciudad de Quito, Provincia de Pichincha, Ecuador"},

{"Nombre": "Cuenca",
"Descripción":" Una ciudad colonial con una arquitectura impresionante, rica historia cultural y declarada Patrimonio de la Humanidad por la UNESCO",
"Actividades": {"Recorridos por el centro histórico", "visitas a iglesias y museos", "paseos por el río Tomebamba"},
"Gastronomía": {"Hornado", "mote pillo", "tamales", "llapingachos"},
"Ubicación": "Ciudad de Cuenca, Provincia de Azuay, Ecuador"},

{"Nombre":"Baños de Agua Santa",
"Descripción": "Conocido por sus aguas termales, impresionantes cascadas y una variedad de deportes de aventura",
"Actividades": {"rafting", "ciclismo de montaña", "relajación en aguas termales", "canopy", "puenting"},
"Gastronomía": {"melcocha"," tortillas de maíz", "cuy asado", "gallina de campo"},
"Ubicación": "Ciudad de Baños, Provincia de Tungurahua, Ecuador"}},


region_amazonica = {{"Nombre": "Parque Nacional Yasuní",
"Descripción": "El Parque Nacional Yasuní es una de las áreas protegidas más biodiversas del mundo, ubicada en el corazón de la selva amazónica ecuatoriana. Es hogar de numerosas especies de flora y fauna, muchas de las cuales son endémicas y algunas aún no descubiertas",
"Actividades": {"observación de vida silvestre", "caminatas por la selva", "visitas a comunidades indígenas", "navegación por ríos", "kayak", "rituales ancestrales de shamanismo"},
"Gastronomía": {"maito de pescado", "yuca frita", "chontacuros", "sopas tradicionales"},
"Ubicación": "Provincia de Pastaza y Orellana, Ecuador"},

{"Nombres": "Reserva de Producción Faunística Cuyabeno",
"Descripción": "Esta reserva es una de las áreas más biodiversas del mundo, famosa por sus hermosos paisajes de selva inundada, lagunas y ríos. Es un lugar ideal para los amantes de la naturaleza y la aventura",
"Actividades": {"observación de vida silvestre", "navegación en canoa por los ríos y lagunas", "pesca deportiva", "visitas a comunidades indígenas", "senderismo en la selva", "observación de aves"},
"Gastronomía": {"maito de pescado", "yuca frita", "chontacuros", "platos tradicionales de la región amazónica"},
"Ubicación": "Provincia de Sucumbíos, Ecuador"}}



print("Bienvenido, estos son los Lugares Turísticos del Ecuador, seleccione una opción")
opcion1 = print("1. Region Insular")
opcion2 = print("2. Region Costa") 
opcion3 = print("3. Region Sierra") 
opcion4 = print("4. Region Amazónica") 
opcion5 = print("5. Salir")


while True: 
    opcion = input("Selecciona una opción: ")
    if opcion == '1':
        print(f"Haz seleccionado la Region Insular")
        print(region_insular)
    elif opcion == '2':
        print("Haz seleccionado Region Costa")
        print(region_costa)
    elif opcion == '3':
        print("Haz seleccionado la Region Sierra")
        print(region_sierra)
    elif opcion == '4':
        print("Haz seleccionado la Region Amazónica")
        print(region_amazonica)
    elif opcion == '':
        print("Saliendo del programa...")
        break
