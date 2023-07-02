import React from "react";
import "./Dashboard.css";

function Dashboard() {
  return (
    <div className="dashboard">
      <div className="row">
        <div className="tile">
          <div className="tile-content">Siksha</div>
        </div>
        <div className="tile">
          <div className="tile-content">Udaan</div>
        </div>
      </div>
      <div className="row">
        <div className="tile">
          <div className="tile-content">Vridhi</div>
        </div>
        <div className="tile">
          <div className="tile-content">EmpowHer</div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
