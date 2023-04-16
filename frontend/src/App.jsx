import { Home , Products,ProductDetails } from "./pages";
import {Routes , Route } from 'react-router-dom'
import "./App.css";

const App = () => {
  return (
    <>
    <Routes>
      <Route path='/' element={<Home/>} />
      <Route path='/products' element={<Products/>} />
      <Route path='/products/id' element={<ProductDetails/>} />
    </Routes>
    </>
  );
};

export default App;
