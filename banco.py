"""Banco de respostas preparadas para a entrevista Compass UOL (AI/R), vaga Python Data Science (PO).

Fonte: notas do vault "Simulacao RH — Compass UOL", "Prep Entrevista — Compass UOL — 2026-11-13" e
"Vaga Compass UOL - Python Data Science PO". Só fatos reais; o que está entre colchetes é para completar.
Material de estudo e treino: decorar antes, não ler durante a entrevista.
"""

BANCO = [
    # ───────────────────────── RH
    dict(id="rh1", grupo="RH", titulo="Tell me about yourself",
         pergunta_en="Tell me about yourself and what brought you to this position.",
         pergunta_pt="Me conta sobre você e o que te trouxe até esta vaga.",
         resposta_en=(
             "Today I work with applied Operations Research. I take a decision problem, write it as a mathematical model, "
             "implement it in Python and deliver a result that someone can use to decide.\n\n"
             "I got here by an unusual path. I was an Army officer for thirty years, from 1995 to 2025, and I retired as a colonel. "
             "A large part of that time was planning with scarce resources: I led the Logistics Department for five years and "
             "managed communications and IT equipment. It was about deciding under uncertainty, with limited budget, time and people.\n\n"
             "During the transition, I realized this has a name: it is exactly what an optimization model formalizes. "
             "So I built the foundation: a degree in Mathematics, an MBA in AI for Business, and I am currently taking MBAs in "
             "Operations Research and in Corporate Finance.\n\n"
             "And I went to practice. I work as an independent consultant, I have a portfolio of Python models with Pyomo, "
             "OR-Tools and Gurobi, and I presented three Operations Research papers at ENEGEP in October. For this position, "
             "I built a project that follows the job description: a chemical plant with stoichiometry, solved in Pyomo and OR-Tools, "
             "with net present value in real terms, a FastAPI service, PostgreSQL and automated tests.\n\n"
             "What attracts me to Compass is putting optimization into production for real clients, in a team that delivers software, "
             "not just reports."),
         resposta_pt=("Hoje trabalho com Pesquisa Operacional aplicada... 30 anos oficial do Exército (1995–2025), chefiei o Departamento "
                      "de Logística por 5 anos... isso tem nome: otimização... Matemática, MBA em IA, cursando MBAs de PO e Finanças... "
                      "consultor independente, portfólio em Pyomo/OR-Tools/Gurobi, 3 artigos no ENEGEP... montei um projeto que segue a "
                      "descrição da vaga... o que me atrai é colocar otimização em produção para clientes reais."),
         pontos=["Operations Research", "thirty years", "Logistics Department", "optimization", "ENEGEP", "Pyomo", "production"],
         palavras={"Operations Research": "ó-pe-RÊI-chans RÍ-sârtch", "stoichiometry": "stói-ki-Ó-me-tri",
                   "Pyomo": "pai-Ô-mou", "colonel": "KÂR-nel (o 'l' do meio não soa)"},
         cuidado="Comece pelo presente e termine na empresa. Diga que os MBAs estão em andamento. Cerca de 1,5 a 2 minutos."),

    dict(id="rh2", grupo="RH", titulo="Why now? Do you miss the Army?",
         pergunta_en="Why data and optimization, and why now? Do you miss the Army? How will it be to leave the hierarchy for a tech team?",
         pergunta_pt="Por que dados e otimização, e por que agora? Sente falta do Exército? Como vai ser sair da hierarquia para um time de tecnologia?",
         resposta_en=(
             "Why now: I completed thirty years of service and retired in April 2025. It was the natural end of a cycle, "
             "and I had been preparing since 2023.\n\n"
             "Why optimization: in the Army, many logistics decisions were based on experience, under pressure and with few resources. "
             "It worked, but I always wanted a way to compare alternatives and defend the choice with numbers. When I studied "
             "Operations Research, I saw it was exactly that. I am not changing subjects: I am doing the same work with a better tool.\n\n"
             "Do I miss it: the people, yes. The routine, no. And what I liked most, planning, I brought with me.\n\n"
             "About adapting: since 2023 I have worked as an independent consultant, with no hierarchy at all: the client defines the problem. "
             "I learned Python and optimization on my own, with public, tested code, and I wrote three papers with co-authors, "
             "discussing as equals. And I have no problem being led by someone younger. In a technical team, whoever knows the problem "
             "best leads, and I am also here to learn."),
         resposta_pt=("Completei 30 anos e fui para a reserva em abril de 2025... queria comparar alternativas e defender a escolha com números... "
                      "sinto falta das pessoas, não da rotina... consultor independente desde 2023, aprendi Python sozinho, artigos com coautores... "
                      "nenhum problema em ser liderado por alguém mais novo."),
         pontos=["April 2025", "compare alternatives", "better tool", "independent consultant", "led by someone younger"],
         palavras={"hierarchy": "RÁI-ar-ki", "co-authors": "kou-Ó-thârs", "consultant": "kân-SÂL-tant"},
         cuidado="Não reclame do Exército nem diga 'tudo tem seu tempo'. A frase sobre ser liderado por alguém mais novo é a que mais tranquiliza."),

    dict(id="rh3", grupo="RH", titulo="How is your English?",
         pergunta_en="How is your English? Could you take part in a technical meeting in English?",
         pergunta_pt="Como está o seu inglês? Conseguiria participar de uma reunião técnica em inglês?",
         resposta_en=(
             "My English is intermediate. I read technical documentation and papers every day, and I write documentation and code "
             "comments in English. In a technical meeting I can follow the discussion and explain a model, especially with the material "
             "on screen. Spontaneous conversation is what I am still developing, and I prepare in advance for every meeting in English. "
             "[My plan: X hours a week of conversation, method.] Does this project have meetings in English from the start?"),
         resposta_pt=("Intermediário, como no CV... leio documentação todo dia, escrevo READMEs... acompanho reunião técnica com material na tela... "
                      "a conversa espontânea ainda estou desenvolvendo... [plano real]... o projeto tem reuniões em inglês desde o começo?"),
         pontos=["intermediate", "documentation", "explain a model", "still developing", "prepare in advance"],
         palavras={"intermediate": "in-ter-MÍ-di-ât", "spontaneous": "spon-TÊI-ni-âs", "documentation": "do-kiu-men-TÊI-shân"},
         cuidado="Nunca diga 'artifícios de tradução' ou 'uso tradutor'. Complete o plano real antes da entrevista."),

    dict(id="rh4", grupo="RH", titulo="A difficult situation (STAR)",
         pergunta_en="Tell me about a difficult situation: what happened, what did you do and what was the result?",
         pergunta_pt="Me conta sobre uma situação difícil: o que aconteceu, o que você fez e qual foi o resultado?",
         resposta_en=(
             "Situation: in 2011, during the operation in the Complexo do Alemão, I was the head of the electronic warfare team. "
             "In the middle of the operation, the communications equipment we were using started to fail.\n\n"
             "Task: we had to decide quickly which equipment to use instead, without compromising the mission. Most of the group "
             "preferred one option, option A.\n\n"
             "Action: another team member and I compared the options against the mission requirements. Option B had longer range and "
             "a battery with more autonomy; the downside was that it was heavier. We judged that range and autonomy mattered more than "
             "weight for that mission. Even as the team leader, I chose not to impose: we presented the comparison to the group and "
             "convinced them with arguments, without friction.\n\n"
             "Result: equipment B worked and the mission was accomplished.\n\n"
             "Lesson: I learned to accept the group's decision when it is good, and when I disagree, to change it with arguments, "
             "never with rank. Looking back, it was a multi-criteria decision: range, autonomy, weight. Today I would structure it "
             "with a method like AHP, weighting the criteria and showing the group why option B wins. That kind of problem is what "
             "led me to Operations Research."),
         resposta_pt=("2011, Complexo do Alemão, chefe da turma de guerra eletrônica, equipamento falhando... grupo preferia A... "
                      "B: mais alcance e autonomia, porém mais pesado... não impus, convencemos com argumentos... missão cumprida... "
                      "hoje estruturaria com AHP."),
         pontos=["2011", "electronic warfare", "range", "autonomy", "heavier", "not to impose", "mission was accomplished", "AHP"],
         palavras={"warfare": "UÓR-fér", "autonomy": "ó-TÓ-no-mi", "weight": "UÊIT (o 'gh' não soa)", "criteria": "krai-TÍ-ri-a"},
         cuidado="Sem detalhe operacional (modelo de equipamento, frequências, o que era monitorado)."),

    dict(id="rh5", grupo="RH", titulo="Studies and a full-time job",
         pergunta_en="You are doing two MBAs and applying for a master's degree. How will you balance that with a full-time job?",
         pergunta_pt="Você faz dois MBAs e se candidata a mestrado. Como vai conciliar com uma vaga de tempo integral?",
         resposta_en=(
             "Work comes first. My studies fit outside working hours.\n\n"
             "The master's degree is in Production Engineering, in the evening, with no exclusive dedication, and it is closely related to "
             "this position: optimization and decision support. What I study there goes back into the project, and what I learn in the "
             "project feeds the research. [Program name and start date.]\n\n"
             "The MBAs are also outside working hours [and they end in ...].\n\n"
             "And this is not a bet: this year I have already balanced the MBAs, consulting, my portfolio and three papers presented at "
             "ENEGEP. I organize my time the way I organized an operation: priority, deadline and delivery."),
         resposta_pt="O trabalho vem em primeiro lugar... mestrado à noite, sem exclusividade... MBAs fora do horário... este ano já conciliei tudo.",
         pontos=["Work comes first", "evening", "decision support", "already balanced", "priority, deadline and delivery"],
         palavras={"master's degree": "MÉS-târz di-GRÍ", "dedication": "de-di-KÊI-shân"},
         cuidado="Diga 'o trabalho desta vaga', não 'o que vamos trabalhar'. Complete programa, início e término dos MBAs."),

    dict(id="rh6", grupo="RH", titulo="Main weakness",
         pergunta_en="What is your main weakness today, and what are you doing about it?",
         pergunta_pt="Qual o seu principal ponto fraco hoje? E o que está fazendo a respeito?",
         resposta_en=(
             "My main weakness today is that I have never worked inside a software development team. Teamwork I have plenty of, from "
             "thirty years in the Army, but I built my code projects on my own, in consulting and in my portfolio. In a consultancy "
             "like Compass the routine is different: code review, shared tasks, team standards, short delivery cycles.\n\n"
             "What I already do about it: even alone, I work as if I were in a team. My repository has automated tests, a minimum "
             "coverage requirement, continuous integration on GitHub and documentation, so that someone else can understand, run "
             "and change the code safely.\n\n"
             "What I will do: in the first months, I want my code to go through review, to learn the team's workflow and adapt to "
             "the house standards. Learning from people who already work this way is one of the things that attract me most to this position."),
         resposta_pt="Nunca trabalhei numa equipe de software... já faço testes, cobertura, CI... vou pedir revisão de código e aprender o fluxo do time.",
         pontos=["software development team", "automated tests", "continuous integration", "code review", "learn"],
         palavras={"weakness": "UÍK-nes", "coverage": "KÂ-ve-ridj", "workflow": "UÂRK-flou"},
         cuidado="Não diga que já trabalha com pull requests: os commits foram direto na branch principal. Cite só um ponto fraco."),

    dict(id="rh7", grupo="RH", titulo="Do you have questions for us?",
         pergunta_en="Do you have any questions for us?",
         pergunta_pt="Você tem alguma pergunta para nós?",
         resposta_en=(
             "Yes, three.\n\n"
             "First: what would my day-to-day look like? One project dedicated to a client, or several demands at the same time? "
             "And who would I work with most closely in the optimization team?\n\n"
             "Second: I saw that the AI/R group is growing in the United States, with the acquisition of Oak Rocket. Does this "
             "optimization team serve clients here or abroad? And the job description mentions stoichiometry and net present value: "
             "is the project in the chemical industry?\n\n"
             "Third: what do you expect me to deliver in the first six months for you to consider the hire a success?"),
         resposta_pt=("1) Dia a dia: projeto dedicado ou várias demandas? Com quem trabalharia? 2) AI/R crescendo nos EUA (Oak Rocket): "
                      "clientes daqui ou de fora? É indústria química? 3) O que esperam nos primeiros seis meses?"),
         pontos=["day-to-day", "Oak Rocket", "here or abroad", "chemical industry", "first six months"],
         palavras={"acquisition": "é-kui-ZÍ-shân", "abroad": "â-BRÓD", "chemical": "KÉ-mi-kâl"},
         cuidado="Não pergunte salário, férias ou aumento nesta etapa (condições já aceitas)."),

    # ───────────────────────── PERFIL
    dict(id="pf1", grupo="Perfil", titulo="The R$ 5.1M case (CV)",
         pergunta_en="Your CV mentions savings of R$ 5.1 million a year. Which client was that, and how was it measured?",
         pergunta_pt="Seu CV cita economia de R$ 5,1 milhões por ano. Qual cliente e como foi medido?",
         resposta_en=(
             "That is a case I modeled in my Gurobi sprint, with constructed data to reproduce a typical distribution network problem: "
             "six distribution centers and ten regions. The 5.1 million is the difference between the optimal solution and the naive "
             "allocation, each region served by the nearest center, inside the case itself. It is not a saving measured at a client. "
             "What it shows is the method: fixed opening costs, capacity, and a test with 20 percent demand growth."),
         resposta_pt="Caso de estudo do sprint de Gurobi, dados construídos, 6 CDs e 10 regiões... não é economia medida em cliente... mostra o método.",
         pontos=["constructed data", "not a saving measured at a client", "method", "capacity"],
         palavras={"constructed": "kân-STRÂK-ted", "naive": "nai-ÍV"},
         cuidado="Antecipe, não espere a pergunta. Nunca apresente como resultado de cliente."),

    dict(id="pf2", grupo="Perfil", titulo="Eixo Estratégico: is it a company?",
         pergunta_en="Tell me about Eixo Estratégico. Is it your company?",
         pergunta_pt="Fale sobre a Eixo Estratégico. É a sua empresa?",
         resposta_en=(
             "I work as an independent consultant under the Eixo Estratégico brand, still without a registered company. "
             "Formalization will come with the first recurring contract."),
         resposta_pt="Atuo como consultor independente sob a marca Eixo Estratégico, ainda sem CNPJ; a formalização vem com o primeiro contrato recorrente.",
         pontos=["independent consultant", "brand", "without a registered company"],
         palavras={"formalization": "for-mâ-lai-ZÊI-shân", "recurring": "ri-KÂR-ing"},
         cuidado="Nunca deixar entender que é empresa com equipe e faturamento. Não use 'founder'."),

    dict(id="pf3", grupo="Perfil", titulo="No corporate experience",
         pergunta_en="You have never worked at a large private company. Why should we hire you?",
         pergunta_pt="Você nunca trabalhou em empresa privada grande. Por que deveríamos contratar você?",
         resposta_en=(
             "I have no experience at a large company. What I have is verifiable delivery: public repositories with tests and "
             "continuous integration, three papers presented at ENEGEP, and an app delivered to a business school. And thirty years "
             "planning operations under uncertainty and resource constraints: optimization is the same problem with mathematical notation."),
         resposta_pt="Não tenho passagem por empresa grande; tenho entrega verificável: repositórios com testes e CI, 3 artigos, app entregue a uma escola de negócios.",
         pontos=["verifiable delivery", "tests", "ENEGEP", "under uncertainty"],
         palavras={"verifiable": "VÉ-ri-fai-â-bâl", "notation": "nou-TÊI-shân"},
         cuidado="Sem pedir desculpa pela carreira anterior."),

    # ───────────────────────── TÉCNICA
    dict(id="tc1", grupo="Técnica", titulo="STAR: chemical plant in two solvers",
         pergunta_en="Tell me about a project where you took a model all the way to software.",
         pergunta_pt="Conte um projeto em que você levou um modelo até virar software.",
         resposta_en=(
             "I modeled a chain from natural gas to hydrogen, ammonia and urea, with molar balances and yields, in both Pyomo and "
             "OR-Tools, with an API and tests. I validated mass conservation for each reaction with molar masses, modeled the decision "
             "to operate each unit as a binary variable with a minimum operating range, and wrote property tests: mass bought equals "
             "mass sold plus discarded plus lost.\n\n"
             "What went wrong: with both solvers in the same process, the program crashed with a segmentation fault. I isolated it: "
             "Pyomo alone worked, OR-Tools alone worked, so I ran OR-Tools in a separate process.\n\n"
             "Result: both engines reach the same optimum, checked by an agreement test, with 58 tests, 98 percent coverage, and CI "
             "on GitHub with PostgreSQL and docker compose."),
         resposta_pt="Cadeia gás → H₂ → NH₃ → ureia... balanço molar... binária com faixa mínima... segfault com dois solvers, isolei em processo separado... 58 testes, 98%.",
         pontos=["molar balances", "binary variable", "property tests", "segmentation fault", "same optimum", "coverage"],
         palavras={"ammonia": "â-MÔU-ni-a", "urea": "iu-RÍ-a", "molar": "MÔU-lâr", "yield": "IÍLD"},
         cuidado="Números verificáveis no repositório otimizacao-prescritiva."),

    dict(id="tc2", grupo="Técnica", titulo="STAR: real NPV and depreciation",
         pergunta_en="How did you evaluate whether the investment pays off?",
         pergunta_pt="Como você avaliou se o investimento se paga?",
         resposta_en=(
             "The investment enters the MILP through the capital recovery factor. The cash flow is in constant currency, with nominal "
             "depreciation deflated, and a Monte Carlo simulation with correlated prices using Cholesky.\n\n"
             "What went wrong: the Monte Carlo showed gas price helping the NPV, which makes no economic sense. It was a correlation "
             "effect, because gas moves together with urea. I solved it with a tornado chart, one price at a time.\n\n"
             "Result: real NPV of 638 million reais, IRR of 11.98 percent, a 27 percent chance of negative NPV, with urea price as "
             "the dominant factor. Treating depreciation as real would have overestimated the NPV by 85 million."),
         resposta_pt="Fator de recuperação de capital no MILP... fluxo real, depreciação nominal deflacionada... Monte Carlo com Cholesky... tornado... VPL real R$ 638 mi.",
         pontos=["capital recovery factor", "constant currency", "Cholesky", "tornado", "real NPV"],
         palavras={"depreciation": "di-prí-shi-ÊI-shân", "Cholesky": "kô-LÉS-ki", "IRR": "ai-ar-ÁR"},
         cuidado="NPV = net present value (VPL); IRR = internal rate of return (TIR)."),

    dict(id="tc3", grupo="Técnica", titulo="Exact method or heuristic?",
         pergunta_en="When do you use an exact method and when a heuristic?",
         pergunta_pt="Quando usar método exato e quando heurística?",
         resposta_en=(
             "Exact, when the size allows it and we need a guarantee, measured by the optimality gap. Heuristic at scale, for example "
             "a vehicle routing problem with two hundred customers, validated against the exact method on a small instance."),
         resposta_pt="Exato quando o tamanho permite e precisa de garantia (gap); heurística em escala, validada contra o exato em instância pequena.",
         pontos=["guarantee", "optimality gap", "at scale", "validated against the exact"],
         palavras={"heuristic": "hiu-RÍS-tik", "instance": "ÍNS-tâns"}, cuidado=""),

    dict(id="tc4", grupo="Técnica", titulo="What if the model does not converge?",
         pergunta_en="What do you do if the model does not converge or takes too long?",
         pergunta_pt="E se o modelo não convergir ou demorar demais?",
         resposta_en=(
             "Set a time limit and a gap, use a warm start, tighten the formulation, break symmetry, decompose the problem, "
             "and report the gap to the client."),
         resposta_pt="Limite de tempo + gap, warm start, apertar a formulação, quebrar simetria, decompor; reportar o gap ao cliente.",
         pontos=["time limit", "warm start", "tighten the formulation", "symmetry", "report the gap"],
         palavras={"converge": "kân-VÂRDJ", "symmetry": "SÍ-me-tri"}, cuidado=""),

    dict(id="tc5", grupo="Técnica", titulo="Infeasible model",
         pergunta_en="What do you do when the model is infeasible?",
         pergunta_pt="O que fazer quando o modelo é inviável?",
         resposta_en=("Compute an irreducible infeasible subsystem, the IIS in Gurobi, or relax the constraints with penalized slack "
                      "variables to find the conflict."),
         resposta_pt="IIS (Gurobi) ou relaxar restrições com folga penalizada para achar o conflito.",
         pontos=["IIS", "relax the constraints", "penalized slack"],
         palavras={"infeasible": "in-FÍ-zi-bâl", "irreducible": "i-ri-DIÚ-si-bâl"}, cuidado=""),

    dict(id="tc6", grupo="Técnica", titulo="Pyomo or OR-Tools?",
         pergunta_en="Pyomo or OR-Tools: which one and why?",
         pergunta_pt="Pyomo ou OR-Tools: qual e por quê?",
         resposta_en=("Pyomo for algebraic modeling and easy solver switching. OR-Tools for CP-SAT on combinatorial and pure integer "
                      "problems, embedded in the application."),
         resposta_pt="Pyomo: modelagem algébrica e troca de solver; OR-Tools: CP-SAT para combinatório e inteiro puro, embutido.",
         pontos=["algebraic modeling", "solver switching", "CP-SAT", "combinatorial"],
         palavras={"algebraic": "al-dji-BRÊI-ik", "combinatorial": "kâm-bai-na-TÓ-ri-âl"}, cuidado=""),

    dict(id="tc7", grupo="Técnica", titulo="Stoichiometry in a MILP",
         pergunta_en="How do you put stoichiometry into a MILP?",
         pergunta_pt="Como colocar estequiometria num MILP?",
         resposta_en=("The extent of each reaction is a variable; there is a molar balance per species; the yield applies to the "
                      "products; and losses close the mass balance."),
         resposta_pt="Extensão da reação como variável; balanço molar por espécie; rendimento nos produtos; perdas fecham a massa.",
         pontos=["extent of each reaction", "molar balance per species", "yield", "losses"],
         palavras={"species": "SPÍ-shiz", "extent": "iks-TÉNT"}, cuidado=""),

    dict(id="tc8", grupo="Técnica", titulo="Real vs nominal NPV",
         pergunta_en="What is the difference between real and nominal NPV in your model?",
         pergunta_pt="Qual a diferença entre VPL real e nominal no seu modelo?",
         resposta_en=("Fisher equation: a real cash flow with a real rate. Depreciation is nominal, so its real tax benefit shrinks "
                      "with inflation."),
         resposta_pt="Fisher; fluxo real com taxa real; depreciação é nominal, então o benefício fiscal real encolhe com a inflação.",
         pontos=["Fisher", "real rate", "depreciation is nominal", "shrinks with inflation"],
         palavras={"nominal": "NÓ-mi-nâl", "inflation": "in-FLÊI-shân"}, cuidado=""),

    dict(id="tc9", grupo="Técnica", titulo="Why a tight big-M?",
         pergunta_en="Why does a tight big-M matter?",
         pergunta_pt="Por que um big-M apertado importa?",
         resposta_en=("It strengthens the linear relaxation, so branch and bound explores fewer nodes. In lot sizing, I use the "
                      "minimum between remaining demand and capacity divided by unit time."),
         resposta_pt="Fortalece a relaxação linear, menos nós no branch and bound. No CLSP: min(demanda restante, capacidade/tempo).",
         pontos=["linear relaxation", "branch and bound", "fewer nodes", "remaining demand"],
         palavras={"relaxation": "ri-lak-SÊI-shân", "branch and bound": "BRÉNTCH ând BÁUND"}, cuidado=""),

    dict(id="tc10", grupo="Técnica", titulo="How do you test an optimization model?",
         pergunta_en="How do you test an optimization model?",
         pergunta_pt="Como você testa um modelo de otimização?",
         resposta_en=("With pytest fixtures and property tests of the plan, not just checking that it ran: for example, demand is met "
                      "and capacity is respected. Coverage is checked in CI. Coverage measures what ran, not what was checked, so the "
                      "assertions matter more than the percentage."),
         resposta_pt="Fixtures do pytest, testes de propriedade do plano (não só 'rodou'), cobertura no CI; cobertura mede o que rodou, não o que foi conferido.",
         pontos=["property tests", "not just checking that it ran", "coverage", "assertions"],
         palavras={"fixtures": "FÍKS-tchârz", "assertions": "â-SÂR-shânz"}, cuidado=""),

    # ───────────────────────── ENTREVISTA LÍDER (português; conferido no código dos repositórios em 26/11/2026)
    dict(id="el1", grupo="Entrevista Líder", lingua="pt", titulo="Pitch de abertura (1min30)",
         pergunta_pt="Para começar, me fala um pouco de você e da sua trajetória.",
         pergunta_en="To start, tell me a bit about yourself and your background.",
         resposta_en="",
         resposta_pt=(
             "Obrigado pela conversa. Sou o Geovane. Trabalho com Pesquisa Operacional e ciência de dados em Python: pego um "
             "problema de negócio, escrevo o modelo de otimização e entrego como software testado.\n\n"
             "Foram 30 anos como oficial de Comunicações do Exército, formado pela AMAN, até coronel. Chefiei a Seção de "
             "Informática de uma brigada e, por anos, a 4ª Seção, que cuida da logística: transporte, suprimento, recurso "
             "limitado e prazo fixo. É PO na prática, antes de eu conhecer o nome.\n\n"
             "Desde 2023 trabalho como consultor independente em otimização e IA. Concluí um MBA em IA para Negócios, faço o "
             "MBA em Pesquisa Operacional e uma pós em Desenvolvimento Web, e tive três artigos aprovados no ENEGEP 2026.\n\n"
             "Meu projeto mais completo prevê a demanda e decide a produção com um MILP em Pyomo, resolvido com HiGHS ou Gurobi, "
             "servido como API em contêiner, com testes e CI. O que me atrai nesta vaga é justamente isso: levar o modelo do "
             "problema do cliente até o software que ele usa. Se fizer sentido, mostro esse projeto."),
         pontos=["Pesquisa Operacional", "software testado", "30 anos", "Seção de Informática", "logística",
                 "consultor independente", "ENEGEP", "Pyomo", "HiGHS ou Gurobi", "do problema do cliente até o software"],
         palavras={},
         cuidado="Não dizer 'liderei equipes de TI' nem 'rodando em produção'. MBA de PO e pós Web em andamento. Terminar oferecendo mostrar o projeto."),

    dict(id="el2", grupo="Entrevista Líder", lingua="pt", titulo="Arquitetura e produção (otimizacao-prescritiva)",
         pergunta_pt="Como você organiza um projeto de otimização para ele não ficar preso num notebook?",
         pergunta_en="How do you structure an optimization project so it does not stay stuck in a notebook?",
         resposta_en="",
         resposta_pt=(
             "Separo em módulos. No otimizacao-prescritiva: previsão com Holt-Winters, modelo de lot sizing capacitado (CLSP) "
             "em Pyomo, escolha do solver por variável de ambiente, HiGHS por padrão e Gurobi quando há licença, e uma API em "
             "FastAPI. Os testes cobrem a validade do plano, o trade-off entre setup e estoque, a inviabilidade e a API, e o CI "
             "exige 85% de cobertura. Roda em contêiner. Uma decisão de modelagem: o big-M de setup usa a demanda restante e a "
             "capacidade do período, não uma constante, o que fortalece a relaxação linear."),
         pontos=["módulos", "Holt-Winters", "Pyomo", "HiGHS", "Gurobi", "FastAPI", "testes", "CI", "contêiner", "big-M"],
         palavras={},
         cuidado="Não dizer que tem scan de dependências no CI (ainda não tem pip-audit) nem que está em produção com cliente."),

    dict(id="el3", grupo="Entrevista Líder", lingua="pt", titulo="Stack e solvers (pyomo-portfolio + gurobi-sprint)",
         pergunta_pt="Qual a sua experiência prática com Pyomo e Gurobi?",
         pergunta_en="What is your hands-on experience with Pyomo and Gurobi?",
         resposta_en="",
         resposta_pt=(
             "No pyomo-portfolio, o modelo de escala de pessoal, com cobertura de turnos, competências e carga horária, fica "
             "separado do solver: o mesmo modelo roda com GLPK, CBC ou Gurobi trocando um argumento, e os dados passam por "
             "schemas antes de entrar no modelo. No gurobi-sprint resolvi em Gurobi os problemas clássicos de logística: "
             "localização de armazéns, transporte e roteirização com capacidade. Ali uso limite de tempo e gap de otimalidade "
             "para equilibrar qualidade e tempo, e comparo com heurísticas."),
         pontos=["escala de pessoal", "separado do solver", "GLPK", "CBC", "Gurobi", "schemas", "localização",
                 "transporte", "roteirização", "gap"],
         palavras={},
         cuidado="Não dizer HiGHS no pyomo-portfolio nem 'tuning avançado de performance'. O gurobi-sprint é sprint de estudo."),

    dict(id="el4", grupo="Entrevista Líder", lingua="pt", titulo="Negócio e redução de custo",
         pergunta_pt="Como você traduz uma dor de negócio em modelo e ajuda o cliente a reduzir custo?",
         pergunta_en="How do you turn a business problem into a model and help the client reduce cost?",
         resposta_en="",
         resposta_pt=(
             "No otimizacao-prescritiva, o objetivo é o menor custo total de setup, produção e estoque, atendendo à demanda "
             "prevista dentro da capacidade. Para o cliente, o resultado mais útil é mostrar quanto custa cada restrição: quanto "
             "se ganha com mais capacidade ou com menos trocas de produto. Num projeto pessoal menor, o compras-po, o mesmo "
             "raciocínio decide em quais mercados comprar, pesando preço contra custo de deslocamento. Na prática é um "
             "problema de localização com custo fixo."),
         pontos=["custo total", "setup", "estoque", "capacidade", "quanto custa cada restrição", "projeto pessoal",
                 "localização com custo fixo"],
         palavras={},
         cuidado="compras-po é app pessoal de mercado: sem lotes mínimos, armazenagem ou prazos. Não citar R$ 5,1M nem 15% como resultado real."),

    dict(id="el5", grupo="Entrevista Líder", lingua="pt", titulo="Incerteza e visualização",
         pergunta_pt="Como você lida com incerteza, como demanda variável, e como apresenta o resultado para o negócio?",
         pergunta_en="How do you deal with uncertainty, like variable demand, and how do you present results to the business?",
         resposta_en="",
         resposta_pt=(
             "Quando a variabilidade importa, não confio só no modelo determinístico. No ps-filas-dashboard calculo a fila "
             "M/M/c pela fórmula de Erlang C e confiro com simulação de eventos discretos em várias replicações. Na vitrine do "
             "otimizacao-prescritiva uso Monte Carlo e gráfico de tornado para mostrar ao cliente quais incertezas mais mexem no "
             "resultado. A entrega é um painel em Streamlit, não um número no terminal."),
         pontos=["determinístico", "M/M/c", "Erlang C", "simulação de eventos discretos", "replicações", "Monte Carlo",
                 "tornado", "Streamlit"],
         palavras={},
         cuidado="Não usar o incerteza-lab aqui: são exercícios de decisão sob incerteza do MBA, não simulação de demanda."),

    dict(id="el6", grupo="Entrevista Líder", lingua="pt", titulo="Coronel numa vaga pleno",
         pergunta_pt="Você foi coronel. Por que uma vaga de nível pleno? Não vai sentir falta de gerenciar?",
         pergunta_en="You were a colonel. Why a mid-level role? Won't you miss managing people?",
         resposta_en="",
         resposta_pt=(
             "Quero escrever o modelo e o código, e é isso que faço hoje: os commits, os testes e o CI estão no GitHub. "
             "Gerenciei por muito tempo e isso me ajuda a entender o que o cliente precisa decidir, mas o que me move agora "
             "é a parte técnica. Começar como pleno num time que já entrega otimização em escala é o jeito certo de aprender "
             "o que ainda não sei, como sustentar um sistema em produção com usuários."),
         pontos=["escrever o modelo e o código", "GitHub", "entender o que o cliente precisa decidir", "parte técnica",
                 "aprender", "produção"],
         palavras={},
         cuidado="Curto e direto. Sem justificar demais nem falar de hierarquia militar."),

    dict(id="el8", grupo="Entrevista Líder", lingua="pt", titulo="Artigos aprovados no ENEGEP 2026",
         pergunta_pt="Você citou artigos no ENEGEP. Do que tratam, e algum usa as ferramentas de PO e IA que a gente usa aqui?",
         pergunta_en="You mentioned papers at ENEGEP. What are they about, and does any of them use the OR and AI tools we use here?",
         resposta_en="",
         resposta_pt=(
             "São três, publicados nos anais do ENEGEP 2026 com DOI, na área de Pesquisa Operacional, com o professor "
             "José Bezerra. O primeiro trata de pronto-socorro: teoria das filas M/M/c, simulação de eventos discretos e "
             "o método multicritério SAPEVO-M para priorizar ações. O segundo propõe o FRAME-SCEN, um método de cenários "
             "para consultoria a PMEs industriais que junta MICMAC, simulação de Monte Carlo e IA, aplicado a um caso "
             "hipotético. No terceiro sou coautor: alocação de recursos do Plano Nacional de Educação com AHP, DEA, "
             "programação por metas estocástica e Monte Carlo.\n\n"
             "Sendo direto sobre a sua pergunta: nenhum deles usa Pyomo, Gurobi ou MILP de logística, e nenhum tem dado "
             "real de cliente. O que eles mostram é modelagem sob incerteza e simulação. A stack que vocês usam, Pyomo com "
             "HiGHS ou Gurobi, API e testes, está nos projetos do GitHub, como o otimizacao-prescritiva."),
         pontos=["três artigos", "DOI", "M/M/c", "simulação de eventos discretos", "SAPEVO-M", "FRAME-SCEN",
                 "Monte Carlo", "caso hipotético", "nenhum usa Pyomo", "otimizacao-prescritiva"],
         palavras={},
         cuidado=("Anais: https://www.abepro.org.br/publicacoes/index.asp?pesq=ok&ano=2026&area=&pchave=&autor=GEOVANE+VIRMECATI&categ= "
                  "· Não citar 93% das metas / -0,7 p.p. do PIB / 84% do artigo do PNE como resultado real (instância em parte sintética). "
                  "No PNE você é coautor, não primeiro autor. Não afirmar qual software foi usado nos artigos.")),

    dict(id="el7", grupo="Entrevista Líder", titulo="Perguntas para o líder",
         pergunta_pt="Como o time faz revisão de código e quem revisaria o meu no começo? O projeto já está em produção ou começa do zero? Onde Java entra, se entra? Qual o cliente e o setor?",
         pergunta_en="", resposta_en="",
         resposta_pt="Escolha duas. A do setor confirma a hipótese de logística (transporte e armazéns caíram na prova técnica).",
         pontos=[], palavras={}, cuidado="Feche com uma pergunta, nunca com 'não tenho perguntas'."),

    # ───────────────────────── PERGUNTAS PARA A LETÍCIA (RH, em português)
    dict(id="le1", grupo="Perguntas para a Letícia", titulo="Inglês no projeto (a mais importante)",
         pergunta_pt="O projeto desta vaga tem reuniões em inglês desde o começo? O cliente é daqui ou de fora?",
         pergunta_en="Does this project have meetings in English from the start? Is the client local or abroad?",
         resposta_en="", resposta_pt="Decide como você se prepara: se for em português, o maior risco da entrevista desaparece.",
         pontos=[], palavras={}, cuidado="Pergunte antes da entrevista técnica."),
    dict(id="le2", grupo="Perguntas para a Letícia", titulo="Regime e nível",
         pergunta_pt="O regime é CLT, por prazo indeterminado? A vaga é para nível pleno ou sênior?",
         pergunta_en="", resposta_en="", resposta_pt="O anúncio aparece como 'Mid/Senior' em outros sites.", pontos=[], palavras={}, cuidado=""),
    dict(id="le3", grupo="Perguntas para a Letícia", titulo="Cliente e setor",
         pergunta_pt="Qual o cliente ou setor do projeto? A parte de estequiometria indica indústria química ou de processos: é isso?",
         pergunta_en="", resposta_en="", resposta_pt="Ajuda a escolher qual caso técnico revisar.", pontos=[], palavras={}, cuidado=""),
    dict(id="le4", grupo="Perguntas para a Letícia", titulo="Ferramentas do time",
         pergunta_pt="O time usa mais Pyomo ou OR-Tools? Usa solver comercial (Gurobi/CPLEX) com licença?",
         pergunta_en="", resposta_en="", resposta_pt="", pontos=[], palavras={}, cuidado=""),
    dict(id="le5", grupo="Perguntas para a Letícia", titulo="Formato da etapa técnica",
         pergunta_pt="Como é a etapa técnica: case de modelagem, código ao vivo ou desafio para fazer em casa? Em português ou em inglês?",
         pergunta_en="", resposta_en="", resposta_pt="Define o treino dos próximos dias.", pontos=[], palavras={}, cuidado=""),
    dict(id="le6", grupo="Perguntas para a Letícia", titulo="Equipamento",
         pergunta_pt="O notebook tem software de monitoramento? Tenho acesso de administrador para instalar solvers e ferramentas?",
         pergunta_en="", resposta_en="", resposta_pt="", pontos=[], palavras={}, cuidado=""),
    dict(id="le7", grupo="Perguntas para a Letícia", titulo="Atividades paralelas",
         pergunta_pt="Existe política sobre atividades paralelas? Tenho consultoria própria em Pesquisa Operacional e faço pesquisa acadêmica. Há cláusula de exclusividade ou de propriedade intelectual?",
         pergunta_en="", resposta_en="", resposta_pt="Importante por causa da consultoria e do mestrado.", pontos=[], palavras={}, cuidado=""),
    dict(id="le8", grupo="Perguntas para a Letícia", titulo="Realocação",
         pergunta_pt="Se o projeto do cliente acabar, como funciona a realocação?",
         pergunta_en="", resposta_en="", resposta_pt="", pontos=[], palavras={}, cuidado=""),
    dict(id="le9", grupo="Perguntas para a Letícia", titulo="Benefícios (só informação)",
         pergunta_pt="Como funcionam a PLR e a coparticipação do plano de saúde?",
         pergunta_en="", resposta_en="", resposta_pt="As condições já foram aceitas: pergunte como informação, sem renegociar.",
         pontos=[], palavras={}, cuidado="Não renegocie salário."),

    # ───────────────────────── PERGUNTAS AO ENTREVISTADOR TÉCNICO
    dict(id="en1", grupo="Perguntas ao entrevistador", titulo="Business decision",
         pergunta_en="Which business decision does this work support, and who uses the result at the client?",
         pergunta_pt="Qual decisão de negócio esse trabalho alimenta, e quem consome o resultado no cliente?",
         resposta_en="", resposta_pt="", pontos=[], palavras={"support": "sâ-PÓRT"}, cuidado=""),
    dict(id="en2", grupo="Perguntas ao entrevistador", titulo="State of the data",
         pergunta_en="What is the real state of the data? Are mass balances and costs already organized, or is that part of the work?",
         pergunta_pt="Qual o estado real dos dados: já existem balanços de massa e custos organizados, ou isso faz parte do trabalho?",
         resposta_en="", resposta_pt="", pontos=[], palavras={}, cuidado=""),
    dict(id="en3", grupo="Perguntas ao entrevistador", titulo="Biggest open problem",
         pergunta_en="What is the biggest unsolved problem of the optimization team today?",
         pergunta_pt="Qual o maior problema não resolvido do time de otimização hoje?",
         resposta_en="", resposta_pt="", pontos=[], palavras={"unsolved": "ân-SÓLVD"}, cuidado=""),
    dict(id="en4", grupo="Perguntas ao entrevistador", titulo="New role?",
         pergunta_en="Is this a new role, or was someone in this position before?",
         pergunta_pt="Essa função é nova, ou alguém ocupava antes?",
         resposta_en="", resposta_pt="", pontos=[], palavras={}, cuidado=""),
]

from caderno import CADERNO, DICIONARIO, G as GRUPO_CADERNO, GD as GRUPO_DICIONARIO

BANCO += CADERNO + DICIONARIO

GRUPOS = ["RH", "Perfil", "Técnica", "Entrevista Líder", GRUPO_CADERNO, GRUPO_DICIONARIO, "Perguntas para a Letícia", "Perguntas ao entrevistador"]
