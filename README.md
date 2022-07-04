# Instructions

Run
```bash
docker build  -t xarray-recreate-bug:latest -f ./Dockerfile.xarray .
docker-compose up -d
```
* Attach container to terminal
* Run `pytest`