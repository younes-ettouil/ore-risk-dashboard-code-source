import React, { Component } from 'react'
import './LimitsCss.css'
import TabNav from '../../componenets/Tabs/TabNav'

export default class LimitsPage extends Component {
    render() {
        return (
            <div className="LimitsPage">
                <div className="TopBar">
                    <div className="topbarWrapper">
                        <span className="logo">ORE Risk Dashboard
                        </span>
                    </div>
                    <hr className="Separtor" />
                    <div>
                       <TabNav /> 
                    </div>
                </div>
                
            </div>
        )
    }
}
