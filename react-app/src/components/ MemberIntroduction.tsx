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
                        Frontend: Ji Wang, Russell Harter, Kaylin Rackley
                    </Paragraph>
                </Col>
            </Row>
            <Row>
                <Col>
                    <Paragraph strong style={{
                        color: "white",
                        fontSize: "20px"
                    }}>
                        Backend: Russell Harter, Ryan Karch, Smayan Nandakumar, Sarah Nicolai
                    </Paragraph>
                </Col>
            </Row>
        </>
    );
}

export default MemberIntroduction;