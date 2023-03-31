import React from "react";
import { Button, Col, Row, Typography, Card } from "antd";

const { Title, Paragraph } = Typography;

interface UserData {
    username: string;
    password: string;
    email: string;
}

const Profile: React.FC = () => {



    return (
        <Row justify="center" align="middle" style={{ height: "100vh" }}>
            <Col span={20} style={{
                padding: "20px",
                borderRadius: "20px",
                backgroundColor: "#001529"
            }}>
                <Row>
                    <Col>
                        <Title level={1} style={{ color: "white" }}>{"Profile:"}</Title>
                        <Title level={4} style={{ color: "white" }}>{"Username:"}</Title>
                        <Paragraph strong style={{ color: "white", fontSize: "20px" }}>
                            {"<name>"}
                        </Paragraph>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Title level={4} style={{ color: "white" }}>{"Email:"}</Title>
                        <Paragraph strong style={{ color: "white", fontSize: "20px" }}>
                            {"<email>"}
                        </Paragraph>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Title level={2} style={{ color: "white" }}>{"Change Email:"}</Title>
                        
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Title level={2} style={{ color: "white" }}>{"Change Password:"}</Title>
                    </Col>
                </Row>
            </Col>
        </Row>
    );
}

export default Profile;