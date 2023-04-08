const Features = ()=>{
  return (
    <section className="px-10 py-16 mb-8 flex flex-wrap justify-evenly items-center bg-[#E2F4FF] rounded-3xl">
      <div className="grid grid-cols-2  md:grid-cols-4">
        <div className="text-center md:border-r">
          <h6 className="text-2xl font-bold text-[#EDA415] ">Free delivery</h6>
          <p className="text-sm font-medium tracking-widest text-gray-800 uppercase lg:text-base">
            On Order above 100$
          </p>
        </div>
        <div className="text-center md:border-r">
          <h6 className="text-2xl font-bold text-[#EDA415] ">Best Quality</h6>
          <p className="text-sm font-medium tracking-widest text-gray-800 uppercase lg:text-base">
            Best quality in low price
          </p>
        </div>
        <div className="text-center md:border-r">
          <h6 className="text-2xl font-bold text-[#EDA415]">1 year warranty</h6>
          <p className="text-sm font-medium tracking-widest text-gray-800 uppercase lg:text-base">
            Avaliable warranty
          </p>
        </div>
        <div className="text-center">
          <h6 className="text-2xl font-bold text-[#EDA415]">Customer Service</h6>
          <p className="text-sm font-medium tracking-widest text-gray-800 uppercase lg:text-base">
            Our customer service Avaliable 24/24 | 7/7
          </p>
        </div>
      </div>
    </section>
  );
};
export default Features