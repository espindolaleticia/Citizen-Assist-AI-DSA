# Citizen Assist AI - Global Solution 2026.2
# Recorte escolhido: Serviços de saúde
# Para executar: python citizen_assist.py


class Servico:
    """Um registro do sistema: um serviço de saúde."""

    def __init__(self, id_servico, titulo, categoria, descricao, requisitos, local):
        self.id = id_servico          # identificador único (número inteiro)
        self.titulo = titulo
        self.categoria = categoria
        self.descricao = descricao
        self.requisitos = requisitos
        self.local = local

    def __str__(self):
        return (f"[{self.id}] {self.titulo} | Categoria: {self.categoria}\n"
                f"    Descrição: {self.descricao}\n"
                f"    Requisitos: {self.requisitos}\n"
                f"    Local: {self.local}")


class No:
    """Um nó da lista: guarda um serviço e aponta para o próximo nó."""

    def __init__(self, servico):
        self.servico = servico
        self.proximo = None           # None = fim da lista


class ListaEncadeada:
    """Lista encadeada simples, implementada do zero."""

    def __init__(self):
        self.inicio = None            # primeiro nó (None = lista vazia)
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def buscar_por_id(self, id_servico):
        """Percorre a lista até achar o id. Retorna o Servico ou None."""
        atual = self.inicio
        while atual is not None:
            if atual.servico.id == id_servico:
                return atual.servico
            atual = atual.proximo
        return None

    def inserir(self, servico):
        """Insere no final da lista. Retorna False se o id já existir."""
        if self.buscar_por_id(servico.id) is not None:
            return False              # id duplicado

        novo = No(servico)
        if self.inicio is None:       # lista vazia: o novo nó é o primeiro
            self.inicio = novo
        else:                         # senão, anda até o último nó
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo
        self.tamanho += 1
        return True

    def percorrer(self):
        """Mostra todos os registros, do primeiro ao último."""
        if self.esta_vazia():
            print("Nenhum registro cadastrado.")
            return
        atual = self.inicio
        while atual is not None:
            print(atual.servico)
            atual = atual.proximo

    def remover(self, id_servico):
        """Remove o nó com o id informado. Retorna True/False."""
        atual = self.inicio
        anterior = None
        while atual is not None:
            if atual.servico.id == id_servico:
                if anterior is None:                  # removendo o primeiro
                    self.inicio = atual.proximo
                else:                                 # "pula" o nó removido
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False                                  # id não encontrado

    # ---------- PASSO 2: atualizar e pesquisar ----------

    def atualizar(self, id_servico, titulo="", categoria="", descricao="",
                  requisitos="", local=""):
        """Atualiza os campos informados. Campo vazio = mantém o valor atual.
        Retorna False se o id não existir."""
        servico = self.buscar_por_id(id_servico)
        if servico is None:
            return False
        if titulo:
            servico.titulo = titulo
        if categoria:
            servico.categoria = categoria
        if descricao:
            servico.descricao = descricao
        if requisitos:
            servico.requisitos = requisitos
        if local:
            servico.local = local
        return True

    def pesquisar(self, campo, texto):
        """Busca linear por 'titulo' ou 'categoria'.
        Ignora maiúsculas/minúsculas e aceita parte do texto.
        Retorna uma lista (vazia se nada for encontrado)."""
        resultados = []
        texto = texto.strip().lower()
        atual = self.inicio
        while atual is not None:               # olha nó por nó
            if campo == "titulo":
                valor = atual.servico.titulo.lower()
            else:
                valor = atual.servico.categoria.lower()
            if texto in valor:
                resultados.append(atual.servico)
            atual = atual.proximo
        return resultados

    # ---------- PASSO 3: ordenação (Insertion Sort) ----------

    def _chave(self, servico, criterio):
        """Devolve o valor usado para comparar dois registros."""
        if criterio == "id":
            return servico.id
        if criterio == "titulo":
            return servico.titulo.lower()
        return servico.categoria.lower()

    def ordenar(self, criterio="titulo"):
        """Ordena a lista (ordem crescente) com Insertion Sort.
        criterio: 'id', 'titulo' ou 'categoria'.
        Retorna False se o critério for inválido."""
        if criterio not in ("id", "titulo", "categoria"):
            return False

        ordenada = None                  # início da nova lista, já ordenada
        atual = self.inicio
        while atual is not None:
            proximo = atual.proximo      # guarda o próximo antes de mexer nos links

            # Caso 1: o nó vai para o início da lista ordenada
            if ordenada is None or \
               self._chave(atual.servico, criterio) < self._chave(ordenada.servico, criterio):
                atual.proximo = ordenada
                ordenada = atual
            # Caso 2: procura a posição certa no meio/fim da lista ordenada
            else:
                aux = ordenada
                while aux.proximo is not None and \
                      self._chave(aux.proximo.servico, criterio) <= self._chave(atual.servico, criterio):
                    aux = aux.proximo
                atual.proximo = aux.proximo
                aux.proximo = atual

            atual = proximo

        self.inicio = ordenada
        return True

    # ---------- PASSO 4: análise ----------

    def contar_por_categoria(self):
        """Percorre a lista uma vez e conta quantos serviços há em cada categoria.
        Retorna um dicionário no formato {categoria: quantidade}."""
        contagem = {}
        atual = self.inicio
        while atual is not None:
            cat = atual.servico.categoria.strip().lower()   # agrupa sem diferenciar maiúsculas
            if cat in contagem:
                contagem[cat] += 1
            else:
                contagem[cat] = 1
            atual = atual.proximo
        return contagem

    def exibir_analise(self):
        """Mostra o total de registros e a distribuição por categoria."""
        print("=== Análise dos registros ===")
        if self.esta_vazia():
            print("Nenhum registro cadastrado.")
            return
        print(f"Total de serviços: {self.tamanho}")
        print("Serviços por categoria:")
        contagem = self.contar_por_categoria()
        for cat in contagem:
            qtd = contagem[cat]
            porcentagem = qtd / self.tamanho * 100
            print(f"  - {cat.capitalize()}: {qtd} ({porcentagem:.1f}%)")


