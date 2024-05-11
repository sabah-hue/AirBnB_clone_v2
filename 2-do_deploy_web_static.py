#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""
from fabric.connection import Connection
from fabric.api import put, run, env
from os import path

env.user = "ubuntu"
env.my_ssh_private_key = "/root/.ssh/id_rsa"
env.hosts = ["100.25.41.212", "100.25.103.239"]


def do_deploy(archive_path):
    """distributes an archive to my web servers"""
    if not path.exists(archive_path):
        return False
    n_folder = archive_path.split("/")[-1].split(".")[0]
    release = "/data/web_static/releases"
    for host in env.hosts:
        with Connection(host=host,
                        user=env.user,
                        connect_kwargs={
                            "key_filename": env.my_ssh_private_key,
                        },
                        ) as c:
            c.put(archive_path, '/tmp/')
            c.run(f"sudo mkdir -p {release}/{n_folder}")
            c.run(f"sudo tar -xzf /tmp/{n_folder}.tgz -C \
                  {release}/web_static_{n_folder}/")
            c.run(f"sudo rm /tmp/web_static_{n_folder}.tgz")
            c.run(f"sudo mv {release}/{n_folder}/web_static/* \
                  {release}/{n_folder}/")
            c.run(f"sudo rm -rf {release}/{n_folder}/web_static")
            c.run("sudo rm -rf /data/web_static/current")
            c.run(f"ln -s {release}/{n_folder}/ /data/web_static/current")
            print("New version deployed!")
