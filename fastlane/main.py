from library.question import yes_question, yes_no_question
from library.call import call, call_cd
from config import config
from resource.gen_file import gen_ios_appfile, gen_podfile, gen_crashlytic_info_plist, gen_app_delegate, gen_ios_fastfile, gen_android_appfile, gen_android_manifest, gen_android_fastfile

def integrate_fastlane():
  install_fastlane()
  integrate_ios()
  integrate_android()

def install_fastlane():
  print '\n\n\n'
  enable_install_fastlane = yes_question('do you want to install fastlane-tools from gem? enter to skip if you have installed it.')
  if enable_install_fastlane:
    call(['gem', 'install', 'fastlane', '-NV'])

def integrate_ios():
  init_fastlane_ios()
  integrate_code_signing()
  integrate_ios_beta_crashlytic()
  config_ios_fastfile()

def integrate_android():
  init_fastlane_android()
  integrate_android_beta_crashlytic()
  config_android_fastfile()

def init_fastlane_ios():
  call_cd('{0}/ios'.format(config.PROJECT_NAME))
  call(['fastlane', 'init'])
  call(['touch', 'Gemfile.lock'])
  call_cd('../..')
  
  if config.IOS_BUNDLE_ID == '':
    bundle_id = raw_input('enter your IOS_BUNDLE_ID (com.trustcircle.example): ')
    config.set_ios_bundle_id(bundle_id)
  else:
    bundle_id = config.IOS_BUNDLE_ID
  
  if config.IOS_APPLE_ID == '':
    apple_id = raw_input('enter your IOS_APPLE_ID (example@trustcircle.com): ')
    config.set_ios_apple_id(apple_id)
  else:
    apple_id = config.IOS_APPLE_ID
  
  if config.IOS_TEAM_ID == '':
    team_id = raw_input('enter your IOS_TEAM_ID if have (example: L34ETLS***). if no press enter to skip: ')
    config.set_ios_team_id(team_id)
  else:
    team_id = config.IOS_TEAM_ID
  
  gen_ios_appfile(bundle_id, apple_id, team_id)
  call(['cp', 'resource/ios/fastlane/Appfile', '{0}/ios/fastlane/Appfile'.format(config.PROJECT_NAME)])
  call(['cp', 'resource/ios/Gemfile', '{0}/ios/Gemfile'.format(config.PROJECT_NAME)])

def integrate_code_signing():
  print '\n\n\n'
  print 'note: make sure you have full access right to create and manage new certificate and provision for your team. if no, please ask team leader for getting the github repository.'
  print 'note: you can find more about code signing at https://codesigning.guide/'
  print 'open github and create new repository (for your certificate and provision), if you have skip this step. press enter to continue...'
  raw_input()
  # has_provision = yes_no_question('did your team have any certificate and provision for code signing?')
  
  if config.IOS_PROVISION_TYPE == '':
    provision_type = raw_input('enter your IOS_PROVISION_TYPE (development, adhoc, enterprise, appstore): ')
    config.set_ios_provision_type(provision_type)
  else:
    provision_type = config.IOS_PROVISION_TYPE
  
  call_cd('{0}/ios/fastlane'.format(config.PROJECT_NAME))
  call(['fastlane', 'match', 'init'])
  call(['fastlane', 'match', provision_type])
  call_cd('../../..')
  
  print '\n\n\n'
  print 'go to xcode and setup bundle id, Provisioning Profile in both Signing (Debug) and Signing (Release) corresponds the Provision you just create or load from fastlane match'
  print 'note: if you can find the provision in XCode, there are some failure with code signing, please visit this docs to check https://github.com/trustcircleglobal/documents/tree/master/technical/client/fastlane#code-signing'
  print 'enter to continue...'
  raw_input()

