"""Sistema de produtos: listas, tuplas e conjuntos.

Cada funcionalidade aparece em Python e, logo abaixo, em Portugol
(comentada), para mostrar que a lógica independe da sintaxe.

Como executar:  python3 sistema_produtos.py

Sobre o Portugol deste arquivo
------------------------------
- A sintaxe segue o Portugol Studio (programa { funcao inicio() { ... } }).
- Os trechos comentados de cada seção fazem parte de UM mesmo programa,
  na ordem em que aparecem, todos dentro de inicio().
- Em Portugol não existem listas que crescem (append), sort(), set(),
  tuplas nem f-strings. Por isso aparecem vetores de tamanho fixo,
  um contador de posições usadas, laços "para", bubble sort,
  conjunto simulado à mão e escreva() com vírgulas.
"""

import math

TAMANHO_MAXIMO = 100  # mesmo tamanho dos vetores do Portugol


# ---------------------------------------------------------------------
# Funções auxiliares de leitura (validam o que o usuário digita)
# ---------------------------------------------------------------------
def ler_texto(mensagem):
    """Lê um texto e repete a pergunta enquanto ele estiver vazio."""
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("  Campo obrigatório. Tente novamente.")


def ler_numero(mensagem):
    """Lê um número real não negativo (aceita 12.50 ou 12,50)."""
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            numero = float(texto)
        except ValueError:
            print("  Digite um número válido (ex.: 12.50 ou 12,50).")
            continue
        if not math.isfinite(numero) or numero < 0:
            print("  Digite um número finito e não negativo.")
            continue
        return numero


def ler_preco(mensagem):
    """Lê um preço, que precisa ser maior que zero."""
    while True:
        preco = ler_numero(mensagem)
        if preco > 0:
            return preco
        print("  O preço deve ser maior que zero.")


def ler_inteiro(mensagem, minimo, maximo):
    """Lê um inteiro entre minimo e maximo (inclusive)."""
    while True:
        texto = input(mensagem).strip()
        try:
            numero = int(texto)
        except ValueError:
            print("  Digite um número inteiro.")
            continue
        if minimo <= numero <= maximo:
            return numero
        print(f"  Digite um valor entre {minimo} e {maximo}.")


# ---------------------------------------------------------------------
# FUNCIONALIDADE 1 - Cadastro de produtos (input + append)
# ---------------------------------------------------------------------
def cadastrar_produtos(quantidade):
    """Lê nome, preço e categoria de cada produto e guarda em uma lista."""
    produtos = []
    for numero_produto in range(1, quantidade + 1):
        print(f"\n--- Produto {numero_produto} de {quantidade} ---")
        nome = ler_texto("Nome: ")
        preco = ler_preco("Preço (R$): ")
        categoria = ler_texto("Categoria: ").title()  # "roupas" == "Roupas"
        produtos.append(
            {"nome": nome, "preco": preco, "categoria": categoria}
        )
    return produtos


# --- Versão em Portugol (vetores de tamanho fixo + laço "para") ------
#
# programa {
#   inclua biblioteca Matematica --> mat
#
#   funcao inicio() {
#     // Vetores paralelos: a posição i descreve o mesmo produto nos três.
#     // Não existe append: "quantidade" diz quantas posições estão em uso.
#     cadeia nomes[100]
#     real precos[100]
#     cadeia categorias[100]
#     inteiro quantidade
#
#     escreva("Quantos produtos deseja cadastrar (1 a 100)? ")
#     leia(quantidade)
#     enquanto (quantidade < 1 ou quantidade > 100) {
#       escreva("Valor inválido. Digite de 1 a 100: ")
#       leia(quantidade)
#     }
#
#     para (inteiro i = 0; i < quantidade; i++) {
#       escreva("\n--- Produto ", i + 1, " de ", quantidade, " ---\n")
#       escreva("Nome: ")
#       leia(nomes[i])
#       escreva("Preço (R$): ")
#       leia(precos[i])
#       enquanto (precos[i] <= 0) {
#         escreva("O preço deve ser maior que zero: ")
#         leia(precos[i])
#       }
#       escreva("Categoria: ")
#       leia(categorias[i])
#     }


