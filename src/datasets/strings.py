rain = [
    "Garoa", "Garoa Morna", "Sereno", "Sereno Morno", "Chuva",
    "Chuva Morna", "Chuva Intensa", "Chuva torrencial", "Chuva com Vento",
    "Tempestade", "Tesmpestade Tropical", "Chuva com Neve",
    "Chuva de Granizo", "Chuva Congelante", "Chuva e Neblina",
]

snow = [
    "Geada", "Nevando Leve", "Nevando Forte",
    "Nevando e com Vento", "Nevasca", "Chuva com Neve"
]

wind = [
    "Brisa", "Brisa Morna", "Vento Frio",
    "Ventos Fortes", "Vendaval", "Rajadas de Vento"
]

cloud = [
    "Nublado e com Vento", "Nublado e Congelante",
    "Nublado e Fresco", "Nublado e Frio",
    "Nublado e Quente", "Nublado e Úmido",
    "Parcialmente nublado",
]

termic = [
    "Ensolarado e Frio",  "Ensolarado e Fresco", "Ensolarado e com Vento",
    "Ensolarado e Quente", "Quente e com Vento", "Quente e Seco",
    "Quente e Úmido", "Ondas de Calor Extremo", "Frio e com Vento",
    "Frio e Seco",  "Frio e Úmido", "Frio Extremo",
]

fog = [
    "Neblina", "Névoa Densa",
    "Névoa Esparsa", "Nuvem de Poeira",
]

weather_names_list = rain + snow + wind + cloud + termic + fog

climate_names_list = [
    "Equatorial: No seasons",
    "Tropical: Dry Season",
    "Tropical: Rainy Season",
    "Arid: No seasons",
    "Semi Arid: Dry Season",
    "Semi Arid: Rainy Season",
    "Mediterranean: Summer",
    "Mediterranean: Winter",
    "Temperate: Spring",
    "Temperate: Summer",
    "Temperate: Autumn",
    "Temperate: Winter",
    "Monsoon: Summer",
    "Monsoon: Winter",
    "Sub Polar: Summer",
    "Sub Polar: Winter",
    "Polar: Summer",
    "Polar: Winter",
    "Alpine: Summer",
    "Alpine: Winter"
]

