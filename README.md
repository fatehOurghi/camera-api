To build the docker image:

```shell
docker build -t camera-api .
```

You can run a container using the command:

```shell
docker run camera-api camera.py -u <ip_address>:<port> -v <path/to/video>
```

or by using your webcam:

```shell
docker run --device=/dev/video0:/dev/video0 camera-api camera.py -u <ip_address>:<port>

```