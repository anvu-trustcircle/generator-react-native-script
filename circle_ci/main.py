from config import config
from library.call import call, call_cd

def integrate_circle_ci():
  call(['mkdir', '{0}/.circleci'.format(config.PROJECT_NAME)])
  call(['cp', 'resource/config.yml', '{0}/.circleci/config.yml'.format(config.PROJECT_NAME)])
  
  print '\n\n\n'
  print 'now, go to Github and create your react-native project repository'
  print 'enter to continue..'
  raw_input()
  
  git_project = raw_input('enter your github link: ')
  
  call_cd(config.PROJECT_NAME)
  call(['git', 'init'])
  call(['git', 'add', '.'])
  call(['git', 'commit', '-m', '"create react-native by python script"'])
  call(['git', 'remote', 'add', 'origin', git_project])
  call(['git', 'push', '-u', 'origin', 'master'])
  call(['firebase', 'login:ci'])
  call_cd('..')
  
  print 'now, go to Circle CI Console https://circleci.com/dashboard > `ADD PROJECTS` in the left menu > `Set Up Project` in the right of your app name > macOS > Objective-C > Start building'
  print 'enter to continue...'
  raw_input()
  
  print 'in the left, find your project and click setting button > `Enviroment Variables` in the left > `Add Variable`'
  print 'add variable name `MATCH_PASSWORD` and value is your cerificate keychain password (if have)'
  print 'add variable name `FASTLANE_PASSWORD` and value is your apple id password'
  print 'add variable name `FIREBASE_DEPLOY_TOKEN` and value is your firebase token you get in last step'
  print 'enter to finish...'
  raw_input()
