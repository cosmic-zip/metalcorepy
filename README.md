# MetalCorePy

MetalCorePy are a simple fullstack application with stock django and DRF app and nginx configuration. includes:

- docker compose
- docker apps
- the main django core app with DDD
- `env` files setup
- database foder for data scripts
- scripts folder for scripts and helpers

## Install localy 

```console
python3 -m  venv venv
source venv/bin/activate
pip install -m app/requirements.txt
cp scripts/commit-msg .git/hooks/
```

## Run with docker

```console
docker compose up
```

## Add new app 


```console
python manage.py create_domain domain_name
```

## Como rodar as migrations dentro do container?

## Passo 1: Entrar no container

Use o nome do container conforme declarado no `docker-compose.yml`. No seu caso:

```bash
docker exec -it metalcorepy_app bash
```

Se estiver usando Alpine ou uma imagem que não tenha `bash`, use:

```bash
docker exec -it metalcorepy_app sh
```

Agora você está **dentro do ambiente do container Django**, com acesso ao código e ao Python com os pacotes corretos.

---

## Passo 2: Executar as migrations

Dentro do container:

```bash
python manage.py migrate
```

Esse comando irá:

* Conectar ao banco PostgreSQL conforme o `.env.dev`
* Criar as tabelas padrão do Django (auth, admin, etc.)
* Aplicar quaisquer migrations customizadas dos seus apps

---

## Alternativa: rodar direto com `docker compose run`

Se preferir executar em uma linha, **sem entrar no container**, pode usar:

```bash
docker compose exec web python manage.py migrate
```

ou, se o serviço se chama `metalcorepy_app`:

```bash
docker compose exec metalcorepy_app python manage.py migrate
```

---

## Atenção: o banco de dados precisa estar pronto

Antes de rodar `migrate`, o banco PostgreSQL precisa:

* Estar acessível (porta correta)
* Estar inicializado com o usuário e senha certos
* Ter o nome do banco criado (o container oficial do PostgreSQL cria automaticamente)

Caso o erro persista, execute:

```bash
docker compose logs postgres
```