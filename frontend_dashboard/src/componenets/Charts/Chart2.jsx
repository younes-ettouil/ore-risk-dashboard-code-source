import React from 'react'
import {
  ReferenceLine,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  Brush,
  AreaChart,
  Area,
  BarChart,
  Bar,
  ResponsiveContainer
} from 'recharts';
import SyncIcon from '@material-ui/icons/Sync';
import BarChartIcon from '@material-ui/icons/BarChart';
import ShowChartIcon from '@material-ui/icons/ShowChart';
import GetAppIcon from '@material-ui/icons/GetApp';
import { Component } from 'react'
import "./Chart.css"

const DataFormater = (number) => {

  if (number > 1000000 || number < 1000000) {
    return (number / 1000000).toFixed(2).toString() + 'm';
  } else if (number > 1000 || number < 1000) {
    return (number / 1000).toFixed(2).toString() + 'K';
  } else {
    return number.toFixed(2).toString();
  }
}

export default class Chart2 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      active: false,
    }
  }





  DataFormater = (number) => {
    if (number > 1000000000 || number < 1000000000) {
      return (number / 1000000000).toString() + 'B';
    } else if (number > 1000000 || number < 1000000) {
      return (number / 1000000).toFixed(2).toString() + 'm';
    } else if (number > 1000 || number <1000) {
      return (number / 1000).toFixed(2).toString() + 'K';
    } else {
      return number.toFixed(2).toString();
    }
  }
  showBarchart = () => {
    if (!this.state.active) {
      this.setState({ active: true });

    } else {
      this.setState({ active: false });
    }
  }
  reloadComponenet = () => {
    window.location.reload(false);
  }
  //   clickHandler() {
  //     this.chartInstance.exportModule.export('PNG', 'sample');
  // }
  showFunction = () => {
    if (!this.state.active) {
      return (
        <AreaChart
          data={this.props.data}
        >


          <XAxis dataKey={this.props.dataKey} />
          <YAxis type="number" domain={[-60000000, 120000000]} tickCount={8} tickFormatter={DataFormater} />
          <Tooltip />
          <Area type="monotone" dataKey={this.props.datakey3} stroke="#6b7a8a" fill="#CDD1D4" />
          <Area type="monotone" dataKey={this.props.dataKey2} stroke="#5ABA9B" fill="#5ABA9B" />
          <Area type="monotone" dataKey={this.props.dataKey1} stroke="#374B60" fill="#374B60" />
          <Brush
            dataKey={this.props.dataKey}
            data={this.props.data}
          />

          <Legend className="Legend" wrapperStyle={{ top: -20 }} />
          <CartesianGrid horizontal={false} />
        </AreaChart>
      );
    }else {
      return(
        <BarChart
        data={this.props.data}
      >

        <XAxis dataKey={this.props.dataKey} />
        <YAxis type="number" domain={[-60000000, 120000000]} tickCount={8} tickFormatter={DataFormater} />
        <Tooltip />
        <ReferenceLine y={0} stroke="#000" />
        <Brush dataKey="name" height={30} stroke="#8884d8" />
        <Bar dataKey={this.props.dataKey1} stroke="#374B60" fill="#374B60" />
        <Bar data={this.props.data2} dataKey={this.props.datakey3} stroke="#6b7a8a" fill="#F7F7F7" />
        <Bar dataKey={this.props.dataKey2} stroke="#5ABA9B" fill="#5ABA9B" />
        <CartesianGrid horizontal={false} />
        <Legend className="Legend" wrapperStyle={{ top: -20 }} />
        <Brush
          dataKey={this.props.dataKey}
          data={this.props.data}
        />
      </BarChart>
      )
    }
  }

  render() {
    return (
      <div>
        <div className="chart">
          <div className="navbarChart">
            <span className="titleChart">Total Exposeur &#36;<br /><small className="subtitleChart" >Historical Credit Exposure Trends : NPV ,CE,EEPE </small> </span>
            <span ></span>
            <div className="icons">
              <ShowChartIcon className="IconsItem active" onClick={this.showBarchart} />
              <BarChartIcon className="IconsItem" onClick={this.showBarchart} />
              <SyncIcon className="IconsItem" onClick={this.reloadComponenet} />
              <GetAppIcon className="IconsItem" />
            </div>
          </div>
          <div className="infosItem">


            <ResponsiveContainer width="100%" height={250}>

            {this.showFunction()}
            </ResponsiveContainer>
          </div>
          <h3 className="ChartTitle">{this.props.title}</h3>
        </div>
      </div>
    )
  }
}


