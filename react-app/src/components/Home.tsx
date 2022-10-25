import React from "react";
import {Button, Col, Row, Typography} from "antd";

const {Title, Paragraph, Text} = Typography;

const Home: React.FC = () => {
    const introduction = "Glaciers are masses of snow that has been compressed into giant sheets of ice. Most glaciers were formed during the last ice age.";

    return (
        <Row justify="center" align="middle" style={{height: "100vh"}}>
            <Col span={12} style={{
                padding: "20px",
                borderRadius: "20px",
                backgroundColor: "rgba(128, 128, 128, 0.3)"
            }}>
                <Row justify="space-around" align="middle">
                    <Col span={24}>
                        <Paragraph strong style={{color: "white"}}>
                            {introduction}
                        </Paragraph>
                    </Col>
                </Row>
                <Row justify="space-around" align="middle">
                    <Col>
                        <Button type="text" size="large" shape="round" href="/map">
                            <Text strong style={{color: "white"}}>
                                Explore in map
                            </Text>
                        </Button>
                    </Col>
                </Row>
            </Col>
        </Row>
    );
}

export default Home;