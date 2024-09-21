#!/usr/bin/env python3

import datetime
import os
import subprocess
import sys


def run_command(command):
    print(f"Executing command: {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing command: {command}")
        print(stdout.decode())
        print(stderr.decode())
        sys.exit(1)
    return stdout.decode()

def main():
    print("\033[0;32mDeploying updates to GitHub...\033[0m")

    # Build the project
#    run_command("hugo")

    # Go to Public folder
#    os.chdir("public")
#    print("current dir: ", os.getcwd())

    # Add changes to git
#    run_command("git add .")

    # Commit changes
#    msg = f"rebuilding site {datetime.datetime.now()}"
#    if len(sys.argv) > 1:
#        msg = " ".join(sys.argv[1:])
#    run_command(f'git commit -m "{msg}"')

    # Push source and build repos
#    run_command("git push origin master")

    # Go back to root directory
#    os.chdir("..")

    # Add content changes to git
    run_command("git add .")

    # Commit content changes
    msg = f"updating content {datetime.datetime.now()}"
    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
    run_command(f'git commit -m "{msg}"')

    # Push content
    run_command("git push origin master")

if __name__ == "__main__":
    main()

