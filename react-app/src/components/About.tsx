import React from "react";
import {Col, Row, Typography} from "antd";
import MemberIntroduction from "./ MemberIntroduction";

const {Title, Paragraph} = Typography;

const About: React.FC = () => {
    const projectIntroductinTitle = "What is the glacier project?"
    const projectIntroductionText = "The Glacier Project is a web application that visualizes data, satellite images, and predictions of our planet's glaciers.";
    const teamIntroductionTitle = "Who we are?"
    const teamIntroductionText = "We are students at Rensselaer Polytechnic Institue (RPI) and members of Rensselaer Center for Open Source (RCOS).";

    return (
        <Row justify="center" align="middle" style={{height: "100vh"}}>
            <Col span={15} style={{
                padding: "20px",
                borderRadius: "20px",
                backgroundColor: "rgba(128, 128, 128, 0.3)"
            }}>
                <Row justify="space-around" align="middle">
                    <Col>
                        <Title style={{color: "white"}}>{projectIntroductinTitle}</Title>
                        <Paragraph strong style={{
                            color: "white",
                            fontSize: "20px"
                        }}>
                            {projectIntroductionText}
                        </Paragraph>
                    </Col>
                </Row>
                <Row justify="space-around" align="middle">
                    <Col>
                        <Title style={{color: "white"}}>{teamIntroductionTitle}</Title>
                        <Paragraph strong style={{
                            color: "white",
                            fontSize: "20px"
                        }}>
                            {teamIntroductionText}
                        </Paragraph>
                        <MemberIntroduction/>
                    </Col>
                </Row>
            </Col>
        </Row>
    )
}

export default About;