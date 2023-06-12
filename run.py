def main():
    import os
    import sys
    dir_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(dir_path, 'mystoreapp', 'py_files'))
    from mystoreapp.py_files import app
    app.run_app()


if __name__ == "__main__":
    main()