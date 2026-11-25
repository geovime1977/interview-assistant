"""Caderno de treino técnico (Abertura + Cenários 1-14), em português.

Cada item tem a pergunta, o cartão telegráfico (4 linhas para olhar na hora) e a resposta padrão
para treinar em voz alta em ~60 s. `chaves` alimenta o casamento automático na tela principal:
termos técnicos (valem em PT e EN) e expressões da pergunta nas duas línguas.
"""

G = "Caderno técnico"


def _item(n, titulo, pergunta, cartao, resposta, pontos, chaves, cuidado=""):
    return dict(id=f"ct{n}", grupo=G, titulo=titulo, lingua="pt",
                pergunta_pt=pergunta, pergunta_en="", cartao=cartao,
                resposta_pt=resposta, resposta_en="", pontos=pontos,
                palavras={}, cuidado=cuidado, chaves=chaves)


CADERNO = [
    _item(0, "Abertura — trajetória e posicionamento",
          "Conte sua trajetória e como você conecta sua experiência operacional com modelos matemáticos e Python.",
          ["BASE: 30 anos Exército (AMAN) | Logística/TI | Recursos escassos",
           "FORMAÇÃO: Lic. Matemática | MBA PO | 3 artigos ENEGEP 2026",
           "STACK: Python | LP/MILP | Gurobi, OR-Tools, PuLP | FastAPI",
           "ENTREGA: Traduzir gargalos reais em motores de decisão"],
          "Sou oficial da reserva do Exército, onde atuei por 30 anos gerindo operações e recursos escassos de "
          "Comunicações e TI, sempre focado em controle de custos. Para formalizar e escalar essa visão analítica, "
          "concluí Licenciatura em Matemática, MBA em Pesquisa Operacional — com três artigos publicados no ENEGEP "
          "em 2026 — e me especializei em Python. Hoje uno essa experiência prática com modelagem LP e MILP usando "
          "Gurobi, OR-Tools, PuLP e FastAPI para transformar problemas operacionais complexos em soluções computacionais.",
          ["30 anos", "recursos escassos", "Matemática", "ENEGEP", "MILP", "Gurobi"],
          ["trajetoria", "tell me about yourself", "about yourself", "your background", "sua experiencia",
           "conte sobre voce", "experiencia operacional", "career", "carreira", "background"],
          cuidado="O roteiro diz 'concluí MBA em Pesquisa Operacional', mas o MBA de PO está em andamento "
                  "(o banco de RH já avisa: 'diga que os MBAs estão em andamento'). Troque por 'estou concluindo'."),

    _item(1, "Cenário 1 — Formulação MILP (lot sizing CLSP)",
          "Fábrica com 3 produtos, 1 linha e 4 semanas, com demanda, custos de produção/estoque/setup e tempo de "
          "setup consumindo capacidade. Formule e valide.",
          ["MODELO: CLSP (MILP) — 3 prod × 4 sem",
           "DECISÕES: x(i,t) prod (cont) | I(i,t) est (cont) | y(i,t) setup (bin)",
           "OBJETIVO/RESTR.: Min custos | Balanço estoque | Capacidade (a·x + b·y ≤ C) | Ligação x ≤ M·y (big-M apertado)",
           "VALIDAÇÃO: Viabilidade total | Casos extremos (setup 0) | Benchmark heurística"],
          "Eu modelaria como um problema clássico de Dimensionamento de Lotes com Capacidade (CLSP) em MILP. Defino "
          "variáveis contínuas para produção e estoque, e binárias para o setup de cada produto na semana. O objetivo "
          "é minimizar a soma dos custos de produção, estoque e setup. Nas restrições, coloco o balanço de estoque "
          "entre semanas, a capacidade de horas da linha somando produção e setup, e a restrição de ligação usando um "
          "big-M apertado pelo mínimo entre a demanda restante e a capacidade da semana, fortalecendo a relaxação "
          "linear. Valido checando viabilidade de capacidade, testando extremos como setup zero e comparando o ganho "
          "contra uma regra heurística.",
          ["CLSP", "binárias", "balanço de estoque", "capacidade", "big-M", "relaxação"],
          ["lot sizing", "clsp", "setup", "dimensionamento de lotes", "production planning", "planejamento da producao",
           "formule", "formulate", "big-m", "big m", "3 produtos", "three products"]),

    _item(2, "Cenário 2 — Solver lento (gap 18% após 10 min)",
          "O mesmo modelo escalou para 50 produtos e 52 semanas e travou com gap de 18% após 10 minutos. O que você faz?",
          ["DIAGNÓSTICO: Log Gurobi — limitante inferior (bound) vs. incumbent",
           "FORMULAÇÃO: Apertar big-M | Quebrar simetria | Reformular (localização)",
           "SOLVER/HEUR.: Warm start | MIPFocus=3 | Relax-and-fix / Fix-and-optimize",
           "NEGÓCIO: Alinhar gap aceitável (ex: 2%) | Horizonte rolante"],
          "Primeiro abro o log do solver para diagnosticar se o problema está no limitante inferior fraco ou na "
          "dificuldade de achar boas soluções viáveis. Em seguida, ataco a formulação, que traz o maior ganho: aperto "
          "os big-Ms, quebro simetrias entre produtos parecidos e avalio reformular o problema como localização de "
          "instalações, que tem relaxação mais justa. No solver, injeto um warm start heurístico, ajusto parâmetros "
          "como MIPFocus=3 no Gurobi e aplico heurísticas de decomposição temporal como relax-and-fix. Por fim, alinho "
          "com o negócio um gap aceitável, como 2%, operando em horizonte rolante.",
          ["log", "limitante", "simetria", "warm start", "MIPFocus", "relax-and-fix", "horizonte rolante"],
          ["gap", "slow", "lento", "travou", "too long", "demora", "converge", "convergir", "50 produtos", "52 semanas",
           "warm start", "mipfocus", "simetria", "symmetry", "time limit"]),

    _item(3, "Cenário 3 — Larga escala e decomposição (Benders)",
          "Quando usar decomposição em larga escala e como funciona a Decomposição de Benders?",
          ["QUANDO: Estrutura em blocos | Variáveis ou restrições acopladoras",
           "BENDERS: Mestre (binárias) + Subproblema LP (fluxo) → Cortes duais (otimalidade/viabilidade)",
           "OUTRAS: Relaxação Lagrangiana (penaliza) | Geração de Colunas (rotas/escalas)",
           "HONESTIDADE: Implementado em estudo/roadmap (ainda não em produção)"],
          "Uso decomposição quando o problema tem estrutura de blocos acoplados por poucas variáveis ou restrições. Na "
          "Decomposição de Benders, separamos as variáveis complicadoras — como decisões binárias de abrir centros de "
          "distribuição — num problema mestre. Com elas fixadas, o subproblema vira um LP contínuo fácil de fluxo, cujo "
          "dual devolve cortes de viabilidade ou otimalidade ao mestre até os limitantes convergirem. Também conheço "
          "Relaxação Lagrangiana e Geração de Colunas para roteirização. Vale destacar com transparência que implementei "
          "esses métodos em nível de estudo e pesquisa, ainda não em produção com cliente.",
          ["blocos", "mestre", "subproblema", "cortes", "Lagrangiana", "Geração de Colunas", "transparência"],
          ["benders", "decomposicao", "decomposition", "larga escala", "large scale", "lagrang", "column generation",
           "geracao de colunas", "master problem", "problema mestre"]),

    _item(4, "Cenário 4 — Simulação vs. otimização (Monte Carlo)",
          "Quando usar simulação em vez de otimização e como validar uma simulação de Monte Carlo?",
          ["DIFERENÇA: Otimização = melhor decisão | Simulação = testa incerteza e dinâmica",
           "HÍBRIDO: Otimizar plano → Simular robustez na operação",
           "VALIDAÇÃO MC: Réplicas (IC da média) | Seed fixa | Correlação (Cholesky) | Analítico (M/M/c)",
           "EXEMPLO: Caso VPL — isolar correlação com gráfico Tornado"],
          "A otimização busca a melhor decisão dado um cenário, enquanto a simulação avalia como essa decisão se "
          "comporta sob incerteza, filas e regras dinâmicas. Na prática, o padrão é otimizar o plano e simular sua "
          "execução. Para validar um Monte Carlo, dimensiono o número de réplicas pelo intervalo de confiança da média, "
          "fixo a semente para reprodutibilidade, preservo correlações entre variáveis via decomposição de Cholesky e "
          "comparo cenários simplificados com soluções analíticas, como filas M/M/c. Em um projeto de VPL, por exemplo, "
          "usei gráfico tornado para isolar um efeito falso de correlação entre variáveis.",
          ["incerteza", "réplicas", "intervalo de confiança", "semente", "Cholesky", "M/M/c", "tornado"],
          ["simulacao", "simulation", "monte carlo", "replicas", "replications", "cholesky", "tornado", "seed",
           "semente", "m/m/c", "queue", "fila"]),

    _item(5, "Cenário 5 — Previsão de demanda para o modelo",
          "Como você prevê a demanda semanal para alimentar o modelo prescritivo e como valida?",
          ["MODELOS: Baseline (ingênuo sazonal) → Holt-Winters/SARIMA → ML (XGBoost com lags)",
           "VALIDAÇÃO: Janela deslizante (rolling origin) — nunca split aleatório",
           "MÉTRICAS: MAE, RMSE e WAPE (quando há zeros)",
           "INTEGRAÇÃO: Absorver erro via estoque de segurança ou otimização estocástica"],
          "Sempre começo por um baseline simples, como o ingênuo sazonal, depois avanço para Holt-Winters ou SARIMA, e "
          "só parto para Machine Learning — como Gradient Boosting com defasagens e feriados — se superar o baseline. "
          "Na validação, uso estritamente janela deslizante temporal, nunca divisão aleatória, para evitar vazamento do "
          "futuro, medindo MAE e WAPE por lidar bem com demanda zerada. Como toda previsão tem erro, conecto ao modelo "
          "de otimização dimensionando estoques de segurança pela distribuição dos resíduos ou gerando cenários para "
          "otimização estocástica.",
          ["baseline", "Holt-Winters", "SARIMA", "janela deslizante", "WAPE", "estoque de segurança"],
          ["forecast", "previsao", "demanda semanal", "weekly demand", "sarima", "holt", "arima", "xgboost",
           "rolling", "wape", "demand forecasting"]),

    _item(6, "Cenário 6 — Do notebook à produção (CI/CD, DevSecOps)",
          "O modelo funciona no notebook. Como você leva para produção com boas práticas?",
          ["ORIGEM: Sem Jupyter — VSCode + terminal | Módulos dados / modelagem / solver",
           "API/TESTES: FastAPI + validação de entrada | pytest (balanço e capacidade respeitados)",
           "INFRA/CI: Docker | GitHub Actions roda os testes a cada push",
           "DEVSECOPS: Chave/licença em variável de ambiente | Auditoria de dependências | Logs status/tempo"],
          "Na verdade, eu nem uso Jupyter; já desenvolvo direto no VSCode e no terminal como software estruturado, "
          "separando dados, modelagem e solver em módulos Python. Exponho o motor via FastAPI com validação de entrada, "
          "garanto a qualidade com pytest — validando inclusive se balanço e capacidade são respeitados — e empacoto "
          "tudo em contêineres Docker. Nas esteiras de CI/CD, como GitHub Actions, automatizo os testes e aplico "
          "práticas de DevSecOps: nunca deixo chaves ou licenças de solver no código, uso variáveis de ambiente, "
          "auditoria de dependências e logs de status e tempo de execução.",
          ["VSCode", "módulos", "FastAPI", "pytest", "balanço e capacidade", "Docker", "variáveis de ambiente"],
          ["notebook", "producao", "production", "deploy", "ci/cd", "pipeline", "docker", "devops", "devsecops",
           "github actions", "fastapi", "best practices", "boas praticas"],
          cuidado="'Auditoria de dependências': nenhum workflow do GitHub em ~/projetos roda pip-audit (conferido em "
                  "25/11). Se perguntarem qual ferramenta, diga 'pip-audit' e que roda localmente, ou ponha no CI antes."),

    _item(7, "Cenário 7 — Modelo voltou inviável",
          "O modelo rodou com dados do cliente e retornou status Inviável. Como você resolve?",
          ["1. COMEÇO — DADOS: Erro de cadastro: unidade trocada, demanda negativa, prazo impossível, capacidade 0 (manutenção)",
           "2. MEIO — SOLVER: computeIIS (menor conjunto em conflito) | Solver aberto: folga com penalidade alta",
           "3. FIM — NEGÓCIO: Validar o déficit | 'Faltam 120 h de máquina na semana 7'",
           "4. OPÇÕES: Hora extra | Antecipar produção | Negociar atraso"],
          "Primeiro eu audito os dados de entrada antes de mexer no código, porque na prática a maioria das "
          "inviabilidades vem de erro de cadastro — como unidades de medida trocadas, demanda negativa, prazo impossível "
          "ou capacidade zerada por manutenção.\n\n"
          "Se os dados estão íntegros, eu uso o computeIIS do Gurobi para isolar o menor subconjunto de restrições que "
          "estão entrando em conflito. Caso estivesse usando um solver aberto sem essa função nativa, eu adicionaria "
          "variáveis de folga com penalidade muito alta nas restrições críticas para descobrir exatamente onde o modelo "
          "precisa 'estourar' para ficar viável.\n\n"
          "Com o conflito isolado, eu valido o tamanho do déficit e levo a solução em linguagem de negócio para o "
          "gestor — por exemplo: explicando que faltam 120 horas de máquina na semana 7 e apresentando as alternativas "
          "concretas de autorizar hora extra, antecipar produção ou negociar atraso.",
          ["cadastro", "unidades", "computeIIS", "folga", "penalidade", "déficit", "hora extra"],
          ["inviavel", "infeasible", "infeasibility", "inviabilidade", "iis", "computeiis", "slack", "folga"]),

    _item(8, "Cenário 8 — Comunicação executiva (diretor desconfiado)",
          "O diretor não entende de matemática e desconfia do plano gerado. Como você convence?",
          ["ABERTURA: Empresa busca lucro → ganho financeiro primeiro (~15% vs. regra atual)",
           "PORQUÊ: Exemplo concreto da operação (ex: agrupar lote pelo setup)",
           "SENSIBILIDADE: Preço-sombra (\"1h extra vale R$ Y\") e trade-offs",
           "CONFIANÇA: Painel interativo (Streamlit) para testar cenários"],
          "Toda empresa busca lucro, seja reduzindo custos ou aumentando vendas. Então eu começaria mostrando direto o "
          "ganho financeiro: que o modelo matemático reduz em cerca de 15% os custos em relação à regra atual da "
          "operação. Explicaria o motivo com um exemplo concreto e usando o preço-sombra — mostrando quanto vale "
          "financeiramente aliviar cada gargalo. Para ele ganhar confiança na prática, eu entregaria um painel "
          "interativo em Streamlit onde o próprio gestor pode alterar as premissas e simular cenários em tempo real.",
          ["lucro", "ganho financeiro", "regra atual", "exemplo concreto", "preço-sombra", "Streamlit"],
          ["diretor", "director", "executive", "executivo", "stakeholder", "convence", "convince", "desconfia",
           "does not trust", "doesn't trust", "nao entende", "non-technical", "explain to", "manager"],
          cuidado="'Cerca de 15%' não tem fonte: é um número de exemplo. Diga 'por exemplo, 15%' ou 'no meu caso de "
                  "estudo...' (o R$ 5,1 mi do CV é de dados construídos). Nunca como resultado medido em cliente."),

    _item(9, "Cenário 9 — Python na prática (estruturas e performance)",
          "Como você usa estruturas de dados e otimiza a montagem de modelos grandes em Python?",
          ["ESTRUTURAS: Tuplas/Dicionários esparsos | set busca O(1) | Listas ordenadas",
           "PERFORMANCE: Evitar iterrows() | Vetorização NumPy / gp.tupledict",
           "ROBUSTEZ: Tipagem estática | Tratar status (OPTIMAL, TIME_LIMIT, INFEASIBLE)"],
          "Em modelos grandes, nunca crio matrizes densas cheias de zeros; indexo variáveis e parâmetros usando "
          "dicionários e tuplas apenas para combinações válidas, usando sets para checagem rápida em O(1). Evito loops "
          "lentos como iterrows no Pandas, preferindo vetorização com NumPy e estruturas nativas como tupledict do "
          "Gurobi para montar restrições rapidamente. Além disso, separo a camada de dados da formulação e trato "
          "explicitamente todos os retornos possíveis do solver, como limite de tempo ou inviabilidade.",
          ["dicionários", "tuplas", "sets", "iterrows", "vetorização", "tupledict"],
          ["estruturas de dados", "data structures", "dictionary", "dicionario", "iterrows", "numpy", "tupledict",
           "performance", "python", "vectoriz", "vetoriz"]),

    _item(10, "Cenário 10 — SQL para preparação de dados",
          "Como você estrutura consultas SQL para preparar históricos de demanda e estoque para os modelos?",
          ["FILTROS: WHERE antes de agregar | HAVING depois do GROUP BY",
           "WINDOW FUNC: LAG(), LEAD(), RANK() OVER (PARTITION BY ... ORDER BY ...)",
           "LIMPEZA: CTEs (WITH) modulares | COALESCE | Cuidado com JOIN duplicado"],
          "Estruturo consultas complexas usando CTEs para manter legibilidade e facilitar validação etapa por etapa. "
          "Uso WHERE para filtrar registros brutos antes da agregação e HAVING apenas após o GROUP BY. Para criar "
          "variáveis temporais, como demanda acumulada ou estoque da semana anterior sem perder granularidade, uso "
          "Window Functions com OVER PARTITION BY produto ORDER BY semana, tratando nulos com COALESCE e validando "
          "cardinalidade nos JOINs para não duplicar demanda.",
          ["CTE", "WHERE", "HAVING", "window", "PARTITION BY", "COALESCE", "JOIN"],
          ["sql", "query", "consulta", "cte", "window function", "partition", "having", "join", "group by"]),

    _item(11, "Cenário 11 — Machine Learning aplicado",
          "Quais cuidados você toma com vazamento de dados, overfitting e escolha de métricas em ML?",
          ["LEAKAGE: fit só no treino dentro de Pipeline | Split temporal em séries",
           "OVERFITTING: Validação cruzada | Regularização L1/L2 | Poda em árvores",
           "MÉTRICAS: Regressão = MAE/RMSE/WAPE | Desbalanceado = Precision, Recall, PR-AUC"],
          "Para evitar data leakage, encapsulo todo pré-processamento, escalonamento e imputação dentro de um Pipeline "
          "ajustado exclusivamente nos dados de treino, usando validação temporal em séries. Controlo overfitting com "
          "validação cruzada, regularização L1/L2 e ajuste de profundidade e taxa de aprendizado em modelos baseados em "
          "árvores. Na avaliação, escolho a métrica pelo negócio: MAE ou WAPE para demanda, e Precision, Recall e "
          "PR-AUC em problemas de classificação desbalanceada, onde acurácia engana.",
          ["Pipeline", "treino", "validação cruzada", "regularização", "Precision", "Recall"],
          ["leakage", "vazamento", "overfitting", "machine learning", "ml", "cross validation", "validacao cruzada",
           "regulariz", "precision", "recall", "metricas", "metrics"]),

    _item(12, "Cenário 12 — Roteirização (VRP) e CP-SAT",
          "Você tem projetos com OR-Tools e roteirização. Como você modela um problema de roteirização de veículos "
          "(VRP) com janelas de tempo e capacidade, e quando escolhe CP-SAT em vez de um solver MILP tradicional?",
          ["VRP: Grafo/Arcos válidos (set) | Capacidade veículo | Janelas de tempo ([a_i, b_i])",
           "ESCOLHA: Inteiro puro / Combinatória / Escalonamento → CP-SAT (OR-Tools) | Contínuas + Inteiros → MILP (Gurobi)",
           "PERFORMANCE: Matriz de distâncias pré-calculada | Meta-heurísticas (Guided Local Search)",
           "PROJETO: Citar seu repositório palestra-roteirizacao"],
          "Em um VRP com capacidade e janelas de tempo, modelo sobre um grafo direcionado filtrando apenas arcos "
          "viáveis, controlando o fluxo binário entre clientes, a carga acumulada e o horário de chegada dentro das "
          "janelas. Escolho o CP-SAT do OR-Tools quando o problema é puramente inteiro ou fortemente combinatório — "
          "como sequenciamento e escalas — porque programação por restrições propaga domínios muito mais rápido que um "
          "Branch-and-Bound tradicional; já quando há fluxo contínuo relevante junto com decisões discretas, vou para "
          "MILP no Gurobi. No meu projeto de roteirização, uso meta-heurísticas como Guided Local Search para escalar bem.",
          ["arcos viáveis", "carga", "janelas", "CP-SAT", "combinatório", "MILP", "Guided Local Search"],
          ["vrp", "routing", "roteirizacao", "roteamento", "vehicle", "veiculos", "time window", "janela de tempo",
           "janelas de tempo", "cp-sat", "cpsat", "cp sat", "or-tools", "ortools", "constraint programming"],
          cuidado="O palestra-roteirizacao não importa OR-Tools nem usa Guided Local Search: é um app Streamlit de "
                  "palestra (conferido em 25/11). Diga 'na palestra de roteirização apresentei...' ou implemente antes."),

    _item(13, "Cenário 13 — Não ficar preso a um solver (Pyomo/PuLP/Gurobi/OR-Tools)",
          "Em um projeto novo na Compass UOL, o cliente ainda não definiu se vai pagar licença comercial ou usar "
          "open-source. Como você arquiteta o código para não ficar preso a um único solver?",
          ["ARQUITETURA: Desacoplar formulação matemática da interface do solver (Padrão Adapter/Strategy)",
           "FERRAMENTAS: Pyomo ou PuLP (agnósticos) vs. Gurobi (API nativa mais rápida)",
           "ESTRATÉGIA: Prototipar com HiGHS / CBC / OR-Tools → Escalar para Gurobi se precisar",
           "HONESTIDADE: Domínio em Gurobi/PuLP/OR-Tools; transição natural para Pyomo"],
          "Eu desacoplo a camada de regras de negócio e dados da camada de otimização usando uma interface limpa. Se a "
          "portabilidade entre solvers for prioridade desde o dia um, bibliotecas algébricas como Pyomo ou PuLP "
          "permitem trocar o motor sem reescrever o modelo — começando com solvers abertos como HiGHS ou CBC e migrando "
          "para Gurobi ou CPLEX caso o volume exija. Tenho experiência prática intensa com Gurobi, PuLP e OR-Tools, e "
          "como a lógica algébrica é a mesma, a adaptação ao Pyomo em qualquer projeto é imediata.",
          ["desacoplo", "interface", "Pyomo", "PuLP", "HiGHS", "CBC", "Gurobi"],
          ["licenca", "license", "open-source", "open source", "preso", "locked", "vendor", "pyomo", "pulp", "highs",
           "cbc", "cplex", "solver agnostic", "trocar o solver", "switch solver"],
          cuidado="O banco de RH já afirma portfólio em Pyomo (tc1: planta química em Pyomo e OR-Tools). "
                  "'Transição natural para Pyomo' subestima o que você já fez: diga que já usa Pyomo."),

    _item(14, "Cenário 14 — Sensibilidade, preço-sombra e pós-otimização",
          "Depois que o modelo encontra a solução ótima, o trabalho não acaba. Como você extrai insights de "
          "pós-otimalidade para apoiar decisões estratégicas, especialmente em um modelo MILP?",
          ["PÓS-OTIMALIDADE: Folgas das restrições (gargalos ativos) | Preço-sombra | Custo reduzido",
           "CUIDADO MILP: MILP não tem dual direto → Fixar binárias e resolver o LP residual",
           "CENÁRIOS: Análise paramétrica (variar demanda/custo ±10%)",
           "DECISÃO: Identificar onde investir (ex: expandir capacidade onde o preço-sombra é alto)"],
          "Após obter o ótimo, analiso primeiro as folgas das restrições para identificar quais recursos estão "
          "saturados e são os verdadeiros gargalos da operação. Como em modelos MILP não existe preço-sombra direto por "
          "conta da não-convexidade das variáveis inteiras, eu fixo as variáveis binárias na solução ótima e resolvo o "
          "problema linear residual para extrair o valor marginal de cada recurso e o custo reduzido das variáveis fora "
          "da base. Complemento com análise de sensibilidade paramétrica variando demanda e custos para mostrar ao "
          "gestor onde investir primeiro.",
          ["folgas", "gargalos", "fixo as variáveis binárias", "LP residual", "custo reduzido", "paramétrica"],
          ["sensibilidade", "sensitivity", "shadow price", "preco-sombra", "preco sombra", "dual", "reduced cost",
           "custo reduzido", "pos-otim", "post-optim", "parametric", "parametrica", "after the optimal"]),
]


