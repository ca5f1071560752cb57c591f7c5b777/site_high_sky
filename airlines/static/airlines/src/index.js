import React from "react";
import {PureComponent} from "react";
import ReactDOM from "react-dom";

const Airport = (props) => {
    const {data, onClick, selected} = props;
    const {id, name, title} = data;
    const mark = selected ? '*' : ' ';
    return <div
            key={data.id} 
            onClick = { evt => {onClick(id); console.log(name)} }>
        {mark} { title }
        </div>;
};

const Airliner = (props) => {
    const {arrivalCount} = props;
    return <div > { props.name }  { props.title } совершает {arrivalCount || 0} посадок</div>;
};

export class App extends PureComponent {

    handleAirportClick(id) {
        this.setState({
            selectedAirport: id
        })

        if (this.state.airports && this.state.airliners) {
            this.state.airports.forEach(airport => {
                this.state.airliners.forEach(airliner => {
                    const arrivalCountKey = `${airport.id}:${airliner.id}`;
                    if (!(arrivalCountKey in this.state.arrivalCountMap))
                        fetch(`/airlines/api/v1/arrival_count?airliner_id=${airliner.id}&airport_id=${airport.id}`)
                            .then(resp => resp.json())
                            .then(data => {
                                const {count} = data;
                                this.state.arrivalCountMap[arrivalCountKey] = count;
                            })
                            .catch(error => console.error('catch', error))
                });
            })
        }
    }

    componentDidMount() {
        this.setState({
            selectedAirport: null,
            arrivalCountMap: {}
        })

        fetch('/airlines/api/v1/airports/')
            .then(resp => resp.json())
            .then(data => {
                console.log('airports', data); 
                this.setState({
                    selectedAirport: data && data[0] && data[0].id || null,
                    airports: data
                    }); 
            })
            .catch(error => console.log('error', error))

        fetch('/airlines/api/v1/airliners/')
            .then(resp => resp.json())
            .then(data => { console.log('airliners', data); this.setState({airliners: data}); })
            .catch(error => console.log('error', error))
    }

    render () {
        let airportElements = [], airlineElements = [];

        if (this.state && this.state.airports) {
            airportElements = this.state.airports.map(airport =>
                <Airport
                    key={airport.id}
                    data={airport}
                    onClick={id => this.handleAirportClick(id)}
                    selected={this.state.selectedAirport === airport.id}
                />
            )
        };

        if (this.state && this.state.airliners) {
            airlineElements = this.state.airliners.map(airliner => {
                const arrivalCountKey = `${this.state.selectedAirport}:${airliner.id}`;
                const arrivalCount = this.state.arrivalCountMap[arrivalCountKey]
                return <Airliner 
                    name={ airliner.name } 
                    title={ airliner.title } 
                    arrivalCount={arrivalCount} />
            })
        };

        return <div>
            <h1>Аэропорты</h1>
            {airportElements} 
            <h2>В выбранном аэпопорту аэролайнеры</h2>
            {airlineElements}
        </div>
    }
};

ReactDOM.render(<App />, document.getElementById("index"))
