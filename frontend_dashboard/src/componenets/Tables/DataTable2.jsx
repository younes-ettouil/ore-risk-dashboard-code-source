import React from 'react'
import { Component } from 'react'
import axios from 'axios'
import { DataGrid } from '@material-ui/data-grid';

const columns = [
    {
        field: 'creditrating',
        headerName: 'Credit Rating',
        width: 150,
        sortable: true,
    },
    {
        field: 'counterparty',
        headerName: 'Counterparty',
        width: 150,
        sortable: true,
        editable: true,
    },
    {
        field: 'nettingset',
        headerName: 'Netting Set',
        width: 150,
        sortable: true,
        editable: true,
    },
    {
        field: 'trade',
        headerName: 'Trade',
        type: 'number',
        width: 110,
        sortable: true,
        editable: true,
    },
    {
        field: 'metrice',
        headerName: 'Metrice',
        sortable: true,
        width: 160,
    },
    {
        field: 'limitValue',
        headerName: 'Limit Value',

        sortable: true,
        width: 160,
        
    },
    {
        field: 'ConsumptionValue',
        headerName: 'Consumption Value',

        sortable: true,
        width: 160,
      
    },
    {
        field: 'date',
        headerName: 'Date',
        sortable: true,
        width: 160,
      
    },
    {
        field: 'cons',
        headerName: 'Cons%',
        sortable: true,
        width: 160,
      
    },
];




export default class DataTable extends Component {
    constructor(props) {
        super(props);
        this.state = {
          
            allData2:[]
        }
       
    }

    componentDidMount() {
        this.refreshList();
        
    
      }
    
      
    
      refreshList = () => {
        axios   //Axios to send and receive HTTP requests
          .get("http://127.0.0.1:8000/api/allData2/")
          .then(res => this.setState({ allData2: res.data }))
          .catch(err => console.log(err));

      };
    
      
    //   renderItems = () => {
    //     const newItems = this.state.CreditRating;
    //     return newItems.map(item => (
    //       <li key={item.id}>
    //         <span>
    //           NPV_Base: {item.NPV_Base} <br />
    //           BaseCurrency : {item.BaseCurrency} <br />
    //           CE_Base:{item.CE_Base}
    //         </span>
    //       </li>
    //     ));
    //   };


      

    render() {
        return (
            <div>
                <div style={{ height: 600, width: '10 0%' }}>
                    <DataGrid
                        rows={this.state.allData2}
                        columns={columns}
                    />
                </div>
            </div>
        )
    }
}
