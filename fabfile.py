# -*- coding: utf-8 -*-

from __future__ import with_statement
from fabric.api import env, local, settings, abort, run, cd, prompt
from fabric.contrib.console import confirm

env.hosts = ['mardanov@109.234.34.140',]


def commit_push():
    """
    Коммит изменений.
    """
    with settings(warn_only=True):
        local('git status')
        prompt('Press <Enter> to continue or <Ctrl+C> to cancel.')  # тут можно прервать коммит, 
            # если в него попали ненужные файлы или наоборот
        local('git add .')
        local('git commit')  # тут вылазит консольный редактор и можно ввести комментарий
    	local("git push origin --all")


def deploy():
    code_dir = '/home/mardanov/testing_visualization/fabric/learning_backend'
    with cd(code_dir):
        run("git pull origin develop")
        if run("uwsgi kutak_u.ini").failed:
        	pass
        run("sudo ln -s kutak_n.conf /etc/nginx/sites-enabled/")
        run("sudo nginx -s reload")
