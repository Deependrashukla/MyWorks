import React from 'react';

function ButtonComponent({ setCurrVal }) {
  const insertVal = (val) => {
    // Append the clicked value to the current state
    setCurrVal((prev) => prev + val);
  };

  const calculateResult = () => {
    setCurrVal((prev) => {
      try {
        // Evaluate the expression using JavaScript's eval function
        return eval(prev).toString(); // Convert result to string
      } catch (error) {
        return 'Error'; // Handle invalid expressions
      }
    });
  };

  return (
    <>
      <div className="buttonComp">
        <button onClick={() => insertVal('1')}>1</button>
        <button onClick={() => insertVal('2')}>2</button>
        <button onClick={() => insertVal('3')}>3</button>
        <button onClick={() => insertVal('4')}>4</button>
        <button onClick={() => insertVal('5')}>5</button>
        <button onClick={() => insertVal('6')}>6</button>
        <button onClick={() => insertVal('7')}>7</button>
        <button onClick={() => insertVal('8')}>8</button>
        <button onClick={() => insertVal('9')}>9</button>
        <button onClick={() => insertVal('0')}>0</button>
        <button onClick={() => insertVal('+')}>+</button>
        <button onClick={() => insertVal('-')}>-</button>
        <button onClick={() => insertVal('*')}>*</button>
        <button onClick={() => insertVal('/')}>/</button>
        <button onClick={calculateResult}>=</button>
        <button onClick={() => setCurrVal('')}>Clear</button>
      </div>
    </>
  );
}

export default ButtonComponent;
