import {Link} from 'react-router-dom'
import { Laptop } from '../assets';

const Anounce = () => {
  return (
    <>
      <section className="relative bg-hero-pattern bg-cover bg-center bg-no-repeat rounded-3xl mx-14 my-10">
        <div className="absolute inset-0  sm:from-white/95 sm:to-white/25 ltr:sm:bg-gradient-to-r rtl:sm:bg-gradient-to-l"></div>

        <div className="relative mx-auto max-w-screen-xl px-4 py-32 sm:px-6 lg:flex lg:h-screen lg:items-center lg:px-8">
          <div className="max-w-xl text-center ltr:sm:text-left rtl:sm:text-right">
            <h1 className="text-3xl font-extrabold sm:text-5xl text-[#2E8FC5]">
              Sale up to 50% off
              <strong className="mt-4 block font-normal text-white">
                15,6 Inch hd display
              </strong>
            </h1>


            <div className="mt-8 flex flex-wrap gap-4 text-center">
              <Link
                to="#"
                className="block w-full rounded-2xl bg-[#EDA415] px-12 py-3 text-sm font-medium text-white shadow hover:text-black hover:bg-white focus:outline-none focus:ring active:text-[#1B5A7D] sm:w-auto"
              >
                View offre
              </Link>

              <Link
                to="#"
                className="block w-full rounded-2xl bg-[#EDA415] px-12 py-3 text-sm font-medium text-white shadow hover:text-black hover:bg-white focus:outline-none focus:ring active:text-[#1B5A7D] sm:w-auto"
              >
                Shop now
              </Link>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Anounce;