GD = "Dicionário de bolso"

# (id, categoria, termo, definição) — para falar com segurança; o termo vira "O que é X?" no banco.
_TERMOS = [
    ("mipgap", "PO e Matemática", "MIP Gap",
     "Não é a solução ótima: é a distância percentual até a garantia de otimalidade. É a diferença entre a melhor "
     "solução real já encontrada (incumbent) e o limite teórico da relaxação linear (best bound). Com 0% o solver "
     "provou que a solução é ótima. Na prática paramos com 1% ou 2%, porque a solução já é excelente e economiza "
     "horas de processamento."),
    ("lp", "PO e Matemática", "LP (Programação Linear)",
     "Modelo em que todas as variáveis podem ser contínuas, números quebrados (ex.: produzir 14,5 litros). Resolve muito rápido."),
    ("milp", "PO e Matemática", "MILP (Programação Inteira Mista)",
     "Mistura variáveis contínuas com inteiras ou binárias (0 ou 1, ex.: abrir ou não uma fábrica). Muito mais difícil de resolver."),
    ("bigm", "PO e Matemática", "Big-M",
     "Número grande que liga uma variável contínua a uma binária (\"só pode produzir se ligar a máquina\"). Deve ser "
     "apertado — o menor valor que não corta solução válida — para o solver rodar rápido."),
    ("iis", "PO e Matemática", "IIS (computeIIS)",
     "Irreducible Inconsistent Subsystem: comando do Gurobi que aponta o menor grupo de restrições que brigam entre si "
     "quando o modelo dá inviável."),
    ("sombra", "PO e Matemática", "Preço-sombra (shadow price)",
     "Quanto o lucro sobe (ou o custo cai) se ganhar 1 unidade a mais de um recurso no gargalo (ex.: 1 hora extra de máquina vale R$ 150)."),
    ("custored", "PO e Matemática", "Custo reduzido",
     "Quanto o custo de uma opção que ficou fora da solução precisa cair para valer a pena usá-la."),
    ("gurobi", "Solvers e bibliotecas", "Gurobi / CPLEX",
     "Solvers comerciais de altíssima performance: os motores mais rápidos do mercado para LP e MILP."),
    ("ortools", "Solvers e bibliotecas", "OR-Tools",
     "Biblioteca aberta do Google; excelente para roteirização (VRP) e problemas inteiros/combinatórios, com o motor CP-SAT."),
    ("pulp", "Solvers e bibliotecas", "PuLP / Pyomo",
     "Bibliotecas Python para escrever a matemática do modelo de forma organizada e mandar para um solver (CBC, HiGHS ou Gurobi)."),
    ("numpy", "Solvers e bibliotecas", "NumPy / Pandas / SciPy",
     "Base do Python científico: tabelas (Pandas), cálculo matricial rápido (NumPy), estatística e otimização básica (SciPy)."),
    ("sqlwhere", "Dados, estatística e ML", "SQL: WHERE vs. HAVING",
     "WHERE filtra linhas antes de agrupar; HAVING filtra grupos depois do GROUP BY."),
    ("window", "Dados, estatística e ML", "Window functions (OVER PARTITION BY)",
     "Cálculos ao longo do tempo — soma acumulada, valor da semana anterior — sem misturar as linhas de produtos diferentes."),
    ("leakage", "Dados, estatística e ML", "Data leakage (vazamento de dados)",
     "Informação do futuro ou do conjunto de teste vaza para o treino e gera falsa precisão."),
    ("overfit", "Dados, estatística e ML", "Overfitting",
     "O modelo decora o treino, inclusive o ruído, e vai mal com dados novos."),
    ("rolling", "Dados, estatística e ML", "Rolling origin (janela deslizante)",
     "Validação correta de previsão no tempo: treina até a semana 10 e prevê a 11; depois treina até a 11 e prevê a 12. "
     "Nunca embaralha datas."),
    ("montecarlo", "Dados, estatística e ML", "Simulação de Monte Carlo",
     "Rodar milhares de cenários sorteando valores para as variáveis incertas (demanda, preço) para medir o risco de uma decisão."),
    ("fastapi", "Engenharia de software", "FastAPI",
     "Framework Python que transforma o código de otimização numa API: recebe dados em JSON e devolve o plano ótimo."),
    ("docker", "Engenharia de software", "Docker",
     "Empacota código, bibliotecas e solver num contêiner, para rodar igual no seu computador e no servidor da empresa."),
    ("git", "Engenharia de software", "Git / GitHub",
     "Controle de versão: guarda o histórico do código e permite trabalhar em equipe sem sobrescrever o trabalho dos outros."),
    ("cicd", "Engenharia de software", "CI/CD",
     "Esteira automática (ex.: GitHub Actions) que roda os testes a cada código novo, para garantir que nada quebrou antes de ir ao ar."),
    ("devsecops", "Engenharia de software", "DevSecOps",
     "Segurança desde o início: nunca escrever senha ou licença do Gurobi no código (usar variável de ambiente) e checar "
     "vulnerabilidades das bibliotecas."),
    ("streamlit", "Engenharia de software", "Streamlit",
     "Biblioteca Python para painéis interativos em poucos minutos, ideal para o diretor simular cenários."),
]

DICIONARIO = [
    dict(id=f"dc_{i}", grupo=GD, titulo=termo, lingua="pt", categoria=cat,
         pergunta_pt=f"O que é {termo}?", pergunta_en="", cartao=[], resposta_pt=defin, resposta_en="",
         pontos=[], palavras={}, cuidado="", chaves=[])
    for i, cat, termo, defin in _TERMOS
]
