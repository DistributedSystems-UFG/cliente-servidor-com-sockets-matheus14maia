# Sistema Cliente-Servidor de Calculadora Remota

Este projeto implementa um sistema cliente-servidor básico em Python utilizando sockets. O servidor atua como uma calculadora remota que pode processar requisições de múltiplos clientes para realizar operações aritméticas.

## Descrição do Funcionamento

O sistema é composto por três arquivos principais:

1.  **`server.py`**: O programa servidor que aguarda conexões de clientes. Ao receber uma requisição, ele a processa, realiza o cálculo solicitado e retorna o resultado.
2.  **`client.py`**: O programa cliente que permite ao usuário final enviar uma operação e dois operandos numéricos para o servidor e exibir o resultado recebido.
3.  **`constCS.py`**: Um arquivo de constantes que define o `HOST` (endereço IP do servidor) e a `PORT` (porta de comunicação) para ambos os programas.

A comunicação entre cliente e servidor é feita através do protocolo TCP/IP. Os dados são estruturados em um dicionário Python, serializados com a biblioteca `pickle` antes do envio e desserializados no recebimento.

### Funções Implementadas pelo Servidor

O servidor é capaz de realizar as seguintes operações matemáticas:

| Operação | Nome a ser enviado | Descrição                                        |
| :------- | :----------------- | :------------------------------------------------- |
| Soma     | `sum`              | Retorna a soma de dois números.                    |
| Subtração| `sub`              | Retorna a diferença entre dois números.            |
| Multiplicação | `mul`         | Retorna o produto de dois números.                 |
| Divisão  | `div`              | Retorna a divisão do primeiro pelo segundo número. |

O servidor também realiza tratamento de erros, como operações inexistentes e divisão por zero, retornando uma mensagem de erro apropriada para o cliente.

## Como Executar o Sistema

Para executar a aplicação, você precisará de dois terminais.

1.  **Inicie o Servidor:**
    No primeiro terminal, navegue até a pasta do projeto e execute o script do servidor:
    ```bash
    python server.py
    ```
    O servidor ficará ativo, aguardando por uma conexão.

2.  **Execute o Cliente:**
    No segundo terminal, na mesma pasta, execute o script do cliente:
    ```bash
    python client.py
    ```
    O cliente solicitará que você insira o nome da operação e os dois operandos. Por exemplo:

    ```
    Operação a invocar (sum, sub, mul, div): mul
    Entre com o 1º operando: 7
    Entre com o 2º operando: 6
    ```
    Após o envio, o cliente exibirá o resultado retornado pelo servidor:
    ```
    Resultado: 42
    ```

    **Exemplo com Erro (Divisão por Zero):**
    ```
    Operação a invocar (sum, sub, mul, div): div
    Entre com o 1º operando: 10
    Entre com o 2º operando: 0
    ```
    Resposta:
    ```
    Ocorreu um erro no servidor.
    Motivo:  Erro: Divisão por zero não é permitida.
    ```