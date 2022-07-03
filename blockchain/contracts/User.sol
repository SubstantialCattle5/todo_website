// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract User{
    address  top_dog_user  ;
    AggregatorV3Interface   priceFeed ;

    // users
    address []  users_address ;


    struct user {
        string username;
        string password;
    }
    // mapping the user address to their userprofile

    mapping(address => user)  userprofile;

    constructor() public {
        top_dog_user = msg.sender ;
    }

    function signup(string memory username , string memory password) public returns(bool flag) {
        if (users_address.length != 0) {
            for(uint i ; i < users_address.length ; i++){
                if(users_address[i] == msg.sender){
                        flag = false ;
                }
                else {
                    userprofile[msg.sender] = user(username , password) ;
                    users_address.push(msg.sender) ;
                    flag = true  ;
                }
            }
        }
        else {
                userprofile[msg.sender] = user(username , password) ;
                users_address.push(msg.sender) ;
                flag = true  ;
        }
    }

    function login(string memory  password) public  returns(bool exist , bool logged_id){
        string memory  pw = password ;
        if (users_address.length != 0) {
            for(uint i ; i < users_address.length ; i++){
                if(users_address[i] == msg.sender){
                        exist = true ;
                        if(keccak256(abi.encodePacked(pw)) == keccak256(abi.encodePacked(userprofile[msg.sender].password))) {
                            logged_id = true ;
                        }
                        else{
                            logged_id = false ;
                        }

                }
                else {
                    exist = false ;
                    logged_id = false ;
                }
            }
    }}

    function recover(address user_add) public view returns(string memory username , string memory password){
        username = userprofile[user_add].username ;
        password = userprofile[user_add].password ;
    }

}