import React from "react";

const CustomInput = (props) => {
  return (
    <>
      <div className="w-32">
        <label
          htmlFor={props.id}
          className="relative block overflow-hidden rounded-md border border-gray-200 px-3 pt-3 shadow-sm focus-within:border-dark focus-within:ring-1 focus-within:ring-dark"
        >
          <input
            type="text"
            id={props.id}
            placeholder={props.placeholder}
            minLength={0}
            className="peer border-none bg-transparent p-2 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm"
          />

          <span className="absolute start-3 top-3 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-3 peer-focus:text-xs">
            {props.placeholder}
          </span>
        </label>
      </div>
    </>
  );
};

export default CustomInput;
