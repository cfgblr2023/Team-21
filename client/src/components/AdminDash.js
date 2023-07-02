import React, { useState, useEffect } from "react";

function AdminDash() {
  const url = "http://172.20.10.3:5050/api/auth/register/mentee";
  const [data, setData] = useState([]);

  const fetchInfo = () => {
    return fetch(url)
      .then((res) => res.json())
      .then((d) => setData(d));
  };

  useEffect(() => {
    fetchInfo();
  }, []);

  return (
    <div className="AdminDash">
      <h1>using JavaScript inbuilt FETCH API</h1>
      <center>
        {data.map((dataObj, index) => {
          return (
            <div
              style={{
                width: "15em",
                backgroundColor: "#35D841",
                padding: 2,
                borderRadius: 10,
                marginBlock: 10,
              }}
            >
              <p>{dataObj.name}</p>
            </div>
          );
        })}
      </center>
    </div>
  );
}

export default AdminDash;
