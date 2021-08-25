import React from 'react'
import './SideBar.css'
import HomeIcon from '@material-ui/icons/Home';
import GetAppIcon from '@material-ui/icons/GetApp';
import StorageIcon from '@material-ui/icons/Storage';
import HelpOutlineIcon from '@material-ui/icons/HelpOutline';
import {Link} from 'react-router-dom'


// function refreshPage() {
//      window.location.reload(false);
//   }
  const NavStyle={
    color:'white',
    'text-decoration': 'none',
}
export default function SideBar() {
    return (
        <div className="SideBar">
            <div className="sideBarWrapper">
                <div className="sideBarMenu ">
                    <ul className="sidebarList">
                        <li className="siderListItem " >
                        <HomeIcon className="sidebarIcone" />
                        <Link style={NavStyle} to="/" >Home</Link>
                        </li>
                        <br />
                        <li className="siderListItem">
                           <GetAppIcon />
                        <span>PDF</span>

                        </li>
                        <br />
                        <li className="siderListItem">
                             <StorageIcon/>
                             <Link style={NavStyle}  to="/Limits" >Limits</Link>
                        </li>
                        <br />

                        <li className="siderListItem">
                             <HelpOutlineIcon/>
                             <span>Help</span>
                        </li>
                    </ul>
                </div>
               
                
            </div>
        </div>
    )
}

