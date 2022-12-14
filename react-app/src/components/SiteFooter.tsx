import React from "react";
import {GithubOutlined} from "@ant-design/icons";
import {Layout, Tooltip} from "antd";

const {Footer} = Layout;

const SiteFooter: React.FC = () => {
    return (
        <Footer style={{
            textAlign: 'center',
            color: "hsla(0,0%,100%,.65)",
            backgroundColor: "#001529"
        }}>
            <a style={{color: "inherit", textDecoration: "none"}} href="https://github.com/dinobenj/GlacierProject">
                <Tooltip title="Github Repository">
                    © 2022 The Glacier Project <GithubOutlined/> An RCOS Project
                </Tooltip>
            </a>
        </Footer>
    );
}

export default SiteFooter;