import {
  Layout,
  Hero,
  SubcategoriesLayout,
  PopularProducts,
  Anounce,
  RecomendedProducts,
  Features,
  CustomerFeedbacks,
  Sponsors,
} from "../sections";
import { SubCategories, ProductCard } from "../components";

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
          <Anounce />
          <RecomendedProducts />
          <Features />
          <CustomerFeedbacks />
          <Sponsors />
        </main>
      </Layout>
    </>
  );
};

export default Home;
