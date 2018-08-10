import React, { Component } from 'react';
import './App.css';
import { fetchAndSaveSlots } from '../actions/slotsActions';
import { startParksPolling } from '../actions/parksActions';
import LeftPane from './LeftPane/LeftPane';
import RightPane from './RightPane/RightPane';

import { Provider } from "mobx-react";
import slotsStore from '../store/slotsStore';
import parksStore from '../store/parksStore';

const stores = {
  slotsStore,
  parksStore
}

class App extends Component {
  async componentDidMount() {
    await fetchAndSaveSlots.execute();
    this.stopPolling = await startParksPolling.execute();
  }
  componentWillUnmount() {
    this.stopPolling && this.stopPolling();
  }
  render() {
    return (
      <Provider {...stores}>
        <div className="App">
          <RightPane />
        </div>
      </Provider>
    );
  }
}

export default App;
