
let item = document.getElementById('add-badge').innerHTML;
console.log(document.getElementById('add-badge').innerHTML)

function addBadge (){
    item ++;
    document.getElementById('add-badge').innerHTML=item;
}