# ---------------------------------------------------------------------
# FUNCIONALIDADE 2 - Filtragem por preço (acima ou abaixo de um valor)
# ---------------------------------------------------------------------
def filtrar_por_preco(produtos, valor_limite, acima=True):
    """Devolve só os produtos com preço acima (ou abaixo) do limite."""
    if acima:
        return [p for p in produtos if p["preco"] > valor_limite]
    return [p for p in produtos if p["preco"] < valor_limite]


# --- Versão em Portugol ---------------------------------------------
#
#     inteiro opcao, encontrados = 0
#     real valor_limite
#
#     escreva("\nFiltrar: 1 - acima de um valor | 2 - abaixo: ")
#     leia(opcao)
#     enquanto (opcao != 1 e opcao != 2) {
#       escreva("Opção inválida. Digite 1 ou 2: ")
#       leia(opcao)
#     }
#     escreva("Valor limite (R$): ")
#     leia(valor_limite)
#
#     escreva("\nProdutos filtrados:\n")
#     para (inteiro i = 0; i < quantidade; i++) {
#       se ((opcao == 1 e precos[i] > valor_limite) ou
#           (opcao == 2 e precos[i] < valor_limite)) {
#         escreva(nomes[i], " | ", categorias[i], " | R$ ",
#                 mat.arredondar(precos[i], 2), "\n")
#         encontrados++
#       }
#     }
#     se (encontrados == 0) {
#       escreva("Nenhum produto encontrado.\n")
#     }


# ---------------------------------------------------------------------
# FUNCIONALIDADE 3 - Ordenação por preço
# ---------------------------------------------------------------------
def obter_preco(produto):
    """Chave de ordenação: o preço do produto."""
    return produto["preco"]


def ordenar_crescente(produtos):
    """Preço crescente com list.sort() (em uma cópia da lista)."""
    copia = produtos.copy()
    copia.sort(key=obter_preco)
    return copia


def ordenar_decrescente(produtos):
    """Preço decrescente com sorted(..., reverse=True)."""
    return sorted(produtos, key=obter_preco, reverse=True)


# --- Versão em Portugol: método da bolha (bubble sort) ---------------
# A cada passada, o maior valor "flutua" para o fim da parte ainda
# desordenada. Como os vetores são paralelos, quando o preço troca de
# lugar o nome e a categoria precisam trocar junto.
#
#     // Cópias, para manter os vetores originais na ordem de cadastro
#     cadeia nomes_ord[100]
#     real precos_ord[100]
#     cadeia categorias_ord[100]
#     cadeia aux_nome
#     real aux_preco
#     cadeia aux_categoria
#
#     // ----- CRESCENTE -----
#     para (inteiro i = 0; i < quantidade; i++) {
#       nomes_ord[i] = nomes[i]
#       precos_ord[i] = precos[i]
#       categorias_ord[i] = categorias[i]
#     }
#     para (inteiro passada = 0; passada < quantidade - 1; passada++) {
#       para (inteiro j = 0; j < quantidade - 1 - passada; j++) {
#         se (precos_ord[j] > precos_ord[j + 1]) {   // fora de ordem
#           aux_preco = precos_ord[j]
#           precos_ord[j] = precos_ord[j + 1]
#           precos_ord[j + 1] = aux_preco
#
#           aux_nome = nomes_ord[j]
#           nomes_ord[j] = nomes_ord[j + 1]
#           nomes_ord[j + 1] = aux_nome
#
#           aux_categoria = categorias_ord[j]
#           categorias_ord[j] = categorias_ord[j + 1]
#           categorias_ord[j + 1] = aux_categoria
#         }
#       }
#     }
#     escreva("\nPreço crescente:\n")
#     para (inteiro i = 0; i < quantidade; i++) {
#       escreva(nomes_ord[i], " | R$ ",
#               mat.arredondar(precos_ord[i], 2), "\n")
#     }
#
#     // ----- DECRESCENTE -----
#     // Mesmo algoritmo, copiando de novo os vetores originais
#     // e trocando apenas a comparação: ">" vira "<".
#     para (inteiro i = 0; i < quantidade; i++) {
#       nomes_ord[i] = nomes[i]
#       precos_ord[i] = precos[i]
#       categorias_ord[i] = categorias[i]
#     }
#     para (inteiro passada = 0; passada < quantidade - 1; passada++) {
#       para (inteiro j = 0; j < quantidade - 1 - passada; j++) {
#         se (precos_ord[j] < precos_ord[j + 1]) {   // só mudou aqui
#           ... (mesmas três trocas do bloco crescente) ...
#         }
#       }
#     }
#     escreva("\nPreço decrescente:\n")
#     para (inteiro i = 0; i < quantidade; i++) {
#       escreva(nomes_ord[i], " | R$ ",
#               mat.arredondar(precos_ord[i], 2), "\n")
#     }


