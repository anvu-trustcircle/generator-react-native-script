import { AppRegistry } from 'react-native'
import App from './src/App'
import codePush from "react-native-code-push";

let codePushOptions = { 
  checkFrequency: codePush.CheckFrequency.ON_APP_RESUME, 
  installMode: codePush.InstallMode.ON_NEXT_RESUME 
}

MyApp = codePush(App);

AppRegistry.registerComponent('AppGenerate', () => MyApp)