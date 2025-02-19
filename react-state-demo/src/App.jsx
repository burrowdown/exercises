import { useState } from "react"
import "./App.css"
import ColorPicker from "./components/ColorPicker"

function App() {
  console.log("App component rendering now")

  const [_, forceRender] = useState()
  const [count, setCount] = useState(0)

  return (
    <>
      <ColorPicker initColor="red" />
      <ColorPicker initColor="blue" />
      <ColorPicker initColor="green" />

      <button onClick={() => setCount((count) => count + 1)}>
        count is {count}
      </button>

      <button onClick={forceRender}>reset</button>
    </>
  )
}

export default App
