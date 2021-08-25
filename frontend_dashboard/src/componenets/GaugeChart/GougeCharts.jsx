import React from 'react';
import './GaugeChart.css'
import HelpOutlineOutlinedIcon from '@material-ui/icons/HelpOutline'
import GaugeChart from "react-gauge-chart";
import { Component } from 'react'
import axios from 'axios'
export default class GougeCharts extends Component {
  constructor(props) {
    super(props);
    this.state = {
      bmi: '0',
      Limit_totalList: [],

    }
    this.handleSelectOptions = this.handleSelectOptions.bind(this);
  }

  componentDidMount() {
    this.refreshList();

  }
  refreshList = () => {
    axios   //Axios to send and receive HTTP requests
      .get("http://127.0.0.1:8000/api/Limits_total/")
      .then(res => this.setState({ Limit_totalList: res.data }))
      .catch(err => console.log(err));
  };

  handleSelectOptions(e) {
    this.setState({ bmi: e.target.value });
  }
  renderItems = () => {
    const newItems = this.state.Limit_totalList;
    return newItems.map(item => (

      <select name="" id="" className="selectItem" onChange={this.handleSelectOptions} >
        <option value={item.CE}>CE</option>
        <option value={item.EEPE}>EEPE</option>
        <option value={item.CVA}>CVA</option>
        <option value={item.DVA}>DVA</option>
        <option value={item.FCA}>FCA</option>
        <option value={item.FBA}>FBA</option>
        <option value={item.FVA}>FVA</option>
      </select>

    ));
  };
  gageCalc = bmi => {
    var result = 0;
    if (bmi >= 7000 && bmi <= 700000) {
      result = this.getPercentage(70000, 70000, 0.11);
    } else if (bmi > 70000 && this.state.bmi < 7000000) {
      result = this.getPercentage(70000, 7000000, 0.33);
    } else if (bmi >= 7000000 && this.state.bmi <= 70000000) {
      result = this.getPercentage(700000, 700000000, 0.66);
    }
    return result;
  };

  getPercentage(lowerBound, upperBound, segmentAdjustment) {
    return (
      (this.state.bmi - lowerBound) / (upperBound - lowerBound) / 3 + segmentAdjustment
    );
  }
  render() {
    return (
      <div className="gaugechart">
        <div className="subnavbar">
          <span className="titlePichart">Gauge Risk</span>
          <HelpOutlineOutlinedIcon className="helpIcon" />
          {this.renderItems()}
          <hr className="Separtormini" />
        </div>
        <GaugeChart
          id="gauge-chart"
          textColor="#000"
          cornerRadius={3}
          marginInPercent={0.015}
          arcWidth={0.3}
          arcPadding={0.01}
          percent={this.gageCalc(this.state.bmi)}
          nrOfLevels={6}
          colors={["#B5D4A8", "#B5D4A8", "#f4c57d", "#f4c57d", "#ED9780", "#ED9780"]}
        />
      </div>
    )
  }
}


// export default function GaugeCharts() {
//   const [bmi, setBmi] = React.useState(0);

//   const handleChangeBmi = event => setBmi(event.target.value);

//   const gageCalc = bmi => {
//     var result = 0;
//     if (bmi >= 16 && bmi <= 18.5) {
//       result = getPercentage(bmi, 16, 18.5, 0);
//     } else if (bmi > 18.5 && bmi < 25) {
//       result = getPercentage(bmi, 18.5, 25, 0.33);
//     } else if (bmi >= 25 && bmi <= 30) {
//       result = getPercentage(bmi, 25, 30, 0.66);
//     }
//     return result;
//   };

//   function getPercentage(bmi, lowerBound, upperBound, segmentAdjustment) {
//     return (
//       (bmi - lowerBound) / (upperBound - lowerBound) / 3 + segmentAdjustment
//     );
//   }

//   return (

//   );
// }
