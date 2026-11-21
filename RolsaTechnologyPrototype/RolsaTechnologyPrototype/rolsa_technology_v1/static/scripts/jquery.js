//function to increase the font size
document.getElementById("text-increase").addEventListener("click", () => {
    const font_Size = $("body").css("font-size");
    var current_Size = parseInt(font_Size);
    var new_Size = `${current_Size + 10}"px"`;
    $("body").css("font-size", new_Size)
})

//function to decrease the font
document.getElementById("text-decrease").addEventListener("click", () => {
    const font_Size = $("body").css("font-size");
    let current_Size = parseInt(font_Size);
    let new_Size = `${current_Size - 1}px`
    $("body").css.remove("font-size")
    $("body").css.Add("font-size", new_Size)
})

//darkmode toggle switch 
document.getElementById("dark-mode-switch").addEventListener("click", () => {
    const light = "#E8F2DA";
    const dark = "#010100";
    let bg_color = $("body").css("background-color")
    if (bg_color === light) {
        $("body").css("background-color", dark);
    }
    else {
        $("body").css("background-color", light);
    }
})