#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""
from fabric.api import put, run, env
from os import path


env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"
env.hosts = ["100.25.41.212", "100.25.103.239"]


def do_deploy(archive_path):
    """distributes an archive to my web servers"""
    if not path.exists(archive_path):
        return False
    n_folder = archive_path.split("/")[-1].split(".")[0]
    release = "/data/web_static/releases"
    put(archive_path, '/tmp/')
    run(f"sudo mkdir -p {release}/{n_folder}/")
    run(f"sudo tar -xzf /tmp/{n_folder}.tgz -C {release}/{n_folder}/")
    run(f"sudo rm /tmp/{n_folder}.tgz")
    run(f"sudo mv {release}/{n_folder}/web_static/* {release}/{n_folder}/")
    run(f"sudo rm -rf {release}/{n_folder}/web_static")
    run("sudo rm -rf /data/web_static/current")
    run(f"sudo ln -s {release}/{n_folder}/ /data/web_static/current")
    run("sudo service nginx restart")
    print("New version deployed!")
