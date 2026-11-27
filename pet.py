"""Banco de questões objetivas para a prova on-line do PET/COPPE/UFRJ (Edital 1218/2026).

Prova: Língua Inglesa (leitura e compreensão de texto técnico ou científico) e Raciocínio Lógico
(coerência de ideias em situações apresentadas). Ambas eliminatórias, on-line, 9h–13h, até 240 min.
Referências de inglês do edital: Murphy, Essential Grammar in Use e Grammar in Use Intermediate.

Textos em inglês escritos para treino, no estilo de artigo e relatório técnico de transportes.
Não reproduzem provas anteriores do PET.
"""

TEXTOS = {
    "t1": (
        "Brazil moves most of its cargo by road, even though the country has long coastlines and large navigable rivers. "
        "This dependence has a cost. Trucks consume more fuel per tonne-kilometre than trains or barges, and long road trips "
        "expose cargo to accidents, theft and delays. Several studies have argued that shifting part of the long-distance "
        "freight to rail and waterways would reduce logistics costs and emissions. However, such a shift is not simply a matter "
        "of building new lines. Rail and waterway terminals must be connected to roads, because the first and last legs of most "
        "trips will still be made by truck. Without these connections, shippers face additional handling costs that can cancel "
        "out the savings of the cheaper mode. For this reason, recent plans emphasise intermodal terminals rather than isolated "
        "infrastructure projects. Critics note, however, that terminals take years to build and that their benefits depend on "
        "stable regulation, which investors consider uncertain."
    ),
    "t2": (
        "Last-mile delivery, the final step from a distribution centre to the customer's door, is often the most expensive part "
        "of the supply chain. Vehicles stop frequently, travel short distances between stops and often return with failed "
        "deliveries when nobody is at home. To reduce these costs, companies have tested several strategies: consolidating "
        "parcels in pick-up points, delivering at night, and using smaller electric vans in dense urban areas. Electric vans are "
        "quieter and produce no local emissions, which makes night deliveries more acceptable to residents. Their limited range, "
        "however, is less of a problem than it seems, since most urban routes are shorter than the range of current models. "
        "The main obstacle is the time needed to recharge them between shifts. Routing software can help: if the charging time "
        "is included as a constraint, the algorithm can assign longer routes to vans that start the day fully charged and "
        "shorter ones to those that need to stop at a charger."
    ),
    "t3": (
        "This paper evaluates the effect of a congestion charge introduced in the central area of a mid-sized city. Using "
        "traffic counts from 120 sensors collected one year before and one year after the policy, we estimate the change in "
        "vehicle flows with a difference-in-differences design, comparing the charged area with similar areas that were not "
        "charged. Results indicate a 14% reduction in vehicle flows inside the charged area and no significant increase in the "
        "surrounding streets. Bus travel times improved by 6% on routes crossing the area. We also find that the reduction was "
        "larger during peak hours, suggesting that drivers shifted the timing of non-essential trips. The analysis has "
        "limitations: the period covers only one year after the policy, and the sensors do not distinguish freight vehicles "
        "from private cars. Further research should assess long-term effects and the impact on urban freight."
    ),
}


def _q(id, modulo, enunciado, opcoes, correta, explicacao, texto=None):
    return dict(id=id, modulo=modulo, texto=texto, enunciado=enunciado, opcoes=opcoes,
                correta="ABCDE".index(correta), explicacao=explicacao)


