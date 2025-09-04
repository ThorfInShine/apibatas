import multiprocessing
import os

# Server socket
bind = "127.0.0.1:8000"
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
timeout = 120
keepalive = 2

# Logging
accesslog = '/var/log/apibatas/access.log'
errorlog = '/var/log/apibatas/error.log'
loglevel = 'info'

# Process naming
proc_name = 'apibatas'

# Server mechanics
daemon = False
# PERBAIKAN: Pindahkan pid file ke tempat yang bisa diakses
pidfile = '/var/www/apibatas.bpskotabatu.com/apibatas.pid'
# Atau gunakan None jika tidak perlu pid file
# pidfile = None

user = 'apibatas'
group = 'www-data'