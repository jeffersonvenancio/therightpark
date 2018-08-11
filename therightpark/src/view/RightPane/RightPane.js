import React, { Component } from 'react';
import { inject, observer } from "mobx-react";
import car from "../../assets/car.png";
import prefIcon from "../../assets/prefIcon.svg";
import slotsStore from '../../store/slotsStore';

class RightPane extends Component {
    state = {  }
    render() { 
        const { parksStore, slotsStore } = this.props;
        const { slots } = slotsStore;
        
        return ( 
            <div className="right-pane">
                <div className="slots">
                    {
                        Array.from(slots).map(slot => {
                            const {occupied, regular, carplate} = parksStore.isSlotOcupied(slot)
                            return (
                                <Slot
                                    name={slot.label}
                                    occupied={occupied}
                                    irregular={!regular}
                                    pref={slot.pref}
                                    carPlate={carplate}
                                />
                            )
                        })
                    }
                </div>
            </div>
        );
    }
}

const Slot = ({
    occupied = false,
    pref = false,
    irregular = false,
    name = "Vaga",
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
                <h1><b>{name}</b> {pref ? " (Preferencial)" : ""} </h1>
                <p className="car">{carPlate}</p>
            </div>
        </div>
    );
}
 


export default inject(s => s)(observer(RightPane));