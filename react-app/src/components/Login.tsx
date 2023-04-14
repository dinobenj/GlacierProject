import React, { useContext, useRef } from "react";
import { Button, Container, Col, Form, Navbar} from "react-bootstrap";
import { AuthContext } from "../context/AuthContext";
import { auth } from "../firebaseSetup";

function Login() {
    const user = useContext(AuthContext);
    const emailRef = useRef<HTMLInputElement>(null);
    const passwordRef = useRef<HTMLInputElement>(null);
    const createAccount = async () => {
      try {
        await auth.createUserWithEmailAndPassword(
          emailRef.current!.value,
          passwordRef.current!.value
        );
      } catch (error) {
        console.error(error);
      }
    };
  
    const signIn = async () => {
      try {
        await auth.signInWithEmailAndPassword(
          emailRef.current!.value,
          passwordRef.current!.value
        );
      } catch (error) {
        console.error(error);
      }
    };
  
    const signOut = async () => {
      await auth.signOut();
    };

    return (
      <>
        <Navbar className="justify-content-between" bg="dark" variant="dark">
        <Navbar.Brand>Glacier Project</Navbar.Brand>
        {user && <Button onClick={signOut}>Sign Out</Button>}
      </Navbar>
      {!user ? (
        <Container style={{ maxWidth: "500px" }} fluid>
          <Form className="mt-4">
            <Form.Group controlId="formEmail">
              <Form.Label>Email</Form.Label>
              <Form.Control ref={emailRef} type="email" placeholder="email" />
            </Form.Group>
            <Form.Group controlId="formPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control
                ref={passwordRef}
                type="password"
                placeholder="password"
              />
            </Form.Group>
                <Button onClick={createAccount} type="button">
                  Sign Up
                </Button>
                <Button
                  onClick={signIn}
                  type="button"
                  variant="secondary"
                >
                  Sign In
                </Button>
          </Form>
        </Container>
      ) : (
        <h2 className="mt-4 text-center">Welcome {user.email}</h2>
      )}
    </>
  );
  }
  export default Login;
  
// const Login: React.FC = () => {
//     const signupText = "Don't have an account yet?";
//     const signupButton = "Sign up";
//     const teamIntroductionTitle = "Who we are?"
//     const teamIntroductionText = "We are students at Rensselaer Polytechnic Institue (RPI) and members of Rensselaer Center for Open Source (RCOS).";

//     // defining the initial state for the form
//     const initialState = {
//         email: "",
//         password: "",
//     };

//     // getting the event handlers from our custom hook
//     const { onChange, onSubmit, values } = useForm(
//         loginUserCallback,
//         initialState
//     );

//     // a submit function that will execute upon form submission
//     async function loginUserCallback() {
//         // send "values" to database
//     }

//     return (
//         <Row justify="center" align="middle" style={{height: "100vh"}}>
//             <Col span={20} style={{
//                 padding: "20px",
//                 borderRadius: "20px",
//                 backgroundColor: "#001529"
//             }}>
//                 <Row justify="space-around" align="middle">
//                     <Col>
//                         <Title style={{color: "white", textAlign: "center"}}>Login</Title>
//                         <Paragraph strong style={{
//                             color: "white",
//                             fontSize: "15px"
//                         }}>
//                             {signupText} <a href="/signup">{signupButton}</a>
//                         </Paragraph>
//                     </Col>
//                 </Row>
//                 <Row justify="space-around" align="middle">
//                     <Col>
//                         <form onSubmit={onSubmit}>
//                             <div style={{ 
//                                 display: "flex",
//                                 flexDirection: "column",
//                                 justifyContent: "center",
//                                 alignItems: "center"
//                             }}>
//                                 <br></br>
//                                 <input
//                                     name='email'
//                                     id='email'
//                                     type='email'
//                                     placeholder='Email'
//                                     onChange={onChange}
//                                     required
//                                     />
                                
//                                 <input
//                                     name='password'
//                                     id='password'
//                                     type='password'
//                                     placeholder='Password'
//                                     onChange={onChange}
//                                     required
//                                     />
//                                 <br></br>
//                                 <button type='submit'>Login</button>
//                             </div>
//                         </form>
//                         <br></br>
//                     </Col>
//                 </Row>
//             </Col>
//         </Row>
//     )
// }

// export default Login;