import random

questoes_base = [{
    "pergunta": "onde baixar o termux? ",
    "resposta": "Fdroid"
},
{
    "pergunta": "Digite os comandos para actualizar",
    "resposta": "update && upgrade"
},
{
    "pergunta": "como instalar o python: ",
    "resposta": "pkg install python"
}]



questoes =[{
    "pergunta": "Qual e o comando que mostra o caminho da pasta actal: ",
    "resposta": "pwd"
},
{
    "pergunta": "Qual comando cria nova pasta? ",
    "resposta": "mkdir nome_da_pasta"
},
{
    "pergunta": "Digite o comando para limpar tela: ",
    "resposta": "clear"
},
{
    "pergunta": "Que comandos serve para ver/ listar oque tem na pasta actual: ",
    "resposta": "ls"
},
{
    "pergunta": "Digite o comando para ver arquivos ocultos: ",
    "resposta": "ls -a"
},
{
    "pergunta": "Que comando serve para entrar na pasta/diretorio: ",
    "resposta": "cd nome_da_pasta"
},
{
    "pergunta": "Que comando volta para a pasta principal home: ",
    "resposta": "cd ~"
},
{
    "pergunta": "Que comando volta apenas um diretorio? ",
    "resposta": "cd .."
},
{
    "pergunta": "Qual comando cria um arquivo vazio: ",
    "resposta": "touch nome_do_arquivo.txt"
},
{
    "pergunta": "Que comando serve para copiar arquivo? ",
    "resposta": "cp nome_do_arquivo.txt /storage/emulated/0/"
},
{
    "pergunta": "Qual comando serve para mover arquivo? ",
    "resposta": "mv nome_do_arquivo.txt /storage/emulated/0/"
},
{
    "pergunta": "Que comando serve para renomear um arquivo? ",
    "resposta": "mv nome_do_arquivo.txt novo_nome.txt"
},
{
    "pergunta": "Digite o comando para apagar arquivo: ",
    "resposta": "rm nome_do_arquivo.txt"
},
{
    "pergunta": "Digite o comando para apagar pasta: ",
    "resposta": "rm -r nome_da_pasta"
},
{
    "pergunta": "Que comando serve para ver/listar os arquivos em formato detalhado. permissões (-rwxrwxrwx), o dono do arquivo, o grupo, o tamanho, a data de modificação e o nome: ",
    "resposta": "ls -l"
},
{
    "pergunta": "Digite o comando que serve para apagar uma pasta, mas apenas se ela estiver vazia: ",
    "resposta": "rmdir nome_da_pasta"
},
{
    "pergunta": "Digite o comando que Exibe o conteúdo de um arquivo de texto diretamente na tela do terminal): ",
    "resposta": "cat nome_do_arquivo.txt"
},
{
    "pergunta": "Digite o arquivo que serve para mover o arquivo para pasta_destino: ",
    "resposta": "mv nome_do_arquivo.txt pasta_destino/"
},
{
    "pergunta": "Digite o comando que mostra uma lista de todos os comandos que você usou recentemente no terminal: ",
    "resposta": "history"
},
{
    "pergunta": "Digite comqndo que abre o 'manual' de um comando.Para sair do manual, pressione q: ",
    "resposta": "man nome do comando"
},
{
    "pergunta": "Digite o comando que executa um comando com privilégios de administrador (superusuário). alterar arquivos críticos do sistema. : ",
    "resposta": "sudo nome do comando"
},
{
    "pergunta": " Digite comandos de Reinicia ou desliga o sistema, respectivamente: ",
    "resposta": "reboot/shutdown"
},
{
    "pergunta": "Digite o comando para testa a conexão com outro computador ou servidor. : ",
    "resposta": "ping endereco IP"
},
{
    "pergunta": "Digite comando para mostra informações sobre as interfaces de rede do seu computador, como o endereço IP.",
    "resposta": "ifconfig/ip a"
}]

random.shuffle(questoes)
tamanho = len(questoes)
ponto = 0
b = 0

for a in questoes_base:
    while True:
        resposta_user = input(a['pergunta'])
        if resposta_user == a['resposta']:
            print("acertou na base")
            break
        else:
            print(f"errou seria: {a['resposta']}")
for a in questoes:
    c = 0
    while True:
        c += 1
        resposta_user = input(a['pergunta'])
        if resposta_user == a['resposta']:
            if c == 1:
                ponto +=1
                print(f"acertou tem {ponto}/{tamanho} errou {b}")
            else:
                print(f"acertou, mas nao ganhou ponto {ponto}/{tamanho} errou {b}")
            break
        else:
            c+=1
            if c == 2:
                b +=1
                print(f"Errado, tente novamente,\nerrou {b} perguntas resposta seria: {a['resposta']} ")

print(f"fim voce acertou {ponto} no total de {tamanho}")
                

