Base Server Setup

This part of the project sets up the basic FastAPI server and environment 
so we can add Postgres and Spark features.


How to Run:

venv\Scripts\activate
python main.py


Test the server:

curl http://localhost:8000/health


What’s Included:

FastAPI server (main.py)
Environment loader (config.py)
.env file with server settings


Project Structure:
mcp_server/
  tools/
  venv/
  .env
  config.py
  main.py
  requirements.txt