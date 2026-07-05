# Especificação para Geração de Mapas Climáticos

## Estrutura

Cada mapa representa uma estação de um determinado clima.

Cada mapa é composto por:

* 19 hexágonos.
* Cada hexágono representa um fenômeno climático.
* Cada fenômeno possui:

  * `name`
  * `severity`
  * `evolutions`

Os 19 hexágonos formam um hexágono de profundidade 2.

---

# Numeração dos hexágonos

A numeração é fixa e deve ser preservada para permitir a geração da representação gráfica.

Critérios:

* inicia no hexágono mais à esquerda da linha superior;
* segue de cima para baixo;
* dentro de cada linha, da esquerda para a direita;
* o hexágono central possui índice **9**.

Índices válidos:

0 a 18.

---

# Severidade

Existem apenas três níveis.

## 0 — Normal

Representa o comportamento esperado para a estação.

Exemplos:

* Chuva
* Garoa
* Ensolarado e Quente
* Brisa
* Parcialmente Nublado

Deve representar a maioria dos hexágonos.

---

## 1 — Perigoso

Representa condições potencialmente perigosas.

Exemplos:

* Ondas de Calor
* Frio Extremo
* Vendaval
* Chuva Intensa
* Chuva Congelante
* Nevando Forte

Deve aparecer poucas vezes no mapa.

---

## 2 — Desastre

Representa eventos climáticos excepcionais.

Exemplos:

* Furacão
* Tempestade Tropical
* Nevasca
* Chuva Torrencial
* Temporal com Granizo

Normalmente apenas um ou poucos hexágonos.

---

# Evolução

Cada ocorrência possui sete possibilidades de evolução:

* permanecer no hexágono atual;
* seis hexágonos adjacentes.

Quando uma direção ultrapassar a borda do mapa, utiliza-se a conexão para o lado oposto (wrap-around).

---

# Pesos padrão

Na ausência de ajustes específicos, utilizar:

| Movimento         | Peso |
| ----------------- | ---: |
| Permanecer        |    2 |
| Superior esquerda |    2 |
| Superior direita  |    1 |
| Inferior esquerda |    2 |
| Inferior direita  |    1 |
| Superior          |    1 |
| Inferior          |    2 |

Esses pesos representam a tendência natural de persistência e evolução do clima.

---

# Bloqueios de evolução

Nem toda adjacência representa uma transição válida.

Quando uma evolução for proibida:

* o hexágono continua ocupando sua posição física;
* porém sua entrada na lista `evolutions` é substituída por outra ocorrência válida.

Assim:

* o mapa continua geometricamente correto;
* determinadas transições tornam-se impossíveis;
* a representação visual deixa explícitas essas restrições.

Exemplo:

```
A é adjacente a B

A → B proibido

evolutions:
- A
- A
- D
- C
- E
- F
- G
```

Neste exemplo, a direção correspondente a **B** foi substituída por **A**.

---

# Critérios de construção

Cada mapa deve possuir:

* um núcleo de condições típicas;
* regiões de transição gradual;
* poucos eventos severos;
* poucos eventos extremos.

Evitar saltos bruscos entre fenômenos incompatíveis.

Exemplo:

Frio Extremo → Ondas de Calor ❌

Preferir:

Frio Extremo

↓

Frio Seco

↓

Ameno

↓

Quente

---

# Diretrizes climáticas

## Equatorial

Predomínio:

* calor
* umidade
* chuva
* tempestades

Nunca incluir:

* neve
* geada
* frio extremo

---

## Tropical — Estação Seca

Predomínio:

* calor
* tempo seco
* céu limpo
* brisas

Pouca chuva.

---

## Tropical — Estação Chuvosa

Predomínio:

* calor
* chuva
* abafamento
* tempestades

---

## Árido

Predomínio:

* calor seco
* céu limpo
* vento
* poeira

Chuvas muito raras.

---

## Semiárido — Estação Seca

Semelhante ao Árido.

Adicionar pequena possibilidade de chuva.

---

## Semiárido — Estação Chuvosa

Misturar:

* calor
* chuva intensa
* vento

---

## Mediterrâneo — Verão

Predomínio:

* quente
* seco
* ensolarado

---

## Mediterrâneo — Inverno

Predomínio:

* ameno
* chuva
* neblina

---

## Temperado — Primavera

Grande variedade.

Misturar:

* chuva
* vento
* frio leve
* calor leve

---

## Temperado — Verão

Predomínio:

* calor
* pancadas de chuva
* tempestades ocasionais

---

## Temperado — Outono

Predomínio:

* vento
* chuva
* neblina
* resfriamento gradual

---

## Temperado — Inverno

Predomínio:

* frio
* neve
* geada

---

## Monções — Verão

Predomínio:

* chuva persistente
* tempestades
* alta umidade

---

## Monções — Inverno

Predomínio:

* seco
* fresco
* vento

---

## Subpolar — Verão

Predomínio:

* fresco
* chuva leve
* neblina

---

## Subpolar — Inverno

Predomínio:

* neve
* vento
* frio intenso

---

## Polar — Verão

Predomínio:

* frio
* neve leve
* neblina

Nunca utilizar calor.

---

## Polar — Inverno

Predomínio:

* frio extremo
* neve
* ventos intensos

Sem chuva líquida.

---

## Alpino — Verão

Predomínio:

* fresco
* chuva
* vento

Possibilidade de granizo e neve leve.

---

## Alpino — Inverno

Predomínio:

* neve
* frio extremo
* ventos fortes

Grande probabilidade de nevascas.


