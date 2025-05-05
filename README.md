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