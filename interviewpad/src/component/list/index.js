import React from 'react';
import './index.css';
import ListGroup from 'react-bootstrap/ListGroup';
import data from '../../data/problems';

function List(props) {

    const toggle = () => {
        return props.toggleActive(1);
    }

    return (
        <div className={"List " + props.slide}>
            <ListGroup>
                {
                    data.map((question, idx) => {
                        return <ListGroup.Item action className="ListItem" key={idx} onClick={() => toggle()}>
                        {question.name}
                        </ListGroup.Item>
                    })
                }
            </ListGroup>
        </div>
    );
}

export default List;
