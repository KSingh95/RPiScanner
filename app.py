from blogsite import app
import subprocess

command = 'sudo apt-get install python-flask'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
