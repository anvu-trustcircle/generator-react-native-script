from config import config
from library.call import call

def integrate_circle_ci():
  call(['mkdir', '{0}/.circleci'.format(config.PROJECT_NAME)])
  call(['cp', 'resource/config.yml', '{0}/.circleci/config.yml'.format(config.PROJECT_NAME)])
