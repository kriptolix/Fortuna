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

summer = [
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

spring = [
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

winter = [
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

autumn = [
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

climate_names_list = [
    "Semi Arid: Dry Season",
    "Semi Arid: Wet Season"
    ]


semi_arid = [
    "High temperatures with distinct wet and dry seasons",
    "Biomes: Savannas, tropical grasslands.",
    "Examples: Indian Subcontinent, African savannas, Northern Australia."
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
