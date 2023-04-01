import React from "react";
import {Col, Row, Typography} from "antd";
import MemberIntroduction from "./ MemberIntroduction";

const {Title, Paragraph} = Typography;

const Dashboard: React.FC = () => {
    const projectIntroductinTitle = "Dashboard"
    const projectIntroductionText = "The Glacier Project is a web application that visualizes data, satellite images, and predictions of our planet's glaciers.";
    const teamIntroductionTitle = "Who we are?"
    const teamIntroductionText = "We are students at Rensselaer Polytechnic Institue (RPI) and members of Rensselaer Center for Open Source (RCOS).";

    return (
        <Row justify="center" align="middle" style={{height: "100vh"}}>
            <Col span={20} style={{
                padding: "20px",
                borderRadius: "20px",
                backgroundColor: "#001529"
            }}>
                <Row justify="center" align="middle">
                    <Title style={{color: "white"}}>Dashboard</Title>
                </Row>
                <br></br>
                <Row gutter={[16, 16]} style={{ padding: "40px"}}>
                    <Col span={6} style={{
                        padding: "10px",
                        borderRadius: "20px",
                        backgroundColor: "#40E0D0",
                        display: "inline",
                        height: "250px"
                    }}> 
                        <Row justify="center" align="middle">
                            Glacier One
                        </Row>
                    </Col>
                    <Col span={6} style={{
                        padding: "10px",
                        borderRadius: "20px",
                        backgroundColor: "#40E0D0",
                        display: "inline",
                        height: "250px"
                    }}> 
                        <Row justify="center" align="middle">
                            Glacier Two
                        </Row>
                    </Col>
                    <Col span={6} style={{
                        padding: "10px",
                        borderRadius: "20px",
                        backgroundColor: "#40E0D0",
                        display: "inline"
                    }}>
                        <Row justify="center" align="middle">
                            Glacier Three
                        </Row>
                    </Col>
                    <Col span={6} style={{
                        padding: "10px",
                        borderRadius: "20px",
                        backgroundColor: "#40E0D0",
                        display: "inline"
                    }}>
                        <Row justify="center" align="middle">
                            Glacier Four
                        </Row>
                    </Col>
                </Row>
                <Row justify="center">
                    <Paragraph style={{ color: "white"}}>Browse through a dashboard of glaciers.</Paragraph>
                </Row>
            </Col>
        </Row>
    )
}

export default Dashboard;