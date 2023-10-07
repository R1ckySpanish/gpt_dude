# Start app with Docker
## Prepare config '.env'
There is template for configuration file - __'.env.sample'__ \
Fill up __'.env'__ file and move them to __gpt_dude/__ directory

## Build docker image 
```
git clone https://github.com/R1ckySpanish/gpt_dude.git
cd gpt_dude/
docker build -t gpt_dude .
```

## Run docker container
```
docker run -d gpt_dude
```
