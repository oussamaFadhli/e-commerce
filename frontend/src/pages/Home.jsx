import {
  Layout,
  Hero,
  SubCategories,
  SubcategoriesLayout,
  PopularProducts,
  ProductCard,
  Anounce,
  RecomendedProducts,
  Features,
  CustomerFeedbacks,
  Sponsors,
  Hamburger,
} from "../sections";

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
          <Anounce/>
          <RecomendedProducts/>
          <Features/>
          <CustomerFeedbacks/>
          <Sponsors/>
        </main>
      </Layout>
    </>
  );
};

export default Home;
