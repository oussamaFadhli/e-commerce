import React from 'react'

const SubcategoriesLayout = ({children}) => {
  return (
    <section className='flex flex-wrap justify-around'>
        {children}
    </section>
  )
}

export default SubcategoriesLayout