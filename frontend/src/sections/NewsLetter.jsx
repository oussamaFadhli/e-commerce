const NewsLetter = () => {
  return (
    <>
      <section className="bg-secondary-100 text-center bg-[#E2F4FF]">
        <div className="px-6 pt-6">
          <form action="#">
            <div className="gird-cols-1 grid items-center justify-center gap-4 md:grid-cols-3">
              <div className="md:ml-auto md:mb-6">
                <p className="text-2xl dark:text-secondary-200 text-[#1B5A7D]">
                  <strong>Sign up for our newsletter</strong>
                </p>
              </div>

              <div className="relative md:mb-6 border rounded-xl">
                <input
                  type="email"
                  className="peer block min-h-[auto] w-full rounded border-0 bg-transparent py-[0.32rem] px-3 leading-[1.6] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 data-[te-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:placeholder:text-secondary-200 [&:not([data-te-input-placeholder-active])]:placeholder:opacity-0"
                  id="Subscribe-NewsLetter"
                  placeholder="Email address"
                />
                <label
                  htmlFor="Subscribe-NewsLetter"
                  className="pointer-events-none absolute top-0 left-3 mb-0 max-w-[90%] origin-[0_0] truncate pt-[0.37rem] leading-[1.6] text-secondary-500 transition-all duration-200 ease-out peer-focus:-translate-y-[0.9rem] peer-focus:scale-[0.8] black-focus:text-blue-600 peer-data-[te-input-state-active]:-translate-y-[0.9rem] peer-data-[te-input-state-active]:scale-[0.8] motion-reduce:transition-none dark:text-secondary-200 dark:peer-focus:text-secondary-200"
                >
                  Email address
                </label>
              </div>

              <div className="mb-6 md:mr-auto">
                <button
                  className="group flex items-center justify-between gap-4 rounded-lg border border-current px-3 py-1 text-black transition-colors hover:bg-[#EDA415] focus:outline-none focus:ring active:bg-[#1B5A7D]"
                  type="submit"
                >
                  <span className="font-medium transition-colors group-hover:text-white">
                    Subscribe
                  </span>
                </button>
              </div>
            </div>
          </form>
        </div>
      </section>
    </>
  );
};

export default NewsLetter;
