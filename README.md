# aurora-metrics

## How to Run
```
docker run -d \
    --network=host \
    --name=aurora-metrics \
    -e FLASK_PORT=5000 \
    -e ENDPOINT=http:127.0.0.1:20080 \
    jionederfull/aurora-metrics:0.1
```

## Basic Test
```
curl localhost:5000/metrics
```
