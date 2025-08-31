# This script is the entry point to run the Flask application.
from app import app

# Check if this script is being run directly
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)