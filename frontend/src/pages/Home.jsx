import {
  Layout,
  Hero,
  SubCategories,
  SubcategoriesLayout,
  PopularProducts,
  ProductCard,
} from "../components";

const Home = () => {
  return (
    <>
      <Layout>
        <main>
          <Hero />
          <SubcategoriesLayout>
            <SubCategories />
            <SubCategories />
            <SubCategories />
            <SubCategories />
            <SubCategories />
          </SubcategoriesLayout>

          <PopularProducts>
            <ProductCard />
            <ProductCard />
            <ProductCard />
            <ProductCard />
            <ProductCard />
            <ProductCard />
            <ProductCard />
            <ProductCard />
            <ProductCard />
            <ProductCard />
          </PopularProducts>
        </main>
      </Layout>
    </>
  );
};

export default Home;
