// Panel colapsable del lado izquierdo
var mini = false;

document.addEventListener('DOMContentLoaded', function() {
  toggleSidebar();
})

function toggleSidebar() {
  if (mini) {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    this.mini = false;
  } else {
    document.getElementById("mySidebar").style.width = "70px";
    document.getElementById("main").style.marginLeft = "70px";
    this.mini = true;
  }
}

