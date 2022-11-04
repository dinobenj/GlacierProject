import {Col, Row} from "antd";
import React from "react";

const Map: React.FC = () => {
//    const url = "https://theglacierproject.shinyapps.io/GlacierProject/"; // Production use
    const PORT = 5671; // Dev use. Specific the PORT of a local Shiny App when developing
    const url = `http://localhost:${PORT}`;
    return (
        <Row justify="center" align="middle" style={{height: "100vh"}}>
            <Col span={24} style={{height: "100vh", width: "100vw"}}>
                <object data={url} type="text/html" id="appObject" aria-label="Glacier Map" style={{height: "100vh", width: "100vw"}}/>
            </Col>
        </Row>
    );
}

export default Map;