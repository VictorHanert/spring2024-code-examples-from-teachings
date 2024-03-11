import subprocess
import os

directory_path = os.getcwd() + '/4.Subprocess'
os.chdir(directory_path)

if not os.path.exists(directory_path + '/spring2024'):
    subprocess.run(["git", "clone", "https://github.com/python-elective-kea/spring2024.git"])

subprocess.run(["open", directory_path + "/spring2024/build/html/index.html"])