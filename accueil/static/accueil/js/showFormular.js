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

     /*if ({% default_libreg %}="{{ default_libreg }}"){
         $(".depform").css("visibility", "visible");
         $("#btnrecherchedep").css("display", "initial");
         $("#btnrecherchereg").css("display", "none");
     }*/



    /* $("#btnrecherchereg").click(function () {
         $(".depform").css("visibility", "visible");
         $("#btnrecherchedep").css("display", "initial");
         $("#btnrecherchereg").css("display", "none");*/
     });
 })
