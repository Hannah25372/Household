import {LuArrowLeft, LuArrowRight} from "react-icons/lu"


function BillsTable() {
  return (
    <div className="table-container">
    <table className="data-table">
      <thead>
        <tr>
          <th>Expense</th>
          <th>Monthly Total</th>
          <th>User 1</th>
          <th>User 2</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Rent</td>
          <td>£1000</td>
          <td>£500 (50%)</td>
          <td>£500 (50%)</td>
        </tr>
        <tr>
          <td>Energy</td>
          <td>£100</td>
          <td>£50 (50%)</td>
          <td>£50 (50%)</td>
        </tr>
        <tr>
          <td>Water</td>
          <td>£30</td>
          <td>£15 (50%)</td>
          <td>£15 (50%)</td>
        </tr>
        <tr>
          <td>Council Tax</td>
          <td>£200</td>
          <td>£100 (50%)</td>
          <td>£100 (50%)</td>
        </tr>
        <tr>
          <td>Broadband</td>
          <td>£20</td>
          <td>£10 (50%)</td>
          <td>£10 (50%)</td>
        </tr>
        <tr>
          <td>Total</td>
          <td>£2700</td>
          <td>£1350 (50%)</td>
          <td>£1350 (50%)</td>
        </tr>
      </tbody>
    </table>
    </div>
  );
}



function Breakdown() {
  return (
    <div className="page-container">
      <h1>Monthly Breakdown</h1>

      <div className="months">
        <button><LuArrowLeft/></button>
        <h2> January 2026 </h2>
        <button><LuArrowRight/></button>
      </div>
      
      <div className="table-section">
        <BillsTable/>
      </div>

      <p>Edit this months amount</p>

    </div>
  );
}

export default Breakdown;