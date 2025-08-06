import os
from datetime import datetime

produtos = [{
    "codigo": "12345",
    "nome": "Arroz",
    "quantidade": "15",
    "validade": "15/07/2023",
    "disponibilidade": False
}]

largura_terminal = os.get_terminal_size().columns

print("""Bem-Vindo ao Ｇｅｒｅｎｃｉａｄｏｒ ｄｅ Ｖａｌｉｄａｄｅ\n""".center(largura_terminal))

def subtitulos(texto):
    os.system("clear")
    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)

def cadastrar_produto():
    subtitulos("Cadastrar Produtos".upper().center(largura_terminal))
    codigo = input("Código: ")
    nome = input("Nome do produto: ")
    quantidade = input("Quantidade de produtos: ")

    while True:
        validade_str = input("Data de Validade (dd/mm/aaaa): ")
        try:
            validade = datetime.strptime(validade_str, "%d/%m/%Y")  # Y maiúsculo para 4 dígitos!
            validade_formatada = validade.strftime("%d/%m/%Y")
            break
        except ValueError:
            print("O formato da data está incorreto.")

    print(f"O produto {nome} foi cadastrado com sucesso!")
    input("Pressione qualquer tecla para retornar ao menu!")

    dados_produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "validade": validade_formatada,
        "disponibilidade": False
    }
    produtos.append(dados_produto)

    main()

def listar_produtos():
    subtitulos("Lista de Produtos Disponíveis".center(largura_terminal).upper())
    for produto in produtos:
        codigo = produto["codigo"]
        nome = produto["nome"]
        quantidade = produto["quantidade"]
        validade = produto["validade"]
        disponibilidade = "Disponível em estoque" if produto["disponibilidade"] else "Indisponível no estoque"
        print(f"Informações do produto:\n Código: {codigo} \n Nome: {nome} \n Quantidade: {quantidade} \n Validade: {validade} \n Situação: {disponibilidade}\n")
    input("Clique em qualquer tecla para retornar ao menu.")
    main()

def alterar_disponibilidade():
    subtitulos("Alterar disponibilidade do estoque".upper().center(largura_terminal))
    
    cod_alteracao = input("Informe o código do produto: ")
    cod_encontrado = False

    for produto in produtos:
        if cod_alteracao == produto["codigo"]:
            print("Produto encontrado!")
            cod_encontrado = True
            resp = input("Deseja alterar sua disponibilidade no estoque? (S/N) ").upper()
            if resp == "S":
                produto["disponibilidade"] = not produto["disponibilidade"]
                if produto["disponibilidade"]:
                    print("O produto está disponível em estoque!")
                else:
                    print("O produto está indisponível no estoque!")
            else:
                input("Tudo bem, o produto não terá sua disponibilidade alterada. Clique em qualquer tecla para retornar ao menu.")
            break
    if not cod_encontrado:
        print("Código inválido.")
    main()

def listar_produtos_vencidos():
    subtitulos("Listagem de Produtos Vencidos".upper().center(largura_terminal))
    data_atual = datetime.today().date()

    for produto in produtos:
        validade_str = produto["validade"]
        validade_data = datetime.strptime(validade_str, "%d/%m/%Y").date()
        if validade_data <= data_atual:
            print(f"O produto {produto['nome']} está fora da validade - {produto['validade']}")

def menu_opcao():
    subtitulos("Menu".upper().center(largura_terminal))
    print("1 - Cadastrar Produto")
    print("2 - Listar produtos")
    print("3 - Alterar disponibilidade")
    print("4 - Listar produtos vencidos")
    print("5 - Buscar produto por nome ou categoria")
    print("6 - Remover produto")

def escolher_opcoes():
    opcao_escolhida = int(input("Informe o número da opção que deseja acessar: "))

    if opcao_escolhida == 1:
        cadastrar_produto()
    
    elif opcao_escolhida == 2:
        listar_produtos()

    elif opcao_escolhida == 3:
        alterar_disponibilidade()
    
    elif opcao_escolhida == 4:
        listar_produtos_vencidos()

    # elif opcao_escolhida == 5:
    #     buscar_produto()

    # elif opcao_escolhida == 6:
    #     remover_produto()

    # else:
    #     print("Opção inválida.")

def main():
    menu_opcao()
    escolher_opcoes()

if __name__ == '__main__':
    main()
