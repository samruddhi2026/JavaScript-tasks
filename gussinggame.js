let gameNum=28;
let userNum= prompt("guss the number");
while(userNum!=gameNum){
    if(userNum<gameNum){
        alert("too low");
    }       
    else{
        alert("too high");
    }

    userNum= prompt("guss the number");


}
prompt("you gussed it right");