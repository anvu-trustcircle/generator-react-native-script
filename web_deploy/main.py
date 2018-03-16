from library.call import call, call_cd
from library.question import yes_question
from config import config
from resource.gen_file import gen_index_web_js, gen_package_json, gen_firebaserc

def integrate_web_deploy():
  install_package()
  import_new_file()
  setup_deploy_firebase()

def install_package():
  call_cd(config.PROJECT_NAME)
  call(['yarn', 'add', 'react-dom', 'react-native-web'])
  call(['yarn', 'add', '--dev', 'babel-plugin-react-native-web'])
  call(['yarn', 'add', '--dev', 'babel-loader', 'url-loader', 'webpack', 'webpack-dev-server'])
  
  print '\n\n\n'
  enable_install_webpack_cli = yes_question('do you want to install webpack-cli? enter to skip if you have installed it.')
  if enable_install_webpack_cli:
    call(['npm', 'install', '-g', 'webpack-cli'])
  call_cd('..')

def import_new_file():
  call(['mkdir', '-p', '{0}/src'.format(config.PROJECT_NAME)])
  call(['mv', '{0}/App.js'.format(config.PROJECT_NAME), '{0}/src'.format(config.PROJECT_NAME)])
  
  gen_index_web_js()
  call(['cp', 'resource/index.web.js', config.PROJECT_NAME])
  call(['mkdir', '-p', '{0}/web'.format(config.PROJECT_NAME)])
  call(['mkdir', '-p', '{0}/web/dist'.format(config.PROJECT_NAME)])
  call(['cp', 'resource/web/dist/index.html', '{0}/web/dist/index.html'.format(config.PROJECT_NAME)])
  call(['cp', 'resource/webpack.config.js', '{0}/webpack.config.js'.format(config.PROJECT_NAME)])
  call(['cp', 'resource/webpack.config.js', '{0}/webpack.prod.config.js'.format(config.PROJECT_NAME)])
  
  gen_package_json()
  call(['cp', 'resource/package.json', '{0}/package.json'.format(config.PROJECT_NAME)])

def setup_deploy_firebase():
  print '\n\n\n'
  enable_install_firebase = yes_question('do you want to install firebase-tools? enter to skip if you have installed it.')
  if enable_install_firebase:
    call(['npm', 'install', '-g', 'firebase-tools'])
  
  call_cd(config.PROJECT_NAME)
  call(['firebase', 'login'])
  print '\n\n\n'
  print 'now, go to your Firebase console and create your own project. https://console.firebase.google.com/.\npress enter to continue..'
  raw_input()
  project_id = raw_input('enter your project id (find in your app setting.): ')
  call(['firebase', 'init'])
  call_cd('..')
  
  call(['cp', 'resource/firebase.json', config.PROJECT_NAME])
  gen_firebaserc(project_id)
  call(['cp', 'resource/.firebaserc', config.PROJECT_NAME])
