import { Home , Products,ProductDetails,CartsPage, Checkout } from "./pages";
import {Routes , Route } from 'react-router-dom'
import "./App.css";

const App = () => {
  return (
    <>
    <Routes>
      <Route path='/' element={<Home/>} />
      <Route path='/products' element={<Products/>} />
      <Route path='/products/id' element={<ProductDetails/>} />
      <Route path='/carts' element={<CartsPage/>} />
      <Route path='/checkout' element={<Checkout/>} />
    </Routes>
    </>
  );
};

export default App;
