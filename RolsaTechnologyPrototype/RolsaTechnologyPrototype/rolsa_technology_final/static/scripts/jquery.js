//ensures the document is fully loaded before it can execute
jQuery(function () {
  //initialises the current font size
  const font_Size = $("body").css("font-size");
  //adds an event listener which activates on click
  //function to increase the font size
  document.getElementById("text-increase").addEventListener("click", () => {
    //changes the current size to an integer
    let current_Size = parseInt(font_Size);
    //which allows it to be added to the set font size, in this case it is 10px
    let new_Size = `${current_Size + 10}px`;
    //gets the font size
    $("body").css("font-size");
    //sets the font size
    $("body").css("font-size", new_Size);
    
  });

  //function to decrease the font
  //adds an event listner which activates on click
  document.getElementById("text-decrease").addEventListener("click", () => {
    let current_Size = parseInt(font_Size);
    //removes 1 from the current font size
    let new_Size = `${current_Size - 1}px`;
    //gets the font size
    $("body").css("font-size");
    //sets the font size
    $("body").css("font-size", new_Size);
  });
  //function to reset the font size
  document.getElementById("reset").addEventListener("click", () => {
    $("body").css("font-size");
    //sets font size back to what it was beforehand
    $("body").css("font-size", font_Size);
  });

  //darkmode toggle switch
  //adds event listener to the switch which triggers with a click
  document.getElementById("darkmode-switch").addEventListener("click", () => {
    //gets and returns the background color
    const background_Color = $("body").css("background-color");
    //sets the two background color values
    const dark = "rgb(1, 1, 0)";
    const light = "rgb(232, 242, 218)";
    //determines which color is already in use
    if (background_Color === dark) {
      //switches it with the other one
      $("body").css("background-color", light);
    } else {
      //switches it with the other one
      $("body").css("background-color", dark);
    }
  });
});
