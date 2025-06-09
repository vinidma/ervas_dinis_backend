from app import create_app

app = create_app()

if __name__ == '__main__':
    # O modo debug reinicia o servidor automaticamente a cada alteração no código.
    app.run(debug=True)