# ---------- PASSO 5: menu interativo e validações ----------

def ler_texto(mensagem):
    """Pede um texto e repete até o usuário digitar algo (não aceita vazio)."""
    while True:
        valor = input(mensagem).strip()
        if valor != "":
            return valor
        print("Entrada inválida: o campo não pode ficar vazio.")


def ler_inteiro(mensagem):
    """Pede um número inteiro maior que zero e repete até a entrada ser válida."""
    while True:
        valor = input(mensagem).strip()
        try:
            numero = int(valor)
        except ValueError:
            print("Entrada inválida: digite um número inteiro.")
            continue
        if numero > 0:
            return numero
        print("Entrada inválida: o número deve ser maior que zero.")


def cadastrar(lista):
    print("\n--- Cadastrar serviço ---")
    id_servico = ler_inteiro("ID (número inteiro): ")
    if lista.buscar_por_id(id_servico) is not None:   # evita ID duplicado
        print("Erro: já existe um serviço com esse ID.")
        return
    titulo = ler_texto("Título: ")
    categoria = ler_texto("Categoria: ")
    descricao = ler_texto("Descrição: ")
    requisitos = ler_texto("Requisitos: ")
    local = ler_texto("Local de atendimento: ")
    lista.inserir(Servico(id_servico, titulo, categoria, descricao, requisitos, local))
    print("Serviço cadastrado com sucesso!")


def consultar(lista):
    print("\n--- Consultar por ID ---")
    if lista.esta_vazia():
        print("Nenhum registro cadastrado.")
        return
    id_servico = ler_inteiro("ID: ")
    servico = lista.buscar_por_id(id_servico)
    if servico is None:
        print("Nenhum serviço encontrado com esse ID.")
    else:
        print(servico)


def atualizar(lista):
    print("\n--- Atualizar serviço ---")
    if lista.esta_vazia():
        print("Nenhum registro cadastrado.")
        return
    id_servico = ler_inteiro("ID do serviço a atualizar: ")
    servico = lista.buscar_por_id(id_servico)
    if servico is None:
        print("Nenhum serviço encontrado com esse ID.")
        return
    print("Dados atuais:")
    print(servico)
    print("Digite o novo valor ou apenas Enter para manter o atual.")
    titulo = input("Novo título: ").strip()
    categoria = input("Nova categoria: ").strip()
    descricao = input("Nova descrição: ").strip()
    requisitos = input("Novos requisitos: ").strip()
    local = input("Novo local: ").strip()
    lista.atualizar(id_servico, titulo, categoria, descricao, requisitos, local)
    print("Serviço atualizado com sucesso!")


