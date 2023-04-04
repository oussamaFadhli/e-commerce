import { Home , Products } from "./pages";
import {Routes , Route } from 'react-router-dom'
import "./App.css";

const App = () => {
  return (
    <>
    <Routes>
      <Route path='/' element={<Home/>} />
      <Route path='/products' element={<Products/>} />
    </Routes>
    </>
  );
};

export default App;
