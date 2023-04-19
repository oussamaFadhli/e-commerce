import { useState } from "react";
import { Registerimg, LogoShop } from "../assets";
import { Link } from "react-router-dom";
const Register = () => {
  const [firstName, setFirstName] = useState("");
  const [isFirstNameValid, setIsFirstNameValid] = useState(true);
  const [lastName, setLastName] = useState("");
  const [isLastNameValid, setIsLastNameValid] = useState(true);
  const [country, setCountry] = useState("");
  const [isCountryValid, setIsCountryValid] = useState(true);
  const [city, setCity] = useState("");
  const [isCityValid, setIsCityValid] = useState(true);
  const [email, setEmail] = useState("");
  const [isEmailValid, setIsEmailValid] = useState(true);
  const [password, setPassword] = useState("");
  const [isValid, setIsValid] = useState(false);
  const [confPassword, setConfPassword] = useState("");
  const [isConfValid, setIsConfValid] = useState(false);

  const handleFirstNameChange = (e) => {
    const { value } = e.target;
    setFirstName(value);
    setIsFirstNameValid(true);
  };

  const handleFirstNameBlur = (e) => {
    const { value } = e.target;
    setIsFirstNameValid(value !== "");
  };

  const handleLastNameChange = (e) => {
    const { value } = e.target;
    setLastName(value);
    setIsLastNameValid(true);
  };

  const handleLastNameBlur = (e) => {
    const { value } = e.target;
    setIsLastNameValid(value !== "");
  };

  const handleCountryChange = (e) => {
    const { value } = e.target;
    setCountry(value);
    setIsCountryValid(true);
  };

  const handleCountryBlur = (e) => {
    const { value } = e.target;
    setIsCountryValid(value !== "");
  };

  const handleCityChange = (e) => {
    const { value } = e.target;
    setCity(value);
    setIsCityValid(true);
  };

  const handleCityBlur = (e) => {
    const { value } = e.target;
    setIsCityValid(value !== "");
  };

  const handleEmailChange = (e) => {
    const { value } = e.target;
    setEmail(value);
    setIsEmailValid(true);
  };

  const handleEmailBlur = (e) => {
    const { value } = e.target;
    const emailRegex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i;
    setIsEmailValid(emailRegex.test(value));
  };

  const validatePassword = (password) => {
    const regex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    return regex.test(password);
  };

  const handleChangePassword = (e) => {
    const { value } = e.target;
    setPassword(value);
    setIsValid(validatePassword(value));
  };
  const handleChangeConfPassword = (e) => {
    const { value } = e.target;
    setConfPassword(value);
    setIsConfValid(value === password);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Submited.");
    setFirstName('')
    setLastName('')
    setCountry('')
    setCity('')
    setEmail('')
    setPassword('')
    setConfPassword('')
  };
  return (
    <>
      <section className="bg-white">
        <div className="lg:grid lg:min-h-screen lg:grid-cols-12">
          <aside className="relative block h-16 lg:order-last lg:col-span-5 lg:h-full xl:col-span-6">
            <img
              src={Registerimg}
              alt="register-img"
              className="absolute inset-0 h-full w-full object-cover min-[320px]:max-[768px]:hidden"
            />
          </aside>

          <main
            aria-label="Main"
            className="flex items-center justify-center px-8 py-8 sm:px-12 lg:col-span-7 lg:px-16 lg:py-12 xl:col-span-6"
          >
            <div className="max-w-xl lg:max-w-3xl">
              <Link className="block text-[#003F62]" to="/">
                <span className="sr-only">Home</span>
                <img
                  src={LogoShop}
                  className="bg-[#003F62] p-2 rounded-2xl"
                  alt="logo"
                />
              </Link>

              <h1 className="mt-6 text-2xl font-bold text-gray-900 sm:text-3xl md:text-4xl">
                Welcome to Electon👋
              </h1>

              <p className="mt-4 leading-relaxed text-gray-500">
                Electon offers a comprehensive selection of computers, laptops,
                tablets, and accessories, from leading brands in the industry.
                Whether you are a student, a professional, or a gaming
                enthusiast, we have the perfect device to meet your needs.
              </p>
              <form
                onSubmit={handleSubmit}
                className="mt-8 grid grid-cols-6 gap-6"
              >
                <div className="col-span-6 sm:col-span-3">
                  <label
                    htmlFor="FirstName"
                    className="block text-sm font-medium text-gray-700"
                  >
                    First Name<span className="text-[#FF0000]">*</span>
                  </label>

                  <input
                    type="text"
                    id="FirstName"
                    name="first_name"
                    value={firstName}
                    onChange={handleFirstNameChange}
                    onBlur={handleFirstNameBlur}
                    required
                    className="mt-1 p-2 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
                  />
                  {!isFirstNameValid && (
                    <p className="text-red-500 mt-2">
                      Please enter your first name.
                    </p>
                  )}
                  <label
                    htmlFor="Country"
                    className="block text-sm font-medium text-gray-700"
                  >
                    Country<span className="text-[#FF0000]">*</span>
                  </label>

                  <input
                    type="text"
                    id="Country"
                    name="Country"
                    value={country}
                    onChange={handleCountryChange}
                    onBlur={handleCountryBlur}
                    required
                    className="mt-1 p-2 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
                  />
                  {!isCountryValid && (
                    <p className="text-red-500 mt-2">
                      Please enter your country.
                    </p>
                  )}
                </div>

                <div className="col-span-6 sm:col-span-3">
                  <label
                    htmlFor="LastName"
                    className="block text-sm font-medium text-gray-700"
                  >
                    Last Name<span className="text-[#FF0000]">*</span>
                  </label>

                  <input
                    type="text"
                    id="LastName"
                    name="last_name"
                    value={lastName}
                    onChange={handleLastNameChange}
                    onBlur={handleLastNameBlur}
                    required
                    className="mt-1 p-2 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
                  />
                  {!isLastNameValid && (
                    <p className="text-red-500 mt-2">
                      Please enter your last name.
                    </p>
                  )}
                  <label
                    htmlFor="City"
                    className="block text-sm font-medium text-gray-700"
                  >
                    City<span className="text-[#FF0000]">*</span>
                  </label>

                  <input
                    type="text"
                    id="City"
                    name="city"
                    value={city}
                    onChange={handleCityChange}
                    onBlur={handleCityBlur}
                    required
                    className="mt-1 p-2 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
                  />
                  {!isCityValid && (
                    <p className="text-red-500 mt-2">Please enter your city.</p>
                  )}
                </div>

                <div className="col-span-6">
                  <label
                    htmlFor="Email"
                    className="block text-sm font-medium text-gray-700"
                  >
                    Email<span className="text-[#FF0000]">*</span>
                  </label>

                  <input
                    type="email"
                    id="Email"
                    name="email"
                    value={email}
                    onChange={handleEmailChange}
                    onBlur={handleEmailBlur}
                    required
                    className="mt-1 p-2 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
                  />
                  {!isEmailValid && (
                    <p className="text-red-500 mt-2">
                      Please enter a valid email address.
                    </p>
                  )}
                </div>

                <div className="col-span-6 sm:col-span-3">
                  <label
                    htmlFor="Password"
                    className="block text-sm font-medium text-gray-700"
                  >
                    Password<span className="text-[#FF0000]">*</span>
                  </label>

                  <input
                    type="password"
                    id="password"
                    name="Password"
                    value={password}
                    onChange={handleChangePassword}
                    required
                    className="mt-1 p-2 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
                  />
                  {!isValid && password.length > 0 && (
                    <p className="text-red-500 mt-2">
                      Password must contain at least one letter and one number,
                      and be at least 8 characters long.
                    </p>
                  )}
                </div>

                <div className="col-span-6 sm:col-span-3">
                  <label
                    htmlFor="PasswordConfirmation"
                    className="block text-sm font-medium text-gray-700"
                  >
                    Password Confirmation
                    <span className="text-[#FF0000]">*</span>
                  </label>

                  <input
                    type="password"
                    id="PasswordConfirmation"
                    name="password_confirmation"
                    value={confPassword}
                    onChange={handleChangeConfPassword}
                    required
                    className="mt-1 p-2 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
                  />
                  {!isConfValid && confPassword.length > 0 && (
                    <p className="text-red-500 mt-2">Passwords do not match.</p>
                  )}
                </div>

                <div className="col-span-6">
                  <label htmlFor="MarketingAccept" className="flex gap-4">
                    <input
                      type="checkbox"
                      id="MarketingAccept"
                      name="marketing_accept"
                      className="h-5 w-5 p-2 rounded-md border-gray-200 bg-white shadow-sm"
                    />

                    <span className="text-sm text-gray-700">
                      I want to receive emails about events, product updates and
                      company announcements.
                    </span>
                  </label>
                </div>

                <div className="col-span-6">
                  <p className="text-sm text-gray-500">
                    By creating an account, you agree to our
                    <Link to="#" className="text-gray-700 underline">
                      terms and conditions
                    </Link>
                    and
                    <Link to="#" className="text-gray-700 underline">
                      privacy policy
                    </Link>
                    .
                  </p>
                </div>

                <div className="col-span-6 sm:flex sm:items-center sm:gap-4">
                  <button
                    type="submit"
                    className="inline-block shrink-0 rounded-md border border-blue-600 bg-blue-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-transparent hover:text-blue-600 focus:outline-none focus:ring active:text-blue-500"
                  >
                    Create an account
                  </button>

                  <p className="mt-4 text-sm text-gray-500 sm:mt-0">
                    Already have an account?
                    <Link to="/login" className="text-gray-700 underline">
                      Log in
                    </Link>
                    .
                  </p>
                </div>
              </form>
            </div>
          </main>
        </div>
      </section>
    </>
  );
};

export default Register;
