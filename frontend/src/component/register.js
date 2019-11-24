import React from "react"
import Axios from "axios"

class Register extends React.Component{
    constructor(props){
    super(props)
    this.state = {
                username:'',
                password:''
    }
}
register(){
        Axios({
            method:"post",
            url:"http://127.0.0.1:5000/Secureregister",
            data:{
                username:this.state.username,
                password:this.state.password

            }
        })
        .then(resp => console.log(resp))
        .catch(err => console.log(err))
}
handleChange(e){
    this.setState({
        [e.target.name]:e.target.value
    })
}
    render(){
        return (
            <div>
                <h1 className="col-xl-12">Register page</h1>
                <label>Username</label>
                <input name="username" onChange={(e)=>this.handleChange(e)}></input>
                <label>Password</label>
                <input name="password" onChange={(e)=>this.handleChange(e)}></input>
                <button onClick={()=>this.register()}>Register</button>
            </div>
        )
    }
}
export default Register