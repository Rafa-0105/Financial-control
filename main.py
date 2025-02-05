from routes.app import app

port = 2025

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=port)