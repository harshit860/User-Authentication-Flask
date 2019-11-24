import React from 'react';
import logo from './logo.svg';
import './App.css';
import Login from './component/login';
import {BrowserRouter as Router,Link,Route,Redirect} from "react-router-dom"
import Register from './component/register';
import Message from './component/messages'

class App extends React.Component{
        constructor(props){
          super(props)
          this.state={
                token:null,
                flag1:false,
                logout:false,
             
          }
        }
        setuser(user){
            this.setState({
              token:user,
              flag1:true,
              logout:true
              
            })
        }
        componentDidMount(){
          this.setState({
            token:null,
            logout:false,
            flag2:false
           
          })
        }
render(){
  return (
    <Router>
      <div className="App">
        <div className="bg-secondary row justify-content-around">
          <Link to="/" className="text-white">Login</Link>
          <Link to="/reg" className="text-white" >Register</Link>
          {this.state.flag1 ? (<Redirect to="/message" ></Redirect>):(<div></div>)}
          <h4 className="text-white">{this.state.token}</h4>
          {this.state.logout ? (<Link to="/" className="btn btn-dark bg-secondary text-warning">Logout</Link>):(<div></div>)}
           
        </div>
        <div>
        <Route exact path="/" render={() => <Login prop1={(e)=>this.setuser(e)}/>}></Route>
        <Route exact path="/reg" render={() => <Register />}></Route>
        <Route exact path="/message" render={()=> <Message name={this.state.token} />} ></Route>
       </div>
      </div>
    </Router>
  )
}
}

export default App;
