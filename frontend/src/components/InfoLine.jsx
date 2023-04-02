import { LocalShippingIcon, LocationOnIcon } from "../assets/index";
const InfoLine = () => {
  return (
    <>
      <header>
        <div className="container flex justify-between items-center px-4 py-4 bg-red-100 text-xs">
          <div>Need help?Call us:(+98) 0234 456 789</div>
          <div className="flex justify-center items-center px-2">
            <a href="/">
              <span>
                <LocationOnIcon />
              </span>
              Our Store
            </a>
            <span className="px-1">
              <LocalShippingIcon />
            </span>
            <a href="orders/">Track Your Order</a>
          </div>
        </div>
      </header>
    </>
  );
};

export default InfoLine;
