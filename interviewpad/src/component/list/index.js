import React from "react";
import "./index.css";
import ListGroup from "react-bootstrap/ListGroup";
import data from "../../data/problems";

function List(props) {
  const toggle = (name, path) => {
    return props.toggleActive(1, name, path);
  };

  return (
    <div className={"List " + props.slide}>
      <ListGroup>
        {data.map((question, idx) => {
          return (
            <ListGroup.Item
              action
              className="ListItem"
              key={idx}
              onClick={() => toggle(question.name, question.path)}
            >
              {question.name}
            </ListGroup.Item>
          );
        })}
      </ListGroup>
    </div>
  );
}

export default List;
