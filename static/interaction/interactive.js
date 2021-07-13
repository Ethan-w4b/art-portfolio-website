// .innerHTML writing into an element 
// element.attribute = new value change attribute
// element.style.property = new style
// document.getElementById(id).onclick = function()
// document.write() writing into html output (for testing)
// window.alert() alert window box

function click_me(){
    alert("it works")
    document.getElementById('demo').innerHTML = "GET OUT"
};

function turn_blue(){
    document.getElementById('demo').style.color = "blue"
}

function get_form(){
    let x = document.forms["myform"]["age"].value;
    alert(x);
}