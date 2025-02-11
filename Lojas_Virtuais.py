import json

# Dados fornecidos
lojas_virtuais = [
    {
        "fantasia": "PIU SHOP",
        "telefone": "(14) 3737-0919",
        "endereco": "R: ANTENOR LARA CAMPOS, CASCATA",
        "cidade": "GARÇA-SP",
        "cep": "17400-136"
    },
    {
        "fantasia": "MP STORE",
        "telefone": "(11) 97055-1818",
        "endereco": "R MARCELO MULLER, 413, JARDIM INDEPENDENCIA",
        "cidade": "SÃO PAULO",
        "cep": "03223-060"
    },
    {
        "fantasia": "MC MUSIC",
        "telefone": "(11) 99236-3031",
        "endereco": "RUA DOS FLOX, 1419",
        "cidade": "CAJAMAR",
        "cep": "07791-030"
    },
    {
        "fantasia": "LIQUIDA MEGA STORE",
        "telefone": "(11) 94984-3948 / (11) 99725-0116",
        "endereco": "R VICENTE R DA SILVA, 475, PIRATININGA",
        "cidade": "OSASCO",
        "cep": "06230-094"
    },
    {
        "fantasia": "RCK",
        "telefone": "(11) 3360-7870",
        "endereco": "R SEVERA, VILA M. BAIXA",
        "cidade": "SÃO PAULO",
        "cep": "02111-000"
    },
    {
        "fantasia": "SHOPER EQUIPAMENTOS",
        "telefone": "(11) 2058-4217",
        "endereco": "R CHACURU, 231, VILA CURUCA",
        "cidade": "SÃO PAULO",
        "cep": "08030-100"
    },
    {
        "fantasia": "J P SHOP MUSIC",
        "telefone": "(11) 96572-7064",
        "endereco": "AVENIDA JOAO BATISTA MEDINA, 217, CENTRO",
        "cidade": "EMBÚ",
        "cep": "06803-447"
    },
    {
        "fantasia": "PANORAMA MUSICAL",
        "telefone": "13 99789-6119",
        "endereco": "JOSE CUSTODIO DE OLIVEIRA, 75, VILA TUPY",
        "cidade": "REGISTRO",
        "cep": "11900-000"
    },
    {
        "fantasia": "BACK STAGE",
        "telefone": "(51) 98641-8259",
        "endereco": "R HELVETIA, 795, CAMPOS ELISEOS",
        "cidade": "RIO GRANDE DO SUL",
        "cep": "01215-010"
    },
    {
        "fantasia": "ELETRO MUSIC",
        "telefone": "(34) 3842-7557",
        "endereco": "R FORMOSA, 263, BOA VISTA",
        "cidade": "MONTE CARMELO",
        "cep": "38500-000"
    },
    {
        "fantasia": "TEMTEC",
        "telefone": "(14) 98116-9269",
        "endereco": "RUA MARIA IZABEL, 696, LABIENOPOLIS",
        "cidade": "GARÇA-SP",
        "cep": "17404-300"
    },
    {
        "fantasia": "ENTER LIGHT",
        "telefone": "(18) 3222-1428 / 0800-7779015",
        "endereco": "AV JOAQUIM CONSTANTINO, 3980, JARDIM SAO LUIS",
        "cidade": "PRESIDENTE PRUDENTE",
        "cep": "19061-000"
    },
    {
        "fantasia": "RBS SHOP STORE",
        "telefone": "(14) 98203-3932",
        "endereco": "RUA ANDRÉ LUIZ, 699, JARDIM MONDRIAN",
        "cidade": "GARÇA-SP",
        "cep": "17400-826"
    },
    {
        "fantasia": "SANTIAGO ELETRO",
        "telefone": "(14) 98133-9199 / (14) 98807-1852",
        "endereco": "AVENIDA DOUTOR LABIENO DA COSTA MACHADO, 09, LABIENÓPOLIS",
        "cidade": "GARÇA-SP",
        "cep": "17404-328"
    },
    {
        "fantasia": "OTTENIO RODRIGUES ELETRON",
        "telefone": "",
        "endereco": "ROD CARLOS J STRASS, 585, PARQUE I. ALICANTE",
        "cidade": "LONDRINA",
        "cep": "86087-350"
    },
    {
        "fantasia": "COLOMERA",
        "telefone": "(43) 3323-8394",
        "endereco": "MARANHÃO, 449, CENTRO",
        "cidade": "LONDRINA",
        "cep": "86010-410"
    },
    {
        "fantasia": "NET MUSIC",
        "telefone": "(48) 98816-9940",
        "endereco": "R HENRIQUE LAGE, 267, CENTRO",
        "cidade": "CRICIUMA",
        "cep": "88801-010"
    },
    {
        "fantasia": "E.N SOM E ACESSORIOS",
        "telefone": "(16) 3632-8137",
        "endereco": "R JOSE BONIFACIO, 272, CENTRO",
        "cidade": "RIBEIRO PRETO",
        "cep": "14010-050"
    },
    {
        "fantasia": "VS SOM",
        "telefone": "(17) 3324-5623",
        "endereco": "AV 7, 1137, FORTALEZA",
        "cidade": "BARRETOS",
        "cep": "14780-240"
    },
    {
        "fantasia": "STATUS SOM GAMES",
        "telefone": "(16) 3242-4536 / (16) 99708-4536",
        "endereco": "R RUI BARBOSA, 557, CENTRO",
        "cidade": "MONTE ALTO",
        "cep": "15910-000"
    }
]

# Atualizando a chave 'fantasia' para 'nome_da_loja'
for loja in lojas_virtuais:
    loja["nome_da_loja"] = loja.pop("fantasia")

# Convertendo para JSON e salvando em um arquivo
with open('lojas_virtuais.json', 'w') as json_file:
    json.dump(lojas_virtuais, json_file, indent=4, ensure_ascii=False)

print("Dados atualizados e salvos no arquivo 'clientes.json'.")
