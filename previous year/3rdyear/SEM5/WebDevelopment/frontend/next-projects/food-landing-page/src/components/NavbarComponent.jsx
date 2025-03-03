import React from 'react'

function NavbarComponent() {
  return (
    <div>
        <h1>My Food Landing Page</h1>
      <nav>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#menu">Menu</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
        <div className="search-container">
          <input type="text" placeholder="Search.."/>
        </div>
    
        <div className="language-selector">
            <select>
              <option value="en">English</option>
              <option value="fr">Français</option>
              <option value="es">Español</option>
            </select>
        </div>
      </nav>
    </div>
  )
}

export default NavbarComponent