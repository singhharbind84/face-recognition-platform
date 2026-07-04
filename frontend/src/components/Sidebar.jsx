import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <div
      style={{
        width: "220px",
        background: "#1e293b",
        color: "white",
        minHeight: "100vh",
        padding: "20px",
      }}
    >
      <h2>Face AI</h2>

      <hr />

      <p><Link to="/">Dashboard</Link></p>
      <p><Link to="/register">Register</Link></p>
      <p><Link to="/recognition">Recognition</Link></p>
      <p><Link to="/attendance">Attendance</Link></p>
      <p><Link to="/persons">Persons</Link></p>
    </div>
  );
}
