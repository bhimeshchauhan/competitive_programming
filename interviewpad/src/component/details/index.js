import React, { useState, useEffect } from 'react';
import './index.css';
import Nav from 'react-bootstrap/Nav';
import ReactMarkdown from 'react-markdown'
import Navbar from 'react-bootstrap/Navbar';
import Button from 'react-bootstrap/Button';

function Details(props) {
  const [text, setText] = useState(null)

  const toggle = () => {
    return props.toggleActive(0);
  }

  useEffect(() => {
    fetch(props.path).then((response) => response.text()).then((text) => {
      setText(text)
    });
  }, [props.path]);


  return (
    <div className={"details"}>
      <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
        <Navbar.Brand href="#home">{props.name}</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="ml-auto">
            <Nav><Button variant="outline-warning" onClick={() => toggle()}>Back</Button></Nav>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
      <ReactMarkdown source={text} className="question"/>
    </div>
  );
}

export default Details;