QUESTOES = [
    # ───────────── Inglês: leitura (texto 1)
    _q("i1", "ingles", "The main purpose of the text is to:",
       ["prove that rail is always cheaper than road.",
        "explain why reducing road dependence requires integrated, intermodal solutions.",
        "describe the history of Brazilian railways.",
        "blame truck drivers for accidents and theft.",
        "argue that waterways should replace all road transport."],
       "B", "Ideia central: o custo da dependência rodoviária e por que a solução passa por terminais intermodais, não por obras isoladas.", "t1"),
    _q("i2", "ingles", "According to the text, trucks:",
       ["consume less fuel per tonne-kilometre than barges.",
        "are rarely used in the first and last legs of trips.",
        "consume more fuel per tonne-kilometre than trains or barges.",
        "are safer than any other mode.",
        "will disappear once intermodal terminals are built."],
       "C", "Informação literal: 'Trucks consume more fuel per tonne-kilometre than trains or barges'.", "t1"),
    _q("i3", "ingles", "In 'However, such a shift is not simply a matter of building new lines', the word 'However' introduces:",
       ["an example of the previous idea.", "a contrast or qualification to the previous idea.",
        "a conclusion identical to the previous sentence.", "a cause of truck accidents.", "a time sequence."],
       "B", "'However' é conectivo de contraste (= no entanto). Ressalva a ideia de que basta transferir a carga para trem e hidrovia.", "t1"),
    _q("i4", "ingles", "In 'costs that can cancel out the savings of the cheaper mode', 'cancel out' is closest in meaning to:",
       ["increase", "offset", "postpone", "confirm", "measure"],
       "B", "'Cancel out' = anular, compensar (offset). O custo de transbordo pode anular a economia do modo mais barato.", "t1"),
    _q("i5", "ingles", "It can be inferred that, for investors, a key concern about intermodal terminals is:",
       ["the excessive number of trucks.", "the lack of navigable rivers.", "uncertainty about regulation.",
        "low emissions.", "short construction time."],
       "C", "Última frase: os benefícios dependem de regulação estável, 'which investors consider uncertain'.", "t1"),
    # ───────────── Inglês: leitura (texto 2)
    _q("i6", "ingles", "According to the text, last-mile delivery is expensive because:",
       ["vehicles travel long distances between stops.", "deliveries are always made at night.",
        "of frequent stops, short trips and failed deliveries.", "electric vans are expensive to buy.",
        "customers prefer pick-up points."],
       "C", "Segunda frase: paradas frequentes, trechos curtos e entregas que falham quando não há ninguém em casa.", "t2"),
    _q("i7", "ingles", "The author considers the limited range of electric vans:",
       ["the main obstacle to their use.", "less important than it appears.", "a reason to avoid night deliveries.",
        "impossible to solve with software.", "the cause of failed deliveries."],
       "B", "'Their limited range, however, is less of a problem than it seems'. O principal obstáculo é o tempo de recarga.", "t2"),
    _q("i8", "ingles", "In 'Their limited range', the word 'Their' refers to:",
       ["residents", "companies", "electric vans", "pick-up points", "routes"],
       "C", "Referência pronominal: a frase anterior fala de 'Electric vans'.", "t2"),
    _q("i9", "ingles", "According to the text, routing software can help by:",
       ["eliminating the need to recharge.", "treating charging time as a constraint when assigning routes.",
        "increasing the range of the batteries.", "choosing customers who are at home.",
        "replacing electric vans with diesel ones."],
       "B", "Última frase: com o tempo de recarga como restrição, o algoritmo distribui rotas longas e curtas conforme a carga da bateria.", "t2"),
    _q("i10", "ingles", "Which strategy is NOT mentioned in the text?",
       ["consolidating parcels in pick-up points", "delivering at night", "using electric vans",
        "raising delivery prices for customers", "using smaller vehicles in dense urban areas"],
       "D", "Questão de 'NOT': aumentar o preço da entrega não aparece no texto; as outras quatro aparecem.", "t2"),
    # ───────────── Inglês: leitura (texto 3, resumo de artigo)
    _q("i11", "ingles", "The method used to estimate the effect of the policy was:",
       ["a survey of drivers.", "a difference-in-differences comparison between charged and non-charged areas.",
        "a simulation without real data.", "a laboratory experiment.", "interviews with bus companies."],
       "B", "'we estimate the change ... with a difference-in-differences design, comparing the charged area with similar areas that were not charged'.", "t3"),
    _q("i12", "ingles", "According to the results:",
       ["traffic increased significantly in the surrounding streets.", "vehicle flows fell 14% inside the charged area.",
        "bus travel times got 6% worse.", "the reduction was smaller in peak hours.", "freight vehicles were the most affected."],
       "B", "Resultado literal. Cuidado com as pegadinhas: ônibus MELHORARAM 6%, a queda foi MAIOR no pico e os sensores não separam carga.", "t3"),
    _q("i13", "ingles", "'suggesting that drivers shifted the timing of non-essential trips' expresses:",
       ["a proven fact.", "an interpretation proposed by the authors.", "a limitation of the sensors.",
        "a recommendation to drivers.", "the objective of the paper."],
       "B", "'suggesting' marca hipótese ou interpretação, não fato comprovado. Comum em resumo científico.", "t3"),
    _q("i14", "ingles", "One limitation acknowledged by the authors is that:",
       ["the city is too large.", "only 12 sensors were used.", "sensors could not separate freight vehicles from private cars.",
        "buses were excluded from the analysis.", "the charge was too low."],
       "C", "'the sensors do not distinguish freight vehicles from private cars'. Eram 120 sensores, não 12.", "t3"),
    _q("i15", "ingles", "In 'Further research should assess long-term effects', 'Further' means:",
       ["farther away", "additional", "previous", "faster", "cheaper"],
       "B", "'Further research' = pesquisa adicional, futura. Não confundir com 'farther' (distância).", "t3"),
    # ───────────── Inglês: gramática em contexto (Murphy)
    _q("g1", "ingles", "The new terminal ___ by the end of next year.",
       ["will complete", "will be completed", "completes", "is completing", "has completed"],
       "B", "Voz passiva no futuro (will be + particípio): o terminal não se completa sozinho, ele é concluído."),
    _q("g2", "ingles", "If the government ___ the railway, freight costs would fall.",
       ["expands", "expanded", "will expand", "has expanded", "expanding"],
       "B", "Segunda condicional: if + passado simples, would + verbo. Situação hipotética."),
    _q("g3", "ingles", "Traffic ___ by 14% since the charge was introduced.",
       ["falls", "fell", "has fallen", "is falling", "had fall"],
       "C", "'since' + período até agora pede present perfect (has fallen)."),
    _q("g4", "ingles", "Shippers must ___ additional handling costs.",
       ["paying", "to pay", "pay", "paid", "pays"],
       "C", "Depois de modal (must, can, should) vem o verbo no infinitivo sem 'to'."),
    _q("g5", "ingles", "The study, ___ was published last year, used sensor data.",
       ["who", "which", "what", "where", "whose"],
       "B", "Pronome relativo para coisa em oração explicativa (entre vírgulas): which. 'Who' é para pessoa."),
    _q("g6", "ingles", "Electric vans are ___ than diesel vans.",
       ["more quiet", "quieter", "quietest", "most quiet", "quiet"],
       "B", "Comparativo de adjetivo curto: quiet → quieter than."),
    # ───────────── Raciocínio lógico
    _q("l1", "logica", "Todo terminal intermodal está ligado a uma rodovia. Algum porto seco não está ligado a uma rodovia. Logo:",
       ["Nenhum porto seco é terminal intermodal.", "Algum porto seco não é terminal intermodal.",
        "Todo porto seco é terminal intermodal.", "Algum terminal intermodal não é porto seco.",
        "Nenhum terminal intermodal está ligado a porto seco."],
       "B", "O porto seco sem rodovia não pode ser terminal intermodal (todos os terminais têm rodovia). Só se conclui sobre ALGUM porto seco, não sobre todos."),
    _q("l2", "logica", "A negação de 'Todos os caminhões da frota foram revisados' é:",
       ["Nenhum caminhão foi revisado.", "Pelo menos um caminhão da frota não foi revisado.",
        "Todos os caminhões não foram revisados.", "Alguns caminhões foram revisados.", "Só um caminhão não foi revisado."],
       "B", "Negar 'todo A é B' = 'existe A que não é B'. 'Nenhum' é forte demais."),
    _q("l3", "logica", "Se chove na região, a estrada fica interditada. A estrada não ficou interditada. Conclui-se que:",
       ["choveu.", "não choveu.", "a estrada está em obras.", "choveu pouco.", "nada se pode concluir."],
       "B", "Modus tollens: se P então Q; não Q; logo não P."),
    _q("l4", "logica", "Se o caminhão atrasar, a entrega falha. A entrega falhou. Logo:",
       ["o caminhão atrasou.", "o caminhão não atrasou.", "não se pode concluir que o caminhão atrasou.",
        "o cliente não estava em casa.", "a entrega não falhou."],
       "C", "Afirmar o consequente é falácia: a entrega pode falhar por outro motivo."),
    _q("l5", "logica", "'Se o terminal operar à noite, então o custo cai' é equivalente a:",
       ["Se o custo cai, o terminal opera à noite.", "Se o custo não cai, o terminal não opera à noite.",
        "Se o terminal não opera à noite, o custo não cai.", "O terminal opera à noite e o custo não cai.",
        "O terminal opera à noite ou o custo cai."],
       "B", "Contrapositiva: P→Q equivale a ¬Q→¬P (e também a '¬P ou Q'). A opção E troca ¬P por P."),
    _q("l6", "logica", "A negação de 'O frete subiu e a demanda caiu' é:",
       ["O frete não subiu e a demanda não caiu.", "O frete não subiu ou a demanda não caiu.",
        "O frete subiu ou a demanda caiu.", "O frete caiu e a demanda subiu.", "Se o frete subiu, a demanda caiu."],
       "B", "De Morgan: ¬(P e Q) = ¬P ou ¬Q."),
    _q("l7", "logica", "Um relatório afirma: 'Todas as rotas do turno da manhã terminaram antes das 12h.' Qual informação, se verdadeira, contradiz o relatório?",
       ["Uma rota da tarde terminou às 18h.", "Uma rota da manhã terminou às 11h50.", "Uma rota da manhã terminou às 12h30.",
        "Nenhuma rota da tarde terminou antes das 12h.", "Duas rotas da manhã terminaram às 10h."],
       "C", "Basta um contraexemplo do mesmo grupo (manhã) fora da regra. Rotas da tarde não importam."),
    _q("l8", "logica", "Argumento: 'A cobrança de congestionamento reduziu o tráfego no centro, pois o fluxo caiu após sua implantação.' Qual informação mais FORTALECE o argumento?",
       ["O preço da gasolina subiu muito no mesmo período em toda a cidade.",
        "Áreas semelhantes sem cobrança não tiveram queda de fluxo no mesmo período.",
        "O número de sensores aumentou.", "Houve obras no centro durante o período.", "A prefeitura mudou de gestão."],
       "B", "O grupo de comparação sem queda afasta explicações alternativas. A e D enfraquecem, porque são outras causas possíveis."),
    _q("l9", "logica", "No mesmo argumento, qual informação mais ENFRAQUECE a conclusão?",
       ["Áreas sem cobrança tiveram queda de fluxo igual no mesmo período.", "Ônibus ficaram mais rápidos.",
        "A queda foi maior no horário de pico.", "Motoristas relataram evitar o centro.", "A cobrança foi bem divulgada."],
       "A", "Se a queda aconteceu igual onde não houve cobrança, a causa provável é outra."),
    _q("l10", "logica", "Cinco caminhões (A, B, C, D, E) chegam ao armazém em sequência. B chega imediatamente depois de A. C chega antes de A. E é o último. D chega antes de C. A ordem de chegada é:",
       ["D, C, A, B, E", "C, D, A, B, E", "D, A, B, C, E", "A, B, C, D, E", "D, C, B, A, E"],
       "A", "D antes de C antes de A; B logo depois de A; E por último: D, C, A, B, E."),
    _q("l11", "logica", "Um frete de R$ 1.000 sobe 10% e, em seguida, cai 10%. O valor final é:",
       ["R$ 1.000", "R$ 990", "R$ 1.010", "R$ 900", "R$ 1.100"],
       "B", "1.000 × 1,1 = 1.100; 1.100 × 0,9 = 990. Percentuais sucessivos não se cancelam."),
    _q("l12", "logica", "'Ter CNH categoria E é necessário para dirigir carreta' significa que:",
       ["quem tem CNH E dirige carreta.", "quem dirige carreta tem CNH E.", "quem não dirige carreta não tem CNH E.",
        "ter CNH E garante dirigir carreta.", "quem não tem CNH E pode dirigir carreta."],
       "B", "Condição necessária: dirigir carreta → ter CNH E. Ter a CNH não basta (não é suficiente)."),
    _q("l13", "logica", "Sobre um depósito: (I) tem mais de 50 vagas; (II) tem menos de 40 vagas; (III) tem pelo menos uma vaga. Exatamente uma afirmação é falsa. Então:",
       ["I é verdadeira.", "II é verdadeira.", "III é verdadeira.", "III é falsa.", "o depósito tem 45 vagas."],
       "C", "I e II não podem ser ambas verdadeiras, logo a falsa é uma delas e III é verdadeira. Se III fosse falsa (0 vagas), I também seria: duas falsas."),
    _q("l14", "logica", "Numa frota, 60% dos veículos são elétricos e, destes, 25% têm mais de 3 anos. Que porcentagem da frota é de elétricos com mais de 3 anos?",
       ["25%", "15%", "35%", "45%", "85%"],
       "B", "Percentual de percentual: 0,60 × 0,25 = 0,15."),
    _q("l15", "logica", "Premissas: 'Nenhuma rota noturna passa pelo centro.' 'Todas as rotas da empresa X passam pelo centro.' Qual conclusão é coerente?",
       ["Alguma rota da empresa X é noturna.", "Nenhuma rota da empresa X é noturna.",
        "Todas as rotas noturnas são da empresa X.", "Algumas rotas noturnas passam pelo centro.", "A empresa X não opera rotas."],
       "B", "Se toda rota de X passa pelo centro e nenhuma noturna passa, nenhuma rota de X é noturna."),
]

