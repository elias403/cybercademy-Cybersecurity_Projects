#portscan simples com interface amigável 
from os import system
from time import sleep
import socket

try:
    #impares: n° porta , pares: descrição da porta -> 0 no começo é para fins de organização
    #para adcionar uma nova porta/descrição -> no final acrescente      ,PORTA,,"DESCRIÇÃO",      antes do ]
    portas = [0,21,'FTP(File Transfer protocol - Protocolo de transferência de arquivo)',22,'SSH (Secure Shell - Shell seguro) - Usada para logins seguros, transferência de arquivos e redirecionamento de porta',23,'Telnet protocol - Comunicação de texto sem encriptação',25,'SMTP (Simple Mail Transfer Protocol - Protocolo simples de envio de e-mail) - usada para roteamento de e-mail entre servidores',50,'IPSec',51,'IPSec',53,'Domain Name System (DNS)',67,'Dynamic Host Configuration Protocol (DHCP)',68,'Dynamic Host Configuration Protocol (DHCP)',69,' Trivial File Transfer Protocol (TFTP)',80,'HyperText Transfer Protocol (HTTP)',110,'Post Office Protocol (POP3)',119,' Network News Transport Protocol (NNTP)',123,'Network Time Protocol (NTP)',135,'EPMAP / Microsoft RPC Locator Service',137,'NetBIOS NetBIOS Name Service',138,'NetBIOS NetBIOS Datagram Service',139,'NetBIOS NetBIOS Session Service',143,'Internet Message Access Protocol (IMAP4)',161,'Simple Network Management Protocol (SNMP)',162,'Simple Network Management Protocol (SNMP)',389,'Lightweight Directory Access Protocol',443,' HTTP with Secure Sockets Layer (SSL)',989,' FTP over SSL/TLS (implicit mode)',990,' FTP over SSL/TLS (implicit mode)',3389,' Remote Desktop Protocol',156,'SQL Server'
    ]
    
    #menu inicial
    def menu():
        
        system('cls'or'clean')
        print('****** SIMPLE PORT SCAN ****** ')
        print('1 - Iniciar SCAN simples')
        print('2 - Outros')
        print('0 - sair do programa')
        print('*este programa tem como objetivo ajudar aos iniciantes da área, use-o apenas em "locais" permitidos para fins educacionais*')
        escolha = input('Opções: ')
        
        #opção 1
        if   escolha == '1':
            system('cls'or'clear')
            print('1 - scan das portas até 1024(pode demorar)')
            print('2 - RECOMENDADO - scan das portas mais comuns com descrição (OBS: descrição do serviço PADRÃO)')
            print('0 -> voltar')
            op1= input(' ')
            if op1 == '0':
                menu()
            elif op1 == '1':
                system('cls'or'clear')
                print('IP ou endereço do alvo (exemplos:192.168.0.1 / scanme.nmap.org)')
                x = input()
                if x == '0':
                    menu()
                scan1024(x)
            elif op1 == '2':
                system('cls'or'clear')
                print('IP ou endereço do alvo (exemplos:192.168.0.1 / scanme.nmap.org)')
                x =input()
                if x == '0':
                    menu()
                scancp(x)

            
            

        elif escolha == '2':
            print('1 -> portas registradas neste programa com suas descrições')
            print('0 -> voltar')
            x = input()
            if x == '0':
                menu()
            elif x == '1':
                configports()
       
        elif escolha == '0':
            exit()
        else:
            menu()    
    #scan comum ate 1024
    def scan1024(ip):
        system('cls'or'clear')
        for count in range(0,1024):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if s.connect_ex((ip, count)) == 0:
                print(f'A porta {count} está aberta')
            s.close()
        print('Fim do scan')
        print('Voltar para o menu? s/n -> n ira sair do programa')
        fim = input()
        if fim =='n':
            exit()
        else:
            menu()
    #scan em portas comumente utilizadas RECOMENDADO
    def scancp(ip):
        system('cls'or'clear')
        ports = list() 
        #função para pegar os valores numericos da lista portas e jogar em ports
        for valores in portas:
            if type(valores) == int:
               ports.append(valores) 

        for count in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #se retornar 0 é porque a porta esta aberta
            if s.connect_ex((ip, count)) == 0:
                print(f'A porta {count} está aberta : {portas[1+(portas.index(count))]}')
                #verificar o index de count em portas e somar com 1
            s.close()
            


        print('Fim do scan')
        print('Voltar para o menu? s/n -> n ira sair do programa')
        fim = input()
        if fim =='n':
            exit()
        else:
            menu()
    #portas registradas no programa
    def configports():
        #função para pegar os valores numericos da lista
        ports = list()
        for valores in portas:
            if type(valores) == int:
               ports.append(valores) 
        print(ports)

    menu()

except KeyboardInterrupt:
    print('saindo do programa...')
    sleep(0.5)