import { Layout, Hero, SubCategories } from "../components";

const Home = () => {
  return (
    <>
      <Layout>
        <main>
          <Hero />
          <div className="flex flex-wrap justify-around">
          <SubCategories />
          <SubCategories />
          <SubCategories />
          <SubCategories />
          <SubCategories />
          </div>
        </main>
      </Layout>
    </>
  );
};

export default Home;
