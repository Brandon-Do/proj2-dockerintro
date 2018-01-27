from flask import Flask, render_template
import os

app = Flask(__name__)

def print_files():
    """
    Helper function to print current directories.
    """
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        print("Current Path:", dirpath)
        print("Directories:", dirnames)
        print("Files:", filenames)
        print()

def get_html():
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        print(dirpath)
        if not dirpath.endswith('error_files'):
            for filename in filenames:
                if filename.endswith('.html'):
                    if filename.startswith('..') or filename.startswith('~') or filename.startswith('//'):
                        return "error_files/403.html"
                    else:
                        return filename
    return "error_files/404.html"

@app.route("/")
@app.route('/templates')
def render_static():
    file = get_html()
    print(file)
    return render_template(file)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
