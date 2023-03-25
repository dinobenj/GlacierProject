import React from "react";
import { Button, Col, Row, Typography, Card } from "antd";
import { PieChartOutlined } from '@ant-design/icons';

const { Title, Paragraph } = Typography;

interface GlacierData {
  name: string;
  area: number;
  length: number;
  elevation: number;
}

const Dashboard: React.FC = () => {
  const glacierData: GlacierData[] = [
    { name: 'Aletsch Glacier', area: 81.7, length: 23.6, elevation: 3800 },
    { name: 'Fox Glacier', area: 13.2, length: 13.6, elevation: 2600 },
    { name: 'Mendenhall Glacier', area: 12.4, length: 19.3, elevation: 1500 },
    { name: 'Perito Moreno Glacier', area: 250, length: 30, elevation: 60 },
    { name: 'Vatnajökull Glacier', area: 8100, length: 135, elevation: 2110 },
  ];
