import { Col, Row, Typography } from "antd";
import React from "react";
import "./MemberIntroduction.css"; // Import custom CSS file

const { Paragraph } = Typography;

const MemberIntroduction: React.FC = () => {
  return (
    <>
      <Row style={{ marginBottom: "20px" }}>
        <Col>
          <Paragraph
            strong
            className="member-intro-text"
          >
            Project Lead: Ben Dennison
          </Paragraph>
        </Col>
      </Row>
      <Row style={{ marginBottom: "20px" }}>
        <Col>
          <Paragraph
            strong
            className="member-intro-text"
          >
            Frontend: Ji Wang, Russell Harter, Kaylin Rackley, William Lin
          </Paragraph>
        </Col>
      </Row>
      <Row style={{ marginBottom: "20px" }}>
        <Col>
          <Paragraph
            strong
            className="member-intro-text"
          >
            Backend: Russell Harter, Ryan Karch, Smayan Nandakumar, Sarah Nicolai
          </Paragraph>
        </Col>
      </Row>
      <Row>
        <Col>
          <Paragraph
            className="member-intro-text"
          >
            All students are from Rensselaer Polytechnic Institute.
          </Paragraph>
        </Col>
      </Row>
    </>
  );
};

export default MemberIntroduction;