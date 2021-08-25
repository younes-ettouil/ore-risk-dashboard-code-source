import React, { Component } from 'react'
import axios from 'axios'
import PieChart, {
  Legend,
  Series,
  Export,
  Tooltip,
  Label,
  SmallValuesGrouping,
  Connector,
 
} from 'devextreme-react/pie-chart';
export default class Piechartc extends Component {
  constructor(props){
    super(props);
    this.state={
      creditRatingList:[],
    title:"",
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
     <div>
        <PieChart
        id="pie"
        type="doughnut"
        title={this.props.title}
        palette="Soft Pastel"
        dataSource={this.props.datasource}
      >
        <Series argumentField={this.props.argField} valueField={this.props.valueField}>
          <SmallValuesGrouping  />
          <Label
            visible={true}
            format="fixedPoint"
            customizeText={this.customizeLabel}
          >
            <Connector visible={true} width={1} />
          </Label>
        </Series>
        <Export enabled={true} />
        <Legend horizontalAlignment="center" visible={false} verticalAlignment="bottom" />
        <Tooltip enabled={true} />
      </PieChart>
     </div>
      
    );
  }

  customizeLabel(point) {
    return `${point.argumentText }`;
  }
}

