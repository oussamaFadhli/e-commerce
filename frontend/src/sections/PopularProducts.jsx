import {CustomButton} from '../components'
const PopularProducts = ({ children }) => {
  return (
    <>
      <section className="pb-3">
        <div className="flex justify-between items-center flex-wrap ">
          <h1 className=" text-3xl text-[#1B5A7D] pb-5 px-7 font-bold">
            Popular Products
          </h1>
          <div className="space-x-10 mr-7 mb-7">
            <CustomButton type='submit' ButtonTitle='Cameras' ButtonStyle="py-2 px-4 mb-2 border-[#1B5A7D] text-[#1B5A7D] bg-transparent rounded-3xl border hover:bg-stone-200 ease-in duration-300" />
            <CustomButton type='submit' ButtonTitle='Laptops' ButtonStyle="p-2 px-4 mb-2 border-[#1B5A7D] text-[#1B5A7D] bg-transparent rounded-3xl border hover:bg-stone-200 ease-in duration-300 " />
            <CustomButton type='submit' ButtonTitle='Tablets' ButtonStyle="p-2 px-4 mb-2 border-[#1B5A7D] text-[#1B5A7D] bg-transparent rounded-3xl border hover:bg-stone-200 ease-in duration-300" />
            <CustomButton type='submit' ButtonTitle='Mouse' ButtonStyle="p-2 px-4 mb-2 border-[#1B5A7D] text-[#1B5A7D] bg-transparent rounded-3xl border hover:bg-stone-200 ease-in duration-300" />
          </div>
        </div>
        <div className="flex flex-wrap justify-around space-x-5">
          {children}
        </div>
      </section>
    </>
  );
};

export default PopularProducts;
