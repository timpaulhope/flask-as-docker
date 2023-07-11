# How To - Create a basic flask app as a Docker container

This repo provides a simple example of how to get a flask app up and running as a docker container on a Linux machine.

## The Files

| File             | Role                                                                                      |
| :--------------- | :---------------------------------------------------------------------------------------- |
| app.py           | A simple flask app that returns the current datetime on the machine                        |
| config.yaml      | A config file that sets variables used in `app.py`                                             |
| Dockerfile       | The instruction file that will build the Docker image                                     |
| requirements.txt | A file used by the `Dockerfile` to install libraries used by `app.py` in the Docker image |

## Build

>**Note: Before proceeding with these steps:** 
>+ Make sure you have Docker installed on your host machine.
>+ Things will go smoother if you have familiarized yourself with the content of the four files listed above.
>+ Do your homework on how to start, stop, and remove docker containers as you'll be on your own for that part.
>+ It is highly recommended installing [Portainer](https://www.portainer.io/) on the host machine to help simplify keeping your docker environment clean.

To build and run `app.py` in Docker, you can follow these steps:

1. Download all the files in this repo to a project directory on the host machine you want to run the container on.

2. In the terminal of the host machine, navigate to the project directory where the `Dockerfile` is located.

3. Build the Docker image by running the following command:

```bash
sudo docker build -t my-flask-app .
```

>This command builds the Docker image using the instruction from `Dockerfile` in the current directory (`.`) and assigns it the tag `my-flask-app`. You can choose a different tag name if you prefer.

4. Once the image is built (may take some time), you can generate a Docker container from the terminal using the following command:

```bash
sudo docker run -d -p 5000:5000 --name my_flask_app my-flask-app
```

>This command starts a Docker container from the `my-flask-app` image with the name `my_flask_app` and maps port 5000 of the container to port 5000 of the host machine (Adjust the port mapping as needed).

5. With the Flask app running in Docker, You can access it by visiting `http://localhost:5000` in your web browser.

6. To stop the container from the terminal, use the following command

```bash
sudo docker stop my_flask_app
```
7. And to start the container up again from the terminal, use the following command

```bash
sudo docker start my_flask_app
```

## Customisation

You can customize this process by swapping out the `app.py` script for an alternate Flask app with the same name.  
If you do, remember that you will need to update the `config.yaml` and `requirements.txt` files to reflect the libraries required by the alternate script.