import React from 'react'
import {Menu} from 'antd'


function Header() {
    return (
        <div>
        <Menu mode='horizontal'>
            <Menu.Item>Groups</Menu.Item>
            <Menu.Item>Users</Menu.Item>
        </Menu>
        </div>
    )
}

export default Header;