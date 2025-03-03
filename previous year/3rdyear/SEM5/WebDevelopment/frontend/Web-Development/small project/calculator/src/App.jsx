import { useState } from 'react';
import './App.css';
import ButtonComponent from './components/ButtonComponent';
import ScreenComponent from './components/ScreenComponent';

function App() {
  const [CurrVal, setCurrVal] = useState('');

  return (
    <>
      <div className="container">
        <ScreenComponent CurrVal={CurrVal} />
        <ButtonComponent setCurrVal={setCurrVal} />
      </div>
    </>
  );
}

export default App;
