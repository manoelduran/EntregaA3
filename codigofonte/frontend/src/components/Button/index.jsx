import React from 'react';
import './styles.css';

const Button = ({ onClick, title, color }) => {
  return (
    <button style={{backgroundColor: `${color}`}} className='custom-button' onClick={onClick}>
      {title}
    </button>
  );
};

export default Button;