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
                <Title level={2} style={{ color: "white", marginBottom: '30px' }}>Profile</Title>
                <Row gutter={[16, 16]}>
                </Row>
            </Col>
        </Row>
    );
}

export default Profile;