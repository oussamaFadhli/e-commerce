import MenuIcon from "@mui/icons-material/Menu";
import CloseIcon from "@mui/icons-material/Close";
import React from "react";
import { useState } from "react";

const Hamburger = () => {
  const [showMenu, setShowMenu] = useState(false);

  const closeMenu = () => {
    setShowMenu(false);
  };

  return (
    <>
        <button
          type="button"
          className="block xl:hidden text-white focus:outline-none mr-4"
          onClick={() => setShowMenu(!showMenu)}
        >
          {showMenu ? "Close" : <MenuIcon />}
        </button>
        <div
          className={`${
            showMenu ? "block" : "hidden"
          } xl:hidden absolute top-0 left-0 h-full`}
        >
          <div className="absolute top-0 left-0 w-56 h-full bg-stone-100">
            <div className="absolute top-0 right-0">
              <button
                type="button"
                className="block text-black font-bold py-2 px-4 hover:bg-gray-800 focus:outline-none"
                onClick={closeMenu}
              >
                <CloseIcon />
              </button>
            </div>
            <div className="absolute top-0 left-0 h-full overflow-y-auto px-4 py-8">
              <nav className="mb-4">
                <ul>
                  <li>
                    <a
                      href="#"
                      className="block px-4 py-2 text-black font-bold hover:bg-gray-800"
                      onClick={closeMenu}
                    >
                      Home
                    </a>
                  </li>
                  <li>
                    <a
                      href="#"
                      className="block px-4 py-2 text-black font-bold hover:bg-gray-800"
                      onClick={closeMenu}
                    >
                      About
                    </a>
                  </li>
                  <li>
                    <a
                      href="#"
                      className="block px-4 py-2 text-black font-bold hover:bg-gray-800"
                      onClick={closeMenu}
                    >
                      Contact
                    </a>
                  </li>
                </ul>
              </nav>
            </div>
          </div>
        </div>
    </>
  );
};

export default Hamburger;
