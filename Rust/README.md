# Setup environment

```sh
$ sudo docker pull rust:1.76.0-alpine
```

```sh
$ docker build -f Docker\Dockerfile.dev -t rust-dev .
```

```sh
$ sudo docker run -it --name rust-dev --mount type=bind,source=.,target=/app rust-dev
```
