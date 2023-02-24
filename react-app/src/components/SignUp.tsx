import React from "react";
import {Col, Row, Typography} from "antd";
import MemberIntroduction from "./ MemberIntroduction";

const {Title, Paragraph} = Typography;

const SignUp: React.FC = () => {
    const signupText = "Don't have an account yet?";
    const signupButton = "Sign up";
    const teamIntroductionTitle = "Who we are?"
    const teamIntroductionText = "We are students at Rensselaer Polytechnic Institue (RPI) and members of Rensselaer Center for Open Source (RCOS).";

    return (
        <Row justify="center" align="middle" style={{height: "100vh"}}>
            <Col span={20} style={{
                padding: "20px",
                borderRadius: "20px",
                backgroundColor: "#001529"
            }}>
                <Row justify="space-around" align="middle">
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

export default SignUp;