### Delta Lake delta-rs Python bindings


## Build the image
```
docker build \
  --build-arg AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  --build-arg AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
  --platform linux/amd64 \
  -t pythonRustDelta .
```

Tag and push the lambda
```
docker build -t pythonrustdelta .
docker tag pythonrustdelta:latest 992921014520.dkr.ecr.us-east-1.amazonaws.com/pythonrustdelta:latest
docker push 992921014520.dkr.ecr.us-east-1.amazonaws.com/pythonrustdelta:latest
```