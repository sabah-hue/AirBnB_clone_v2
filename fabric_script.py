from fabric import Connection

servers = ["100.25.41.212", "100.25.103.239"]
for server in servers:
    with Connection(host=server,
        user="ubuntu",
        connect_kwargs={
            "key_filename": "/root/.ssh/id_rsa",
        }) as c:
        c.local('mkdir -p versions')
        c.local('touch versions/simple_file')
        c.local('echo file to upload > versions/simple_file')
        c.put('versions/simple_file', remote='/home/ubuntu')
        c.run('sudo mkdir -p /data/web_static/releases/test/')
