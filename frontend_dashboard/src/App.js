import React from 'react';
import './App.css';
import SideBar from './componenets/SideBar/SideBar'
import CreditRatingPage from './pages/Home/CreditRatingPage';
import LimitsPage from './pages/LimitsPage/LimitsPage';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import CounterParty from './pages/CounterParty/CounterParty';
import NettingSet from './pages/Nettingset/NettingSet';
import Trade from './pages/Trade/Trade';

function App() {
  return (

    <Router>
      <div className="App">
        <SideBar />

        <div className="container" >
         
          <Switch>
            <Route exact path="/" component={CreditRatingPage} />
            <Route exact path="/Limits" component={LimitsPage} />
            <Route exact path="/CounterParty" component={CounterParty} />
            <Route exact path="/NettingSet" component={NettingSet} />
            <Route exact path="/Trade" component={Trade} />
          </Switch>
        </div>
      </div>
    </Router>

  )
}

export default App;
