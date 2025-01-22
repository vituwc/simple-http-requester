# **Requester - Script de Requisição HTTP**

Este é um simples **script de requisição HTTP** desenvolvido em Python, criado para fins educacionais e aprendizado. Ele permite fazer requisições `GET` ou `HEAD` a um site e exibe o status da resposta, cabeçalhos e, opcionalmente, o código fonte da página.

---

## **Como Usar**

1. Faça o download ou clone este repositório.
2. Execute o script no terminal:

```bash
python requester.py
```

3. O script solicitará o **endereço do site**, a **porta** (com valor padrão 80), o **método de requisição** (GET ou HEAD), e se você deseja ver o **código fonte** da página.

---

## **Exemplo de Execução**

```bash
[-] Endereço do site: www.businesscorp.com.br

[-] Porta do site (Default: 80): 80

[-] Selecione o que quer:
[!] 1 - GET / HTTP/1.0
[!] 2 - HEAD / HTTP/1.0
> 1

[?] Deseja ver o código fonte? (S/n):
> n

[+] Resposta Recebida! 
[+] Status: 200 - OK
[+] Cabeçalhos da resposta:
  Date: Mon, 21 Jan 2025 15:00:00 GMT
  Server: Apache/2.4.41 (Debian)
  Content-Type: text/html; charset=UTF-8
  ...

[-] Deseja voltar para o menu? (S/n):
> s
```

---

## **Descrição**

**Requester** - Script simples de requisição HTTP em Python: Ferramenta para realizar requisições `GET` ou `HEAD` a um site, exibindo a resposta, status HTTP e cabeçalhos. Desenvolvido com foco educacional e aprendizado, o script pode conter falhas, pois é um projeto de prática. Exibe as respostas da requisição e permite visualizar o código fonte da página.

---

## **Aviso de Uso**

Este script foi feito **apenas para fins educacionais** e **não é adequado para uso em produção**. O código pode conter falhas e vulnerabilidades, sendo recomendado seu uso apenas em **ambientes controlados e para aprendizado**. Evite usá-lo em sistemas de terceiros sem permissão.

---

## **Requisitos**

- Python 3.x
- Biblioteca `requests`
- Biblioteca `termcolor` para colorir a saída no terminal

---

## **Instalação**

Para rodar o script, instale as bibliotecas necessárias:

```bash
pip install requests termcolor
```
