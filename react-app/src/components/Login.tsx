import React from "react";
import { Button, Col, Row, Typography } from "antd";
import MemberIntroduction from "./MemberIntroduction";
import { useForm } from "../useForm";

const { Title, Paragraph } = Typography;

const Login: React.FC = () => {
  const signupText = "Don't have an account yet?";
  const signupButton = "Sign up";
  const teamIntroductionTitle = "Who we are?";
  const teamIntroductionText =
    "We are students at Rensselaer Polytechnic Institue (RPI) and members of Rensselaer Center for Open Source (RCOS).";

  // defining the initial state for the form
  const initialState = {
    email: "",
    password: "",
  };

  // getting the event handlers from our custom hook
  const { onChange, onSubmit, values } = useForm(loginUserCallback, initialState);

  // a submit function that will execute upon form submission
  async function loginUserCallback() {
    // send "values" to database
  }

  return (
    <header>
      TEST
    </header>
  );
};

export default Login;