def integrate_ios_beta_crashlytic():
  print 'goto Beta Crashlytics Console https://fabric.io/home and get your organization api token and build secrect'
  
  if config.CRASHLYTIC_ORGANIZATION_API_TOKEN == '':
    api_token = raw_input('enter your CRASHLYTIC_ORGANIZATION_API_TOKEN: ')
    config.set_crashlytic_api_token(api_token)
  else:
    api_token = config.CRASHLYTIC_ORGANIZATION_API_TOKEN
  
  if config.CRASHLYTIC_ORGANIZATION_BUILD_SECRECT == '':
    build_secrect = raw_input('enter your CRASHLYTIC_ORGANIZATION_BUILD_SECRECT: ')
    config.set_crashlytic_build_secrect(build_secrect)
  else:
    build_secrect = config.CRASHLYTIC_ORGANIZATION_BUILD_SECRECT
  
  print 'go to Beta Crashlytics Console > see the left menu > select Manage Group (hidden until select Beta tab) > select New Group and create a group with some tester'
  if config.CRASHLYTIC_TESTER_GROUP == '':
    tester_group = raw_input('enter your CRASHLYTIC_TESTER_GROUP: ')
    config.set_crashlytic_tester_group(tester_group)
  else:
    tester_group = config.CRASHLYTIC_TESTER_GROUP
  
  call_cd('{0}/ios'.format(config.PROJECT_NAME))
  call(['pod', 'init'])
  call_cd('../..')
  
  gen_podfile()
  call(['cp', 'resource/ios/Podfile', '{0}/ios/Podfile'.format(config.PROJECT_NAME)])
  
  call_cd('{0}/ios'.format(config.PROJECT_NAME))
  call(['pod', 'install'])
  call_cd('../..')
  
  gen_crashlytic_info_plist(api_token)
  call(['cp', 'resource/Info.plist', '{0}/ios/{1}/Info.plist'.format(config.PROJECT_NAME, config.PROJECT_NAME)])
  
  print '\n\n\n'
  print 'open your xcode target, navigate to build phases and add a new run script'
  print '"${PODS_ROOT}' + '/Fabric/run" {0} {1}'.format(api_token, build_secrect)
  print 'press enter to continue..'
  raw_input()
  
  gen_app_delegate()
  call(['cp', 'resource/ios/AppDelegate.m', '{0}/ios/{1}/AppDelegate.m'.format(config.PROJECT_NAME, config.PROJECT_NAME)])

def config_ios_fastfile():
  gen_ios_fastfile()
  call(['cp', 'resource/ios/fastlane/Fastfile', '{0}/ios/fastlane/Fastfile'.format(config.PROJECT_NAME)])

def init_fastlane_android():
  call_cd('{0}/android'.format(config.PROJECT_NAME))
  call(['fastlane', 'init'])
  call(['touch', 'Gemfile.lock'])
  call_cd('../..')
  
  if config.ANDROID_PACKAGE_NAME == '':
    package_name = raw_input('enter your ANDROID_PACKAGE_NAME (com.trustcircle.example): ')
    config.set_android_package_name(package_name)
  else:
    package_name = config.ANDROID_PACKAGE_NAME
  
  if config.ANDROID_JSON_PATH == '':
    json_path = raw_input('enter your ANDROID_JSON_PATH, enter to skip: ')
    config.set_android_json_path(json_path)
  else:
    json_path = config.ANDROID_JSON_PATH
  
  gen_android_appfile(json_path, package_name)
  call(['cp', 'resource/android/fastlane/Appfile', '{0}/android/fastlane/Appfile'.format(config.PROJECT_NAME)])

def integrate_android_beta_crashlytic():
  gen_android_manifest()
  call(['cp', 'resource/android/AndroidManifest.xml', '{0}/android/app/src/main/AndroidManifest.xml'.format(config.PROJECT_NAME)])

def config_android_fastfile():
  gen_android_fastfile()
  call(['cp', 'resource/android/fastlane/Fastfile', '{0}/android/fastlane/Fastfile'.format(config.PROJECT_NAME)])
