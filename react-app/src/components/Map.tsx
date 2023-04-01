import React from "react";
import {Col, Row, Image} from "antd";

const Map: React.FC = () => {
    const url = "https://theglacierproject.shinyapps.io/Production/"; // Production use
    // const PORT = 5671; // Dev use. Specific the PORT of a local Shiny App when developing
    // const url = `http://localhost:${PORT}`;

    return (
        <Row justify="center" align="middle" style={{height: "100vh"}}>
            <Image
                preview={false}
                width={100}
                src="https://upload.wikimedia.org/wikipedia/commons/6/61/Compass_rose_transparent.png"
                style={{
                    display: "inline-flex"
                }}
            />
            <Col span={24}>
                <object data={url} type="text/html" id="appObject" aria-label="Glacier Map" style={{height: "100vh", width: "100vw"}}/>
            </Col>
        </Row>
    );
}

export default Map;