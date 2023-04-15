import { Layout, ProductsFiltersLayout,Anounce } from "../sections";
import { ProductCard } from "../components";

const Products = () => {
  return (
    <>
      <Layout>
        <ProductsFiltersLayout>
        <section className="flex flex-wrap gap-20">
          <ProductCard/>
          <ProductCard/>
          <ProductCard/>
          <ProductCard/>
          <ProductCard/>
          <ProductCard/>
          <ProductCard/>
          <ProductCard/>
          <ProductCard/>
          <ProductCard/>
          <ProductCard/>
          <ProductCard/>
        </section>
        </ProductsFiltersLayout>
        <Anounce/>
      </Layout>
    </>
  );
};

export default Products;
