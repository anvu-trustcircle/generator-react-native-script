from library.call import call, call_cd
from library.question import yes_question
from config import config
from resource.gen_file import gen_main_application, gen_strings_xml, gen_info_plist, gen_gradle_properties, gen_app_build_gradle

def integrate_code_push():
  install_cli()
  setup_project()
  signed_android_apk()

def install_cli():
  install_cli_package()
  register_cli_acount()
  register_cli_app()

def setup_project():
  get_cli_staging_key()
  install_react_native_code_push()
  fix_code_push_issue()

def signed_android_apk():
  call(['keytool', '-genkey', '-v', '-keystore', 'my-release-key.keystore', '-alias', 'my-key-alias', '-keyalg', 'RSA', '-keysize', '2048', '-validity', '10000'])
  call(['mv', 'my-release-key.keystore', '{0}/android/app'.format(config.PROJECT_NAME)])
  
  print '\n\n\n'
  STORE_RELEASE_PASSWORD = raw_input('re-enter your keystore password (for auto config project): ')
  KEY_RELEASE_PASSWORD = raw_input('re-enter your key password (for auto config project): ')
  
  gen_gradle_properties(STORE_RELEASE_PASSWORD, KEY_RELEASE_PASSWORD)
  call(['cp', 'resource/gradle.properties', '{0}/android/gradle.properties'.format(config.PROJECT_NAME)])
  
  gen_app_build_gradle()
  call(['cp', 'resource/app/build.gradle', '{0}/android/app/build.gradle'.format(config.PROJECT_NAME)])
  
  print '\n\n'
  print '*note: if you want to test code push, please config your app to build release, or you can find it by this link: https://github.com/trustcircleglobal/documents/tree/master/technical/client/code-push#build-your-release-app*'

def install_cli_package():
  print '\n\n\n'
  enable_install_cli = yes_question('do you want to install code-push-cli? enter to skip if you have installed it.')
  if enable_install_cli:
    call(['yarn', 'global', 'add', 'code-push-cli'])

def register_cli_acount():
  call(['code-push', 'log-out'])
  call(['code-push', 'register'])

def register_cli_app():
  ios_name = config.CODE_PUSH_IOS_APP_NAME
  if ios_name == '':
    ios_name = config.PROJECT_NAME + '_IOS'
  
  print '\n\n\n'
  input = raw_input('enter your CODE_PUSH_IOS_APP_NAME. enter to skip and use default ({0}): '.format(ios_name))
  if input != '':
    ios_name = input
  
  config.set_code_push_ios_name(ios_name)
  
  android_name = config.CODE_PUSH_ANDROID_APP_NAME
  if android_name == '':
    android_name = config.PROJECT_NAME + '_ANDROID'
  
  input = raw_input('enter your CODE_PUSH_ANDROID_APP_NAME. enter to skip and use default ({0}): '.format(android_name))
  if input != '':
    android_name = input
  
  config.set_code_push_android_name(android_name)
  
  call(['code-push', 'app', 'add', config.CODE_PUSH_IOS_APP_NAME, 'ios', 'react-native'])
  call(['code-push', 'app', 'add', config.CODE_PUSH_ANDROID_APP_NAME, 'android', 'react-native'])

def get_cli_staging_key():
  global CODE_PUSH_IOS_STAGING
  global CODE_PUSH_ANDROID_STAGING
  
  call(['code-push', 'deployment', 'ls', config.CODE_PUSH_IOS_APP_NAME, '-k'])
  call(['code-push', 'deployment', 'ls', config.CODE_PUSH_ANDROID_APP_NAME, '-k'])
  
  print '\n\n\n'
  CODE_PUSH_IOS_STAGING = raw_input('enter ios staging key you get above: ')
  CODE_PUSH_ANDROID_STAGING = raw_input('enter android staging key you get above: ')

def install_react_native_code_push():
  call_cd(config.PROJECT_NAME)
  call(['npm', 'install'])
  call(['npm', 'install', '--save', 'react-native-code-push@latest'])
  call(['react-native', 'link', 'react-native-code-push'])
  call_cd('..')

def fix_code_push_issue():
  global CODE_PUSH_IOS_STAGING
  global CODE_PUSH_ANDROID_STAGING
  
  gen_main_application()
  call(['cp', 'resource/MainApplication.java', '{0}/android/app/src/main/java/com/{1}/MainApplication.java'.format(config.PROJECT_NAME, config.PROJECT_NAME)])
  
  gen_strings_xml(CODE_PUSH_ANDROID_STAGING)
  call(['cp', 'resource/strings.xml', '{0}/android/app/src/main/res/values/strings.xml'.format(config.PROJECT_NAME)])
  
  gen_info_plist(CODE_PUSH_IOS_STAGING)
  call(['cp', 'resource/Info.plist', '{0}/ios/{1}/Info.plist'.format(config.PROJECT_NAME, config.PROJECT_NAME)])
  
  call(['cp', 'resource/index.js', config.PROJECT_NAME])
