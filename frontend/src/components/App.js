

import React from 'react';
import ReactDOM from 'react-dom';
import Timer from './Timer.js';
import Blinds from './Blinds.js';
import Pot from './Pot.js';
import Debts from './Debts.js';
import Clock from './Clock.js';

import { startingSeconds, payouts, buyIn, smallBlinds } from './variables.js';

export default class App extends React.Component {
    componentWillMount() {
        window.addEventListener( 'blinds-up', this.handleBlindsUp, false );
    }

    componentWillUnmount() {
        window.removeEventListener( 'blinds-up', this.handleBlindsUp, false );
    }

    handleBlindsUp() {
        let body = document.getElementsByTagName( 'body' )[0];
        body.classList.add( 'flashing' );
        setTimeout( function() { body.classList.remove( 'flashing' ); }, 1700 );
        setTimeout( function() { body.classList.add( 'flashing' ); }, 1800 );
        setTimeout( function() { body.classList.remove( 'flashing' ); }, 3500 );
    }

    render() {
        return (
            <div>
                <div className="orange-bg">
                    <div className="container header">
                        <div className="col1">
                            <Clock />
                        </div>
                        <div className="col2">
                            <h2 className="poker-title">Poker Simulator</h2>
                        </div>
                        <div className="col3">
                            &nbsp;
                        </div>
                        <div className="clear-both"></div>
                    </div>
                </div>
                <div className="container">
                    <div className="col1">
                        <Blinds smallBlinds={ smallBlinds } />
                    </div>
                    <div className="col2">
                        <Timer startingTime={ startingSeconds } />
                    </div>
                    <div className="col3">
                        <Pot payouts={ payouts } buyIn={ buyIn } />
                        <Debts />
                    </div>
                    <div className="clear-both"></div>
                </div>
            </div>
        );
    }
}

ReactDOM.render( <App/>, document.getElementById( 'app' ) );
