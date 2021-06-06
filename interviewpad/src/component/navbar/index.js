import React from 'react';
import Form from 'react-bootstrap/Form';
import Navbar from 'react-bootstrap/Navbar';
import FormControl from 'react-bootstrap/FormControl';

function Navigation() {
  return (
    <div className="NavBar">
        <Navbar bg="dark" variant="dark">
            <Navbar.Brand className="mr-auto">INTERVIEW PAD</Navbar.Brand>
            <Form inline>
                <FormControl type="text" placeholder="Search" className="mr-sm-2" />
            </Form>
        </Navbar>
    </div>
  );
}

export default Navigation;
