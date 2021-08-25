import React from 'react'
import { BarChart, Bar,  XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import { Component } from 'react'
import HelpOutlineOutlinedIcon from '@material-ui/icons/HelpOutline' 

import './BarChartc.css'

export default class BarChartc extends Component {
    constructor(props) {
        super(props);
        this.state = {
         
            value:this.props.value,
            xpv_creditratingList:[],
            npv_creditratingList:[],
            Limits_creditratingList:[],
        }
        
        this.handleSelectOptions= this.handleSelectOptions.bind(this);
        this.title= this.title.bind(this);
    }
    handleSelectOptions(e){
        this.setState({value:e.target.value});
    }

    componentDidMount() {
        this.datakey1();
    
      }
    
    
   
       DataFormater = (number) => {
         if (number > 1000000 || number<1000000) {
          return (number / 1000000).toFixed(2).toString() + 'm';
        } else if (number > 1000 || number<1000) {
          return (number / 1000 ).toFixed(2).toString() + 'K';
        } else {
          return number.toFixed(2).toString();
        }
      }
      title=()=>{
            if(this.state.value === '1' || this.state.value === '2' || this.state.value === '3'  || this.state.value === '4' ){
                return 'CREDIT'  ;
            }else if(this.state.value === '6' || this.state.value === '7' || this.state.value === '8'  || this.state.value ===  '9'){
                return 'LIQUIDITY';
            }else {
                return "MARKET"
            }
      }

      datakey1(){
        if(this.state.value === '1'){
            return (
                <BarChart
                width={450}
                height={250}
                data={this.props.datasource}
                layout="vertical"
            >
                <XAxis type="number" domain={[0,14000000]} tickFormatter={this.DataFormater} />
                <YAxis type="category"  dataKey={this.props.dataKey} />
                <CartesianGrid horizontal={false} />
                <Tooltip   />
                <Legend />
                <Bar dataKey="CE_Base" fill="#BBDCAB" />
                <Bar data={this.props.dataLimits} dataKey="CE" fill="#EE9A73" />
                                 
            </BarChart>
            );
        }else if(this.state.value === '2'){
            return (
                <BarChart
                width={450}
                height={250}
                data={this.props.datasource}
                layout="vertical"
            >
                <XAxis type="number"  domain={[0,6000000]} tickFormatter={this.DataFormater} />
                <YAxis type="category"  dataKey={this.props.dataKey} />
                <CartesianGrid horizontal={false} />
                <Tooltip   />
                <Legend />
                <Bar dataKey="BaselEEPE" fill="#BBDCAB" />
                <Bar data={this.props.dataLimits} dataKey="EEPE" fill="#EE9A73" />
                                 
            </BarChart>
            );
        }else if(this.state.value === '3'){
            return (
                <BarChart
                width={450}
                height={250}
                data={this.props.datasource}
                layout="vertical"
            >
                <XAxis type="number" domain={[0,600000]}  tickFormatter={this.DataFormater} />
                <YAxis type="category"  dataKey={this.props.dataKey}  />
                <CartesianGrid horizontal={false} />
                <Tooltip   />
                <Legend />
                <Bar dataKey="CVA" fill="#BBDCAB" />
                <Bar data={this.props.dataLimits} dataKey="CVA" fill="#EE9A73" />
                                 
            </BarChart>
            );
        }else if(this.state.value === '4'){
            return (
                <BarChart
                width={450}
                height={250}
                data={this.props.datasource}
                layout="vertical"
            >
                <XAxis type="number" domain={[0,400000]}   tickFormatter={this.DataFormater} />
                <YAxis type="category"  dataKey={this.props.dataKey}  />
                <CartesianGrid horizontal={false} />
                <Tooltip   />
                <Legend />
                <Bar dataKey="DVA" fill="#BBDCAB" />
                <Bar data={this.props.dataLimits} dataKey="DVA" fill="#EE9A73" />
                                 
            </BarChart>
            );
        }else if(this.state.value === '5'){
            return (
                <BarChart
                width={450}
                height={250}
                data={this.props.datasource}
                layout="vertical"
            >
                <XAxis type="number" domain={[0,3500000]}  tickFormatter={this.DataFormater} />
                <YAxis type="category"  dataKey={this.props.dataKey}  />
                <CartesianGrid horizontal={false} />
                <Tooltip   />
                <Legend />
                <Bar dataKey="NPV_Base" fill="#BBDCAB" />
                
                                 
            </BarChart>
            );
        }else if(this.state.value === '6'){
            return (
                <BarChart
                width={450}
                height={250}
                data={this.props.datasource}
                layout="vertical"
            >
                <XAxis type="number" domain={[-700000,0]}  tickFormatter={this.DataFormater} />
                <YAxis type="category"  dataKey={this.props.dataKey}  />
                <CartesianGrid horizontal={false} />
                <Tooltip   />
                <Legend />
                <Bar dataKey="FCA" fill="#BBDCAB" />
                <Bar data={this.props.dataLimits} dataKey="FCA" fill="#EE9A73" />
                                 
            </BarChart>
            );
        }else if(this.state.value === '7'){
            return (
                <BarChart
                width={450}
                height={250}
                data={this.props.datasource}
                layout="vertical"
            >
                <XAxis type="number" domain={[-700000,0]}   tickFormatter={this.DataFormater} />
                <YAxis type="category"  dataKey={this.props.dataKey}  />
                <CartesianGrid horizontal={false} />
                <Tooltip   />
                <Legend />
                <Bar dataKey="FBA" fill="#BBDCAB" />
                <Bar data={this.props.dataLimits} dataKey="FBA" fill="#EE9A73" />
                                 
            </BarChart>
            );
        }else if(this.state.value === '8'){
            return (
                <BarChart
                width={450}
                height={250}
                data={this.props.datasource}
                layout="vertical"
            >
                <XAxis type="number" domain={[-1500000,0]}   tickFormatter={this.DataFormater} />
                <YAxis type="category"  dataKey={this.props.dataKey}  />
                <CartesianGrid horizontal={false} />
                <Tooltip   />
                <Legend />
                <Bar dataKey="FVA" fill="#BBDCAB" />
                <Bar   data={this.props.dataLimits} dataKey="FVA" fill="#EE9A73" />
                                 
            </BarChart>
            );
        }else if(this.state.value === '9'){
            return (
                <BarChart
                width={450}
                height={250}
                data={this.props.datasource}
                layout="vertical"
            >
                <XAxis type="number"  tickFormatter={this.DataFormater} />
                <YAxis type="category"  dataKey={this.props.dataKey}  />
                <CartesianGrid horizontal={false} />
                <Tooltip   />
                <Legend />
                <Bar dataKey="COLVA" fill="#BBDCAB" />
                
                                 
            </BarChart>
            );
        }
        
      }
    render() {
        return (
            <div className="Barchart">
                <div className="subnavbar">
                    <span className="titlePichart"> {this.title()} </span>
                    <HelpOutlineOutlinedIcon className="helpIcon" />
                    <select name="select" id="" onChange={this.handleSelectOptions} className="selectItem">
                        <option selected value="1">CE</option>
                        <option value="2">EPEE</option>
                        <option value="3">CVA</option>
                        <option value="4">DVA</option>
                        <option value="5">NPV</option>
                        <option value="6">FCA</option>
                        <option value="7">FBA</option>
                        <option value="8">FVA</option>
                        <option value="9">Colva</option>
                    </select>
                    <hr className="Separtormini" />
                </div>
               <div className="BarChartGraph" >
                {this.datakey1()}
               </div>

            </div>
        )
    }
}
