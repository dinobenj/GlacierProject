import { Col, Row, Typography} from "antd";
import React from "react";
import Citations from "./Citations";

const {Title, Paragraph} = Typography;

const CitationsPage: React.FC = () => {

    const citationsTitle = "Citations:";

    return (
        <Row justify="center" align="middle" style={{height: "100vh"}}>

        <Col span={15} style={{
            padding: "20px",
            borderRadius: "20px",
            backgroundColor: "rgba(128, 128, 128, 0.6)"
        }}>
            <Row justify="space-around" align="middle">
                <Col>
                    <Title style={{color: "white"}}>{citationsTitle}</Title>
                    <Citations/>
                </Col>
            </Row>
        </Col>
    </Row>
        
    );
}

export default CitationsPage;