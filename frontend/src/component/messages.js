import React from 'react'
import Axios from 'axios'

class Message extends React.Component{
    constructor(props){
        super(props)
        this.state={
                    message_store:[]
        }
    }
    componentDidMount(){
                Axios({
                    method:"post",
                    url:"http://127.0.0.1:5000/showmessage",
                    data:{
                        username:this.props.name
                    }
                })
                .then(resp =>
                    this.setState({
                            message_store:resp.data.message_list
                    }))
                    // console.log(resp))
                .catch(err => console.log(err))
    }
    render(){
        console.log(this.state)
        let disp = this.state.message_store.map(a=> {
            return <div className="row border justify-content-left container">
                <h3 >{a.msg}</h3>
                <h3 className="ml-5 ">from :  {a.sender}</h3>
            </div>
        })
        return(
            <div>
                {disp}
            </div>
        )
    }
}
export default Message