import React, { useState } from "react";
import { Button, Col, Form, Input, Row, Typography } from "antd";
import MemberIntroduction from "./MemberIntroduction";
import { useForm } from "../useForm";

const { Title, Paragraph } = Typography;

interface LoginFormData {
  email: string;
  password: string;
}

const Login: React.FC = () => {
  const signupText = "Don't have an account yet?";
  const signupButton = "Sign up";
  const teamIntroductionTitle = "Who we are?";
  const teamIntroductionText =
    "We are students at Rensselaer Polytechnic Institue (RPI) and members of Rensselaer Center for Open Source (RCOS).";

  // defining the initial state for the form
  const initialState: LoginFormData = {
    email: "",
    password: "",
  };

  // getting the event handlers from our custom hook
  const { onChange, onSubmit, values } = useForm(loginUserCallback, initialState);

  // state to keep track of login status
  const [loginError, setLoginError] = useState<string>("");

  // a submit function that will execute upon form submission
  async function loginUserCallback() {
    // send "values" to database or API for authentication
    try {
      // simulate authentication check
      if (values.email === "user@example.com" && values.password === "password") {
        setLoginError("");
        console.log("Login successful");
      } else {
        setLoginError("Invalid email or password");
      }
    } catch (error) {
      console.error(error);
      setLoginError("Something went wrong. Please try again later.");
    }
  }

  return (
    <Row justify="center">
      <Col xs={24} sm={20} md={16} lg={12} xl={8}>
        <Title level={2}>Login</Title>
        <Form onFinish={onSubmit} layout="vertical">
          <Form.Item
            label="Email"
            name="email"
            rules={[{ required: true, message: "Please input your email!" }]}
          >
            <Input value={values.email} onChange={onChange} type="email" />
          </Form.Item>

          <Form.Item
            label="Password"
            name="password"
            rules={[{ required: true, message: "Please input your password!" }]}
          >
            <Input.Password value={values.password} onChange={onChange} />
          </Form.Item>

          {loginError && <p style={{ color: "red" }}>{loginError}</p>}

          <Form.Item>
            <Button type="primary" htmlType="submit">
              Login
            </Button>
          </Form.Item>
        </Form>

        <Paragraph>
          {signupText} <a href="#">{signupButton}</a>
        </Paragraph>

        <MemberIntroduction title={teamIntroductionTitle} text={teamIntroductionText} />
      </Col>
    </Row>
  );
};

export default Login;
