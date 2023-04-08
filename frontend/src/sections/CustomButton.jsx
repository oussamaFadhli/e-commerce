import React from 'react'

const CustomButton = (props) => {
  return (
    <button type={props.type} className={props.ButtonStyle}>{props.ButtonTitle}</button>
  )
}

export default CustomButton