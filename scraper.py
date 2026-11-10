#!/usr/bin/env python3
"""
MCU Data Scraper - Universo Cinematográfico Marvel
Coleta capas em alta resolução (IMDb), trailers oficiais dublados/legendados (YouTube)
e consolida com sinopses sem spoiler em português e ordens cronológica e de lançamento.
"""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

# Base catalog with metadata and spoiler-free synopsis in Portuguese
MCU_CATALOG = [
    # FASE 1 - A Saga do Infinito
    {
        "id": "ca1",
        "title": "Capitão América: O Primeiro Vingador",
        "original_title": "Captain America: The First Avenger",
        "year": 2011,
        "phase": 1,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 5,
        "chronoOrder": 1,
        "chronoDetail": "Década de 1940 (Segunda Guerra Mundial)",
        "synopsis": "Durante a Segunda Guerra Mundial, o jovem franzino Steve Rogers se voluntaria para um experimento militar secreto que o transforma no primeiro supersoldado do mundo, iniciando sua luta contra a organização nazista Hydra liderada pelo terrível Caveira Vermelha.",
        "search_imdb": "Captain America: The First Avenger 2011",
        "search_yt": "Marvel Brasil trailer oficial Capitão América O Primeiro Vingador"
    },
    {
        "id": "cm",
        "title": "Capitã Marvel",
        "original_title": "Captain Marvel",
        "year": 2019,
        "phase": 3,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 21,
        "chronoOrder": 2,
        "chronoDetail": "Ano de 1995",
        "synopsis": "Na década de 1990, Carol Danvers é uma nobre guerreira alienígena que começa a ter flashes do seu passado na Terra. Ao cair no planeta, ela se alia ao jovem agente Nick Fury para desvendar sua verdadeira identidade em meio a uma guerra intergaláctica entre duas raças alienígenas.",
        "search_imdb": "Captain Marvel 2019",
        "search_yt": "Marvel Brasil trailer oficial Capitã Marvel"
    },
    {
        "id": "im1",
        "title": "Homem de Ferro",
        "original_title": "Iron Man",
        "year": 2008,
        "phase": 1,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 1,
        "chronoOrder": 3,
        "chronoDetail": "Ano de 2008",
        "synopsis": "O bilionário industrial e gênio inventor Tony Stark é capturado por terroristas e gravemente ferido. Usando sua inteligência, constrói uma armadura de alta tecnologia para escapar do cativeiro e decide usar sua criação para combater o crime e o tráfico de armas como o Homem de Ferro.",
        "search_imdb": "Iron Man 2008",
        "search_yt": "Marvel Brasil trailer Homem de Ferro 2008"
    },
    {
        "id": "im2",
        "title": "Homem de Ferro 2",
        "original_title": "Iron Man 2",
        "year": 2010,
        "phase": 1,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 3,
        "chronoOrder": 4,
        "chronoDetail": "Ano de 2010",
        "synopsis": "Com sua identidade de super-herói revelada mundialmente, Tony Stark sofre pressões do governo e de rivais corporativos para entregar sua tecnologia, enquanto sua própria saúde se deteriora e um cientista russo vingativo planeja sua destruição.",
        "search_imdb": "Iron Man 2 2010",
        "search_yt": "Marvel Brasil trailer Homem de Ferro 2"
    },
    {
        "id": "hulk",
        "title": "O Incrível Hulk",
        "original_title": "The Incredible Hulk",
        "year": 2008,
        "phase": 1,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 2,
        "chronoOrder": 5,
        "chronoDetail": "Ano de 2010 (paralelo a HF2)",
        "synopsis": "O cientista Bruce Banner vive foragido pelo mundo em busca de uma cura para a radiação gama em suas células, que o transforma em um monstro verde incontrolável quando irritado, enquanto o exército norte-americano tenta capturá-lo para transformar seu poder em arma militar.",
        "search_imdb": "The Incredible Hulk 2008",
        "search_yt": "O Incrível Hulk 2008 trailer oficial dublado"
    },
    {
        "id": "thor1",
        "title": "Thor",
        "original_title": "Thor",
        "year": 2011,
        "phase": 1,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 4,
        "chronoOrder": 6,
        "chronoDetail": "Ano de 2010",
        "synopsis": "Após reacender imprudentemente uma guerra ancestral, o guerreiro nórdico Thor é despojado de seus poderes por seu pai Odin e banido para a Terra, onde precisa aprender o verdadeiro valor da humildade e provar que é digno de empunhar novamente o martelo Mjölnir.",
        "search_imdb": "Thor 2011",
        "search_yt": "Marvel Brasil trailer oficial Thor 2011"
    },
    {
        "id": "av1",
        "title": "Os Vingadores",
        "original_title": "The Avengers",
        "year": 2012,
        "phase": 1,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 6,
        "chronoOrder": 7,
        "chronoDetail": "Ano de 2012 (Batalha de NY)",
        "synopsis": "Quando o deus da trapaça Loki invade a Terra com um exército alienígena Chitauri para se apossar do Tesseract, Nick Fury recruta Homem de Ferro, Capitão América, Thor, Hulk, Viúva Negra e Gavião Arqueiro para formarem a iniciativa Vingadores.",
        "search_imdb": "The Avengers 2012",
        "search_yt": "Marvel Brasil trailer oficial Os Vingadores 2012"
    },

    # FASE 2 - A Saga do Infinito
    {
        "id": "im3",
        "title": "Homem de Ferro 3",
        "original_title": "Iron Man 3",
        "year": 2013,
        "phase": 2,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 7,
        "chronoOrder": 8,
        "chronoDetail": "Natal de 2012 / início de 2013",
        "synopsis": "Atormentado por traumas e ataques de pânico após a batalha de Nova York, Tony Stark vê seu mundo pessoal desmoronar após um ataque terrorista atribuído ao misterioso Mandarim, tendo que contar apenas com sua engenhosidade para proteger quem ama.",
        "search_imdb": "Iron Man 3 2013",
        "search_yt": "Marvel Brasil trailer oficial Homem de Ferro 3"
    },
    {
        "id": "aos_s1",
        "title": "Agents of S.H.I.E.L.D. (Temp 1 - Ep 1 a 16)",
        "original_title": "Agents of S.H.I.E.L.D.",
        "year": 2013,
        "phase": 2,
        "saga": "A Saga do Infinito",
        "type": "series",
        "releaseOrder": 7.1,
        "chronoOrder": 8.5,
        "chronoDetail": "Pré-Soldado Invernal",
        "synopsis": "O agente Phil Coulson comanda uma equipe de elite de agentes especiais para investigar ocorrências inexplicadas e novos super-humanos ao redor do globo, atuando nas sombras do universo pós-Batalha de Nova York.",
        "search_imdb": "Agents of S.H.I.E.L.D.",
        "search_yt": "Marvel Agents of SHIELD trailer dublado oficial"
    },
    {
        "id": "thor2",
        "title": "Thor: O Mundo Sombrio",
        "original_title": "Thor: The Dark World",
        "year": 2013,
        "phase": 2,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 8,
        "chronoOrder": 9,
        "chronoDetail": "Ano de 2013",
        "synopsis": "Uma antiga raça de Elfos Negros liderada por Malekith retorna para mergulhar o cosmos em trevas através do poder misterioso do Éter. Para salvar os Nove Reinos e Jane Foster, Thor é obrigado a formar uma perigosa aliança com seu irmão aprisionado Loki.",
        "search_imdb": "Thor: The Dark World 2013",
        "search_yt": "Marvel Brasil trailer oficial Thor O Mundo Sombrio"
    },
    {
        "id": "ca2",
        "title": "Capitão América: O Soldado Invernal",
        "original_title": "Captain America: The Winter Soldier",
        "year": 2014,
        "phase": 2,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 9,
        "chronoOrder": 10,
        "chronoDetail": "Ano de 2014",
        "synopsis": "Trabalhando para a S.H.I.E.L.D. em Washington, Steve Rogers e Natasha Romanoff desvendam uma perigosa conspiração enraizada no coração da agência, enquanto enfrentam um assassino letal de identidade oculta conhecido como Soldado Invernal.",
        "search_imdb": "Captain America: The Winter Soldier 2014",
        "search_yt": "Marvel Brasil trailer oficial Capitão América O Soldado Invernal"
    },
    {
        "id": "aos_s1_end",
        "title": "Agents of S.H.I.E.L.D. (Temp 1 - Ep 17 em diante)",
        "original_title": "Agents of S.H.I.E.L.D.",
        "year": 2014,
        "phase": 2,
        "saga": "A Saga do Infinito",
        "type": "series",
        "releaseOrder": 9.1,
        "chronoOrder": 10.5,
        "chronoDetail": "Repercussão da queda da S.H.I.E.L.D.",
        "synopsis": "Em choque com as revelações e o colapso interno da S.H.I.E.L.D. mostrados em O Soldado Invernal, Phil Coulson e sua equipe precisam lutar contra traidores internos e sobreviver em um mundo onde não sabem em quem confiar.",
        "search_imdb": "Agents of S.H.I.E.L.D.",
        "search_yt": "Marvel Agents of SHIELD trailer"
    },
    {
        "id": "gotg1",
        "title": "Guardiões da Galáxia",
        "original_title": "Guardians of the Galaxy",
        "year": 2014,
        "phase": 2,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 10,
        "chronoOrder": 11,
        "chronoDetail": "Ano de 2014",
        "synopsis": "O aventureiro cósmico Peter Quill rouba uma esfera cobiçada pelo fanático Kree Ronan. Caçado pela galáxia, Quill é forçado a se aliar a quatro desajustados improváveis: Gamora, Drax, Rocket e Groot, formando os Guardiões da Galáxia.",
        "search_imdb": "Guardians of the Galaxy 2014",
        "search_yt": "Marvel Brasil trailer oficial Guardiões da Galáxia"
    },
    {
        "id": "gotg2",
        "title": "Guardiões da Galáxia Vol. 2",
        "original_title": "Guardians of the Galaxy Vol. 2",
        "year": 2017,
        "phase": 3,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 15,
        "chronoOrder": 12,
        "chronoDetail": "Poucos meses após Guardiões 1",
        "synopsis": "Os Guardiões viajam pelo cosmos como protetores contratados enquanto lidam com rivalidades familiares e desvendam a verdadeira ascendência e os segredos do pai biológico de Peter Quill, o misterioso Ego.",
        "search_imdb": "Guardians of the Galaxy Vol. 2 2017",
        "search_yt": "Marvel Brasil trailer oficial Guardiões da Galáxia Vol 2"
    },
    {
        "id": "daredevil_s1",
        "title": "Demolidor (Temporada 1)",
        "original_title": "Daredevil",
        "year": 2015,
        "phase": 2,
        "saga": "A Saga do Infinito",
        "type": "series",
        "releaseOrder": 10.5,
        "chronoOrder": 12.5,
        "chronoDetail": "Pós-Vingadores 1 em Hell's Kitchen",
        "synopsis": "Cego na infância e com os demais sentidos ampliados sobre-humanamente, o advogado Matt Murdock luta contra a corrupção e o crime nas ruas de Hell's Kitchen, Nova York, desafiando a ascensão do império sombrio de Wilson Fisk.",
        "search_imdb": "Daredevil 2015",
        "search_yt": "Demolidor trailer oficial Netflix dublado"
    },
    {
        "id": "av2",
        "title": "Vingadores: Era de Ultron",
        "original_title": "Avengers: Age of Ultron",
        "year": 2015,
        "phase": 2,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 11,
        "chronoOrder": 13,
        "chronoDetail": "Ano de 2015",
        "synopsis": "Ao tentar reativar um programa de manutenção da paz global, Tony Stark cria involuntariamente Ultron, uma inteligência artificial que chega à conclusão de que a única salvação para a Terra é extinguir a raça humana.",
        "search_imdb": "Avengers: Age of Ultron 2015",
        "search_yt": "Marvel Brasil trailer oficial Vingadores Era de Ultron"
    },
    {
        "id": "ant1",
        "title": "Homem-Formiga",
        "original_title": "Ant-Man",
        "year": 2015,
        "phase": 2,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 12,
        "chronoOrder": 14,
        "chronoDetail": "Ano de 2015",
        "synopsis": "O trapaceiro Scott Lang recebe a chance de se redimir quando o Dr. Hank Pym o convida a vestir um traje extraordinário capaz de reduzir seu tamanho e multiplicar sua força, preparando um roubo audacioso para salvar a tecnologia do cientista.",
        "search_imdb": "Ant-Man 2015",
        "search_yt": "Marvel Brasil trailer oficial Homem-Formiga"
    },

    # FASE 3 - A Saga do Infinito
    {
        "id": "ca3",
        "title": "Capitão América: Guerra Civil",
        "original_title": "Captain America: Civil War",
        "year": 2016,
        "phase": 3,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 13,
        "chronoOrder": 15,
        "chronoDetail": "Ano de 2016",
        "synopsis": "A criação do Tratado de Sokovia para regulamentar os heróis gera uma cisão profunda entre os Vingadores: Tony Stark apoia a vigilância política, enquanto Steve Rogers rejeita o controle de governos sobre suas ações.",
        "search_imdb": "Captain America: Civil War 2016",
        "search_yt": "Marvel Brasil trailer oficial Capitão América Guerra Civil"
    },
    {
        "id": "bw",
        "title": "Viúva Negra",
        "original_title": "Black Widow",
        "year": 2021,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "movie",
        "releaseOrder": 24,
        "chronoOrder": 16,
        "chronoDetail": "Logo após Guerra Civil (Cuidado com pós-créditos!)",
        "synopsis": "Fugitiva internacional após os acontecimentos de Guerra Civil, Natasha Romanoff precisa encarar as sombras e os laços rompidos de seu passado espião para desmantelar a Sala Vermelha antes que outras agentes sejam escravizadas.",
        "search_imdb": "Black Widow 2021",
        "search_yt": "Marvel Brasil trailer oficial Viúva Negra"
    },
    {
        "id": "bp",
        "title": "Pantera Negra",
        "original_title": "Black Panther",
        "year": 2018,
        "phase": 3,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 18,
        "chronoOrder": 17,
        "chronoDetail": "Logo após Guerra Civil",
        "synopsis": "Após a morte de seu pai, o príncipe T'Challa retorna para assumir a coroa e liderar a nação secreta de Wakanda como o Pantera Negra, mas tem sua liderança colocada em xeque por um rival que deseja expor as armas do país ao mundo.",
        "search_imdb": "Black Panther 2018",
        "search_yt": "Marvel Brasil trailer oficial Pantera Negra"
    },
    {
        "id": "sm1",
        "title": "Homem-Aranha: De Volta ao Lar",
        "original_title": "Spider-Man: Homecoming",
        "year": 2017,
        "phase": 3,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 16,
        "chronoOrder": 18,
        "chronoDetail": "Meses após Guerra Civil",
        "synopsis": "Empolgado após sua aventura ao lado dos Vingadores, o jovem Peter Parker tenta conciliar a rotina colegial no Queens com o combate a criminosos locais, chamando a atenção do perigoso contrabandista de armas Abutre.",
        "search_imdb": "Spider-Man: Homecoming 2017",
        "search_yt": "Marvel Brasil trailer oficial Homem-Aranha De Volta ao Lar"
    },
    {
        "id": "ds1",
        "title": "Doutor Estranho",
        "original_title": "Doctor Strange",
        "year": 2016,
        "phase": 3,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 14,
        "chronoOrder": 19,
        "chronoDetail": "Anos 2016 a 2017",
        "synopsis": "Depois que um terrível acidente de trânsito encerra sua carreira médica, o arrogante cirurgião Stephen Strange gasta tudo o que tem em busca de cura no Kamar-Taj, onde é apresentado ao mundo dos magos e das dimensões místicas.",
        "search_imdb": "Doctor Strange 2016",
        "search_yt": "Marvel Brasil trailer oficial Doutor Estranho"
    },
    {
        "id": "thor3",
        "title": "Thor: Ragnarok",
        "original_title": "Thor: Ragnarok",
        "year": 2017,
        "phase": 3,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 17,
        "chronoOrder": 20,
        "chronoDetail": "Ano de 2017",
        "synopsis": "Desprovido de seu martelo e exilado na arena de gladiadores do planeta Sakaar, Thor precisa vencer uma luta épica contra seu antigo companheiro Hulk para regressar a Asgard a tempo de conter a impiedosa deusa Hela.",
        "search_imdb": "Thor: Ragnarok 2017",
        "search_yt": "Marvel Brasil trailer oficial Thor Ragnarok"
    },
    {
        "id": "ant2",
        "title": "Homem-Formiga e a Vespa",
        "original_title": "Ant-Man and the Wasp",
        "year": 2018,
        "phase": 3,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 20,
        "chronoOrder": 21,
        "chronoDetail": "Paralelo a Guerra Infinita",
        "synopsis": "Cumprindo prisão domiciliar após Guerra Civil, Scott Lang é procurado por Hope van Dyne e Hank Pym para uma missão científica de resgate através do misterioso Reino Quântico enquanto são caçados por uma nova ameaça espectral.",
        "search_imdb": "Ant-Man and the Wasp 2018",
        "search_yt": "Marvel Brasil trailer oficial Homem-Formiga e a Vespa"
    },
    {
        "id": "av3",
        "title": "Vingadores: Guerra Infinita",
        "original_title": "Avengers: Infinity War",
        "year": 2018,
        "phase": 3,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 19,
        "chronoOrder": 22,
        "chronoDetail": "Ano de 2018",
        "synopsis": "O temido guerreiro cósmico Thanos inicia uma investida implacável para recolher as seis Joias do Infinito e eliminar metade de todas as vidas do universo, obrigando os Vingadores e Guardiões da Galáxia a lutarem em várias frentes.",
        "search_imdb": "Avengers: Infinity War 2018",
        "search_yt": "Marvel Brasil trailer oficial Vingadores Guerra Infinita"
    },
    {
        "id": "av4",
        "title": "Vingadores: Ultimato",
        "original_title": "Avengers: Endgame",
        "year": 2019,
        "phase": 3,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 22,
        "chronoOrder": 23,
        "chronoDetail": "Anos 2018 a 2023",
        "synopsis": "Cinco anos após a tragédia desencadeada por Thanos, os heróis remanescentes unem forças para elaborar um plano arriscado que envolve viagens no tempo, decididos a desfazer a dizimação cósmica e restaurar seus entes queridos.",
        "search_imdb": "Avengers: Endgame 2019",
        "search_yt": "Marvel Brasil trailer oficial Vingadores Ultimato"
    },
    {
        "id": "sm2",
        "title": "Homem-Aranha: Longe de Casa",
        "original_title": "Spider-Man: Far From Home",
        "year": 2019,
        "phase": 3,
        "saga": "A Saga do Infinito",
        "type": "movie",
        "releaseOrder": 23,
        "chronoOrder": 28,
        "chronoDetail": "Ano de 2024 (Verão)",
        "synopsis": "Ainda sentindo o peso da perda de Tony Stark, Peter Parker viaja para uma excursão escolar pela Europa, mas é recrutado por Nick Fury para combater monstros elementais ao lado do enigmático herói Mysterio.",
        "search_imdb": "Spider-Man: Far From Home 2019",
        "search_yt": "Marvel Brasil trailer oficial Homem-Aranha Longe de Casa"
    },

    # FASE 4 - A Saga do Multiverso
    {
        "id": "loki_s1",
        "title": "Loki (Temporadas 1 & 2)",
        "original_title": "Loki",
        "year": 2021,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "series",
        "releaseOrder": 24.5,
        "chronoOrder": 23.5,
        "chronoDetail": "Fora do fluxo normal do tempo (AVT)",
        "synopsis": "Ao usar o Tesseract para escapar em Ultimato, uma versão alternativa de Loki é capturada pela Autoridade de Variância Temporal (AVT) e obrigado a consertar linhas temporais corrompidas para impedir o colapso do multiverso.",
        "search_imdb": "Loki 2021",
        "search_yt": "Marvel Brasil trailer oficial Loki série"
    },
    {
        "id": "whatif",
        "title": "What If...? (Temporadas 1 a 3)",
        "original_title": "What If...?",
        "year": 2021,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "series",
        "releaseOrder": 25.5,
        "chronoOrder": 23.6,
        "chronoDetail": "Multiverso alternativo",
        "synopsis": "Guiados pela narração do onisciente Vigia, testemunhamos eventos cruciais do Universo Cinematográfico Marvel se desenrolarem sob decisões e caminhos totalmente diferentes, explorando o potencial infinito do multiverso.",
        "search_imdb": "What If...? 2021",
        "search_yt": "Marvel Brasil trailer oficial What If série"
    },
    {
        "id": "wandavision",
        "title": "WandaVision",
        "original_title": "WandaVision",
        "year": 2021,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "series",
        "releaseOrder": 23.2,
        "chronoOrder": 24,
        "chronoDetail": "3 semanas após Ultimato",
        "synopsis": "Wanda Maximoff e Visão vivem uma vida conjugal suburbana aparentemente perfeita inspirada em séries de TV clássicas, mas aos poucos descobrem anomalias inquietantes que revelam que aquela cidade esconde um mistério perturbador.",
        "search_imdb": "WandaVision 2021",
        "search_yt": "Marvel Brasil trailer oficial WandaVision"
    },
    {
        "id": "shangchi",
        "title": "Shang-Chi e a Lenda dos Dez Anéis",
        "original_title": "Shang-Chi and the Legend of the Ten Rings",
        "year": 2021,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "movie",
        "releaseOrder": 25,
        "chronoOrder": 25,
        "chronoDetail": "Ano de 2024",
        "synopsis": "Vivendo discretamente como manobrista nos Estados Unidos, Shang-Chi é confrontado pelo seu próprio passado quando a milenar organização armada dos Dez Anéis, comandada por seu pai imortal Wenwu, vem atrás de segredos de sua linhagem.",
        "search_imdb": "Shang-Chi and the Legend of the Ten Rings 2021",
        "search_yt": "Marvel Brasil trailer oficial Shang-Chi"
    },
    {
        "id": "fatws",
        "title": "Falcão e o Soldado Invernal",
        "original_title": "The Falcon and the Winter Soldier",
        "year": 2021,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "series",
        "releaseOrder": 23.5,
        "chronoOrder": 26,
        "chronoDetail": "6 meses após Ultimato",
        "synopsis": "Sam Wilson e Bucky Barnes formam uma parceria global para combater um grupo de rebeldes com habilidades ampliadas chamados Apátridas, enquanto Sam pondera o imenso fardo moral e social de empunhar o escudo do Capitão América.",
        "search_imdb": "The Falcon and the Winter Soldier 2021",
        "search_yt": "Marvel Brasil trailer oficial Falcão e o Soldado Invernal"
    },
    {
        "id": "eternos",
        "title": "Eternos",
        "original_title": "Eternals",
        "year": 2021,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "movie",
        "releaseOrder": 26,
        "chronoOrder": 27,
        "chronoDetail": "Ano de 2024",
        "synopsis": "Uma linhagem de seres cósmicos imortais enviados pelos Celestiais para guardar a Terra há mais de 7 mil anos precisa sair do anonimato após uma tragédia inesperada anunciar o retorno de predadores monstruosos chamados Deviantes.",
        "search_imdb": "Eternals 2021",
        "search_yt": "Marvel Brasil trailer oficial Eternos"
    },
    {
        "id": "sm3",
        "title": "Homem-Aranha: Sem Volta Para Casa",
        "original_title": "Spider-Man: No Way Home",
        "year": 2021,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "movie",
        "releaseOrder": 27,
        "chronoOrder": 29,
        "chronoDetail": "Logo após Longe de Casa",
        "synopsis": "Após sua identidade ser escancarada ao mundo, Peter Parker recorre à feitiçaria do Doutor Estranho para recuperar o anonimato. O feitiço é corrompido, rompendo os limites do tempo-espaço e atraindo vilões lendários de realidades paralelas.",
        "search_imdb": "Spider-Man: No Way Home 2021",
        "search_yt": "Marvel Brasil trailer oficial Homem-Aranha Sem Volta Para Casa"
    },
    {
        "id": "hawkeye",
        "title": "Gavião Arqueiro",
        "original_title": "Hawkeye",
        "year": 2021,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "series",
        "releaseOrder": 27.2,
        "chronoOrder": 30,
        "chronoDetail": "Natal de 2024",
        "synopsis": "Durante as festas de fim de ano em Nova York, Clint Barton tenta voltar para a família a tempo do Natal, mas cruza com a jovem prodígio do arco e flecha Kate Bishop e precisa enfrentar inimigos remanescentes de seus anos sombrios como Ronin.",
        "search_imdb": "Hawkeye 2021",
        "search_yt": "Marvel Brasil trailer oficial Gavião Arqueiro"
    },
    {
        "id": "moonknight",
        "title": "Cavaleiro da Lua",
        "original_title": "Moon Knight",
        "year": 2022,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "series",
        "releaseOrder": 27.4,
        "chronoOrder": 31,
        "chronoDetail": "Ano de 2025",
        "synopsis": "Steven Grant, um tímido atendente de museu britânico, descobre que sofre de transtorno dissociativo de identidade e compartilha a mente com o mercenário Marc Spector, tornando-se o avatar do deus egípcio Khonshu contra ameaças mitológicas.",
        "search_imdb": "Moon Knight 2022",
        "search_yt": "Marvel Brasil trailer oficial Cavaleiro da Lua"
    },
    {
        "id": "ds2",
        "title": "Doutor Estranho no Multiverso da Loucura",
        "original_title": "Doctor Strange in the Multiverse of Madness",
        "year": 2022,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "movie",
        "releaseOrder": 28,
        "chronoOrder": 32,
        "chronoDetail": "Ano de 2024 / 2025",
        "synopsis": "Stephen Strange cruza caminhos com a jovem América Chavez, capaz de abrir portais para outras dimensões, e se lança em uma eletrizante fuga pelo multiverso para protegê-la de uma terrível e corrompida força mágica.",
        "search_imdb": "Doctor Strange in the Multiverse of Madness 2022",
        "search_yt": "Marvel Brasil trailer oficial Doutor Estranho no Multiverso da Loucura"
    },
    {
        "id": "msmarvel",
        "title": "Ms. Marvel",
        "original_title": "Ms. Marvel",
        "year": 2022,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "series",
        "releaseOrder": 28.2,
        "chronoOrder": 33,
        "chronoDetail": "Ano de 2025",
        "synopsis": "Kamala Khan, uma adolescente paquistanesa-americana de Nova Jersey apaixonada pelos Vingadores, tem sua vida transformada ao herdar uma relíquia ancestral de família que lhe concede a habilidade de moldar construções de luz sólida.",
        "search_imdb": "Ms. Marvel 2022",
        "search_yt": "Marvel Brasil trailer oficial Ms Marvel"
    },
    {
        "id": "thor4",
        "title": "Thor: Amor e Trovão",
        "original_title": "Thor: Love and Thunder",
        "year": 2022,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "movie",
        "releaseOrder": 29,
        "chronoOrder": 34,
        "chronoDetail": "Ano de 2025",
        "synopsis": "Thor vê sua aposentadoria pacífica interrompida por Gorr, o Carniceiro dos Deuses, que jurou exterminar todas as divindades do cosmo. Para vencê-lo, ele recorre à ajuda do Rei Valquíria, Korg e de Jane Foster, agora empunhando o restaurado Mjölnir.",
        "search_imdb": "Thor: Love and Thunder 2022",
        "search_yt": "Marvel Brasil trailer oficial Thor Amor e Trovão"
    },
    {
        "id": "shehulk",
        "title": "Mulher-Hulk: Defensora de Heróis",
        "original_title": "She-Hulk: Attorney at Law",
        "year": 2022,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "series",
        "releaseOrder": 29.2,
        "chronoOrder": 35,
        "chronoDetail": "Ano de 2025",
        "synopsis": "A advogada Jennifer Walters ganha poderes semelhantes aos do seu primo Bruce Banner após um acidente, precisando conciliar sua vida profissional nos tribunais defendendo indivíduos com superpoderes com sua nova fama de Mulher-Hulk.",
        "search_imdb": "She-Hulk: Attorney at Law 2022",
        "search_yt": "Marvel Brasil trailer oficial Mulher-Hulk"
    },
    {
        "id": "bp2",
        "title": "Pantera Negra: Wakanda Para Sempre",
        "original_title": "Black Panther: Wakanda Forever",
        "year": 2022,
        "phase": 4,
        "saga": "A Saga do Multiverso",
        "type": "movie",
        "releaseOrder": 30,
        "chronoOrder": 36,
        "chronoDetail": "Ano de 2025",
        "synopsis": "Abalada com a perda de seu rei T'Challa, a rainha Ramonda e Shuri lutam para proteger os recursos de Wakanda contra a cobiça de governos internacionais e o confronto iminente com a civilização aquática de Talokan, regida por Namor.",
        "search_imdb": "Black Panther: Wakanda Forever 2022",
        "search_yt": "Marvel Brasil trailer oficial Pantera Negra Wakanda Para Sempre"
    },

    # FASE 5 - A Saga do Multiverso
    {
        "id": "ant3",
        "title": "Homem-Formiga e a Vespa: Quantumania",
        "original_title": "Ant-Man and the Wasp: Quantumania",
        "year": 2023,
        "phase": 5,
        "saga": "A Saga do Multiverso",
        "type": "movie",
        "releaseOrder": 31,
        "chronoOrder": 37,
        "chronoDetail": "Ano de 2026",
        "synopsis": "Scott Lang, Hope van Dyne, Hank Pym e Cassie são inadvertidamente transportados para o coração inexplorado do Reino Quântico, descobrindo civilizações exóticas e encarando o perigoso déspota Kang, o Conquistador.",
        "search_imdb": "Ant-Man and the Wasp: Quantumania 2023",
        "search_yt": "Marvel Brasil trailer oficial Quantumania"
    },
    {
        "id": "gotg3",
        "title": "Guardiões da Galáxia Vol. 3",
        "original_title": "Guardians of the Galaxy Vol. 3",
        "year": 2023,
        "phase": 5,
        "saga": "A Saga do Multiverso",
        "type": "movie",
        "releaseOrder": 32,
        "chronoOrder": 38,
        "chronoDetail": "Ano de 2026",
        "synopsis": "Ainda abalado com a ausência de sua Gamora, Peter Quill lidera os Guardiões em uma arriscada missão para proteger a vida de Rocket Racoon, confrontando as terríveis experiências genéticas do Alto Evolucionário.",
        "search_imdb": "Guardians of the Galaxy Vol. 3 2023",
        "search_yt": "Marvel Brasil trailer oficial Guardiões da Galáxia Vol 3"
    },
    {
        "id": "invasion",
        "title": "Invasão Secreta",
        "original_title": "Secret Invasion",
        "year": 2023,
        "phase": 5,
        "saga": "A Saga do Multiverso",
        "type": "series",
        "releaseOrder": 32.2,
        "chronoOrder": 39,
        "chronoDetail": "Ano de 2026",
        "synopsis": "Ao tomar conhecimento de uma conspiração oculta de Skrulls rebeldes disfarçados entre figuras proeminentes da geopolítica terrestre, Nick Fury retorna à Terra sem seus aliados Vingadores para conter a invasão invisível.",
        "search_imdb": "Secret Invasion 2023",
        "search_yt": "Marvel Brasil trailer oficial Invasão Secreta"
    },
    {
        "id": "marvels",
        "title": "As Marvels",
        "original_title": "The Marvels",
        "year": 2023,
        "phase": 5,
        "saga": "A Saga do Multiverso",
        "type": "movie",
        "releaseOrder": 33,
        "chronoOrder": 40,
        "chronoDetail": "Ano de 2026",
        "synopsis": "Capitã Marvel, Monica Rambeau e Kamala Khan têm suas frequências de energia quântica acidentalmente conectadas, fazendo com que troquem fisicamente de lugar no espaço a cada ativação de seus poderes cósmicos.",
        "search_imdb": "The Marvels 2023",
        "search_yt": "Marvel Brasil trailer oficial As Marvels"
    },
    {
        "id": "echo",
        "title": "Echo",
        "original_title": "Echo",
        "year": 2024,
        "phase": 5,
        "saga": "A Saga do Multiverso",
        "type": "series",
        "releaseOrder": 33.2,
        "chronoOrder": 41,
        "chronoDetail": "Ano de 2026",
        "synopsis": "Perseguida impiedosamente pelo cartel do Rei do Crime, Maya Lopez retorna à sua terra natal em Oklahoma para redescobrir sua herança e o significado de sua família enquanto se prepara para um embate decisivo.",
        "search_imdb": "tt13966962",
        "search_yt": "Marvel Brasil trailer oficial Echo série"
    },
    {
        "id": "dp3",
        "title": "Deadpool & Wolverine",
        "original_title": "Deadpool & Wolverine",
        "year": 2024,
        "phase": 5,
        "saga": "A Saga do Multiverso",
        "type": "movie",
        "releaseOrder": 34,
        "chronoOrder": 42,
        "chronoDetail": "Fora do tempo / Linha da Fox + AVT",
        "synopsis": "Retirado de sua rotina mundana pela Autoridade de Variância Temporal, um relutante Wade Wilson precisa resgatar seu próprio universo e une forças com uma variante desiludida e traumatizada do Wolverine.",
        "search_imdb": "Deadpool and Wolverine 2024",
        "search_yt": "Marvel Brasil trailer 2 oficial dublado Deadpool Wolverine"
    },
    {
        "id": "agatha",
        "title": "Agatha Desde Sempre",
        "original_title": "Agatha All Along",
        "year": 2024,
        "phase": 5,
        "saga": "A Saga do Multiverso",
        "type": "series",
        "releaseOrder": 34.5,
        "chronoOrder": 43,
        "chronoDetail": "3 anos após WandaVision",
        "synopsis": "Liberta do transe que a prendia em Westview mas sem seus poderes, a feiticeira Agatha Harkness forma uma improvável aliança de bruxas desamparadas para enfrentar as provações mortais do lendário Caminho das Bruxas.",
        "search_imdb": "Agatha All Along 2024",
        "search_yt": "Marvel Brasil trailer oficial Agatha Desde Sempre"
    },
    {
        "id": "ca4",
        "title": "Capitão América: Admirável Mundo Novo",
        "original_title": "Captain America: Brave New World",
        "year": 2025,
        "phase": 5,
        "saga": "A Saga do Multiverso",
        "type": "movie",
        "releaseOrder": 35,
        "chronoOrder": 44,
        "chronoDetail": "Ano de 2026 / 2027",
        "synopsis": "Consolidado no manto de Capitão América, Sam Wilson se vê no centro de um complô internacional de assassinato e desestabilização global logo após um tenso encontro com o recém-eleito presidente norte-americano Thaddeus Ross.",
        "search_imdb": "Captain America: Brave New World 2025",
        "search_yt": "Marvel Brasil trailer oficial Capitão América Admirável Mundo Novo"
    },
    {
        "id": "thunderbolts",
        "title": "Thunderbolts*",
        "original_title": "Thunderbolts*",
        "year": 2025,
        "phase": 5,
        "saga": "A Saga do Multiverso",
        "type": "movie",
        "releaseOrder": 36,
        "chronoOrder": 45,
        "chronoDetail": "Ano de 2026 / 2027",
        "synopsis": "Uma equipe de renegados e anti-heróis sem rumo – incluindo Yelena Belova, Bucky Barnes, Guardião Vermelho e John Walker – é reunida sob a tutela clandestina do governo em missões onde o fracasso não é uma opção.",
        "search_imdb": "Thunderbolts 2025",
        "search_yt": "Marvel Brasil trailer oficial Thunderbolts"
    },
    {
        "id": "daredevil_ba",
        "title": "Demolidor: Renascido",
        "original_title": "Daredevil: Born Again",
        "year": 2025,
        "phase": 5,
        "saga": "A Saga do Multiverso",
        "type": "series",
        "releaseOrder": 36.5,
        "chronoOrder": 46,
        "chronoDetail": "Ano de 2026 / 2027",
        "synopsis": "Matt Murdock e Wilson Fisk buscam novos começos na cidade de Nova York através da lei e da política, mas as velhas rivalidades e identidades sombrias do passado voltam a ameaçar a paz das ruas.",
        "search_imdb": "Daredevil: Born Again",
        "search_yt": "Marvel trailer dublado Demolidor Renascido"
    },
    {
        "id": "f4",
        "title": "Quarteto Fantástico: Primeiros Passos",
        "original_title": "The Fantastic Four: First Steps",
        "year": 2025,
        "phase": 6,
        "saga": "A Saga do Multiverso",
        "type": "movie",
        "releaseOrder": 37,
        "chronoOrder": 47,
        "chronoDetail": "Universo alternativo retrofuturista anos 60",
        "synopsis": "Em um universo retrofuturista inspirado nos anos 1960, a família pioneira de exploradores formada por Reed Richards, Sue Storm, Johnny Storm e Ben Grimm precisa unir suas forças para salvar seu planeta do titânico Galactus.",
        "search_imdb": "The Fantastic Four: First Steps 2025",
        "search_yt": "Marvel Quarteto Fantástico Primeiros Passos trailer oficial"
    }
]

