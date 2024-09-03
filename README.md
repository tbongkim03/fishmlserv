# fishmlserv

## Deploy

## Run
- dev

- http://localhost:8000/docs

```bash
# uvicorn --help
$ uvicorn src.fishmlserv.main:app --reload
```

- prd
```bash
$ uvicorn src.finshmlserv.main:app --host 0.0.0.0 --port 8949
```

## Docker

Dockerfile pip install git+https://~~~~~~~~~@<BRANCH>

```bash
$ sudo docker build -t fishmlserv:0.7.1 .
$ sudo docker run -d --name fmlserv-071 -p 8877:8765 fishmlserv:0.7.1
f4356dc740c9603026d4a0f76835b79395b9a9bb347ac0ad8c12b96bd855e607

$ sudo docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED         STATUS         PORTS                                       NAMES
f4356dc740c9   fishmlserv:0.7.1   "uvicorn main:app --…"   4 seconds ago   Up 4 seconds   0.0.0.0:8877->8765/tcp, :::8877->8765/tcp   fmlserv-071

$ sudo docker exec -it fmlserv-071 bash
root@f4356dc740c9:/code# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"

root@f4356dc740c9:/code# exit
exit

$ sudo docker logs -f <CONTAINER ID>
```

### Fly.io
```bash
$ fly launch --no-deploy
$ flyctl launch --name puangfish
$ flyctl scale memory 256
$ flyctl deploy
```

### Docker

https://hub.docker.com/r/tbongkim03/fishmlserv

### Ref
https://curlconverter.com/python
