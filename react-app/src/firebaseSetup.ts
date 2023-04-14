// Import the functions you need from the SDKs you need
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDGkCPKcMClid5sqg1aHSepW-PUcU5gqDU",
  authDomain: "glaicer-project-auth.firebaseapp.com",
  projectId: "glaicer-project-auth",
  storageBucket: "glaicer-project-auth.appspot.com",
  messagingSenderId: "891754961384",
  appId: "1:891754961384:web:04b8d088de9aeaf394ac5d"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

export const auth = firebase.auth();