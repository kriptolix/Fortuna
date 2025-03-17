weather_events = [
    "Neblina",
    "Neblina fria",
    "Névoa densa",
    "Névoa fria",
    "Nuvem de poeira",
    "Frio Extremo",
    "Tempo ensolarado e limpo"
]

rain = [
    "Ensolarado",    
    "Parcialmente Nublado",
    "Nublado",
    ["Garoa", "morna"],
    ["Sereno","morno"],
    ["Chuva", "morna"],
    "Chuva torrencial",
    ["Tempestade", "tropical"]
]


fog = ["combina com "
    "Neblina",
    "Neblina fria",
    "Névoa densa",
    "Névoa fria",
    "Nuvem de poeira",
    ]

temp_humi = ["vento", "umidade", "precipitação"
             "Frio Extremo",
             "Frio",
             "Confortavel",
             "Calor",
             "Ondas de calor extremo",


             "Tempo frio e com vento",
             "Tempo frio e ensolarado",
             "Tempo frio e seco",
             "Tempo frio e úmido",
             "Tempo ensolarado e com vento",
             "Tempo ensolarado e fresco",
             "Tempo quente e abafado",
             "Tempo quente e com vento",
             "Tempo quente e seco",
             "Tempo úmido e fresco",
             ]

humidity = [
    "seco",
    "fresco"
    "úmido",
]

rain_events = [
    "Garoa",
    "Garoa morna",
    "Sereno",
    "Sereno morno",
    "Chuva",
    "Chuva morna",
    "Chuva com rajadas de vento",
    "Chuva torrencial",
    "Tempestade",
    "Tempestade tropical",
]

snow_events = [
    "Geada",
    "Nevando leve",
    "Nevando e com vento",
    "Nevando forte",
    "Chuva de granizo",
    "Neve granizada",
    "Neve semi derretida",
    "Chuva com neve",
    "Nevasca",
]


cloud_events = [
    "Nublado e com vento",
    "Nublado e congelante",
    "Nublado e fresco",
    "Nublado e frio",
    "Nublado e gelado",
    "Nublado e morno",
    "Nublado e quente",
    "Nublado e úmido",
    "Parcialmente nublado e fresco",
    "Parcialmente nublado e fresco",
]


wind_events = [
    "Parado"
    "Brisa"
    "Brisa morna",
    "Vento frio",
    "Vento gelado",
    "Vento quente e úmido",
    "Rajadas de vento esporádicas",
    "Ventos fortes",
    "vendaval"
]

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
