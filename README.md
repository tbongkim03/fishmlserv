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
```bash
$ sudo docker build -t fishmlserv:0.6.0 .
$ sudo docker run -d --name fmlserv-040 -p 8877:8765 fishmlserv:0.6.0
```

### Fly.io
```bash
$ fly launch --no-deploy
$ flyctl launch --name puangfish
$ flyctl scale memory 256
$ flyctl deploy
```


### Ref
https://curlconverter.com/python
