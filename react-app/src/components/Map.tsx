import { Col, Row } from "antd";

function Map() {
//    const url = "https://theglacierproject.shinyapps.io/GlacierProject/"; // Production use
    const PORT = 5671; // Dev use. Specific the PORT of a local Shiny App when developing
    const url = `http://localhost:${PORT}`;
    return (
        <Row justify="center" align="middle" style={{height: "100vh"}}>
            <Col span={24} style={{height: "100vh", width: "100vw"}}>

                <object data={url} type="text/html" id="appObject" style={{height: "100vh", width: "100vw"}}>
                    Alternate Content
                </object>
            </Col>
        </Row>
    );
}

export default Map;