import React from 'react'
import HelpOutlineOutlinedIcon from '@material-ui/icons/HelpOutlineOutlined';
import  { Component } from 'react'
import axios from 'axios'

import {
  PieChart,
  Pie,
  Tooltip,
  Cell,
} from "recharts";

const COLORS = ['#395067', '#63CBA9', '#cfd6da','#55A8F1','#9B59B6','#8ABB6F','#759C6A'];


export default class Piechartc extends Component {
  constructor(props){
    super(props);
    this.state={
      creditRatingList:[],
    title:""
    }
  }
  componentDidMount() {
    this.refreshList();

  }


  refreshList = () => {
    axios   //Axios to send and receive HTTP requests
      .get("http://127.0.0.1:8000/api/xpvCRs/")
      .then(res => this.setState({ creditRatingList: res.data }))
      .catch(err => console.log(err));
  };














  render() {
    return (
      <div className="Pichartc" >
      <div className="subnavbar">
        <span className="titlePichart"> {this.props.title} </span>
        <HelpOutlineOutlinedIcon className="helpIcon" />
        
        <hr className="Separtormini" /> 
      </div>
    <PieChart width={350} height={350}>

      <Pie
       data={this.state.creditRatingList} dataKey="CVA"
       cx="50%" cy="50%" innerRadius={60}
       outerRadius={90} fill="#82ca9d" label >
          {this.state.creditRatingList.map((entry, index) => (
          <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
        ))}
      </Pie>
      <Tooltip />
    </PieChart>
  </div>
    )
  }
}

// import React, { PureComponent } from 'react';
// import { PieChart, Pie, Sector, ResponsiveContainer,Cell } from 'recharts';
// import axios from 'axios'
// const COLORS=['#87878',"#f5f5f"]

// const renderActiveShape = (props) => {
//   const RADIAN = Math.PI / 180;
//   const { cx, cy, midAngle, innerRadius, outerRadius, startAngle, endAngle, fill, payload, percent, value } = props;
//   const sin = Math.sin(-RADIAN * midAngle);
//   const cos = Math.cos(-RADIAN * midAngle);
//   const sx = cx + (outerRadius + 10) * cos;
//   const sy = cy + (outerRadius + 10) * sin;
//   const mx = cx + (outerRadius + 30) * cos;
//   const my = cy + (outerRadius + 30) * sin;
//   const ex = mx + (cos >= 0 ? 1 : -1) * 22;
//   const ey = my;
//   const textAnchor = cos >= 0 ? 'start' : 'end';
  
//   return (
//     <g>
//       <text x={cx} y={cy} dy={8} textAnchor="middle" fill={fill}>
//         {payload.name}
//       </text>
//       <Sector
//         cx={cx}
//         cy={cy}
//         innerRadius={innerRadius}
//         outerRadius={outerRadius}
//         startAngle={startAngle}
//         endAngle={endAngle}
//         fill={fill}
//       />
//       <Sector
//         cx={cx}
//         cy={cy}
//         startAngle={startAngle}
//         endAngle={endAngle}
//         innerRadius={outerRadius + 6}
//         outerRadius={outerRadius + 10}
//         fill={fill}
//       />
//       <path d={`M${sx},${sy}L${mx},${my}L${ex},${ey}`} stroke={fill} fill="none" />
//       <circle cx={ex} cy={ey} r={2} fill={fill} stroke="none" />
//       <text x={ex + (cos >= 0 ? 1 : -1) * 12} y={ey} textAnchor={textAnchor} fill="#333">{`CreditRating ${value}`}</text>
//       <text x={ex + (cos >= 0 ? 1 : -1) * 12} y={ey} dy={18} textAnchor={textAnchor} fill="#999">
//         {`(Rate ${(percent * 100).toFixed(2)}%)`}
//       </text>
//     </g>
//   );
// };

// export default class PieChartc extends PureComponent {
//   constructor(props){
//     super(props);
//     this.state = {
//       activeIndex: 0,
//       data:[],
//     };
//   }

 

//   onPieEnter = (_, index) => {
//     this.setState({
//       activeIndex: index,
//     });
//   };



//   componentDidMount() {
//     this.refreshList();

//   }


//   refreshList = () => {
//     axios   //Axios to send and receive HTTP requests
//       .get("http://127.0.0.1:8000/api/xpvCRs/")
//       .then(res => this.setState({ data: res.data }))
//       .catch(err => console.log(err));
//   };








//   render() {
//     return (
     
//         <PieChart width={400} height={400}>
//           <Pie
//             activeIndex={this.state.activeIndex}
//             activeShape={renderActiveShape}
//             data={this.state.data}
//             cx="50%"
//             cy="50%"
//             innerRadius={60}
//             outerRadius={80}
//             fill="#8884d8"
//             dataKey="CVA"
//             onMouseEnter={this.onPieEnter}
//           />
//              {
//           	this.state.data.map((entry, index) => <Cell fill={COLORS[index % COLORS.length]}/>)
//           }
//         </PieChart>
     
//     );
//   }
// }
