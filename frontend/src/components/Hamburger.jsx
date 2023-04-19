import MenuIcon from "@mui/icons-material/Menu";
import CloseIcon from "@mui/icons-material/Close";
import { Link } from "@mui/material";
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
          className="block lg:hidden text-white focus:outline-none mr-4"
          onClick={() => setShowMenu(!showMenu)}
        >
          {showMenu ? "Close" : <MenuIcon />}
        </button>
        <div
          className={`${
            showMenu ? "block" : "hidden"
          } lg:hidden absolute top-0 left-0 h-full`}
        >
          <div className="absolute top-0 left-0 w-56 h-full bg-stone-200">
            <div className="absolute top-0 right-0">
              <button
                type="button"
                className="block text-black font-bold py-2 px-4 hover:bg-[#003F62] focus:outline-none"
                onClick={closeMenu}
              >
                <CloseIcon />
              </button>
            </div>
            <div className="absolute top-0 left-0 h-full overflow-y-auto px-4 py-8">
              <nav className="mb-4">
                <ul>
                  <li>
                    <Link
                      to="/register"
                      className="block no-underline px-4 py-2 text-black font-bold hover:bg-[#003F62]"
                      onClick={closeMenu}
                    >
                      Login
                    </Link>
                  </li>
                  <li>
                    <Link
                      to="/products"
                      className="block px-4 py-2 text-black font-bold hover:bg-[#003F62]"
                      onClick={closeMenu}
                    >
                      Home
                    </Link>
                  </li>
                  <li>
                    <Link
                      to="/"
                      className="block px-4 py-2 text-black font-bold hover:bg-[#003F62]"
                      onClick={closeMenu}
                    >
                      Products
                    </Link>
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
