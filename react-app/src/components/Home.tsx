import React from "react";
import {Button, Col, Row} from "antd";

const Home: React.FC = () => {
    return (
        <Row justify="center" align="middle">
            <Col>
                <Row justify="space-around" align="middle">
                    <Col>
                        <h1>Explore Glaciers</h1>
                    </Col>
                </Row>
                <Row justify="space-around" align="middle">
                    <Col>
                        <Button type="text" size="large" shape="round" href="/map">
                            Go to map
                        </Button>
                    </Col>
                </Row>
            </Col>
        </Row>
    );
}

export default Home;