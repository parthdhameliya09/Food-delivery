document.addEventListener("DOMContentLoaded", function () {
    const navItems = document.querySelectorAll(".nav-list");
  
    navItems.forEach((item) => {
      item.addEventListener("click", function () {
        navItems.forEach((navItem) => navItem.classList.remove("active"));
        this.classList.add("active");
      });
    });
  });
  
  // document.querySelector("#show-login").addEventListener("click",function(){
  //   document.querySelector(".popup").classList.add("active");
  // });
  // document.querySelector(".popup .close-btn").addEventListener("click",function(){
  //   document.querySelector(".popup").classList.remove("active");
  // });
  
  function toggle(){
    var blur = document.getElementById('blur');
    blur.classList.toggle('active');
    var popup = document.getElementById('popup');
    popup.classList.toggle('active');
  }