# INTENSIFIER

This script is designed to enhance communication within team environments by adding a touch of humor and making Slack interactions more dynamic. With this tool, you can take advantage of Slack reactions in a fun and effective way, fostering a collaborative and lighthearted atmosphere at work.

![Base emoji](./images/emoji.png) 
![Intensified emoji](./images/emoji-intensifies.gif)

This is not only related to emojis. You can also use pictures.

## Repositories

This image is stored in both [docker](https://hub.docker.com/repository/docker/alvarvg/intensifier/tags) and [quay.io](https://quay.io/repository/alvarvg/intensifier) repositories, you can choose the one best fits for you. This image is also mutliarch and is being built for arm64 and amd64 architectures.

## Usage

In order to use this tool just run the following docker command. In this case 

```bash
docker run --rm -v $(pwd):/app intensifier:latest <your_image>
```

### Tip

If you use this command frequently, it is advisable to create an alias to facilitate its use.

```bash
alias intensify="docker run --rm -v $(pwd):/app intensifier:latest"
intensify <your_image>
```
