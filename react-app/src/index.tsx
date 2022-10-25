import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import Home from './components/Home';
import Map from "./components/Map";
import SiteHeader from './components/SiteHeader';
import SiteFooter from './components/SiteFooter';
import backgroundImage from './assets/background.jpg'
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
    }
]);

const root = ReactDOM.createRoot(
    document.getElementById('root') as HTMLElement
);
root.render(
    <React.StrictMode>
        <Layout style={{height: "100vh"}}>
            <SiteHeader/>
            <Content style={{backgroundImage: `url${backgroundImage}`}}>
                <RouterProvider router={router}/>
            </Content>
            <SiteFooter/>
        </Layout>
    </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
