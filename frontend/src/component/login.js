import React from "react"
import axios from "axios"

class Login extends React.Component{
    constructor(props){
        super(props)
        this.state={    
            username:'',
            password:''
        }
    }
    handleChange(e){
        this.setState({
            [e.target.name]:e.target.value
        })
    }
    login(){
        axios({
            method:"post",
            url:"http://127.0.0.1:5000/login",
            data:{
                username:this.state.username,
                password:this.state.password
            }

        })
        .then(resp => this.props.prop1(resp.data.success.username))       
            // console.log(resp))
        .catch(err => console.log(err))
        
    }
    render(){
        console.log(this.props.prop1)
        return(
            <div >
                <h1 className="col-xl-12">Login Page</h1>
                <label>Username</label>
                <input name="username" onChange={(e)=>this.handleChange(e)} placeholder="enter your name"></input>
                <label>Password</label>
                <input name="password" onChange={(e)=>this.handleChange(e)} placeholder="enter password"></input>
                <button onClick={()=>this.login()} style={{border:"2px solid grey",backgroundColor:"grey",fontSize:"15px",color:"white"}}>Login</button>
            </div>
        )
    }
}
export default Login