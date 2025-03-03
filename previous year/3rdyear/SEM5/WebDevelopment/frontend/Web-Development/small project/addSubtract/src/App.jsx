import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import DisplayComponent from './components/DisplayComponent'

function App() {
  const [count, setCount] = useState(0)
  function increment(){
    setCount(count + 1)
  }
  function decrement(){
    if(count > 0){
      setCount(count - 1)
    }
  }

  function MyComponent(myCount) {
    if (count > 5) {
      return <button onClick={decrement}>subtract</button>
    } else {
      return 
    }
  }
  
  return (
    <>
      <button onClick={increment}>add</button>
      {/* <h1>{count}</h1> */}
      <DisplayComponent mycount ={count}/>
      {/* {count > 5 && <button onClick={decrement}>subtract</button>} */}
      <MyComponent myCount={count}/>
    </>
  )
}

export default App
