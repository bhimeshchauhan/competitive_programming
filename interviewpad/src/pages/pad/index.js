import React, {useState} from 'react';
import './index.css';
import List from '../../component/list/index';
import Carousel from 'react-bootstrap/Carousel';
import Details from '../../component/details/index';

function Pad() {
    const [index, setIndex] = useState(0);
    const [path, setPath] = useState(null);
    const [name, setName] = useState('Challenge');

    const handleSelect = (selectedIndex, name, path) => {
        if(name!== null && name!== undefined) {
            console.log(name)
            setName(name);
        }
        if(selectedIndex!== null && selectedIndex!== undefined){
            console.log(selectedIndex)
            setIndex(selectedIndex);
        }
        if(path!== null && path!== undefined){
            console.log(path)
            setPath(path);
        }
    };

    return (
        <div className="Pad">
            <Carousel activeIndex={index} controls={false} touch={false} wrap={false} indicators={false}>
                <Carousel.Item>
                    <List className="panel" toggleActive={handleSelect}></List>
                </Carousel.Item>
                <Carousel.Item>
                    <Details className="panel" toggleActive={handleSelect} name={name} path={path}></Details>
                </Carousel.Item>
            </Carousel>
        </div>
    );
}

export default Pad;
