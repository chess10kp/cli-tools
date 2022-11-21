import click
import subprocess
#user = input("Enter github username: ")
user = "chess10kp"
#key = input ("Enter github PAT")
key = ""
push_type_options = ["ssh","https"]
push_type = 0
Access = 'false'
name = input("Enter REPO_NAME")

startup = ["git init", "touch .gitignore README.md LICENSE.txt", "git add .", "git commit -m 'feat: Initial commit'",  "git branch -m master main",]
connect = f'''curl -u "{user}" https://api.github.com/user/repos -d ' ''' + "{" + f''' "name":"{name}", "private":true''' + "}'"

if push_type:
    push_type = push_type_options[push_type]
    clone_url = f'''https://github.com/{user}/{name}.git'''
else:
    push_type = push_type_options[push_type]
    clone_url = f'''git@github.com:{user}/{name}.git'''

local_to_remote = [f"git remote add origin {clone_url}"]
x
push = "git push -u origin main"

@click.command
def initrepo():
    subprocess.run("rm *", shell=True)
    for i in startup:
        print(i)
        subprocess.run(i, shell=True)

    subprocess.run(connect, shell=True)
    interrupt = input("Continue?")
    print("clone_url:", clone_url!

    subprocess.run(local_to_remote, shell=True)
    subprocess.run(push, shell=True)

print("Done")
