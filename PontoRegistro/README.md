# README #

Neste projeto simples, apenas para criar uma aplicação com em python que ficará up através do systemd que ficará responsável por manter up o processo pelo gunicorn e recebendo as requisições do socket pelo nginx

### Instalação

   - sudo apt update && sudo apt install python3-pip ( PIP é o gerenciador de pacotes, conferir se está na versão 20.x ou maior)
   - pip install pipenv  - (PIPENV é o utilitário do pip que vai permitir criar os ambiente para rodar o projeto, podendo ser persinalizado e separado das libs do ambiente, pois roda apenas para o usuário. Que é basicamente o uso do virtualenv + requeriments.txt)

   À partir daqui pode rodar os comandos dentro do diretório do respositório.
   
   - pipenv --python 3.6 - (pode ser outra versão da sua preferência, mas acima da 3.6 é o necessário pra rodar, caso não encontre, coloque o patch completo do python para que ele possa executar. Esta ação serve para definir qual ambiente será usado no virtualenv.)
   - pipenv install flask gunicorn pytz python-dotenv - (flask é o serviço que vai disponibilizar o aplicativo, gunicorn serve as aplicações em ambiente de produção/dev/ etc.., pytz para buscar a timezone do local onde será gravado o horário, python-dotenv para guardar as informações do flask (.flaskenv))
   - pipenv shell - (vai carregar o virtualenv.)
   - which gunicorn - (você precisará substituir nos arquivos em intragracao/: registroponto.service o path do arquivo, e o caminho físico do projeto)
   - sudo apt install nginx - (para tratar as requisições do socket, no arquivo registroponto.conf alterar o também o caminho onde está o arquivo do socket)
   - systemctl status registroponto.conf
   - systemctl start registroponto.conf - (conferir se não vai dar erro)
   - para testar usar o nome do server_name do vhost, ficando à sua escolha, basta adicionar no arquivo hosts ao lado do localhost o endereço. 
   copiar o vhost em /etc/nginx/sites-available, depois criar o link simbólico para /etc/nginx/sites-enable, nginx -t ver se tá tudo certo, sudo systemctl reload nginx
   - para sair do virtualenv CTRL+D (como no terminal mesmo).
   
Para acessar basta, usar a url pontoregistro.local/user/nomeusuario/entrada ou saida, qualquer registro que queira gravar, vai mandar para o .txt no diretório registropontos/

   > Obs: configurar o .flaskenv para o nome do script inicial, se quiser mudar o nome do mesmo, se não basta deixar como está, também lembrar de alterar os imports nos scripts wsgi.py e ponto.py que são os responsáveis por iniciar a app.





### links de apoio 

[configurando pipenv](https://imasters.com.br/py/gerenciando-seu-projeto-python-com-o-pipenv)

[criando projeto com pipenv](https://prettyprinted.com/tutorials/automatically_load_environment_variables_in_flask)

[configurando serviços](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04-pt#passo-5-%E2%80%94-configurando-o-nginx-para-solicita%C3%A7%C3%B5es-de-proxy)

[instalar virtualenv](https://linuxize.com/post/how-to-install-flask-on-ubuntu-18-04/)

[instalar flask](https://linuxize.com/post/how-to-install-flask-on-ubuntu-18-04/)

[criar rotas](https://www.tutorialspoint.com/python_network_programming/python_routing.htm)

[pipenv](https://docs.pipenv.org/en/latest/)
