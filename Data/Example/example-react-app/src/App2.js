import React, { Component } from "react";
import Select from "react-select";

import "./App.css";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedOption: "",
      queryList: [
        { queryID: "q1", queryLabel: "query1" },
        { queryID: "q2", queryLabel: "query2" },
        { queryID: "q3", queryLabel: "query3" },
        { queryID: "q4", queryLabel: "query4" },
        { queryID: "q5", queryLabel: "query5" },
        { queryID: "q6", queryLabel: "query6" },
        { queryID: "q7", queryLabel: "query7" },
        { queryID: "q8", queryLabel: "query8" },
        { queryID: "q9", queryLabel: "query9" },
        { queryID: "q10", queryLabel: "query10" },
        { queryID: "q11", queryLabel: "query11" },
      ],
    };
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    alert("Your query: " + this.state.value);
    event.preventDefault();
  }

  handleChange = (event) => {
    this.setState({ value: event.target.value });
  };

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <br />
        <br />
        <label>
          Looping through Array
          <select value={this.state.key} onChange={this.handleChange}>
            {this.state.queryList.map((item) => (
              <option key={item.queryID} value={item.queryLabel}>
                {item.queryLabel}
              </option>
            ))}
          </select>
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

/* export the component to be used in other components */
export default App;
