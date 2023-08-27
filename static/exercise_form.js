document.addEventListener('DOMContentLoaded', function() {
    const exerciseForm = document.getElementById('exercise-form');
    exerciseForm.addEventListener('submit', function(event) {
        const durationInput = document.getElementById('duration');
        if (parseInt(durationInput.value) <= 0) {
            alert('Duration must be a positive number.');
            event.preventDefault();
        }
    });
});


//
//<document.addEventListener("DOMContentLoaded", function () {
  //  const exerciseForm = document.getElementById("exercise-form");
    //const durationInput = document.getElementById("duration");
    //const intensityInput = document.getElementById("intensity");
  
    //exerciseForm.addEventListener("submit", function (event) {
      //if (durationInput.value <= 0 || intensityInput.value < 1 || intensityInput.value > 10) {
        //event.preventDefault();
        //alert("Please enter valid values for duration (greater than 0) and intensity (between 1 and 10).");
     // }
    //});
  //}); 
  