#!/bin/bash

# Start the backend in the background
python Backend/app.py &

# Start the frontend HTTP server (fix directory name)
python -m http.server 8000 --directory FrontEnd &

# Keep the container running
wait
