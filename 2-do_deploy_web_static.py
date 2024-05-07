#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""
from fabric.api import put, run, env
from os import path


env.user = "ubuntu"
env.my_ssh_private_key = "/root/.ssh/id_rsa"
env.hosts = ["100.25.41.212", "100.25.103.239"]


def do_deploy(archive_path):
    """distributes an archive to my web servers"""
    if not (path.exists(archive_path)):
        return false
    n_folder = archive_path.split("/")[-1].split(".")[0]
    for host in env.hosts:
        put(archive_path, '/tmp/')
        run(f"sudo mkdir -p /data/web_static/releases/{n_folder}")
        run(f"sudo tar -xzf /tmp/{n_folder}.tgz -C \
            /data/web_static/releases/web_static_{n_folder}/")
        run(f"sudo rm /tmp/web_static_{n_folder}.tgz")
        run(f"sudo mv /data/web_static/releases/ \
            {n_folder}/web_static/* /data/web_static/releases/{n_folder}/")
        run(f"sudo rm -rf /data/web_static/releases/ {n_folder}/web_static")
        run("sudo rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{n_folder}/ \
            /data/web_static/current")
        print("New version deployed!")