def fetch_imdb_info(query):
    """Obtém capa em alta resolução e ID do IMDb através do endpoint de sugestão."""
    try:
        clean_query = query.replace('&', 'and').replace('*', '').replace(':', '')
        if clean_query.startswith("tt"):
            url = f"https://v3.sg.media-imdb.com/suggestion/t/{clean_query}.json"
        else:
            url = f"https://v3.sg.media-imdb.com/suggestion/x/{urllib.parse.quote(clean_query)}.json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'})
        with urllib.request.urlopen(req, timeout=8) as response:
            data = json.loads(response.read().decode('utf-8'))
            results = data.get('d', [])
            if results:
                item = results[0]
                img_url = item.get('i', {}).get('imageUrl', '')
                if '._V1_' in img_url:
                    img_url = img_url.split('._V1_')[0] + '._V1_.jpg'
                return {
                    'imdb_id': item.get('id', ''),
                    'cover_url': img_url,
                    'stars': item.get('s', '')
                }
    except Exception as e:
        print(f"  [Aviso IMDb] Falha ao buscar '{query}': {e}")
    return {'imdb_id': '', 'cover_url': '', 'stars': ''}

def fetch_youtube_trailer(query):
    """Busca o link oficial do trailer no YouTube."""
    try:
        url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'})
        with urllib.request.urlopen(req, timeout=8) as response:
            html = response.read().decode('utf-8')
            video_ids = re.findall(r'\"videoId\":\"([a-zA-Z0-9_-]{11})\"', html)
            if video_ids:
                unique_ids = []
                for vid in video_ids:
                    if vid not in unique_ids:
                        unique_ids.append(vid)
                chosen_id = unique_ids[0]
                return {
                    'video_id': chosen_id,
                    'trailer_url': f"https://www.youtube.com/watch?v={chosen_id}",
                    'trailer_embed': f"https://www.youtube.com/embed/{chosen_id}"
                }
    except Exception as e:
        print(f"  [Aviso YouTube] Falha ao buscar trailer '{query}': {e}")
    return {'video_id': '', 'trailer_url': '', 'trailer_embed': ''}

