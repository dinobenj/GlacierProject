import React from "react";
import {Button, Col, Row, Typography} from "antd";

const {Title, Paragraph, Text} = Typography;

const Home: React.FC = () => {
    const titleText = "Do you know?";
    const glacierIntroductionText = "Glaciers are masses of snow that has been compressed into giant sheets of ice. Most glaciers were formed during the last ice age.";
    const appIntroductionText = "We built an app to let you see glaciers all over the world, and their detailed data.";
    const welcomeText = "Welcome to the world of ice!";
    const buttonText = "GO TO MAP";


    return (
        <Row justify="center" align="middle" style={{height: "100vh"}}>
            <Col span={12} style={{
                padding: "20px",
                borderRadius: "20px",
                backgroundColor: "rgba(128, 128, 128, 0.6)"
            }}>
                <Row justify="space-around" align="middle">
                    <Col>
                        <Title style={{color: "white"}}>{titleText}</Title>
                    </Col>
                </Row>
                <Row justify="space-around" align="middle">
                    <Col span={24}>
                        <Paragraph strong style={{
                            color: "white",
                            fontSize: "20px"
                        }}>
                            {glacierIntroductionText}
                        </Paragraph>
                        <Paragraph strong style={{
                            color: "white",
                            fontSize: "20px"
                        }}>
                            {appIntroductionText}
                        </Paragraph>
                        <Paragraph strong style={{
                            color: "white",
                            fontSize: "20px",
                            textAlign: "center"
                        }}>
                            {welcomeText.toUpperCase()}
                        </Paragraph>
                    </Col>
                </Row>
                <Row justify="space-around" align="middle">
                    <Col>
                        <Button ghost size="large" shape="round" href="/map">
                            <Text strong style={{color: "white"}}>
                                {buttonText}
                            </Text>
                        </Button>
                    </Col>
                </Row>
            </Col>
        </Row>
    );
}

export default Home;