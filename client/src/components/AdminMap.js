import React, { useEffect, useState } from 'react';

function App() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    fetch("http://172.20.10.3:5050/api/mapping/automap")
      .then(response => response.json())
      .then(json => setUsers(json.mapping))
      .catch(error => console.log(error))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="App">
      {loading ? (
        <div>Loading...</div>
      ) : (
        <>
          <h1>Users</h1>
          <table border={1}>
            <tbody>
              <tr>
                <th>Mentor ID</th>
                <th>Mentee ID</th>
                <th>Project ID</th>
                <th>Mentor Name</th>
                <th>Mentee Name</th>
                <th>Common Languages</th>
              </tr>
              {users.map((user, index) => (
                <tr key={index}>
                  <td>{user.mentor_id}</td>
                  <td>{user.mentee_id}</td>
                  <td>{user.project_id}</td>
                  <td>{user.mentor_name}</td>
                  <td>{user.mentee_name}</td>
                  <td>{user.common_languages.join(', ')}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      )}
    </div>
  );
}

export default App;