TEMAS = {
    "ideia central": "Leia o 1º e o último período do texto antes das alternativas. Descarte alternativas com 'always', 'all', 'never': exageram o texto.",
    "informação literal": "Ache no texto a palavra-chave do enunciado e leia a frase inteira. A resposta certa costuma ser paráfrase dessa frase.",
    "inferência": "A resposta não está escrita, mas tem que ser sustentada por uma frase do texto. Se precisar de informação de fora, está errada.",
    "vocabulário": "Substitua a palavra pela alternativa na frase original e veja se o sentido se mantém. Desconfie de falsos cognatos.",
    "conectivos e referência": "Contraste: however, although, but. Causa: because, since, due to. Conclusão: thus, therefore. Pronome: volte à frase anterior e ache o substantivo.",
    "texto científico": "Resumo de artigo segue objetivo → método → resultado → limitação. 'suggest', 'may', 'indicate' marcam interpretação, não fato.",
    "pegadinha de NOT/EXCEPT": "Marque no enunciado o NOT. Confira cada alternativa no texto e elimine as que aparecem.",
    "tempos verbais": "Murphy, units 7–21: since/for → present perfect; ontem/data fechada → past simple; hipótese → if + passado, would + verbo.",
    "voz passiva": "Se o sujeito não faz a ação (o terminal é construído), use be + particípio no tempo pedido.",
    "modais e formas verbais": "Depois de must, can, should, will vem verbo sem 'to'. Comparativo: adjetivo curto + -er; longo: more + adjetivo.",
    "pronomes relativos": "who = pessoa; which = coisa (sempre em oração entre vírgulas); that = pessoa ou coisa, nunca entre vírgulas; whose = posse.",
    "quantificadores": "Desenhe conjuntos (diagrama de Venn). 'Algum' só garante um elemento; 'todo' não garante que o conjunto tenha elementos.",
    "negação": "¬(todo A é B) = algum A não é B. ¬(algum A é B) = nenhum A é B. ¬(P e Q) = ¬P ou ¬Q. ¬(P ou Q) = ¬P e ¬Q.",
    "condicional": "P→Q equivale a ¬Q→¬P. Inválidos: afirmar o consequente (Q, logo P) e negar o antecedente (¬P, logo ¬Q). Necessário = consequente; suficiente = antecedente.",
    "argumentação": "Fortalecer = afastar outra causa possível (grupo de comparação). Enfraquecer = mostrar outra causa ou que o efeito aconteceu sem a causa. Contradizer = um contraexemplo.",
    "ordenação e verdade/mentira": "Escreva as posições numa linha e preencha primeiro as regras fixas (último, imediatamente depois). Em verdade/mentira, teste quais afirmações não podem ser verdadeiras juntas.",
    "porcentagem": "Percentuais sucessivos multiplicam (1,1 × 0,9), não somam. 'X% de Y%' = multiplicação dos dois.",
}

