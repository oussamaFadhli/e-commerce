import {
  InfoLine,
  NavBar,
  CategoriesBrowser,
  NewsLetter,
  Footer,
} from "./index";
const Layout = ({ children }) => {
  return (
    <>
      <InfoLine />
      <NavBar />
      <CategoriesBrowser />
      <main>{children}</main>
      <NewsLetter />
      <Footer />
    </>
  );
};

export default Layout;
