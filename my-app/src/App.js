import React from "react";
import ReactDOM from "react-dom";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedQueryId: "no query",
      query1: "query1",
      query2: "query2",
      query3: "query3",
      query4: "query4",
      query5: "query5",
      query6: "query6",
      query7: "query7",
      query8: "query8",
      query9: "query9",
      query10: "query10",
      query11: "query11",
    };

    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    alert("Your query id is: " + this.state.selectedQueryId);
    event.preventDefault();
  }

  handleChange = (event) => {
    this.setState({ selectedQueryId: event.target.value });
  };

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Please pick your query:
          <select
            value={this.state.selectedQueryId}
            onChange={this.handleChange}
          >
            <option value="q1">{this.state.query1}</option>
            <option value="q2">{this.state.query2}</option>
            <option value="q3">{this.state.query3}</option>
            <option value="q4">{this.state.query4}</option>
            <option value="q5">{this.state.query5}</option>
            <option value="q6">{this.state.query6}</option>
            <option value="q7">{this.state.query7}</option>
            <option value="q8">{this.state.query8}</option>
            <option value="q9">{this.state.query9}</option>
            <option value="q10">{this.state.query10}</option>
            <option value="q11">{this.state.query11}</option>
          </select>
        </label>
        <input type="submit" value="Submit Query" />
      </form>
    );
  }
}

/* export the component to be used in other components */
export default App;
