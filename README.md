# SCRIPT GENERATOR for new react native project.

## Why write this document ?

> It explains how to use script and how script work.

> If you do not need this document, you will not run and setup new react-native project with full function.

> If you have some problem, you can contact me at Slack: an.vu or an.vu@trustcircle.com

## Contents

1. Requirement

2. How to use

3. How it works

4. Test

## Requirement

Some tools for terminal: xcode-select, gem, brew, npm, yarn, pod, git, fastlane, code-push-cli, webpack-cli, firebase-tools...

## How to use

- clone or download this [project](https://github.com/anvu-trustcircle/generator-react-native-script).

- copy all file to a folder.

- update the config file in /config/config.py (if needed).

- run script python generator.py.

## How it works

1. Create new react-native project

  - make new project
  
  - config android sdk location

2. [Integrate code-push](../code-push)

  - install cli package (code-push-cli)
  
  - integrate code push to project
  
  - signed android apk

3. [Integrate web-deploy](../react-native-web)
  
  - install packages (webpack-cli)
  
  - import new files
  
  - setup deploy firebase (firebase-tools)

4. [Integrate fastlane](../fastlane)
  
  - install fastlane
  
  - integrate fastlane and beta crashlytic for ios
  
  - integrate fastlane and beta crashlytic for android

5. [Integrate circle ci](../circle-ci)
  
  - create config.yml file
  
  - integrate git

## Test

- run project: 

`$ yarn ios` 

`$ yarn android`

`$ yarn web`

- try to test code-push, circle ci, beta crashlytic

## Note

this document init in 2018, 19th Mar. using: 

macos: *v10.12.6*

react-native: *v0.53.3*

react: *v16.2.0*

ruby: *v2.5.0*

yarn: *v1.3.2*

npm: *v5.6.0*

## Troubleshooting

If you need support, chat on [Slack](https://trustcircle.slack.com/signup) at channel:

* **#tech_team**
* **#tech_qc**

or direct message to:

* **an.vu**
* **toan.do**
* **vu.nguyen**