import { LogoShop } from "../assets"

const NavBar = () => {
  return (
    <>
      <nav className='w-full h-24 bg-[#003F62] flex justify-center items-center gap-80 flex-row'>
        <div>
          <img src={LogoShop} alt="logo"/>
        </div>
        <div className="flex flex-row items-center pb-6 gap-2 isolate w-80 h-14 bg-[#FFFFFF]
        rounded-xl ">
          <input
          type="search"
          placeholder="Search any things..."
          className="flex-none order-1 grow-0"/>
        </div>

      </nav>
    </>
  )
}

export default NavBar