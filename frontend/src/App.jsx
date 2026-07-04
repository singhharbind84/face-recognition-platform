import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Register from "./pages/Register";
import Recognition from "./pages/Recognition";
import Attendance from "./pages/Attendance";
import Persons from "./pages/Persons";

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Dashboard />} />

        <Route path="/register" element={<Register />} />

        <Route path="/recognition" element={<Recognition />} />

        <Route path="/attendance" element={<Attendance />} />

        <Route path="/persons" element={<Persons />} />

      </Routes>

    </BrowserRouter>

  );

}

export default App;
