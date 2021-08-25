import './TopBar.css'
import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

const NavStyle={
    color:'#000',
    'text-decoration': 'none',
}
export default class TopBar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            Npv_totalList: []
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
    };

    renderItems = () => {
        const newItems = this.state.Npv_totalList;
        return newItems.map(item => (
            <option key={item.id}>{item.date} </option>
        ));
    };

    render() {
        return (
            <div className="TopBar">

                <div className="topbarWrapper">
                    <span className="logo">ORE Risk Dashboard
                    </span>
                    <div className="topbarIconsContainer">
                        <Link style={NavStyle} to="/" > <span>Credit Rating</span> </Link>
                    </div>
                    <div className="topbarIconsContainer">
                        <Link style={NavStyle} to="/counterParty" > <span>Counterparty</span> </Link>
                    </div>
                    <div className="topbarIconsContainer">
                        <Link style={NavStyle} to="/Nettingset" > <span>Netting Set</span> </Link>
                    </div>
                    <div className="topbarIconsContainer">
                        <Link style={NavStyle} to="/trade" > <span>Trade</span> </Link>
                    </div>
                    <div className="topbarIconsContainerSelect">
                        <span>Select date :</span>
                        <select name="" id="">
                            {this.renderItems()}
                        </select>
                    </div>
                </div>
            </div>
        )
    }
}
