import React, { Component } from 'react'
import TopBar from '../../componenets/TopBar/TopBar'
import Charts from '../../componenets/Charts/Chart'
import Charts2 from '../../componenets/Charts/Chart2'
import Piechartc from '../../componenets/PieChart/Piechartc'
import BarChartc from '../../componenets/BarChart/BarChartc'
import GaugeChart from '../../componenets/GaugeChart/GougeCharts'
import axios from 'axios'

export default class Trade extends Component {
    constructor(props) {
        super(props);
        this.state = {
          Npv_totalList: [],
          xpv_totalList: [],
          exposeur_total: [],
          xpv_cr: []
        };
      }
      componentDidMount() {
        this.refreshList();
    
      }
    
    
      refreshList = () => {
        axios   //Axios to send and receive HTTP requests
          .get("http://127.0.0.1:8000/api/npvs/")
          .then(res => this.setState({ Npv_totalList: res.data }))
          .catch(err => console.log(err));
    
        axios
          .get("http://127.0.0.1:8000/api/xpvs/")
          .then(res => this.setState({ xpv_totalList: res.data }))
          .catch(err => console.log(err))
        axios
          .get("http://127.0.0.1:8000/api/exposeurT/")
          .then(res => this.setState({ exposeur_total: res.data }))
          .catch(err => console.log(err))
        axios
          .get("http://127.0.0.1:8000/api/xpvCRs/")
          .then(res => this.setState({ xpv_cr: res.data }))
          .catch(err => console.log(err))
      };
    
      renderItems = () => {
        const newItems = this.state.Npv_totalList;
        return newItems.map(item => (
          <li key={item.id}>
            <span>
              NPV_Base: {item.NPV_Base} <br />
              BaseCurrency : {item.BaseCurrency} <br />
              CE_Base:{item.CE_Base}
            </span>
          </li>
        ));
      };
    
      renderItemsd = () => {
        const newItems = this.state.Npv_totalList;
        return newItems.map(item => (
          <option key={item.id}>{item.date} </option>
        ));
      };
    



    render() {
        return (
            <div>
                <TopBar />
                <div className="Home">
        
        <div className="pathNav">
          <ol>

          </ol>
        </div>
        <hr className="Separtor" />
        <div className="ChartsItem">
          <Charts data={this.state.Npv_totalList} data2={this.state.xpv_totalList} dataKey="date" dataKey1="CE_Base" dataKey2="NPV_Base" datakey3="BaselEEPE" />
          <Charts2 data={this.state.exposeur_total} dataKey="Date" dataKey1="PFE" dataKey2="EPE" datakey3="ENE" />
        </div>
        <hr className="Separtor" />
        <div className="PieChart" >
          <GaugeChart />
          <Piechartc title="CVA" datasource={this.state.xpv_cr} className="Piechartc" valueField="CVA" />
          <Piechartc title="FVA" datasource={this.state.xpv_cr} className="Piechartc" valueField="DVA" />
          <Piechartc title="COLVA" datasource={this.state.xpv_cr} className="Piechartc" valueField="COLVA" />
        </div>
        <hr className="Separtor" />
        <div className="bottom_side">
          <div className="BarChartc">
            <BarChartc value='1' />
            <BarChartc value="5" />
            <BarChartc value="6" />
          </div>
          <hr className="Separtor" />
          <div className="BarChartc">
            <BarChartc value="7" />
            <BarChartc value="2" />
            <BarChartc value="3" />
          </div>
        </div>


      </div>
            </div>
        )
    }
}
