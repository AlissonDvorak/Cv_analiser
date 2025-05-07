import uuid

from models.job import Job
from database import AnalyseDatabase


database = AnalyseDatabase()

name = 'Vaga de Estágio em Programação'

activities = '''
Apoiar no desenvolvimento de novas funcionalidades da plataforma da empresa, com foco em aplicações web
Realizar manutenção evolutiva e corretiva no front-end (como React.js) e back-end (como .NET)
Participar de reuniões ágeis (dailies, refinamentos, revisões de código)
Colaborar na documentação técnica e testes das entregas realizadas
Aprender na prática com um time experiente em desenvolvimento de software
'''

prequisites = '''
Estar matriculado(a) em curso de graduação em Tecnologia da Informação, Sistemas de Informação, Ciência da Computação, Engenharia de Software ou áreas correlatas
Conhecimento básico em lógica de programação e estrutura de dados
Noções de desenvolvimento web (HTML, CSS, JavaScript)
Interesse em atuar tanto no front-end quanto no back-end
Disponibilidade para estagiar 6h por dia, com modelo híbrido (mínimo 4 dias presenciais)
'''

differentials = '''
Conhecimento prévio em C# e .NET
Familiaridade com React.js ou outras bibliotecas de front-end
Experiência com Git e controle de versão
Conhecimento básico de APIs RESTful
Participação em projetos pessoais, bootcamps ou hackathons
Interesse por metodologias ágeis e boas práticas de desenvolvimento de software
'''


job = Job(
    id=str(uuid.uuid4()),
    name=name,
    main_activity=activities,
    prerequisites=prequisites,
    differentials=differentials,
)

database.jobs.insert(job.model_dump())