_TEMA_DICA = {
    "i1": ("ideia central", "Qual frase resume o texto inteiro, e não um detalhe dele?"),
    "i2": ("informação literal", "Procure 'tonne-kilometre' no texto."),
    "i3": ("conectivos e referência", "'However' liga duas ideias que se opõem ou se completam?"),
    "i4": ("vocabulário", "O custo de transbordo faz a economia aumentar ou desaparecer?"),
    "i5": ("inferência", "Releia a última frase e veja o que os 'investors' acham."),
    "i6": ("informação literal", "A resposta está na segunda frase do texto."),
    "i7": ("informação literal", "Ache 'limited range' e leia a frase até o fim: há um 'however' ali."),
    "i8": ("conectivos e referência", "'Their' é plural: qual substantivo plural fecha a frase anterior?"),
    "i9": ("informação literal", "Leia a última frase: o que o algoritmo passa a considerar?"),
    "i10": ("pegadinha de NOT/EXCEPT", "Confira as quatro estratégias listadas depois de 'several strategies'."),
    "i11": ("texto científico", "Procure o verbo 'estimate' e o que vem depois de 'with'."),
    "i12": ("texto científico", "Atenção aos sinais: ônibus melhoraram ou pioraram? Queda maior ou menor no pico?"),
    "i13": ("texto científico", "O que o verbo 'suggest' indica sobre o grau de certeza?"),
    "i14": ("texto científico", "Ache 'limitations' e confira os números: quantos sensores?"),
    "i15": ("vocabulário", "'Further' e 'farther' parecem iguais, mas um deles é distância."),
    "g1": ("voz passiva", "O terminal faz a ação ou recebe a ação?"),
    "g2": ("tempos verbais", "A segunda parte usa 'would': que condicional é essa?"),
    "g3": ("tempos verbais", "'since' indica um período que chega até agora."),
    "g4": ("modais e formas verbais", "O que vem depois de 'must'?"),
    "g5": ("pronomes relativos", "'The study' é pessoa ou coisa? E a oração está entre vírgulas."),
    "g6": ("modais e formas verbais", "'quiet' é adjetivo curto (uma sílaba e meia): -er ou more?"),
    "l1": ("quantificadores", "Desenhe: o círculo 'terminal' fica dentro do círculo 'rodovia'. Onde fica o porto seco sem rodovia?"),
    "l2": ("negação", "Para negar 'todos', basta um caso contrário."),
    "l3": ("condicional", "Se P então Q. Aconteceu não-Q. O que se conclui sobre P?"),
    "l4": ("condicional", "A entrega pode falhar por outro motivo além do atraso?"),
    "l5": ("condicional", "Inverta e negue os dois lados."),
    "l6": ("negação", "Negação de 'e' vira 'ou', com as duas partes negadas."),
    "l7": ("argumentação", "Só um caso do grupo 'manhã' fora da regra derruba o relatório."),
    "l8": ("argumentação", "Qual alternativa descarta outra explicação para a queda do fluxo?"),
    "l9": ("argumentação", "Se a queda aconteceu também onde não houve cobrança, o que isso diz sobre a causa?"),
    "l10": ("ordenação e verdade/mentira", "Comece por E (último) e pelo par fixo A-B."),
    "l11": ("porcentagem", "Calcule em duas etapas: primeiro +10%, depois −10% sobre o novo valor."),
    "l12": ("condicional", "'Necessário' fica do lado do 'então': dirigir carreta → ?"),
    "l13": ("ordenação e verdade/mentira", "I e II podem ser verdadeiras ao mesmo tempo?"),
    "l14": ("porcentagem", "25% de 60% é multiplicação."),
    "l15": ("quantificadores", "Desenhe 'rotas de X' dentro de 'passam pelo centro', e 'noturnas' fora dele."),
}

