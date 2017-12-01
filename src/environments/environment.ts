// The file contents for the current environment will overwrite these during build.
// The build system defaults to the dev environment which uses `environment.ts`, but if you do
// `ng build --env=prod` then `environment.prod.ts` will be used instead.
// The list of which env maps to which file can be found in `.angular-cli.json`.

export const environment = {
  production: false,
  firebaseConfig : {
    apiKey: "AIzaSyAln8IPzovW8Z0O5HNhqeW7MQuLhY7llZY",
    authDomain: "online-store-gs.firebaseapp.com",
    databaseURL: "https://online-store-gs.firebaseio.com",
    projectId: "online-store-gs",
    storageBucket: "online-store-gs.appspot.com",
    messagingSenderId: "1021992878664"
  }
};
