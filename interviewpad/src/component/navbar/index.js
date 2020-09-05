import React from 'react';
import Nav from 'react-bootstrap/Nav';
import Form from 'react-bootstrap/Form';
import Navbar from 'react-bootstrap/Navbar';
import Button from 'react-bootstrap/Button';
import FormControl from 'react-bootstrap/FormControl';

function Navigation() {
  return (
    <div className="NavBar">
        <Navbar bg="dark" variant="dark">
            <Navbar.Brand className="mr-auto">INTERVIEW PAD</Navbar.Brand>
            <Form inline>
                <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                <Button variant="outline-info">Search</Button>
            </Form>
        </Navbar>
    </div>
  );
}

export default Navigation;
