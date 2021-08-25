import React, { Component } from 'react'
import TopBar from '../../componenets/TopBar/TopBar'
import Charts from '../../componenets/Charts/Chart'
import Charts2 from '../../componenets/Charts/Chart2'
import Piechartc from '../../componenets/PieChart/Piechartc'
import BarChartc from '../../componenets/BarChart/BarChartc'
import GaugeChart from '../../componenets/GaugeChart/GougeCharts'
import axios from 'axios'

export default class NettingSet extends Component {
    constructor(props) {
        super(props);
        this.state = {
          Npv_totalList: [],
          xpv_totalList: [],
          exposeur_total: [],
          xpv_NettingSet: [],
          npv_NettingSet:[],
          Limits_Nettingset:[],

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
          .get("http://localhost:8000/api/xpvCPs/")
          .then(res => this.setState({ xpv_NettingSet: res.data }))
          .catch(err => console.log(err))
        axios
          .get("http://127.0.0.1:8000/api/nettingsets/")
          .then(res => this.setState({ npv_NettingSet: res.data }))
          .catch(err => console.log(err))
          axios
          .get("http://127.0.0.1:8000/api/Limits_NS/")
          .then(res => this.setState({ Limits_Nettingset: res.data }))
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
          <Piechartc title="CVA" argField="Counterparty" datasource={this.state.xpv_NettingSet} className="Piechartc" valueField="CVA" />
          <Piechartc title="FVA" argField="Counterparty" datasource={this.state.xpv_NettingSet} className="Piechartc" valueField="DVA" />
          <Piechartc title="COLVA" argField="Counterparty" datasource={this.state.xpv_NettingSet} className="Piechartc" valueField="COLVA" />
        </div>
        <hr className="Separtor" />
        <div className="bottom_side">
        <div className="BarChartc">
              <BarChartc
                datasource={this.state.npv_NettingSet}
                dataLimits={this.state.Limits_Nettingset}
                dataKey="nettingset"
                value='1' />
              <BarChartc
                datasource={this.state.npv_NettingSet}
                dataKey="nettingset"
                dataLimits={this.state.Limits_Nettingset}
                value="5" />
              <BarChartc datasource={this.state.xpv_NettingSet} dataKey="Nettingset" dataLimits={this.state.Limits_Nettingset} value="6" />
            </div>
            <hr className="Separtor" />
            <div className="BarChartc">
              <BarChartc datasource={this.state.xpv_NettingSet} dataKey="Nettingset" dataLimits={this.state.Limits_Nettingset} value="7" />
              <BarChartc datasource={this.state.xpv_NettingSet} dataKey="Nettingset" dataLimits={this.state.Limits_Nettingset} value="2" />
              <BarChartc datasource={this.state.xpv_NettingSet} dataKey="Nettingset" dataLimits={this.state.Limits_Nettingset} value="3" />
            </div>
        </div>


      </div>
            </div>
        )
    }
}
