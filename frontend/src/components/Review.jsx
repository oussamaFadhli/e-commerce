import React from "react";

const Review = () => {
  return (
    <>
      <section>
        <form>
          <div className="w-full mb-4 border border-gray-200 rounded-lg bg-gray-50">
            <div className="px-4 py-2 bg-white rounded-t-lg">
              <label htmlFor="comment" className="sr-only">
                Your comment
              </label>
              <textarea
                id="comment"
                rows="4"
                className="w-full px-2 py-4 text-sm text-gray-900 bg-white border-0  focus:ring-0"
                placeholder="Write a comment..."
                required
              ></textarea>
            </div>
            <div className="flex items-center justify-end px-3 py-2 border-t ">
              <button
                type="submit"
                className="inline-flex items-center py-2.5 px-4 text-xs font-medium text-center border-2 text-white bg-[#003F62] rounded-lg focus:ring-4 focus:ring-blue-200  hover:bg-white hover:text-black hover:ease-in duration-200"
              >
                Post comment
              </button>
            </div>
          </div>
        </form>
      </section>
    </>
  );
};

export default Review;