season_tips = [
    ["There are no distinct seasons, weather conditions remain almost constant"
     " throughout the year. Average temperatures range from 25°C to 28°C, "
     "with high humidity (above 85%) and frequent rainfall. Precipitation is"
     " evenly distributed, varying between 2000 mm and 3000 mm annually.",
     "Biomes: Rainforests.",
     "Examples: Congo Basin (Africa), Borneo (Indonesia), Amazon Basin."
     ],
    ["Dry season is defined by minimal rainfall (less than 100 mm), "
     "lower humidity, and clear skies. Temperatures range from 24°C to 30°C.",
     "Rainy season is characterized by average temperatures of 25°C to "
     "30°C, high humidity (above 80%), and intense rainfall, often "
     "exceeding 2000 mm. Thunderstorms may occur.",
     "Biomes: Savannas, tropical grasslands.",
     "Examples: Indian Subcontinent, African savannas, Northern Australia."
     ],
    ["There are no distinct seasons, little to no precipitation "
     "throughout the year (less than 250 mm). Temperatures may "
     "exceed 40°C during the day while dropping significantly at night"
     ". Low humidity (below 30%) is a constant feature.",
     "Biomes: Deserts.",
     "Examples: Sahara Desert (Africa), Atacama Desert (Chile), "
     "Mojave Desert (USA)."
     ],
    ["Dry season dominates most of the year, with high daytime temperatures"
     " (30°C to 40°C) and cooler nights. Humidity is low, and the"
     " soil remains predominantly dry.",
     "Rainy season is brief, with scattered rains (250 mm to 500 mm annually),"
     " high evaporation, and average temperatures between 25°C and 35°C.",
     "Biomes: Steppe, shrublands.",
     "Examples: Great Plains (USA), Central Asia, parts of Northern Mexico."
     ],
    ["Summer is hot and dry, with temperatures ranging from 25°C to 35°C,"
     " low humidity, and almost no precipitation.",
     "Winter has moderate rainfall (300 mm to 600 mm annually), temperatures"
     " between 10°C and 15°C, and higher humidity.",
     "Biomes: Mediterranean vegetation (maquis, garrigue).",
     "Examples: Southern Italy, coastal California (USA), "
     "South Africa's Cape Region."
     ],
    ["Spring has mild temperatures (10°C to 20°C), light rainfall,"
     " and active plant growth.",
     "Summer si warm, with temperatures between 20°C and 30°C, "
     "high humidity, and the possibility of quick and intense showers.",
     "Autumn shows gradually cooling temperatures (10°C to 20°C), fewer "
     "rainfalls, and falling leaves.",
     "Winter is cold, with negative temperatures in some regions "
     "(-5°C to 10°C), potential snowfall, and low precipitation.",
     "Biomes: Temperate forests, grasslands.",
     "Examples: Central Europe, Eastern USA, Eastern China."
     ],
    ["Summer is hot and humid, with temperatures between 25°C and"
     " 35°C and concentrated rainfall (above 1000 mm).",
     "Winter has mild temperatures (10°C to 15°C), lower precipitation,"
     " and more moderate humidity.",
     "Biomes: Subtropical forests.",
     "Examples: Southeastern USA, Southeastern China, parts of Argentina."
     ],
    ["Summer is short and cool, with temperatures between 10°C and 15°C,"
     " low humidity, and moderate rainfall.",
     "Winter is Long and harsh, with temperatures below -10°C, "
     "frequent snowfall, and low humidity.",
     "Biomes: Taiga, boreal forests.",
     "Examples: Siberia (Russia), Alaska (USA), Northern Canada.",
     ],
    ["Summer has temperatures slightly above 0°C (0°C to 10°C),"
     " almost no precipitation, and long periods of sunlight.",
     "Winter is extremely cold (below -50°C), prolonged polar "
     "nights, snowfall, and very low humidity.",
     "Biomes: Tundra, glacial regions.",
     "Examples: Antarctica, Greenland, Arctic regions."
     ],
    ["Summer is cool and short, with temperatures between 10°C"
     " and 20°C, increased rainfall, and chilly nights.",
     "Winter is cold, with temperatures often below 0°C, "
     "predominant snowfall, and low humidity.",
     "Biomes: Alpine vegetation.",
     "Examples: Andes (South America), Himalayas (Asia), Alps (Europe)."
     ]
]

semi_arid_dry = [
    [21, 0, 3, 0, 0, 0, 0, 0, 0],
    [26, 0, 3, 0, 1, 0, 0, 0, 0],
    [38, 0, 6, 0, 0, 1, 0, 0, 0],
    [24, 0, 3, 1, 0, 0, 0, 0, 0],
    [35, 0, 6, 0, 0, 0, 0, 0, 0],
    [22, 0, 6, 0, 0, 0, 0, 0, 0],
    [40, 1, 7, 0, 0, 1, 1, 0, 0],
    [27, 0, 5, 1, 0, 0, 0, 0, 0],
    [33, 0, 5, 0, 0, 0, 0, 0, 0],
    [37, 0, 6, 0, 0, 0, 0, 0, 0],
    [39, 1, 7, 0, 0, 0, 0, 0, 0],
    [49, 1, 7, 0, 0, 1, 1, 0, 0],
    [29, 0, 5, 1, 0, 0, 0, 0, 0],
    [32, 0, 5, 0, 0, 0, 0, 0, 0],
    [31, 0, 5, 0, 0, 0, 0, 0, 0],
    [41, 2, 7, 0, 0, 0, 1, 1, 1],
    [8, 0, 2, 0, 0, 0, 0, 0, 1],
    [5, 0, 1, 0, 0, 0, 0, 0, 0],
    [3, 0, 1, 0, 0, 1, 0, 0, 1]
]

