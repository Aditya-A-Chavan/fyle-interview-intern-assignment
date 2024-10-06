# Docker Application README

This README provides instructions on how to build and run the application using Docker and Docker Compose.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Docker
- Docker Compose

## Building and Running the Application

### Using Docker Compose (Recommended)

1. Navigate to the root directory of the project where the `docker-compose.yml` file is located.

2. Build and start the container:
   ```
   docker-compose up --build
   ```

   This command will build the Docker image and start the container. The `--build` flag ensures that the image is rebuilt if there are any changes.

3. The application will be available at `http://0.0.0.0:7755`.

4. To run the container in detached mode (in the background):
   ```
   docker-compose up -d
   ```

5. To stop and remove the containers when running in detached mode:
   ```
   docker-compose down
   ```

### Using Docker Directly

If you prefer to use Docker commands directly:

1. Build the Docker image:
   ```
   docker build -t <your-app-name> .
   ```

2. Run the container:
   ```
   docker run -p 7755:7755 <your-app-name>
   ```


## Development

The Docker setup is configured for development:
- The application directory is mounted as a volume, allowing for live code changes without rebuilding the image.
- The Flask environment is set to development mode.

## Notes

- The application runs on port 7755. Ensure this port is free on your host machine.
- The `gunicorn_config.py` file is used to configure Gunicorn. Make sure this file is present in your project root.
- The application is served using Gunicorn with the entry point `core.server:app`. Ensure your Flask application is structured accordingly.

## Troubleshooting

If you encounter any issues:
1. Ensure all required files (`Dockerfile`, `docker-compose.yml`, `requirements.txt`, `gunicorn_config.py`) are present in the project root.
2. Check if the required ports 7755 is free on your host machine.
