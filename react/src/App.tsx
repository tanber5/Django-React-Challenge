import React from 'react';
import './App.css';
import EncodeForm from './components/EncodeForm'

const App:React.FC = ():JSX.Element => {
  return (
    <div className="container">
        <div className="row">
            <div className="col-6 form-div">
                <h1>Hack This (^_^)</h1>
                <EncodeForm/>
            </div>
        </div>
    </div>
  );
}

export default App;
