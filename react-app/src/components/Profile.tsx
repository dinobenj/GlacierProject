import React from "react";
import { Button, Col, Row, Typography, Card } from "antd";

const { Title, Paragraph } = Typography;

interface UserData {
    username: string;
    password: string;
    email: string;
}

const Profile: React.FC = () => {

    const username = "JDoe1";
    const email = "JohnDoe@gmail.com";


    return (
        <Row justify="center" align="middle" style={{ height: "100vh" }}>
            <Col span={20} style={{
                padding: "20px",
                borderRadius: "20px",
                backgroundColor: "#001529"
            }}>
                <Row>
                    <Col>
                        <Title level={1} style={{ color: "white" }}>{"Profile:"}</Title>
                        <Title level={4} style={{ color: "white" }}>{"Username:"}</Title>
                        <Paragraph strong style={{ color: "white", fontSize: "20px" }}>
                            {username}
                        </Paragraph>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Title level={4} style={{ color: "white" }}>{"Email:"}</Title>
                        <Paragraph strong style={{ color: "white", fontSize: "20px" }}>
                            {email}
                        </Paragraph>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Title level={2} style={{ color: "white" }}>{"Change Email:"}</Title>
                        <form>
                            <div style={{
                                display: "flex",
                                flexDirection: "column",
                                justifyContent: "center",
                                alignItems: "start"
                            }}>
                                <input
                                    name='newEmail'
                                    id='newEmail'
                                    type='newEmail'
                                    placeholder='New Email'
                                    //onChange={}
                                    required
                                    />
                                <input
                                    name='confirmEmail'
                                    id='confirmEmail'
                                    type='confrimEmail'
                                    placeholder='Confirm Email'
                                    //onChange={}
                                    required
                                    />
                                <br></br>
                                <button type='submit'>Change Email</button>
                            </div>
                        </form>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Title level={2} style={{ color: "white" }}>{"Change Password:"}</Title>
                        <form>
                            <div style={{
                                display: "flex",
                                flexDirection: "column",
                                justifyContent: "normal",
                                alignItems: "start"
                            }}>
                                <input
                                    name='newPassword'
                                    id='newPassword'
                                    type='newPassword'
                                    placeholder='New Password'
                                    //onChange={}
                                    required
                                    />
                                <input
                                    name='confirmPassword'
                                    id='confirmPassword'
                                    type='confrimPassword'
                                    placeholder='Confirm Password   '
                                    //onChange={}
                                    required
                                    />
                                <br></br>
                                <button type='submit'>{"Change Password"}</button>
                            </div>
                        </form>
                    </Col>
                </Row>
            </Col>
        </Row>
    );
}

export default Profile;