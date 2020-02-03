// console.log("ahiahi")

var imgs = document.getElementsByClassName("pi-pic");
console.log(imgs);
for(var i = 0 ;i<imgs.length;i++){
    var img = imgs[i];
    // console.log(btn_one);
    img.addEventListener("click",function(e){
    // var position = e.target;
    // var parent = position.parentNode;// lay ra con me tu con con
    // parent.remove();
   
    console.log("hello");
    // $("#img1 a").attr("href", "http://localhost:3000/book-detail");
    location.replace("http://localhost:3000/book-detail")

});

}