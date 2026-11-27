"""Versão completa em português das respostas que nasceram em inglês no banco.

Mesmos fatos da resposta em inglês, sem acréscimo. O texto curto que já existia em `resposta_pt`
passa a ser `resumo_pt` (versão de bolso para revisar).
"""

PT = {
    "rh1": ("Fale sobre você", """Hoje trabalho com Pesquisa Operacional aplicada. Pego um problema de decisão, escrevo como modelo matemático, implemento em Python e entrego um resultado que alguém consegue usar para decidir.

Cheguei aqui por um caminho pouco comum. Fui oficial do Exército por trinta anos, de 1995 a 2025, e fui para a reserva como coronel. Boa parte desse tempo foi planejamento com recurso escasso: chefiei o Departamento de Logística por cinco anos e cuidei de equipamentos de comunicações e TI. Era decidir sob incerteza, com orçamento, prazo e pessoal limitados.

Na transição, percebi que isso tem nome: é exatamente o que um modelo de otimização formaliza. Então construí a base: graduação em Matemática, MBA em IA para Negócios, e estou cursando MBAs em Pesquisa Operacional e em Finanças Corporativas.

E fui para a prática. Trabalho como consultor independente, tenho um portfólio de modelos em Python com Pyomo, OR-Tools e Gurobi, e apresentei três artigos de Pesquisa Operacional no ENEGEP em outubro. Para esta vaga, montei um projeto que segue a descrição: uma planta química com estequiometria, resolvida em Pyomo e OR-Tools, com valor presente líquido em termos reais, um serviço FastAPI, PostgreSQL e testes automatizados.

O que me atrai na Compass é colocar otimização em produção para clientes reais, num time que entrega software, não só relatório."""),
    "rh2": ("Por que agora? Sente falta do Exército?", """Por que agora: completei trinta anos de serviço e fui para a reserva em abril de 2025. Foi o fim natural de um ciclo, e eu vinha me preparando desde 2023.

Por que otimização: no Exército, muitas decisões de logística eram tomadas com base na experiência, sob pressão e com pouco recurso. Funcionava, mas eu sempre quis um jeito de comparar alternativas e defender a escolha com números. Quando estudei Pesquisa Operacional, vi que era exatamente isso. Não estou mudando de assunto: estou fazendo o mesmo trabalho com uma ferramenta melhor.

Se sinto falta: das pessoas, sim. Da rotina, não. E o que eu mais gostava, que era planejar, eu trouxe comigo.

Sobre a adaptação: desde 2023 trabalho como consultor independente, sem hierarquia nenhuma: quem define o problema é o cliente. Aprendi Python e otimização por conta própria, com código público e testado, e escrevi três artigos com coautores, discutindo de igual para igual. E não tenho problema em ser liderado por alguém mais novo. Num time técnico, lidera quem conhece melhor o problema, e eu também estou aqui para aprender."""),
    "rh3": ("Como está o seu inglês?", """Meu inglês é intermediário. Leio documentação técnica e artigos todos os dias, e escrevo documentação e comentários de código em inglês. Numa reunião técnica consigo acompanhar a discussão e explicar um modelo, principalmente com o material na tela. A conversa espontânea é o que ainda estou desenvolvendo, e me preparo antes de cada reunião em inglês. [Meu plano: X horas por semana de conversação, método.] Este projeto tem reuniões em inglês desde o começo?"""),
    "rh4": ("Uma situação difícil (STAR)", """Situação: em 2011, na operação do Complexo do Alemão, eu era o chefe da turma de guerra eletrônica. No meio da operação, o equipamento de comunicações que usávamos começou a falhar.

Tarefa: precisávamos decidir rápido qual equipamento usar no lugar, sem comprometer a missão. A maior parte do grupo preferia uma opção, a opção A.

Ação: eu e outro integrante da equipe comparamos as opções com os requisitos da missão. A opção B tinha mais alcance e bateria com mais autonomia; a desvantagem era ser mais pesada. Avaliamos que alcance e autonomia pesavam mais que o peso naquela missão. Mesmo sendo o chefe da equipe, escolhi não impor: apresentamos a comparação ao grupo e convencemos com argumentos, sem atrito.

Resultado: o equipamento B funcionou e a missão foi cumprida.

Lição: aprendi a aceitar a decisão do grupo quando ela é boa e, quando discordo, mudá-la com argumento, nunca com a patente. Olhando para trás, era uma decisão multicritério: alcance, autonomia, peso. Hoje eu estruturaria com um método como o AHP, ponderando os critérios e mostrando ao grupo por que a opção B vence. É esse tipo de problema que me levou à Pesquisa Operacional."""),
    "rh5": ("Estudos e trabalho em tempo integral", """O trabalho vem em primeiro lugar. Os estudos ficam fora do horário de trabalho.

O mestrado é em Engenharia de Produção, à noite, sem dedicação exclusiva, e tem tudo a ver com esta vaga: otimização e apoio à decisão. O que estudo lá volta para o projeto, e o que aprendo no projeto alimenta a pesquisa. [Nome do programa e data de início.]

Os MBAs também são fora do horário [e terminam em ...].

E isso não é aposta: este ano já conciliei os MBAs, a consultoria, o portfólio e três artigos apresentados no ENEGEP. Organizo meu tempo como organizava uma operação: prioridade, prazo e entrega."""),
    "rh6": ("Principal ponto fraco", """Meu principal ponto fraco hoje é nunca ter trabalhado dentro de um time de desenvolvimento de software. Trabalho em equipe eu tenho de sobra, de trinta anos de Exército, mas meus projetos de código eu construí sozinho, na consultoria e no portfólio. Numa consultoria como a Compass a rotina é outra: revisão de código, tarefas compartilhadas, padrões do time, ciclos curtos de entrega.

O que já faço a respeito: mesmo sozinho, trabalho como se estivesse num time. Meu repositório tem testes automatizados, exigência de cobertura mínima, integração contínua no GitHub e documentação, para que outra pessoa consiga entender, rodar e mudar o código com segurança.

O que vou fazer: nos primeiros meses, quero que meu código passe por revisão, para aprender o fluxo do time e me adaptar aos padrões da casa. Aprender com quem já trabalha assim é uma das coisas que mais me atraem nesta vaga."""),
    "rh7": ("Você tem perguntas para nós?", """Sim, três.

Primeira: como seria o meu dia a dia? Um projeto dedicado a um cliente ou várias demandas ao mesmo tempo? E com quem eu trabalharia mais de perto no time de otimização?

Segunda: vi que o grupo de IA/R está crescendo nos Estados Unidos, com a aquisição da Oak Rocket. Esse time de otimização atende clientes daqui ou de fora? E a descrição da vaga fala em estequiometria e valor presente líquido: o projeto é na indústria química?

Terceira: o que vocês esperam que eu entregue nos primeiros seis meses para considerarem a contratação um sucesso?"""),
    "pf1": ("O caso de R$ 5,1 milhões (CV)", """É um caso que modelei no meu sprint de Gurobi, com dados construídos para reproduzir um problema típico de rede de distribuição: seis centros de distribuição e dez regiões. Os 5,1 milhões são a diferença entre a solução ótima e a alocação ingênua, cada região atendida pelo centro mais próximo, dentro do próprio caso. Não é economia medida num cliente. O que ele mostra é o método: custo fixo de abertura, capacidade e um teste com crescimento de 20% na demanda."""),
    "pf2": ("Eixo Estratégico: é uma empresa?", """Trabalho como consultor independente sob a marca Eixo Estratégico, ainda sem empresa registrada. A formalização vem com o primeiro contrato recorrente."""),
    "pf3": ("Sem experiência corporativa", """Não tenho experiência em empresa grande. O que tenho é entrega verificável: repositórios públicos com testes e integração contínua, três artigos apresentados no ENEGEP e um app entregue a uma escola de negócios. E trinta anos planejando operações sob incerteza e com recurso limitado: otimização é o mesmo problema com notação matemática."""),
    "tc1": ("STAR: planta química em dois solvers", """Modelei uma cadeia de gás natural para hidrogênio, amônia e ureia, com balanços molares e rendimentos, em Pyomo e em OR-Tools, com API e testes. Validei a conservação de massa de cada reação com as massas molares, modelei a decisão de operar cada unidade como variável binária com faixa mínima de operação e escrevi testes de propriedade: massa comprada igual a massa vendida mais descartada mais perdida.

O que deu errado: com os dois solvers no mesmo processo, o programa caía com falha de segmentação. Isolei: Pyomo sozinho funcionava, OR-Tools sozinho funcionava, então rodei o OR-Tools num processo separado.

Resultado: os dois motores chegam ao mesmo ótimo, conferido por um teste de concordância, com 58 testes, 98% de cobertura e CI no GitHub com PostgreSQL e docker compose."""),
    "tc2": ("STAR: VPL real e depreciação", """O investimento entra no MILP pelo fator de recuperação de capital. O fluxo de caixa é em moeda constante, com a depreciação nominal deflacionada, e uma simulação de Monte Carlo com preços correlacionados por Cholesky.

O que deu errado: o Monte Carlo mostrava o preço do gás ajudando o VPL, o que não faz sentido econômico. Era efeito da correlação, porque o gás anda junto com a ureia. Resolvi com um gráfico de tornado, um preço de cada vez.

Resultado: VPL real de 638 milhões de reais, TIR de 11,98%, 27% de chance de VPL negativo, com o preço da ureia como fator dominante. Tratar a depreciação como real teria superestimado o VPL em 85 milhões."""),
    "tc3": ("Método exato ou heurística?", """Exato, quando o tamanho permite e precisamos de garantia, medida pelo gap de otimalidade. Heurística em escala, por exemplo um problema de roteirização com duzentos clientes, validada contra o método exato numa instância pequena."""),
    "tc4": ("E se o modelo não convergir?", """Defino limite de tempo e de gap, uso warm start, aperto a formulação, quebro simetria, decomponho o problema e informo o gap ao cliente."""),
    "tc5": ("Modelo inviável", """Calculo um subsistema irredutível inviável, o IIS no Gurobi, ou relaxo as restrições com variáveis de folga penalizadas para achar o conflito."""),
    "tc6": ("Pyomo ou OR-Tools?", """Pyomo para modelagem algébrica e troca fácil de solver. OR-Tools para o CP-SAT em problemas combinatórios e inteiros puros, embutido na aplicação."""),
    "tc7": ("Estequiometria num MILP", """A extensão de cada reação é uma variável; há um balanço molar por espécie; o rendimento se aplica aos produtos; e as perdas fecham o balanço de massa."""),
    "tc8": ("VPL real × nominal", """Equação de Fisher: fluxo de caixa real com taxa real. A depreciação é nominal, então o benefício fiscal real dela encolhe com a inflação."""),
    "tc9": ("Por que um big-M apertado?", """Fortalece a relaxação linear, então o branch and bound explora menos nós. No lot sizing, uso o mínimo entre a demanda restante e a capacidade dividida pelo tempo unitário."""),
    "tc10": ("Como testar um modelo de otimização?", """Com fixtures do pytest e testes de propriedade do plano, não só conferindo que rodou: por exemplo, a demanda é atendida e a capacidade é respeitada. A cobertura é conferida no CI. Cobertura mede o que rodou, não o que foi conferido, então as asserções importam mais que o percentual."""),
}

TITULOS_PT = {
    "en1": "Decisão de negócio",
    "en2": "Situação dos dados",
    "en3": "Maior problema em aberto",
    "en4": "Vaga nova?",
}


def aplicar(banco: list[dict]) -> None:
    for b in banco:
        if b["id"] in PT:
            titulo, texto = PT[b["id"]]
            b["titulo_pt"] = titulo
            if b.get("resposta_pt"):
                b["resumo_pt"] = b["resposta_pt"]
            b["resposta_pt"] = texto
        elif b["id"] in TITULOS_PT:
            b["titulo_pt"] = TITULOS_PT[b["id"]]
