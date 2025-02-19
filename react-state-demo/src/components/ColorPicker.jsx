import { useState } from "react"

function ColorPicker({ initColor }) {
  const [color, setColor] = useState(initColor)
  const handleColorChange = (e) => {
    setColor((color) => e.target.value)
  }

  return (
    <div className="color-field" style={{ backgroundColor: color }}>
      <input type="color" value={color} onChange={handleColorChange} />
    </div>
  )
}
export default ColorPicker
