import React, { Component } from 'react';

import car from "../../assets/car.png";
import prefIcon from "../../assets/prefIcon.svg";

class RightPane extends Component {
    state = {  }
    render() { 
        return ( 
            <div className="right-pane">
                <div className="slots">
                    <Slot occupied irregular />
                    <Slot pref carPlate="Carro 1" />
                </div>
            </div>
        );
    }
}

const Slot = ({
    occupied = false,
    pref = false,
    irregular = false,
    carPlate = ""
}) => {
    return ( 
        <div className="slot">
            <div className="slot-car">
                {
                    pref ? (
                        <div className="pref">
                            <img src={prefIcon} />
                        </div>
                    ) : ("")
                }
                <div className={`occupied ${occupied ? "active" : "" }`}>
                    <img src={car} />
                </div>
            </div>
            <div className="slot-description">
                {
                    occupied ? irregular ? (
                        <div className="slot-label irregular">
                            Irregular
                        </div>
                    ) : (
                        <div className="slot-label occupied">
                            Ocupada
                        </div>
                    ) : (
                        <div className="slot-label free">
                            Livre
                        </div>
                    )
                }
                <h1><b>Vaga 1</b> {pref ? " (Preferencial)" : ""} </h1>
                <p className="car">{carPlate}</p>
            </div>
        </div>
    );
}
 


export default RightPane;