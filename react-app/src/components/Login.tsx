import React from "react";
<<<<<<< Updated upstream
import {Button, Col, Row, Typography} from "antd";

const Login: React.FC = () => {
    return (
        <header>
            TEST
        </header>
=======
import {Col, Row, Typography} from "antd";
import MemberIntroduction from "./ MemberIntroduction";
import { useForm } from "../useForm";

const {Title, Paragraph} = Typography;

const Login: React.FC = () => {
    const signupText = "Don't have an account yet?";
    const signupButton = "Sign up";
    const teamIntroductionTitle = "Who we are?"
    const teamIntroductionText = "We are students at Rensselaer Polytechnic Institue (RPI) and members of Rensselaer Center for Open Source (RCOS).";

    // defining the initial state for the form
    const initialState = {
        email: "",
        password: "",
    };

    // getting the event handlers from our custom hook
    const { onChange, onSubmit, values } = useForm(
        loginUserCallback,
        initialState
    );

    // a submit function that will execute upon form submission
    async function loginUserCallback() {
        // send "values" to database
    }

    return (
        <Row justify="center" align="middle" style={{height: "100vh"}}>
            <Col span={20} style={{
                padding: "20px",
                borderRadius: "20px",
                backgroundColor: "#001529"
            }}>
                <Row justify="space-around" align="middle">
                    <Col>
                        <Title style={{color: "white", textAlign: "center"}}>Login</Title>
                        <Paragraph strong style={{
                            color: "white",
                            fontSize: "15px"
                        }}>
                            {signupText} <a href="/signup">{signupButton}</a>
                        </Paragraph>
                    </Col>
                </Row>
                <Row justify="space-around" align="middle">
                    <Col>
                        <form onSubmit={onSubmit}>
                            <div style={{ 
                                display: "flex",
                                flexDirection: "column",
                                justifyContent: "center",
                                alignItems: "center"
                            }}>
                                <br></br>
                                <input
                                    name='email'
                                    id='email'
                                    type='email'
                                    placeholder='Email'
                                    onChange={onChange}
                                    required
                                    />
                                
                                <input
                                    name='password'
                                    id='password'
                                    type='password'
                                    placeholder='Password'
                                    onChange={onChange}
                                    required
                                    />
                                <br></br>
                                <button type='submit'>Login</button>
                            </div>
                        </form>
                        <br></br>
                    </Col>
                </Row>
            </Col>
        </Row>
>>>>>>> Stashed changes
    )
}

export default Login;