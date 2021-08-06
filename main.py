from pymongo import MongoClient

cliente = MongoClient('localhost', 27017)

banco = cliente.escola

classe = banco.aluno

newClass = [{
    "nome": "Bruno Lemes",
    "curso": "Analise e Desenvolvimento de Sistemas Mobile",
    "ano": "2020"
}, {

    "nome": "Bruno Lemos",
    "curso": "Sistemas de Informação",
    "ano": "2021"
}
]

alunoid = classe.insert_many(newClass);
