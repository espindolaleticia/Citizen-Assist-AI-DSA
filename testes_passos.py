# Testes dos passos 1 a 4 (para rodar: python testes_passos.py)
from citizen_assist import Servico, ListaEncadeada


# Teste rápido do passo 1 (só roda se executar este arquivo diretamente)
if __name__ == "__main__":
    lista = ListaEncadeada()
    lista.percorrer()                                 # lista vazia

    lista.inserir(Servico(1, "Vacinação contra gripe", "Vacinação",
                          "Vacina anual gratuita", "Documento com foto", "UBS Centro"))
    lista.inserir(Servico(2, "Consulta clínico geral", "Atendimento básico",
                          "Consulta na rede pública", "Cartão SUS", "UBS Norte"))
    print("Inserir id duplicado:", lista.inserir(Servico(1, "X", "X", "X", "X", "X")))

    lista.percorrer()
    print("Remover id 1:", lista.remover(1))
    print("Remover id 99:", lista.remover(99))
    lista.percorrer()

    # Testes do passo 2
    print("\n--- Passo 2: atualizar e pesquisar ---")
    lista.inserir(Servico(3, "Consulta de pediatria", "Atendimento básico",
                          "Atendimento para crianças", "Cartão SUS", "UBS Leste"))
    print("Atualizar id 2:", lista.atualizar(2, local="UBS Sul"))
    print("Atualizar id 99:", lista.atualizar(99, local="X"))

    achados = lista.pesquisar("titulo", "consulta")
    print(f"Pesquisa título 'consulta': {len(achados)} resultado(s)")
    for s in achados:
        print(s)

    achados = lista.pesquisar("categoria", "atendimento")
    print(f"Pesquisa categoria 'atendimento': {len(achados)} resultado(s)")

    achados = lista.pesquisar("categoria", "xyz")
    print(f"Pesquisa categoria 'xyz': {len(achados)} resultado(s)")

    # Testes do passo 3
    print("\n--- Passo 3: ordenação ---")

    def mostrar_resumo(l):
        atual = l.inicio
        while atual is not None:
            print(f"  {atual.servico.id} - {atual.servico.titulo} ({atual.servico.categoria})")
            atual = atual.proximo

    lista.inserir(Servico(9, "Acompanhamento nutricional", "Atendimento básico",
                          "Orientação alimentar", "Encaminhamento médico", "UBS Oeste"))
    lista.inserir(Servico(4, "Vacinação infantil", "Vacinação",
                          "Vacinas do calendário infantil", "Caderneta de vacinação", "UBS Centro"))
    print("Ordem de cadastro:")
    mostrar_resumo(lista)

    lista.ordenar("titulo")
    print("Ordenado por título:")
    mostrar_resumo(lista)

    lista.ordenar("id")
    print("Ordenado por id:")
    mostrar_resumo(lista)

    lista.ordenar("categoria")
    print("Ordenado por categoria:")
    mostrar_resumo(lista)

    print("Critério inválido:", lista.ordenar("local"))
    lista_vazia = ListaEncadeada()
    print("Ordenar lista vazia:", lista_vazia.ordenar("titulo"))

    # Testes do passo 4
    print("\n--- Passo 4: análise ---")
    lista.exibir_analise()
    lista_vazia.exibir_analise()