for _q_ in QUESTOES:
    _q_["tema"], _q_["dica"] = _TEMA_DICA[_q_["id"]]

GERADOR_PET = """Você elabora questões objetivas para a prova de seleção do mestrado em Engenharia de Transportes (PET/COPPE/UFRJ).
Módulo pedido: {modulo}.
- ingles: escreva UM texto original de 150 a 200 palavras, estilo artigo ou relatório técnico de transportes, logística ou mobilidade,
  e 5 questões de compreensão em inglês (ideia central, informação literal, inferência, vocabulário em contexto, referência pronominal ou conectivo).
- logica: 5 questões de raciocínio lógico em português sobre coerência de ideias em situações de transporte ou logística
  (negação, condicional, contrapositiva, falácias, quantificadores, fortalecer/enfraquecer argumento, ordenação, porcentagem).
Regras: 5 alternativas por questão, exatamente uma correta, distratores plausíveis; explicação curta em português;
confira cada gabarito antes de responder. Não use dados reais que você não tenha certeza; números do texto podem ser hipotéticos.
Para cada questão, dê uma "dica" curta em português que oriente o raciocínio SEM revelar a resposta, e um "tema" escolhido desta lista: {temas}.
Responda SOMENTE com JSON válido:
{{"texto": "... ou null", "questoes": [{{"enunciado": "...", "opcoes": ["...","...","...","...","..."], "correta": "A", "explicacao": "...", "dica": "...", "tema": "..."}}]}}"""
