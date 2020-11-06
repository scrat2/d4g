 $(document).ready(function () {

     $("#popupcookie").click(function () {
         let windowPopup = $(".popup");
         windowPopup.delay(2000).show();
         windowPopup.css("width", "400px");
         windowPopup.css("z-index", "5");
         localStorage.setItem("firsVisit", "shown")
     })

      $("#popupcookie").mouseover(function (){
          $(this).css("text-decoration", "underline");
      })
     $("#popupcookie").mouseleave(function (){
          $(this).css("text-decoration", "none");
      })

     //close the popup
     $("#closePopup").click(function () {
         $(".popup").css("display", "none");
     });

     /*$("#reinitialiser").click(function(e){
         e.preventDefault();
         window.location = "http://127.0.0.1:8000";
     });*/

 });

function deleteItems() {
    sessionStorage.clear();
    $(".listresult").empty();
    history.go(0);
    window.location = "http://127.0.0.1:8000";
    }