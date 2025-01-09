# MiniCell
Projeto de orientação a objetos simulando aplicativos em um celular, com I/O no terminal.

Para que este programa funcione é necessário a instalação do repositório do bot do telegram, que pode ser feito usando este comando no terminal do linux:
	
	pip install python-telegram-bot --upgrade
	
Manual de uso:

	Menus:
		Para escolher qual opção do menu é desejada, escreva aquilo que está escrito após os dois pontos na opção desejada.

-----------------------------------
	
	Calculadora Simples:
		Caso você queira utilizar o valor da resposta anterior, digite, no local de um dos valores: Resp.
		Caso você queira utilizar o valor de M digite, no local de um dos valores: M
		
		-soma, subtração, multiplicação, divisão, módulo, potência:
			
			Digite dois números separados por um espaço:
			
				a b
					
		-fatorial, somar ao M, subtrair do M:
		
			Digite um número:
				
				a
				
-----------------------------------
				
	Contatos:
	
		-adicionar pessoas:
		
			Digite o nome (completo ou não) da pessoa.
			Digite o número de telefone da pessoa no formato:
				
				(+XX) XX XXXXX-XXXX
				
			Digite o email da pessoa.
			
		-alterar contato, exibir parâmetro:
		
			Digite o nome completo (salvo no app) da pessoa em questão.
			Digite o nome do parâmetro a ser alterado ou exibido, utilizando um dos nomes dos parâmetros escritos dentro dos parênteses do prompt no terminal. (O valor do parametro TeleID só pode ser alterado dentro do app de mensagens)
			
		-deletar pessoas:
		
			Digite o nome completo (salvo no app) da pessoa em questão.
			Digite sim ou não para confirmar ou negar a remoção da pessoa dos contatos.
			
		(OBS: Para que os dados sejam utilizados em outros aplicativos do programa (Bot do Telegram),e para que as mudanças não sejam perdidas entre usos do programa, é necessário salvar as mudanças feitas aos contatos usando o comando "salvar".)
		
-----------------------------------
		
	Mensagens (Telegram Bot):
		Para enviar uma mensagem é necessário que o contato salvo no programa (através do app Contatos) tenha um TeleID salvo (que pode ser feito através do comando "newid"), que só pode ser feito após a pessoa ter mandado ao menos uma mensagem ao bot @MiniVit_bot no Telegram.
		
		-enviar mensagem:
			
			Digite o nome completo (salvo no app de contatos) da pessoa em questão.
			Digite a mensagem a ser enviada à pessoa.
			
		-salvar um novo id:
		
			Digite o nome completo (salvo no app de contatos) da pessoa em questão.
			Envie uma mensagem ao bot @MiniVit_bot no Telegram, na conta da pessoa que terá o ID salvo.
			Digite "enviado" para confirmar que a mensagem acima foi enviada.
			
		(OBS: Se caso, ao tentar salvar um id novo, o terminal diga que essa pessoa não foi encontrada, certifique-se que as últimas mudanças feitas no app dos contatos foram salvas.)
		
		
