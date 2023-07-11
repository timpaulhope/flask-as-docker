To build this Flask app in Docker, you can follow these steps:

1. Open `Dockerfile` from the project directory and familiarize yourself with the steps.

2. Open `requirements.txt` 

3. Build the Docker image. Open a terminal or command prompt, navigate to the project directory (where the `Dockerfile` is located), and run the following command to build the Docker image:

```
docker build -t my-flask-app .
```

This command builds the Docker image using the Dockerfile in the current directory (`.`) and assigns it the tag `my-flask-app` (you can choose a different tag name if you prefer).

4. Run the Docker container. After the image is built, you can run a container from it using the following command:

```
docker run -p 5000:5000 my-flask-app
```

This command starts a Docker container from the `my-flask-app` image and maps port 5000 of the container to port 5000 of the host machine. Adjust the port mapping as needed.

The Flask app should now be running in a Docker container. You can access it by visiting `http://localhost:5000` in your web browser.

Note: Make sure you have Docker installed and running on your machine before proceeding with these steps.