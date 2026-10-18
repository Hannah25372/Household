import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import Breakdown from "./pages/Breakdown";
import Expenses from "./pages/Expenses";
import Users from "./pages/Users";
import Bills from "./pages/Bills";
import "./App.css";
import { LuSettings, LuInfo, LuUser } from "react-icons/lu";

function App() {
  return (
    <BrowserRouter>
      <nav className="navbar">
        <div className="nav-links">
          <Link to="/">Breakdown</Link>
          <Link to="/bills">Bills</Link>
          <Link to="/expenses">Expenses</Link>
          <Link to="/users">Users</Link>
        </div>
        <div className="nav-actions">
          <button><LuInfo/></button>
          <button><LuUser/></button>
          <button><LuSettings/></button>
        </div>
      </nav>

      <main>
        <Routes>
          <Route path="/" element={<Breakdown />} />
          <Route path="/bills" element={<Bills/>} />
          <Route path="/expenses" element={<Expenses />} />
          <Route path="/users" element={<Users />} />
        </Routes>
      </main>
    </BrowserRouter>
  );
}

export default App;