# ---------------------------------------------------------------------
# FUNCIONALIDADE 4 - Conjunto de categorias únicas
# ---------------------------------------------------------------------
def obter_categorias_unicas(produtos):
    """Cria um set() com as categorias; duplicatas somem sozinhas."""
    categorias_unicas = set()
    for produto in produtos:
        categorias_unicas.add(produto["categoria"])
    return categorias_unicas


# --- Versão em Portugol: conjunto simulado à mão ---------------------
# Não existe set(). Para cada categoria, percorremos as já guardadas;
# se achar igual, ignora (repetida); senão, guarda no vetor de únicas.
# Obs.: aqui a comparação é exata ("Roupas" != "roupas"). O Python
# normaliza com .title() ao cadastrar; em Portugol, o usuário precisa
# digitar sempre do mesmo jeito (ou usar a biblioteca Texto).
#
#     cadeia categorias_unicas[100]
#     inteiro total_unicas = 0
#     logico ja_existe
#
#     para (inteiro i = 0; i < quantidade; i++) {
#       ja_existe = falso
#       para (inteiro j = 0; j < total_unicas; j++) {
#         se (categorias[i] == categorias_unicas[j]) {
#           ja_existe = verdadeiro
#         }
#       }
#       se (nao ja_existe) {
#         categorias_unicas[total_unicas] = categorias[i]
#         total_unicas++
#       }
#     }
#     escreva("\nCategorias únicas (", total_unicas, "):\n")
#     para (inteiro i = 0; i < total_unicas; i++) {
#       escreva("- ", categorias_unicas[i], "\n")
#     }


# ---------------------------------------------------------------------
# FUNCIONALIDADE 5 - Tupla de estatísticas (imutável)
# ---------------------------------------------------------------------
def calcular_estatisticas(produtos):
    """Devolve a tupla (menor_preco, maior_preco, preco_medio)."""
    precos = [produto["preco"] for produto in produtos]
    menor_preco = min(precos)
    maior_preco = max(precos)
    preco_medio = sum(precos) / len(precos)
    return (menor_preco, maior_preco, preco_medio)


# --- Versão em Portugol: vetor de 3 posições + laço "para" -----------
# Não existe tupla (nem min/max/sum prontos). O vetor de 3 posições
# faz o papel dela: [0] = menor, [1] = maior, [2] = média. Atenção: o
# vetor continua alterável; a imutabilidade é uma garantia do Python.
#
#     real estatisticas[3]
#     real soma_precos = 0
#
#     estatisticas[0] = precos[0]   // menor (começa no 1º preço)
#     estatisticas[1] = precos[0]   // maior (começa no 1º preço)
#     para (inteiro i = 0; i < quantidade; i++) {
#       se (precos[i] < estatisticas[0]) {
#         estatisticas[0] = precos[i]
#       }
#       se (precos[i] > estatisticas[1]) {
#         estatisticas[1] = precos[i]
#       }
#       soma_precos = soma_precos + precos[i]
#     }
#     estatisticas[2] = soma_precos / quantidade


# ---------------------------------------------------------------------
# FUNCIONALIDADE 6 - Relatório final (f-strings)
# ---------------------------------------------------------------------
def imprimir_tabela(titulo, produtos):
    """Imprime uma lista de produtos em colunas alinhadas."""
    print(f"\n{titulo}")
    if not produtos:
        print("  (nenhum produto)")
        return
    for produto in produtos:
        print(
            f"  {produto['nome']:<22} {produto['categoria']:<15} "
            f"R$ {produto['preco']:>9.2f}"
        )


