import json

import requests

try:
    from .salt_config import config
except ImportError:
    print('No config file')
    exit()

"""
    Script to test salt master via salt-api. 
    Requires config file in same dir(config.py) in case of security
    I`m using external pillar for configuring minions dynamically.
    Pillar can be changed due to tasks
"""

pillar = {"dbhost": "localhost", "dbport": "5432",
          "app_fqdn": "app.{}".format(config['base_url']),
          "admin_fqdn": "admin.{}".format(config['base_url']),
          "shell_fqdn": "shell.{}".format(config['base_url']),
          "static_fqdn": "static.{}".format(config['base_url']),
          "app_url": "http://app.{}/dev1/".format(config['base_url']),
          "admin_url": "http://admin.{}/".format(config['base_url']),
          "shell_url": "http://shell.{}/".format(config['base_url']),
          "static_url": "http://static.{}/".format(config['base_url']),
          "shell2_fqdn": "shell2.{}".format(config['base_url']),
          "static_root": "/data/server/static",
          "celery_settings": "appserver.settings",
          "celery_python_path": "/data/server/application",
          "celeryd_nodes": "sync billing default",
          "celeryd_opts": "--time-limit=300 --concurrency=2 -Ofair -Q:sync sync -Q:billing billing -Q default",
          "venv_root": "/data/server/venv",
          "app_root": "/data/server/webapp-django",
          "fs_root": "/data/server",
          "appname": "appserver",
          "fs_user": "www-data",
          "fs_group": "www-data",
          "dbengine": "django.db.backends.postgresql_psycopg2",
          "dbname": config['dbname'],
          "dbuser": config['dbuser'],
          "dbpass": config['dbpass'],
          "pg_version": "9.5",
          "django_settings": "appserver.settings",
          "common_app_root": "/data/server/application",
          "os_username": config['os_username'],
          "os_user_pass": config['os_user_pass'],
          "os_support_username": config['os_support_username'],
          "os_support_pass": config['os_support_pass'],
          "office_name": 'demo',
          "office_address": 'address',
          'domain_name': 'demo',
          "admin_login": config['admin_login'],
          "admin_password": config['admin_password'],
          "app_arch_url": config['app_arch_url'],
          "app_arch_md5": config['app_arch_md5'],
          "server_ip": config['server_ip'],
          'app_name': 'app_server',
          'portal_client_id': config['portal_client_id'],
          'portal_client_secret': ['portal_client_secret'],
          'admin_email': config['admin_email']}

if __name__ == '__main__':
    url = config['master_url']
    payload = [{
        'Accept': 'application/json',
        'username': config['username'],
        'password': config['password'],
        'eauth': 'pam',
        'client': 'local',
        'fun': 'state.apply',
        'tgt': config['tgt'],
        'kwarg': {
            'pillar': pillar
        }
    }]
    resp = requests.post(url, json.dumps(payload), headers={"Content-Type": "application/json"}, timeout=600)
    print(resp)
