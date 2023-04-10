import { NavBar, Hero, NewsLetter, Footer } from "./index";
const Layout = ({ children }) => {
  return (
    <>
      <NavBar />
      <main>{children}</main>
      <NewsLetter />
      <Footer />
    </>
  );
};

export default Layout;
