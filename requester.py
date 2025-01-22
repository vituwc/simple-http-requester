import requests
from termcolor import colored

def fazer_requisicao(url, metodo, mostrar_codigo_fonte=False):
    try:
        if metodo == "GET":
            response = requests.get(url)
        elif metodo == "HEAD":
            response = requests.head(url)
        else:
            print(colored("[!] Método inválido!", "red"))
            return None
        
        if response.status_code == 200:
            status_color = "green"
        else:
            status_color = "red"
        
        print(colored(f"[+] Status: {response.status_code} - {response.reason}", status_color))
        print(colored("[+] Cabeçalhos da resposta:", "green"))
        for header, value in response.headers.items():
            print(f"  {header}: {value}")

        if mostrar_codigo_fonte:
            print(f"\n[+] Código Fonte do site: \n{response.text}")
        
        return response
    
    except requests.RequestException as e:
        print(colored(f"[!] Erro: {e}", "red"))
        return None

def salvar_arquivo(codigo_fonte, nome_arquivo):
    try:
        with open(nome_arquivo, "w") as f:
            f.write(codigo_fonte)
        print(f"Arquivo salvo em {nome_arquivo}")
    except Exception as e:
        print(colored(f"Erro ao salvar arquivo: {e}", "red"))

def menu_principal():
    while True:
        url = input("[-] Endereço do site: ").strip()
        if not url:
            print(colored("[!] Endereço inválido. Tente novamente.", "red"))
            continue
        break

    print()
    while True:
        porta = input("[-] Porta do site (Default: 80):").strip() or "80"
        if not porta.isdigit() or int(porta) < 1 or int(porta) > 65535:
            print(colored("[!] Porta inválida. Tente novamente.", "red"))
            continue
        break

    url = f"http://{url}:{porta}"

    while True:
        print("[-] Selecione o que quer:")
        print("[!] 1 - GET / HTTP/1.0")
        print("[!] 2 - HEAD / HTTP/1.0")
        metodo_opcao = input("> ").strip()

        if metodo_opcao == "1":
            metodo = "GET"
            break
        elif metodo_opcao == "2":
            metodo = "HEAD"
            break
        else:
            print(colored("[!] Opção inválida. Tente novamente.", "red"))

    while True:
        print("[?] Deseja ver o código fonte? (S/n):")
        mostrar_fonte = input("> ").strip().lower()
        if mostrar_fonte not in ['s', 'n']:
            print(colored("[!] Opção inválida. Tente novamente.", "red"))
            continue
        mostrar_fonte = mostrar_fonte == 's'
        break

    while True:
        print("[?] Deseja salvar o código fonte? (S/n):")
        salvar = input("> ").strip().lower()
        if salvar not in ['s', 'n']:
            print(colored("[!] Opção inválida. Tente novamente.", "red"))
            continue
        salvar = salvar == 's'
        break

    response = fazer_requisicao(url, metodo, mostrar_fonte)

    if response:
        print(colored("[+] Resposta Recebida!", "green"))

        if salvar:
            print("[-] Qual vai ser o nome do arquivo? (a extensão será .txt)")
            nome_arquivo = input("> ").strip()
            nome_arquivo = nome_arquivo if nome_arquivo.endswith('.txt') else nome_arquivo + '.txt'
            salvar_arquivo(response.text, nome_arquivo)

        while True:
            print("[?] Deseja voltar para o menu? (S/n):")
            voltar = input("> ").strip().lower()
            if voltar == 's':
                break  
            else:
                print(colored("[+] Saindo do programa...", "green"))
                return  

def main():
    menu_principal()

if __name__ == "__main__":
    main()
