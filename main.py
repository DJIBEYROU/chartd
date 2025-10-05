import sys
import os

# Add the server directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "server"))

from app import app

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
