function ColorPicker({ color }) {
  // TODO: set color using react state
  const handleColorChange = (e) => {}

  return (
    <div className="color-field" style={{ backgroundColor: color }}>
      <input type="color" value={color} onChange={handleColorChange} />
    </div>
  )
}
export default ColorPicker
