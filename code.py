from flask import Flask
import getpass
app = Flask(_name_)

@app.route('/htop')
def htop():
    import os
    from datetime import datetime
    import subprocess
    name = "M MOHAMMED SAIFULLAH"
    username = getpass.getuser()
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.getoutput("top -bn1 | head -n 10")
    return f"Name: {name}, Username: {username}, Server Time: {server_time}, Top Output: {top_output}"

if _name_ == "_main_":
    app.run(debug=True, host='0.0.0.0', port=5000)
