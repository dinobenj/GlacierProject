import React from "react";
import { Button, Col, Row, Typography, Card } from "antd";
import { PieChartOutlined } from '@ant-design/icons';
import { Link } from "react-router-dom"

const { Title, Paragraph } = Typography;

interface GlacierData {
  name: string;
  area: number;
  length: number;
  elevation: number;
}

const Dashboard: React.FC = () => {
  const glacierData: GlacierData[] = [
    { name: 'Aletsch', area: 81.7, length: 23.6, elevation: 3800 },
    { name: 'Fox', area: 13.2, length: 13.6, elevation: 2600 },
    { name: 'Mendenhall', area: 12.4, length: 19.3, elevation: 1500 },
    { name: 'Perito Moreno', area: 250, length: 30, elevation: 60 },
    { name: 'Vatnajökull', area: 8100, length: 135, elevation: 2110 },
  ];

  const renderGlacierCards = () => {
    return glacierData.map((glacier) => (
      <Col xs={24} sm={12} md={8} lg={6} xl={4} key={glacier.name}>
        <div style={{ textAlign: "center" }}>
          <Link to="/map">
          <Card hoverable style={{ marginBottom: "20px" }}>
            <Title level={4}>{glacier.name}</Title>
            <Paragraph>
              <b>Area:</b> {glacier.area} km²
            </Paragraph>
            <Paragraph>
              <b>Length:</b> {glacier.length} km
            </Paragraph>
            <Paragraph>
              <b>Elevation:</b> {glacier.elevation} m
            </Paragraph>
          </Card>
          </Link>
        </div>
      </Col>
    ));
  };

  return (
    <Row justify="center" align="middle" style={{ height: "100vh" }}>
      <Col span={20} style={{
        padding: "30px",
        borderRadius: "10px",
        backgroundColor: "#001529"
      }}>
        <Title level={2} style={{ color: "white", marginBottom: '30px', textAlign: "center" }}>Glacier Dashboard</Title>
        <Row justify="center" gutter={[16, 16]}>
          {renderGlacierCards()}
        </Row>
      </Col>
    </Row>
  );
}

export default Dashboard;