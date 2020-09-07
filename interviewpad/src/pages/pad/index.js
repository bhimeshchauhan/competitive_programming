import React, {useState} from 'react';
import './index.css';
import List from '../../component/list/index';
import Carousel from 'react-bootstrap/Carousel';
import Details from '../../component/details/index';

function Pad() {
    const [currentProblem, setCurrentProblem] = useState(null)
    const [index, setIndex] = useState(0);

    const handleSelect = (selectedIndex, e) => {
        setIndex(selectedIndex);
    };

    const toggleActiveStatus = (index) => {
        console.log(index);
        setCurrentProblem(index);
    }

    return (
    <div className="Pad">
        <Carousel activeIndex={index} controls={false} touch={false} wrap={false} indicators={false}>
            <Carousel.Item>
                <List className="panel" toggleActive={handleSelect}></List>
            </Carousel.Item>
            <Carousel.Item>
                <Details className="panel" toggleActive={handleSelect}></Details>
            </Carousel.Item>
        </Carousel>
    </div>
    );
}

export default Pad;
