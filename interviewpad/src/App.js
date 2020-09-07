import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navigation from './component/navbar/index.js';
import Pad from './pages/pad/index.js';

function App() {
  return (
    <div className="App">
      <Navigation></Navigation>
      <Pad></Pad>
    </div>
  );
}

export default App;
