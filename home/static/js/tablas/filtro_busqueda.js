
$(document).ready(function () {
  $("#sort").DataTable({
    columnDefs: [{ type: "date", targets: [3] }],
  });
});

  const containerClase = document.querySelectorAll(".container");
  containerClase[0].classList.remove("container");


  const rows = document.getElementsByClassName("row");
  rows[0].classList.remove("row");
