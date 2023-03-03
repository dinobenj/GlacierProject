import React from "react";
import {Col, Row, Typography} from "antd";
import MemberIntroduction from "./ MemberIntroduction";
import { useForm } from "../useForm";

const {Title, Paragraph} = Typography;

const SignUp: React.FC = () => {
    const loginText = "Already signed up?";
    const loginButton = "Log in";

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
        const response = await fetch("/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(values),
        }); 
    }

    return (
        <Row justify="center" align="middle" style={{height: "100vh"}}>
            <Col span={20} style={{
                padding: "20px",
                borderRadius: "20px",
                backgroundColor: "#001529"
            }}>
                <Row justify="space-around" align="middle">
                </Row>
                <Row justify="space-around" align="middle">
                    <Col>
                        <Title style={{color: "white", textAlign: "center"}}>Sign Up</Title>
                        <Paragraph strong style={{
                            color: "white",
                            fontSize: "20px"
                        }}>
                            <Paragraph style={{color: "white", textAlign: "center"}}>{loginText} <a href="/login">{loginButton}</a></Paragraph>
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
                                    name="name"
                                    id="name"
                                    type="name"
                                    placeholder="Name"
                                    onChange={onChange}
                                    required
                                    />
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
                                <input
                                    name="confirmPassword"
                                    id="confirmPassword"
                                    placeholder="Confirm Password"
                                    onChange={onChange}
                                    required
                                    />
                                <br></br>
                                <button type='submit'>Sign Up</button>
                            </div>
                        </form>
                        <br></br>
                    </Col>
                </Row>
            </Col>
        </Row>
    )
}

export default SignUp;