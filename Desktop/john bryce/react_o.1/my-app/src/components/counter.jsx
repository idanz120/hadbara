import React, { Component } from 'react'

class Counter extends Component {
    state = {
        count: 0,
        tags:['tags1','tags2','tags3']
    };

    handleIncrement =(product)=>{
        console.log(product)
        this.setState({count: this.state.count +1});
    };



    render() {
        return <div>
            <span className={this.calc()}>{this.formatCount()}</span>
            <button onClick={()=>this.handleIncrement(product)} className='btn btn-secondary btn-sm'>PUSH</button>
            <ul>
                {this.state.tags.map(tag => <li key={tag}>{tag}</li>)}
            </ul>
        </div>;
    }

    calc() {
        let classes = "btn m-2 btn-";
        classes += this.state.count === 0 ? "warning" : "primary";
        return classes;
    }

    formatCount() {
        const { count } = this.state;
        return count === 0 ? 'Zero' : count;
    }
}


export default Counter;