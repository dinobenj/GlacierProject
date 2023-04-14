import React from "react";
import { Button, Col, Row, Typography } from "antd";
import "./Home.css";

const { Title, Paragraph, Text } = Typography;

const Home: React.FC = () => {
  const titleText = "Do you know?";
  const glacierIntroductionText =
    "Glaciers are masses of snow that has been compressed into giant sheets of ice. Most glaciers were formed during the last ice age.";
  const appIntroductionText =
    "We built an app to let you see glaciers all over the world, and their detailed data.";
  const welcomeText = "Welcome to the world of ice!";
  const buttonText = "GO TO MAP";

  return (
    <Row justify="center" align="middle" className="home-container">
      <Col span={12} className="home-card">
        <Row justify="space-around" align="middle">
          <Col>
            <Title className="home-title">{titleText}</Title>
          </Col>
        </Row>
        <Row justify="space-around" align="middle">
          <Col span={24}>
            <Paragraph strong className="home-paragraph">
              {glacierIntroductionText}
            </Paragraph>
            <Paragraph strong className="home-paragraph">
              {appIntroductionText}
            </Paragraph>
            <Paragraph strong className="home-welcome-text">
              {welcomeText.toUpperCase()}
            </Paragraph>
          </Col>
        </Row>
        <Row justify="space-around" align="middle">
          <Col>
            <Button ghost size="large" shape="round" to="/map">
              <Text strong className="home-button-text">
                {buttonText}
              </Text>
            </Button>
          </Col>
        </Row>
      </Col>
    </Row>
  );
};

export default Home;
