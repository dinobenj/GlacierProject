import React from "react";
import {Button, Col, Row, Typography} from "antd";
const {Title, Paragraph} = Typography;

const Dashboard: React.FC = () => {
    return(
        <Row justify="center" align="middle" style={{height: "100vh"}}>
            <Col span={20} style={{
                padding: "20px",
                borderRadius: "20px",
                backgroundColor: "#001529"
            }}></Col>
        </Row>
    ); 

}

export default Dashboard;