import { useEffect, useState } from "react"

function App() {
  const [users, setUsers] = useState([])
  const [loading, setLoading] = useState(false)
  useEffect(() => {
    setLoading(true)
    fetch("http://172.20.10.3:5050/api/mapping/automap")
      .then(response => response.json())
      .then(json => setUsers(json))
      .finally(() => {
        setLoading(false)
      })
  }, [])

  return (
    <div className="App">
      {loading ? (
        <div>Loading...</div>
      ) : (
        <>
          <h1>Users</h1>
          <table border={1}>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Phone</th>
            </tr>
            {users.map(user => (
              <tr key={user.id}>
                <td>{user.mentor_id}</td>
                <td>{user.mentee_id}</td>
                <td>{user.project_id}</td>
                <td>{user.mentor_name}</td>
                <td>{user.mentee_name}</td>
                <td>{user.common_languages}</td>
              </tr>
            ))}
          </table>
        </>
      )}
    </div>
  )
}

export default App
