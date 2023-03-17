import {Col, Row, Typography} from "antd";
import React from "react";

const {Paragraph} = Typography;

const MemberIntroduction: React.FC = () => {
    return (
        <>
            <Row>
                <Col>
                    <Paragraph strong style={{
                        color: "white",
                        fontSize: "20px"
                    }}>
                        Project Lead: Ben Dennison
                    </Paragraph>
                </Col>
            </Row>
            <Row>
                <Col>
                    <Paragraph strong style={{
                        color: "white",
                        fontSize: "20px"
                    }}>
                        Deployment Solution: Ben Dennison, Eddie Poon, Hannah Jin
                    </Paragraph>
                </Col>
            </Row>
            <Row>
                <Col>
                    <Paragraph strong style={{
                        color: "white",
                        fontSize: "20px"
                    }}>
                        Frontend: Tevin Zhuo, Owen Witkos, Will Lin
                    </Paragraph>
                </Col>
            </Row>
            <Row>
                <Col>
                    <Paragraph strong style={{
                        color: "white",
                        fontSize: "20px"
                    }}>
                        API: Hannah Jin, Ben Dennison, Anthony DiGiovanna, Sid Kilaru, Sarah Nicolai

                    </Paragraph>
                </Col>
            </Row>
            <Row>
                <Col>
                    <Paragraph strong style={{
                        color: "white",
                        fontSize: "20px"
                    }}>
                        Geological Algorithms: Sarah Nicola, Sid Kilaru, Audrey Kling
                    </Paragraph>
                </Col>
            </Row>
            <Row>
                <Col>
                    <Paragraph strong style={{
                        color: "white",
                        fontSize: "20px"
                    }}>
                        RShiny: Ben Dennison, Audrey Kling, Tevin Zhuo, Hayeon Oh, Will Lin
                    </Paragraph>
                </Col>
            </Row>
        </>
    );
}

export default MemberIntroduction;