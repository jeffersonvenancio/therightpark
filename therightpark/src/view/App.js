import React, { Component } from 'react';
import './App.css';
import { fetchAndSaveSlots } from '../actions/slotsActions';
import { startParksPolling } from '../actions/parksActions';
import LeftPane from './LeftPane/LeftPane';
import RightPane from './RightPane/RightPane';

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
      <div className="App">
        <RightPane />
      </div>
    );
  }
}

export default App;
