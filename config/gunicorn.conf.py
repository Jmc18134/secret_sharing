def pre_fork(server, worker):
    open('/tmp/app-initialized', 'w').close()
