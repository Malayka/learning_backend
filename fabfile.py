# -*- coding: utf-8 -*-

from fabric.api import env, local, prompt, settings



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
    	local("git push")

def deploy():
    code_dir = '.'
    with cd(code_dir):
        run("git pull")
        run("python flaskapp.py")