def excluir(lista):
    print("\n--- Excluir serviço ---")
    if lista.esta_vazia():
        print("Nenhum registro cadastrado.")
        return
    id_servico = ler_inteiro("ID do serviço a excluir: ")
    if lista.remover(id_servico):
        print("Serviço excluído com sucesso!")
    else:
        print("Nenhum serviço encontrado com esse ID.")


def pesquisar(lista):
    print("\n--- Pesquisar serviços ---")
    if lista.esta_vazia():
        print("Nenhum registro cadastrado.")
        return
    print("1 - Por título")
    print("2 - Por categoria")
    escolha = input("Pesquisar por: ").strip()
    campos = {"1": "titulo", "2": "categoria"}
    if escolha not in campos:
        print("Opção inválida.")
        return
    texto = ler_texto("Texto a buscar: ")
    resultados = lista.pesquisar(campos[escolha], texto)
    if len(resultados) == 0:
        print("Nenhum serviço encontrado para essa pesquisa.")
    else:
        print(f"{len(resultados)} serviço(s) encontrado(s):")
        for servico in resultados:
            print(servico)


def ordenar(lista):
    print("\n--- Ordenar registros ---")
    if lista.esta_vazia():
        print("Nenhum registro cadastrado.")
        return
    print("1 - Por ID")
    print("2 - Por título")
    print("3 - Por categoria")
    escolha = input("Ordenar por: ").strip()
    criterios = {"1": "id", "2": "titulo", "3": "categoria"}
    if escolha not in criterios:
        print("Opção inválida.")
        return
    lista.ordenar(criterios[escolha])
    print(f"Lista ordenada por {criterios[escolha]}:")
    lista.percorrer()


def carregar_exemplos(lista):
    """Cadastra alguns serviços de exemplo (útil para a demonstração)."""
    exemplos = [
        Servico(1, "Vacinação contra gripe", "Vacinação",
                "Vacina anual gratuita", "Documento com foto", "UBS Centro"),
        Servico(2, "Consulta clínico geral", "Atendimento básico",
                "Consulta na rede pública", "Cartão SUS", "UBS Norte"),
        Servico(3, "Consulta de pediatria", "Atendimento básico",
                "Atendimento para crianças", "Cartão SUS", "UBS Leste"),
        Servico(4, "Exame de sangue", "Exames",
                "Coleta para exames laboratoriais", "Pedido médico", "Laboratório Municipal"),
        Servico(5, "Acompanhamento nutricional", "Atendimento básico",
                "Orientação alimentar", "Encaminhamento médico", "UBS Oeste"),
    ]
    novos = 0
    for servico in exemplos:
        if lista.inserir(servico):      # ignora IDs que já existem
            novos += 1
    print(f"{novos} serviço(s) de exemplo carregado(s).")


def mostrar_menu():
    print("\n===== CITIZEN ASSIST AI - Serviços de Saúde =====")
    print("1 - Cadastrar serviço")
    print("2 - Consultar por ID")
    print("3 - Atualizar serviço")
    print("4 - Excluir serviço")
    print("5 - Pesquisar (título ou categoria)")
    print("6 - Ordenar e exibir")
    print("7 - Listar todos")
    print("8 - Apresentar análise")
    print("9 - Carregar dados de exemplo")
    print("0 - Encerrar")


def main():
    lista = ListaEncadeada()
    try:
        while True:
            mostrar_menu()
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "1":
                cadastrar(lista)
            elif opcao == "2":
                consultar(lista)
            elif opcao == "3":
                atualizar(lista)
            elif opcao == "4":
                excluir(lista)
            elif opcao == "5":
                pesquisar(lista)
            elif opcao == "6":
                ordenar(lista)
            elif opcao == "7":
                print("\n--- Todos os serviços ---")
                lista.percorrer()
            elif opcao == "8":
                lista.exibir_analise()
            elif opcao == "9":
                carregar_exemplos(lista)
            elif opcao == "0":
                print("Encerrando o Citizen Assist AI. Até logo!")
                break
            else:
                print("Opção inexistente. Escolha um número do menu.")
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma encerrado.")


if __name__ == "__main__":
    main()
