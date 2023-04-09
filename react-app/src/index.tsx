import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import Home from './components/Home';
import Map from "./components/Map";
import About from "./components/About";
import Dashboard from "./components/Dashboard";
import SiteHeader from './components/SiteHeader';
import SiteFooter from './components/SiteFooter';
import 'antd/dist/antd.min.css';
import {Layout} from 'antd';

const {Content} = Layout;

const router = createBrowserRouter([
    {
        path: "/",
        element: <Home/>
    },
    {
        path: "/map",
        element: <Map/>
    },
    {
        path: "/about",
        element: <About/>
    },
    {
        path: "/dashboard",
        element: <Dashboard/>
    },
]);

const root = ReactDOM.createRoot(
    document.getElementById('root') as HTMLElement
  );
  
  // Register a service worker for offline support
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/service-worker.js')
        .then(registration => {
          console.log('Service worker registered:', registration);
        })
        .catch(error => {
          console.error('Service worker registration failed:', error);
        });
    });
  }
  
  root.render(
    <React.StrictMode>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </React.StrictMode>
  );
  
  reportWebVitals();
  In this example, a service worker is registered to enable offline support for the application. The if statement checks if the serviceWorker API is available in the browser, and if it is, registers the service worker when the page loads. The console.log and console.error statements are used to print messages to the console to indicate whether the service worker registration was successful or not.
  
  
  
  
  
  