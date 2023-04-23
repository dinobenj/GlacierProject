import React from "react";
import {Layout, Menu} from "antd";

const {Header} = Layout;

const SiteHeader: React.FC = () => {
    return (
        <Header>
            <Menu theme="dark" mode="horizontal" style={{textTransform: "uppercase"}}>
                <Menu.Item key="home">
                    <a href="/">Home</a>
                </Menu.Item>
                <Menu.Item key="map">
                    <a href="/map">Map</a>
                </Menu.Item>
                <Menu.Item key="dashboard">
                    <a href="/dashboard">Dashboard</a>
                </Menu.Item>
                <Menu.Item key="about">
                    <a href="/about">About</a>
                </Menu.Item>
                <Menu.Item key="login" style={{marginLeft: 'auto', marginRight: '0px'}}>
                    <a href="/login">Login</a>
                </Menu.Item>
                <Menu.Item key="profile" style={{marginLeft: '0px'}}>
                    <a href="/profile">Profile</a>
                </Menu.Item>
            </Menu>
        </Header>
    );
}

export default SiteHeader;