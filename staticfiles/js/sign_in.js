

function validateForm(){
    user1=request.POST.get('username')
    pass1=request.POST.get('password')         
   var box = document.getElementById('username');
   var box1 = document.getElementById("password");


    if(box1.value == ""){
        alert("the field cannot be empty");
        box.focus();
        box.style.border = "solid 3px red";
        return false;
    }
    
    
   
};
