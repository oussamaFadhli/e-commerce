import { brand4,brand5,brand6,brand7,brand8 } from "../assets";
const Sponsors = () => {
  return (
    <>
      <section className="bg-[#E2F4FF] my-7">
        <div className="py-5 lg:py-16 mx-auto max-w-screen-xl px-4">
          <h2 className="mb-8 lg:mb-16  text-3xl font-extrabold tracking-tight leading-tight text-center text-gray-900">
            Our Sponsors
          </h2>
          <div className="grid grid-cols-2 gap-8 text-gray-500 sm:gap-12 md:grid-cols-3 lg:grid-cols-6 ">
            <img src={brand4} className="h-9 " />
            <img src={brand5} className="h-9 " />
            <img src={brand8} className="h-9 " />
            <img src={brand6} className="h-9 " />
            <img src={brand7} className="h-9 " />
            <img src={brand8} className="h-9 " />
          </div>
        </div>
      </section>
    </>
  );
};

export default Sponsors;
