import { Layout} from "../sections";
import { macbook } from "../assets";
import { Review } from "../components";
import CheckIcon from "@mui/icons-material/Check";

const ProductDetails = () => {
  return (
    <>
      <Layout>
        <section>
          <div className="relative mx-auto max-w-screen-xl px-4 py-8">
            <div>
              <h1 className="text-2xl font-bold lg:text-3xl">Macbook Pro M1</h1>

              <p className="mt-1 text-sm text-gray-500">SKU: #012345</p>
            </div>

            <div className="grid gap-8 lg:grid-cols-4 lg:items-start">
              <div className="lg:col-span-3">
                <div className="relative mt-4">
                  <img
                    alt="macbook"
                    src={macbook}
                    className="h-72 w-full rounded-xl object-cover lg:h-[540px]"
                  />
                </div>
              </div>

              <div className="lg:sticky lg:top-0">
                <form className="space-y-4 lg:pt-8">
                  <fieldset>
                    <legend className="text-lg font-bold">Availability</legend>

                    <div className="mt-2 flex flex-wrap gap-1">
                      <CheckIcon className="text-green-500" />
                      <h2 className="ml-2">In Stock</h2>
                    </div>
                  </fieldset>

                  <fieldset>
                    <legend className="text-lg font-bold">Brand</legend>

                    <div className="mt-2 flex flex-wrap gap-1">
                      <h2 className="text-bold ml-4">Lenovo</h2>
                    </div>
                  </fieldset>

                  <div className="rounded border bg-gray-100 p-4">
                    Quantity : 90
                  </div>

                  <div>
                    <p className="text-xl font-bold">$19.99</p>
                  </div>

                  <button
                    type="submit"
                    className="w-full rounded bg-[#EDA415] px-6 py-3 text-sm font-bold uppercase tracking-wide text-white"
                  >
                    Add to cart
                  </button>

                  <button
                    type="button"
                    className="w-full rounded border border-gray-300 bg-gray-100 px-6 py-3 text-sm font-bold uppercase tracking-wide"
                  >
                    Add to favorites
                  </button>
                </form>
              </div>

              <div className="lg:col-span-3">
                <div className="prose max-w-none">
                  <p>
                    The MacBook Pro M1 is the latest addition to Apple's premium
                    laptop lineup, boasting impressive features and performance
                    that cater to professionals and power users. With its
                    cutting-edge M1 chip, this laptop delivers exceptional speed
                    and efficiency, allowing users to accomplish their tasks
                    with ease. The MacBook Pro M1 features a stunning Retina
                    display that offers exceptional color accuracy and contrast,
                    providing a truly immersive viewing experience. The laptop
                    also comes with a Touch Bar and Touch ID, enabling users to
                    access shortcuts and functions quickly and securely. This
                    MacBook Pro M1 is designed with professionals in mind,
                    providing powerful tools and applications for creative work
                    such as video editing, music production, and graphic design.
                    With up to 17 hours of battery life, this laptop can keep up
                    with the demands of the most intensive workloads, making it
                    an ideal choice for professionals on the go.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </section>
      <Review/>
      </Layout>
    </>
  );
};

export default ProductDetails;
