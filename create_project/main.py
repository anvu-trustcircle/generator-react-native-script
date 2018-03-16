from library.call import call, write_line
from library.question import yes_no_question as yes_no
from config import config
from config.config import PROJECT_NAME, REACT_NATIVE_VERSION, set_project_name
import getpass

def make_new_project():
  init_project()
  config_sdk_android()

def init_project():
  if PROJECT_NAME == '':
    name = raw_input('enter the project name (no space): ')
    set_project_name(name)
  else:
    name = PROJECT_NAME
  
  if REACT_NATIVE_VERSION == '':
    version = ''
  else:
    version = '--version={0}'.format(REACT_NATIVE_VERSION)
  
  call(['react-native', 'init', name, version])
  call(['cp', 'resource/.gitignore', config.PROJECT_NAME])
  
  print '\n\n\n'
  print 'now, open your project and replace all com.{0} by your android package-name'.format(config.PROJECT_NAME.lower())
  print 'open your xcode project and replace your bundle id'
  print 'enter to continue...'
  raw_input()

def config_sdk_android():
  local_file = '{0}/android/local.properties'.format(config.PROJECT_NAME)
  user = getpass.getuser()
  sdk_dir = '/Users/{0}/Library/Android/sdk'.format(user)
  
  print '\n\n\n'
  print 'enter your android sdk location or press enter for default: {0}\n'.format(sdk_dir)
  new_dir = raw_input()
  if new_dir != '':
    sdk_dir = new_dir
  
  call(['touch', local_file])
  write_line(local_file, 'sdk.dir = {0}'.format(sdk_dir))