temperate_summer = [
    ["Chuva", 0, 0, 0, 0],
    ["Garoa morna", 0, 0, 0, 0],
    ["Tempo quente e abafado", 1, 0, 0, 5],
    ["Chuva forte", 1, 0, 0, 1],
    ["Sereno morno", 0, 0, 0, 0],
    ["Nublado e quente", 0, 0, 0, 0],
    ["Quente e com vento", 1, 0, 0, 4],
    ["Chuva torrencial!", 2, 0, 0, 1],
    ["Nublado e humido", 0, 0, 0, 0],
    ["Agradavelmente morno", 0, 0, 0, 0],
    ["Quente e seco", 1, 0, 0, 0],
    ["Seco,com ondas de calor", 2, 0, 0, 4],
    ["Tempestade!", 2, 0, 0, 1],
    ["Nublado e com vento", 0, 0, 0, 0],
    ["Brisa morna", 0, 0, 0, 0],
    ["Tempo ensolarado e claro", 0, 0, 0, 4],
    ["Vento forte!", 1, 0, 0, 2],
    ["parcialmente nublado e ameno", 0, 0, 0, 0],
    ["tempo limpo e ameno", 0, 0, 0, 0],
]

temperate_spring = [
    ["garoa fria", 0, 0, 0, 0],
    ["quente e humido", 0, 0, 0, 6],
    ["quente e seco", 1, 0, 0, 5],
    ["chuva leve", 0, 0, 0, 1],
    ["umido e ameno", 1, 0, 0, 5],
    ["nublado e quente", 0, 0, 0, 0],
    ["ar cheio de polem", 1, 0, 4, 5],
    ["chuva forte", 1, 0, 0, 1],
    ["granizo pequeno", 1, 0, 0, 1],
    ["tempo claro e ameno", 1, 0, 0, 0],
    ["ensolarado e claro", 1, 0, 0, 0],
    ["agradavelmente morno", 1, 0, 0, 4],
    ["chuva com neve", 1, 0, 0, 0],
    ["chuva de granizo", 1, 0, 0, 0],
    ["nevoa fria", 1, 0, 0, 0],
    ["frio e seco", 0, 0, 0, 3],
    ["nevando e com vento", 0, 0, 0, 2],
    ["nevando forte", 0, 0, 0, 2],
    ["nevando leve", 0, 0, 0, 1]
]

temperate_winter = [
    ["frio e claro", 0, 0, 0, 0],
    ["chuva de granizo", 1, 0, 0, 0],
    ["nevasca", 2, 0, 0, 5],
    ["nublado e ameno", 0, 0, 0, 0],
    ["claro e com vento", 0, 0, 0, 0],
    ["chuva com neve", 1, 0, 0, 0],
    ["nevando e com vento", 1, 0, 0, 0],
    ["ensolarado e ameno", 0, 0, 0, 0],
    ["nevoa fria", 0, 0, 0, 0],
    ["frio e humido", 0, 0, 0, 0],
    ["chuva com neve", 1, 0, 0, 0],
    ["nevando leve", 1, 0, 0, 4],
    ["garoa leve", 0, 0, 0, 0],
    ["sereno frio", 1, 0, 0, 0],
    ["nublado e frio", 0, 0, 0, 0],
    ["chuva de granizo", 0, 0, 0, 0],
    ["chuva forte", 1, 0, 0, 2],
    ["ventos gelados", 0, 0, 0, 0],
    ["nublado e congelante", 0, 0, 0, 0],
]

temperate_autumn = [
    ["ensolarado e ameno", 0, 0, 0, 1],
    ["garoa", 0, 0, 0, 0],
    ["tempestade", 2, 0, 0, 4],
    ["agradavelmente morno", 0, 0, 0, 0],
    ["parcialmente nublado", 0, 0, 0, 0],
    ["rajadas de chuva e vento", 1, 0, 0, 0],
    ["chuva pesada", 1, 0, 0, 0],
    "ventos esporadicos!",
    "neblina fria",
    "ensolarado e claro",
    "nublado e congelante",
    "ventos frios",
    "ensolarado e ameno",
    "nublado e ameno",
    "nublado e humido",
    "nevoa densa!",
    "garoa",
    "chuva e vento",
    "chuva e neblina!",
    "limpo e com vento",
    "tempestade!"
]
