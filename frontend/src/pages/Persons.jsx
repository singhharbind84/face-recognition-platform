import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import api from "../services/api";

export default function Persons() {
  const [persons, setPersons] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadPersons();
  }, []);

  const loadPersons = async () => {
    try {
      const response = await api.get("/persons");
      setPersons(response.data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout>
      <h1>Registered Persons</h1>

      {loading ? (
        <p>Loading...</p>
      ) : persons.length === 0 ? (
        <p>No registered persons found.</p>
      ) : (
        <table
          border="1"
          cellPadding="10"
          style={{
            marginTop: "20px",
            borderCollapse: "collapse",
            width: "100%",
          }}
        >
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Image</th>
            </tr>
          </thead>

          <tbody>
            {persons.map((person) => (
              <tr key={person.id}>
                <td>{person.id}</td>
                <td>{person.name}</td>
                <td>
                  <img
                    src={`http://192.168.75.168:8000/${person.image}`}
                    width="100"
                    alt={person.name}
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </Layout>
  );
}
