# react-native init PROJECT_NAME --version=REACT_NATIVE_VERSION
PROJECT_NAME = ''
REACT_NATIVE_VERSION = ''

# code-push config
CODE_PUSH_IOS_APP_NAME = ''
CODE_PUSH_ANDROID_APP_NAME = ''

# ios
IOS_BUNDLE_ID = ''
IOS_APPLE_ID = ''
IOS_TEAM_ID = ''
IOS_PROVISION_TYPE = ''

# android
ANDROID_PACKAGE_NAME = ''
ANDROID_JSON_PATH = ''

#crashlytics
CRASHLYTIC_ORGANIZATION_API_TOKEN = ''
CRASHLYTIC_ORGANIZATION_BUILD_SECRECT = ''
CRASHLYTIC_TESTER_GROUP = ''

def set_project_name(name):
  global PROJECT_NAME
  PROJECT_NAME = name

def set_code_push_ios_name(name):
  global CODE_PUSH_IOS_APP_NAME
  CODE_PUSH_IOS_APP_NAME = name

def set_code_push_android_name(name):
  global CODE_PUSH_ANDROID_APP_NAME
  CODE_PUSH_ANDROID_APP_NAME = name

def set_ios_bundle_id(name):
  global IOS_BUNDLE_ID
  IOS_BUNDLE_ID = name

def set_ios_apple_id(name):
  global IOS_APPLE_ID
  IOS_APPLE_ID = name

def set_ios_team_id(name):
  global IOS_TEAM_ID
  IOS_TEAM_ID = name

def set_ios_provision_type(name):
  global IOS_PROVISION_TYPE
  IOS_PROVISION_TYPE = name

def set_crashlytic_api_token(name):
  global CRASHLYTIC_ORGANIZATION_API_TOKEN
  CRASHLYTIC_ORGANIZATION_API_TOKEN = name

def set_crashlytic_build_secrect(name):
  global CRASHLYTIC_ORGANIZATION_BUILD_SECRECT
  CRASHLYTIC_ORGANIZATION_BUILD_SECRECT = name

def set_crashlytic_tester_group(name):
  global CRASHLYTIC_TESTER_GROUP
  CRASHLYTIC_TESTER_GROUP = name

def set_android_package_name(name):
  global ANDROID_PACKAGE_NAME
  ANDROID_PACKAGE_NAME = name

def set_android_json_path(name):
  global ANDROID_JSON_PATH
  ANDROID_JSON_PATH = name