def run_scraper(output_file="mcu_data.json", force_refresh=False):
    print("=" * 65)
    print("🎬 INICIANDO SCRAPER OFICIAL DO MCU (Filmes e Séries)")
    print(f"📦 Total de títulos a processar: {len(MCU_CATALOG)}")
    print("=" * 65)

    existing_data = {}
    if os.path.exists(output_file) and not force_refresh:
        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                loaded = json.load(f)
                for item in loaded:
                    existing_data[item['id']] = item
            print(f"ℹ️ Encontrado cache com {len(existing_data)} itens.")
        except Exception:
            pass

    scraped_records = []

    for idx, item in enumerate(MCU_CATALOG, start=1):
        item_id = item['id']
        title = item['title']
        cached = existing_data.get(item_id, {})

        print(f"\n[{idx:02d}/{len(MCU_CATALOG):02d}] 🔍 Processando: {title} ({item['year']})...")

        # Capa / IMDb
        if cached.get('cover_url') and not force_refresh:
            imdb_info = {
                'imdb_id': cached.get('imdb_id', ''),
                'cover_url': cached.get('cover_url', ''),
                'stars': cached.get('stars', '')
            }
            print("  ✓ IMDb (cache)")
        else:
            imdb_info = fetch_imdb_info(item['search_imdb'])
            print(f"  ✓ IMDb: {imdb_info.get('imdb_id')} | Capa: {'OK' if imdb_info.get('cover_url') else 'Pendente'}")
            time.sleep(0.2)

        # Trailer / YouTube
        if cached.get('trailer_url') and not force_refresh:
            yt_info = {
                'video_id': cached.get('video_id', ''),
                'trailer_url': cached.get('trailer_url', ''),
                'trailer_embed': cached.get('trailer_embed', '')
            }
            print("  ✓ Trailer (cache)")
        else:
            yt_info = fetch_youtube_trailer(item['search_yt'])
            print(f"  ✓ Trailer YouTube: {yt_info.get('trailer_url')}")
            time.sleep(0.2)

        record = {
            "id": item["id"],
            "title_pt": item["title"],
            "title_en": item["original_title"],
            "title": item["title"],
            "original_title": item["original_title"],
            "year": item["year"],
            "phase": item["phase"],
            "saga": item["saga"],
            "type": item["type"],
            "releaseOrder": item["releaseOrder"],
            "chronoOrder": item["chronoOrder"],
            "chronoDetail": item["chronoDetail"],
            "synopsis": item["synopsis"],
            "cover_url": imdb_info.get("cover_url", ""),
            "imdb_id": imdb_info.get("imdb_id", ""),
            "imdb_url": f"https://www.imdb.com/title/{imdb_info.get('imdb_id')}/" if imdb_info.get("imdb_id") else "",
            "stars": imdb_info.get("stars", ""),
            "video_id": yt_info.get("video_id", ""),
            "trailer_url": yt_info.get("trailer_url", ""),
            "trailer_embed": yt_info.get("trailer_embed", "")
        }
        scraped_records.append(record)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(scraped_records, f, ensure_ascii=False, indent=2)

    # Gera também data.js para suporte offline e fallback imediato sem CORS
    js_file = output_file.replace('.json', '.js') if output_file.endswith('.json') else 'data.js'
    if js_file == output_file:
        js_file = 'data.js'
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write('window.__MCU_FALLBACK_DATA__ = ' + json.dumps(scraped_records, ensure_ascii=False, indent=2) + ';\n')

    print("\n" + "=" * 65)
    print(f"🎉 SUCESSO! Dados raspados e salvos em: {output_file} e {js_file}")
    print(f"📊 Total de registros salvos: {len(scraped_records)}")
    print("=" * 65)
    return scraped_records

if __name__ == "__main__":
    force = "--force" in sys.argv
    run_scraper("mcu_data.json", force_refresh=force)
