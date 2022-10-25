import React from "react";
import {Layout, Menu} from "antd";

const {Header} = Layout;

const SiteHeader: React.FC = () => {
    return (
        <Header>
            <Menu theme="dark" mode="horizontal">
                <Menu.Item key="home">
                    <a href="/">Home</a>
                </Menu.Item>
                <Menu.Item key="map">
                    <a href="/map">Map</a>
                </Menu.Item>
            </Menu>
        </Header>
    );
}

export default SiteHeader;