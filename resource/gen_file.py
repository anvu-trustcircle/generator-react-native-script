from config import config
import pdb

def gen_main_application():
  f = open('{0}/android/app/src/main/java/com/{1}/MainApplication.java'.format(config.PROJECT_NAME, config.PROJECT_NAME), 'r')
  contents = f.readlines()
  f.close()
  
  for index in range(len(contents)):
    if 'new CodePush' in contents[index]:
      contents[index] = '          new CodePush(getResources().getString(R.string.reactNativeCodePush_androidDeploymentKey), getApplicationContext(), BuildConfig.DEBUG),\n'
    if 'super.onCreate' in contents[index]:
      contents.insert(index + 1, '      Fabric.with(this, new Crashlytics());\n')
  
  f = open('resource/MainApplication.java', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_strings_xml(android_key):
  f = open('{0}/android/app/src/main/res/values/strings.xml'.format(config.PROJECT_NAME), 'r')
  contents = f.readlines()
  f.close()
  
  contents[1] = '    <string moduleConfig="true" name="reactNativeCodePush_androidDeploymentKey">{0}</string>\n'.format(android_key)
  
  f = open('resource/strings.xml', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_info_plist(ios_key):
  f = open('{0}/ios/{1}/Info.plist'.format(config.PROJECT_NAME, config.PROJECT_NAME), 'r')
  contents = f.readlines()
  f.close()
  
  for index in range(len(contents)):
    if 'NSExceptionAllowsInsecureHTTPLoads' in contents[index]:
      contents.insert(index + 2, '          <key>codepush.azurewebsites.net</key>\n')
      contents.insert(index + 3, '          <dict/>\n')
      contents.insert(index + 4, '          <key>codepush.blob.core.windows.net</key>\n')
      contents.insert(index + 5, '          <dict/>\n')
      contents.insert(index + 6, '          <key>codepushupdates.azureedge.net</key>\n')
      contents.insert(index + 7, '          <dict/>\n')
      contents[index + 12] = '    <string>{0}</string>\n'.format(ios_key)
  
  f = open('resource/Info.plist', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_gradle_properties(keystore, key):
  f = open('resource/gradle.properties.base', 'r')
  contents = f.readlines()
  f.close()
  
  num_of_line = len(contents)
  contents[num_of_line - 2] = contents[num_of_line - 2].replace('STORE_RELEASE_PASSWORD', keystore)
  contents[num_of_line - 1] = contents[num_of_line - 1].replace('KEY_RELEASE_PASSWORD', key)
  
  f = open('resource/gradle.properties', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_app_build_gradle():
  f = open('{0}/android/app/build.gradle'.format(config.PROJECT_NAME), 'r')
  contents = f.readlines()
  f.close()
  
  for index in range(len(contents)):
    if 'splits {' in contents[index]:
      contents.insert(index + 8, '    signingConfigs {\n')
      contents.insert(index + 9, '        release {\n')
      contents.insert(index + 10, '            if (project.hasProperty(\'MYAPP_RELEASE_STORE_FILE\')) {\n')
      contents.insert(index + 11, '                storeFile file(MYAPP_RELEASE_STORE_FILE)\n')
      contents.insert(index + 12, '                storePassword MYAPP_RELEASE_STORE_PASSWORD\n')
      contents.insert(index + 13, '                keyAlias MYAPP_RELEASE_KEY_ALIAS\n')
      contents.insert(index + 14, '                keyPassword MYAPP_RELEASE_KEY_PASSWORD\n')
      contents.insert(index + 15, '            }\n')
      contents.insert(index + 16, '        }\n')
      contents.insert(index + 17, '    }\n')
      contents.insert(index + 22, '            signingConfig signingConfigs.release\n')
    
    if 'dependencies {' in contents[index]:
      contents.insert(index + 1, '    compile(\'com.crashlytics.sdk.android:crashlytics:2.9.1@aar\') {\n')
      contents.insert(index + 2, '        transitive = true;\n')
      contents.insert(index + 3, '    }\n')
      contents.insert(index + 0, 'buildscript {\n')
      contents.insert(index + 1, '    repositories {\n')
      contents.insert(index + 2, '        maven { url \'https://maven.fabric.io/public\' }\n')
      contents.insert(index + 3, '    }\n')
      contents.insert(index + 4, '    dependencies {\n')
      contents.insert(index + 5, '        classpath \'io.fabric.tools:gradle:1.+\'\n')
      contents.insert(index + 6, '    }\n')
      contents.insert(index + 7, '}\n')
      contents.insert(index + 8, '\n')
      contents.insert(index + 9, 'apply plugin: \'io.fabric\'\n')
      contents.insert(index + 10, '\n')
      contents.insert(index + 11, 'repositories {\n')
      contents.insert(index + 12, '    maven { url \'https://maven.fabric.io/public\' }\n')
      contents.insert(index + 13, '}\n')
      contents.insert(index + 14, '\n')
      break
  
  f = open('resource/app/build.gradle', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_index_web_js():
  f = open('resource/index.web.js.base', 'r')
  contents = f.readlines()
  f.close()
  
  contents[4] = 'AppRegistry.registerComponent(\'{0}\', () => App);\n'.format(config.PROJECT_NAME)
  contents[5] = 'AppRegistry.runApplication(\'{0}\', '.format(config.PROJECT_NAME) + '{\n'
  
  f = open('resource/index.web.js', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_package_json():
  f = open('{0}/package.json'.format(config.PROJECT_NAME), 'r')
  contents = f.readlines()
  f.close()
  
  contents.insert(6, '    "ios": "react-native run-ios",\n')
  contents.insert(7, '    "android": "react-native run-android",\n')
  contents.insert(8, '    "web": "webpack-dev-server --config web/webpack.config.js --hot",\n')
  contents.insert(9, '    "build-web": "yarn build && yarn deploy",\n')
  contents.insert(10, '    "build": "webpack -p --config web/webpack.prod.config.js",\n')
  contents.insert(11, '    "build-ios": "cd ios && pod install && fastlane beta_c && cd ..",\n')
  contents.insert(12, '    "build-android": "yarn copyAndroidBundle && cd android && fastlane beta_c && cd ..",\n')
  contents.insert(13, '    "deploy": "firebase deploy",\n')
  contents.insert(14, '    "bundleInsideAndroid": "cd .. && yarn copyAndroidBundle && cd android",\n')
  contents.insert(15, '    "copyAndroidBundle": "react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res",\n')
  contents.insert(16, '    "web:serve": "http-serve -p 3001 --gzip true ./web/dist",\n')
  contents.insert(17, '    "build-web-local": "yarn build && yarn web:serve",\n')
  
  f = open('resource/package.json', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_firebaserc(project_id):
  f = open('resource/.firebaserc.base', 'r')
  contents = f.readlines()
  f.close()
  
  contents[2] = '    "default": "{0}"'.format(project_id)
  
  f = open('resource/.firebaserc', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_ios_appfile(bundle_id, apple_id, team_id):
  f = open('resource/ios/fastlane/Appfile.base', 'r')
  contents = f.readlines()
  f.close()
  
  contents[0] = 'app_identifier "{0}"\n'.format(bundle_id)
  contents[1] = 'apple_id "{0}"\n'.format(apple_id)
  if (team_id != ''): contents[2] = 'team_id "{0}"\n'.format(team_id)
  
  f = open('resource/ios/fastlane/Appfile', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_podfile():
  f = open('resource/ios/Podfile.base', 'r')
  contents = f.readlines()
  f.close()
  
  contents[0] = 'target \'{0}\' do\n'.format(config.PROJECT_NAME)
  
  f = open('resource/ios/Podfile', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_crashlytic_info_plist(api_token):
  f = open('{0}/ios/{1}/Info.plist'.format(config.PROJECT_NAME, config.PROJECT_NAME), 'r')
  contents = f.readlines()
  f.close()
  
  index = len(contents) - 3
  contents.insert(index + 0, '    <key>ITSAppUsesNoneExemptEncryption</key>\n')
  contents.insert(index + 1, '    <false/>\n')
  contents.insert(index + 2, '    <key>Fabric</key>\n')
  contents.insert(index + 3, '    <dict>\n')
  contents.insert(index + 4, '      <key>APIKey</key>\n')
  contents.insert(index + 5, '      <string>{0}</string>\n'.format(api_token))
  contents.insert(index + 6, '      <key>Kits</key>\n')
  contents.insert(index + 7, '      <array>\n')
  contents.insert(index + 8, '        <dict>\n')
  contents.insert(index + 9, '          <key>KitInfo</key>\n')
  contents.insert(index + 10, '          <dict/>\n')
  contents.insert(index + 11, '          <key>KitName</key>\n')
  contents.insert(index + 12, '          <string>Crashlytics</string>\n')
  contents.insert(index + 13, '        </dict>\n')
  contents.insert(index + 14, '      </array>\n')
  contents.insert(index + 15, '    </dict>\n')
  
  f = open('resource/Info.plist', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_app_delegate():
  f = open('{0}/ios/{1}/AppDelegate.m'.format(config.PROJECT_NAME, config.PROJECT_NAME), 'r')
  contents = f.readlines()
  f.close()
  
  for index in range(len(contents)):
    if 'didFinishLaunchingWithOptions' in contents[index]:
      contents.insert(index + 2, '  [Fabric with:@[Crashlytics.self]];\n')
  
  f = open('resource/ios/AppDelegate.m', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_ios_fastfile():
  f = open('resource/ios/fastlane/Fastfile.base', 'r')
  contents = f.readlines()
  f.close()
  
  for index in range(len(contents)):
    if 'match(type' in contents[index]:
      contents[index] = '    match(type: "{0}")\n'.format(config.IOS_PROVISION_TYPE)
    if 'scheme' in contents[index]:
      contents[index] = '      scheme: "{0}",\n'.format(config.PROJECT_NAME)
    if 'export_method' in contents[index]:
      contents[index] = '      export_method: "{0}",\n'.format(config.IOS_PROVISION_TYPE)
    if 'api_token' in contents[index]:
      contents[index] = '      api_token: "{0}",\n'.format(config.CRASHLYTIC_ORGANIZATION_API_TOKEN)
    if 'build_secret' in contents[index]:
      contents[index] = '      build_secret: "{0}",\n'.format(config.CRASHLYTIC_ORGANIZATION_BUILD_SECRECT)
    if 'groups' in contents[index]:
      contents[index] = '      groups: "{0}",\n'.format(config.CRASHLYTIC_TESTER_GROUP)
  
  f = open('resource/ios/fastlane/Fastfile', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_android_appfile(json_path, package_name):
  f = open('resource/android/fastlane/Appfile.base', 'r')
  contents = f.readlines()
  f.close()
  
  contents[1] = 'package_name "{0}"\n'.format(package_name)
  if (json_path != ''): contents[0] = 'json_key_file "{0}"\n'.format(json_path)
  
  f = open('resource/android/fastlane/Appfile', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_android_manifest():
  f = open('{0}/android/app/src/main/AndroidManifest.xml'.format(config.PROJECT_NAME), 'r')
  contents = f.readlines()
  f.close()
  
  for index in range(len(contents)):
    if '</application>' in contents[index]:
      contents.insert(index + 0, '      <meta-data\n')
      contents.insert(index + 1, '        android:name="io.fabric.ApiKey"\n')
      contents.insert(index + 2, '        android:value="{0}"\n'.format(config.CRASHLYTIC_ORGANIZATION_API_TOKEN))
      contents.insert(index + 3, '      />\n')
      break
  
  f = open('resource/android/AndroidManifest.xml', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()

def gen_android_fastfile():
  f = open('resource/android/fastlane/Fastfile.base', 'r')
  contents = f.readlines()
  f.close()
  
  for index in range(len(contents)):
    if 'api_token' in contents[index]:
      contents[index] = '      api_token: "{0}",\n'.format(config.CRASHLYTIC_ORGANIZATION_API_TOKEN)
    if 'build_secret' in contents[index]:
      contents[index] = '      build_secret: "{0}",\n'.format(config.CRASHLYTIC_ORGANIZATION_BUILD_SECRECT)
    if 'groups' in contents[index]:
      contents[index] = '      groups: "{0}",\n'.format(config.CRASHLYTIC_TESTER_GROUP)
  
  f = open('resource/android/fastlane/Fastfile', 'w')
  contents = "".join(contents)
  f.write(contents)
  f.close()
