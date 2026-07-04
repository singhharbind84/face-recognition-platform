import { useState } from "react";
import api from "../services/api";
import Layout from "../components/Layout";

export default function Register() {
  const [name, setName] = useState("");
  const [image, setImage] = useState(null);
  const [message, setMessage] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();

    if (!name || !image) {
      setMessage("Please enter name and select an image.");
      return;
    }

    const formData = new FormData();

    formData.append("name", name);
    formData.append("image", image);

    try {
      const res = await api.post("/register", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setMessage(res.data.message);

      setName("");
      setImage(null);

      document.getElementById("image").value = "";
    } catch (err) {
      setMessage(
        err.response?.data?.detail || "Registration failed."
      );
    }
  };

  return (
    <Layout>
      <h1>Register Person</h1>

      <form onSubmit={handleRegister}>

        <div style={{ marginTop: 20 }}>
          <label>Name</label>

          <br />

          <input
            value={name}
            onChange={(e) => setName(e.target.value)}
            style={{ width: 300, padding: 8 }}
          />
        </div>

        <div style={{ marginTop: 20 }}>
          <label>Photo</label>

          <br />

          <input
            id="image"
            type="file"
            accept="image/*"
            onChange={(e) => setImage(e.target.files[0])}
          />
        </div>

        <button
          style={{
            marginTop: 20,
            padding: "10px 25px",
          }}
        >
          Register
        </button>

      </form>

      <h3>{message}</h3>

    </Layout>
  );
}