def imprimir_relatorio(produtos, descricao_filtro, produtos_filtrados):
    """Imprime todos os resultados do sistema, formatados com f-strings."""
    produtos_crescente = ordenar_crescente(produtos)
    produtos_decrescente = ordenar_decrescente(produtos)
    categorias_unicas = obter_categorias_unicas(produtos)
    estatisticas = calcular_estatisticas(produtos)
    menor_preco, maior_preco, preco_medio = estatisticas  # desempacota

    linha = "=" * 58
    print(f"\n{linha}")
    print(f"{'RELATÓRIO FINAL DE PRODUTOS':^58}")
    print(linha)
    print(f"Total de produtos cadastrados: {len(produtos)}")

    imprimir_tabela("Produtos (ordem de cadastro):", produtos)
    imprimir_tabela(f"Filtro: {descricao_filtro}", produtos_filtrados)
    imprimir_tabela("Preço crescente (sort):", produtos_crescente)
    imprimir_tabela(
        "Preço decrescente (sorted, reverse=True):", produtos_decrescente
    )

    print(f"\nCategorias únicas ({len(categorias_unicas)}):")
    for categoria in sorted(categorias_unicas):
        print(f"  - {categoria}")

    print("\nEstatísticas de preço:")
    print(f"  Menor preço : R$ {menor_preco:>9.2f}")
    print(f"  Maior preço : R$ {maior_preco:>9.2f}")
    print(f"  Preço médio : R$ {preco_medio:>9.2f}")
    print(linha)


# --- Versão em Portugol: sem f-string, o texto é montado no escreva() -
# O escreva() aceita vários valores separados por vírgula; o
# arredondamento (toFixed / :.2f do Python) vem de mat.arredondar().
#
#     escreva("\n==============================================\n")
#     escreva("          RELATÓRIO FINAL DE PRODUTOS\n")
#     escreva("==============================================\n")
#     escreva("Total de produtos cadastrados: ", quantidade, "\n")
#
#     escreva("\nProdutos (ordem de cadastro):\n")
#     para (inteiro i = 0; i < quantidade; i++) {
#       escreva("  ", nomes[i], " | ", categorias[i], " | R$ ",
#               mat.arredondar(precos[i], 2), "\n")
#     }
#
#     // (Os blocos "filtrados", "crescente", "decrescente" e
#     //  "categorias únicas" já imprimem seus resultados com escreva,
#     //  nas seções anteriores.)
#
#     escreva("\nEstatísticas de preço:\n")
#     escreva("  Menor preço : R$ ",
#             mat.arredondar(estatisticas[0], 2), "\n")
#     escreva("  Maior preço : R$ ",
#             mat.arredondar(estatisticas[1], 2), "\n")
#     escreva("  Preço médio : R$ ",
#             mat.arredondar(estatisticas[2], 2), "\n")
#   }   // fim de inicio()
# }     // fim de programa


# ---------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------
def main():
    """Cadastra os produtos, aplica o filtro e imprime o relatório."""
    print("=== Sistema de Produtos ===")
    quantidade = ler_inteiro(
        f"Quantos produtos deseja cadastrar (1 a {TAMANHO_MAXIMO})? ",
        1,
        TAMANHO_MAXIMO,
    )
    produtos = cadastrar_produtos(quantidade)

    opcao = ler_inteiro(
        "\nFiltrar produtos: 1 - acima de um valor | 2 - abaixo: ", 1, 2
    )
    valor_limite = ler_numero("Valor limite (R$): ")
    acima = opcao == 1
    produtos_filtrados = filtrar_por_preco(produtos, valor_limite, acima)
    sentido = "acima" if acima else "abaixo"
    descricao_filtro = f"preço {sentido} de R$ {valor_limite:.2f}"

    imprimir_relatorio(produtos, descricao_filtro, produtos_filtrados)


if __name__ == "__main__":
    main()
