
let inpUser = document.getElementById('inp-user')
let inpPass = document.getElementById('inp-pass')
let logout = document.getElementById('btn-logout')
let prikaz= document.getElementById('prikaz')
let greska = document.getElementById('error-msg')

let login = document.getElementById('login2')

function checkLoggedIn() {
    var loggedIn = sessionStorage.getItem("loggedIn");

    console.log(loggedIn)
    
    if (!loggedIn || loggedIn !== "true") {
      return false;
    }
    return true;
}


function load(){

    hide(!checkLoggedIn())
    //hide(true)
   // let intervalId = setInterval(myFunction, 5000)
   // clearInterval(intervalId)
}
/*
function myFunction()
{
    console.log('pozvan')
    let cnt = document.getElementsByTagName('body')[0]
    let broj = Math.random()*10;
    let bgCol = "background-color: rgb(147,116,101," + broj + ");";
    
    cnt.style = "background-color: rgb(147,116,101," + broj + ");";
    
}*/

function  checkLogin(){

    let user = inpUser.value
    let pass = inpPass.value

    let regUser = /^@[a-zA-Z]{2,}[0-9]{2}[a-zA-Z]*$/
    let regUserDuzina = /^.{6,}$/

    let regPass = /^[a-zA-Z]*[A-Z]{1,}[a-zA-Z]*[\-_!?~]{1}$/

    //console.log(user + " : " + pass) 

    
    if (regUser.test(user) && regUserDuzina.test(user ) && 
        regPass.test(pass))
    {
        sessionStorage.setItem("loggedIn", "true");
        hide(false )
        greska.innerHTML = ""
    }
    else  
    {
        greska.innerHTML = "GRESKA"
    }
}
function hide(bul){
    logout.hidden = bul
    prikaz.hidden = bul 
    login.hidden = !bul 
}
